#!/usr/bin/env python3
"""Collect publisher-provided qlik.dev Markdown exports and local indexes.

Requires Python 3.10+ and requests. Source content is never executed.
Run: python scripts/collect-qlik-dev.py
Validate: python scripts/collect-qlik-dev.py --validate-only
Refresh: python scripts/collect-qlik-dev.py --refresh
"""
import argparse
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
import hashlib
import html
import json
import os
from pathlib import Path
import re
import threading
import time
from urllib.parse import unquote, urljoin, urlsplit, urlunsplit
import xml.etree.ElementTree as ET

import requests

ORIGIN = "https://qlik.dev"
SECTIONS = ("extend", "manage", "apis", "toolkits")
SCRIPT_ROOT = Path(__file__).resolve().parents[1]
MAX_BYTES = 128 * 1024 * 1024
_thread = threading.local()

def session():
    if not hasattr(_thread, "http"):
        _thread.http = requests.Session()
        _thread.http.headers["User-Agent"] = "QlikMarkdownCollection/1.0"
    return _thread.http

def utc():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")

def sha(data):
    return hashlib.sha256(data).hexdigest()

def request(url, stream=False):
    for attempt in range(3):
        try:
            response = session().get(url, timeout=(15, 60), stream=stream)
            if response.status_code in (429, 500, 502, 503, 504) and attempt < 2:
                delay = response.headers.get("Retry-After", "1")
                response.close()
                time.sleep(min(float(delay) if delay.isdigit() else 1, 10))
                continue
            response.raise_for_status()
            return response
        except requests.RequestException as error:
            if attempt == 2 or (error.response is not None and error.response.status_code < 429):
                raise
            time.sleep(attempt + 1)
    raise RuntimeError("Request retries exhausted")

def canonical_page(url):
    u = urlsplit(urljoin(ORIGIN, url))
    if u.hostname != "qlik.dev":
        return None
    path = u.path.rstrip("/")
    if path.endswith(".md"):
        path = path[:-3]
    if path.strip("/").split("/")[0] not in SECTIONS:
        return None
    return ORIGIN + path + "/"

def markdown_url(page):
    return page.rstrip("/") + ".md"

def local_path(export_url):
    path = unquote(urlsplit(export_url).path).lstrip("/")
    if not path.endswith(".md") or any(x in ("", ".", "..") for x in path.split("/")):
        raise ValueError("Unsafe or unexpected Markdown URL: " + export_url)
    if re.search(r'[<>:"\\|?*\x00-\x1f]', path):
        raise ValueError("Unsupported filename: " + path)
    return path

def read_bytes(response):
    with response:
        body = bytearray()
        for chunk in response.iter_content(65536):
            body.extend(chunk)
            if len(body) > MAX_BYTES:
                raise ValueError("Export exceeds 128 MiB")
        return bytes(body)

def discover():
    urls = set()
    visited = set()
    pending = [ORIGIN + "/sitemap-index.xml"]
    while pending:
        url = pending.pop()
        if url in visited:
            continue
        visited.add(url)
        with request(url) as response:
            tree = ET.fromstring(response.content)
        locs = [element.text for element in tree.iter() if element.tag.endswith("}loc")]
        if tree.tag.endswith("}sitemapindex"):
            pending.extend(locs)
        else:
            urls.update(page for url in locs if (page := canonical_page(url)))
    # Include section navigation entries even if an entry is absent from the sitemap.
    for section in SECTIONS:
        with request(ORIGIN + "/" + section + "/") as response:
            source = response.text
        for href in re.findall(r'href=["\']([^"\']+)["\']', source):
            page = canonical_page(urljoin(ORIGIN + "/" + section + "/", html.unescape(href)))
            if page and not urlsplit(page).path.endswith((".pdf/", ".svg/", ".png/")):
                urls.add(page)
    paths = [local_path(markdown_url(page)) for page in urls]
    if len({p.casefold() for p in paths}) != len(paths):
        raise ValueError("Case-insensitive filename collision")
    return sorted(urls), sorted(visited)

def offered_export(page):
    # API class routes can offer their parent API's combined export.
    with request(page, stream=True) as response:
        sample = bytearray()
        for chunk in response.iter_content(16384):
            sample.extend(chunk)
            text = sample.decode("utf-8", errors="replace")
            links = re.findall(r'href=["\']([^"\']+\.md(?:#[^"\']*)?)["\']', text)
            for href in links:
                u = urlsplit(urljoin(page, html.unescape(href)))
                if u.hostname == "qlik.dev":
                    return urlunsplit((u.scheme, u.netloc, u.path, "", ""))
            if len(sample) >= 4 * 1024 * 1024:
                break
    raise ValueError("Page offers no discoverable Markdown export")

def title_and_update(data, page):
    text = data.decode("utf-8")
    title = re.search(r"^# (.+)$", text, re.M)
    update = re.search(r"^last_updated:\s*(.+)$", text, re.M)
    return (
        title.group(1).strip() if title else urlsplit(page).path.rstrip("/").split("/")[-1],
        update.group(1).strip() if update else None,
    )

def atomic_write(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    part = path.with_name(path.name + ".part")
    part.write_bytes(data)
    for attempt in range(7):
        try:
            part.replace(path)
            return
        except PermissionError as error:
            if os.name != "nt" or getattr(error, "winerror", None) not in (5, 32, 33) or attempt == 6:
                raise
            time.sleep(0.05 * (2 ** attempt))

def reference_bytes(page, export_url, title):
    import posixpath
    own = local_path(markdown_url(page))
    destination = local_path(export_url)
    relative = posixpath.relpath(destination, posixpath.dirname(own) or ".")
    route = urlsplit(page).path.rstrip("/").split("/")[-1]
    text = [
        "---",
        "source: " + page,
        "collection_kind: shared_export_reference",
        "markdown_export: " + export_url,
        "---", "",
        "# " + title + ": " + route, "",
        "Qlik serves this page through a shared Markdown export containing the complete API reference.", "",
        "[Open the complete official Markdown export](" + relative + ")", "",
        "[Open the original web page](" + page + ")", "",
    ]
    return ("\n".join(text)).encode("utf-8")

class Collector:
    def __init__(self, root, previous, refresh):
        self.root = root.resolve()
        self.previous = {p["source_url"]: p for p in previous.get("pages", [])}
        self.refresh = refresh
        self.lock = threading.Lock()
        self.export_locks = {}
        self.exports = {}
        self.cached_exports = {}
        for row in self.previous.values():
            if row.get("status") == "collected" and row.get("kind") == "native_markdown":
                self.cached_exports[row["markdown_url"]] = row

    def path(self, relative):
        destination = (self.root / relative).resolve()
        if not destination.is_relative_to(self.root):
            raise ValueError("Output path leaves collection folder: " + relative + " -> " + str(destination))
        return destination

    def export(self, url, page):
        with self.lock:
            guard = self.export_locks.setdefault(url, threading.Lock())
        with guard:
            if url in self.exports:
                data, headers, error, fetched = self.exports[url]
                if error:
                    raise error
                return data, headers, fetched
            cached = self.cached_exports.get(url)
            if cached and not self.refresh:
                path = self.path(cached["local_path"])
                if path.is_file() and sha(path.read_bytes()) == cached["sha256"]:
                    data = path.read_bytes()
                    self.exports[url] = (data, {"Content-Type": cached["content_type"]}, None, cached["retrieved_at"])
                    return data, {"Content-Type": cached["content_type"]}, cached["retrieved_at"]
            try:
                response = request(url, stream=True)
                headers = response.headers.copy()
                data = read_bytes(response)
                if "markdown" not in headers.get("Content-Type", "").lower():
                    raise ValueError("Response is not publisher Markdown")
                text = data.decode("utf-8")
                if text.lstrip().lower().startswith(("<!doctype html", "<html")) or not text.strip():
                    raise ValueError("Invalid Markdown export")
                native = self.path(local_path(url))
                if native.exists() and not self.refresh:
                    if native.read_bytes() != data:
                        raise ValueError("Existing export differs; use --refresh deliberately")
                else:
                    atomic_write(native, data)
                self.exports[url] = (data, headers, None, utc())
            except Exception as error:
                self.exports[url] = (None, None, error, None)
                raise
            return self.exports[url][0], headers, self.exports[url][3]

    def collect(self, page):
        relative = local_path(markdown_url(page))
        old = self.previous.get(page)
        if old and old.get("status") == "collected" and not self.refresh:
            path = self.path(old["local_path"])
            if path.is_file() and sha(path.read_bytes()) == old["sha256"]:
                return old
        expected = markdown_url(page)
        try:
            actual = expected
            try:
                data, headers, fetched = self.export(actual, page)
            except (requests.RequestException, ValueError):
                actual = offered_export(page)
                data, headers, fetched = self.export(actual, page)
            title, updated = title_and_update(data, page)
            export_path = local_path(actual)
            kind = "native_markdown"
            saved = data
            if actual != expected:
                kind = "shared_export_reference"
                saved = reference_bytes(page, actual, title)
                reference = self.path(relative)
                if reference.exists() and not self.refresh and reference.read_bytes() != saved:
                    raise ValueError("Existing reference differs; use --refresh deliberately")
                atomic_write(reference, saved)
                title += ": " + urlsplit(page).path.rstrip("/").split("/")[-1]
            return {
                "source_url": page, "markdown_url": actual,
                "local_path": relative, "export_local_path": export_path,
                "section": urlsplit(page).path.strip("/").split("/")[0],
                "title": title, "last_updated": updated,
                "retrieved_at": fetched, "status": "collected", "kind": kind,
                "content_type": headers.get("Content-Type", "text/markdown"),
                "bytes": len(saved), "sha256": sha(saved),
                "export_bytes": len(data), "export_sha256": sha(data),
            }
        except Exception as error:
            return {
                "source_url": page, "section": urlsplit(page).path.strip("/").split("/")[0],
                "status": "unavailable", "error": str(error), "checked_at": utc(),
            }

def link_label(text):
    return text.replace("[", "\\[").replace("]", "\\]").replace("|", "\\|")

def write_metadata(root, records, sitemaps):
    collected = [p for p in records if p["status"] == "collected"]
    failures = [p for p in records if p["status"] != "collected"]
    native = [p for p in collected if p["kind"] == "native_markdown"]
    aliases = [p for p in collected if p["kind"] == "shared_export_reference"]
    report = {
        "collection": "Qlik Developer Portal official Markdown exports",
        "generated_at": utc(), "source_sections": [ORIGIN + "/" + s + "/" for s in SECTIONS],
        "sitemaps": sitemaps, "discovered_pages": len(records),
        "collected_pages": len(collected), "native_markdown_pages": len(native),
        "shared_export_references": len(aliases), "unavailable_pages": len(failures),
        "pages": sorted(records, key=lambda p: p["source_url"]),
    }
    atomic_write(root / "manifest.json", (json.dumps(report, ensure_ascii=False, indent=2) + "\n").encode("utf-8"))
    indexes = root / "indexes"
    indexes.mkdir(parents=True, exist_ok=True)
    for section in SECTIONS:
        rows = sorted((p for p in collected if p["section"] == section), key=lambda p: p["source_url"])
        groups = defaultdict(list)
        for row in rows:
            segments = urlsplit(row["source_url"]).path.strip("/").split("/")
            group = "/".join(segments[1:3] if section in ("extend", "toolkits") else segments[1:2]) or "Overview"
            groups[group].append(row)
        lines = ["# " + ("APIs" if section == "apis" else section.title()) + ": local index", "", "[Collection overview](../README.md)", ""]
        for group, members in sorted(groups.items()):
            lines += ["## " + group, ""]
            for row in members:
                suffix = " (shared export reference)" if row["kind"] == "shared_export_reference" else ""
                lines += ["- [" + link_label(row["title"]) + "](../" + row["local_path"] + ")" + suffix]
            lines += [""]
        atomic_write(indexes / (section + ".md"), "\n".join(lines).encode("utf-8"))
    readme = [
        "# Qlik Developer Portal Markdown repository", "",
        "Official publisher-provided Markdown exports from Extend, Manage, APIs, and Toolkits.", "",
        f"Coverage: **{len(collected)} collected pages**, including **{len(native)} native exports** and **{len(aliases)} references to shared exports**. Unavailable pages: **{len(failures)}**.", "",
        "| Section | Collected pages | Browse | Official overview |", "| --- | ---: | --- | --- |",
    ]
    for section in SECTIONS:
        count = sum(p["section"] == section for p in collected)
        readme += [f"| {section.upper() if section == 'apis' else section.title()} | {count} | [Local index](indexes/{section}.md) | [Qlik overview]({section}.md) |"]
    readme += [
        "", "## Start building", "",
        "- [Extension development guidelines](extend/extensions/extension-guidelines.md)",
        "- [Manage key concepts](manage/key-concepts.md)",
        "- [Your first API call](manage/get-started-first-api-call.md)",
        "- [API namespaces](apis/namespaces.md)",
        "- [JavaScript/TypeScript toolkit](toolkits/qlik-api.md)",
        "- [CLI reference index](indexes/toolkits.md)", "",
        "## File conventions", "",
        "Native exports are preserved byte-for-byte. Their source metadata, code examples, schemas, and tables remain as Qlik publishes them. Publisher timestamps are included when present; generated API exports do not always include front matter.", "",
        "Shared-export reference files point to a combined API reference when Qlik's Markdown action serves the same export for multiple web pages. The manifest distinguishes these from native exports.", "",
        "Local indexes and reference files use local links. Links inside unchanged publisher exports retain their original web targets; resolve relative links against the source page URL recorded in the manifest. Images and external assets remain online.", "",
        "[Coverage report](COVERAGE.md) | [Source attribution](SOURCE-NOTICE.md) | [Manifest](manifest.json)", "",
        "## Collect or update", "",
        "From the repository root:", "", "~~~powershell",
        "python scripts/collect-qlik-dev.py",
        "python scripts/collect-qlik-dev.py --validate-only",
        "python scripts/collect-qlik-dev.py --refresh", "~~~", "",
        "The collector requires Python 3.10+ and requests. Normal runs resume verified existing files and retry unavailable pages. The refresh option explicitly updates the snapshot from the current exports.", "",
    ]
    atomic_write(root / "README.md", "\n".join(readme).encode("utf-8"))
    notice = [
        "# Source attribution", "",
        "Documentation content belongs to Qlik and its respective contributors. Copy and Markdown actions do not make the content public domain.", "",
        "Native files were obtained from the Markdown exports offered by the Qlik Developer Portal. Source URLs, retrieval timestamps, publisher update metadata when available, and checksums are recorded in the manifest.", "",
        "[Qlik Developer Portal terms](https://qlik.dev/qlik-developer-portal-terms-of-use.pdf)", "",
        "[API policy](https://qlik.dev/apis/api-policy/)", "",
        "This local collection preserves source attribution and does not grant additional redistribution or software-license rights.", "",
    ]
    atomic_write(root / "SOURCE-NOTICE.md", "\n".join(notice).encode("utf-8"))
    coverage = [
        "# Collection coverage", "", "Scope: sitemap-listed and section-navigation-linked English pages beneath /extend/, /manage/, /apis/, and /toolkits/.", "",
        f"- Discovered: {len(records)}", f"- Collected: {len(collected)}",
        f"- Native exports: {len(native)}", f"- Shared-export reference files: {len(aliases)}",
        f"- Unavailable: {len(failures)}", "",
        "## Shared API exports", "",
        "Some API class routes offer the parent API's complete Markdown reference. Local reference files preserve those individual routes while avoiding repeated copies of a combined export.", "",
        "## Outside this snapshot", "",
        "Authenticate, Embed, changelog, external repositories, linked assets, videos, and downloadable specifications are outside this four-section snapshot. Cross-links remain available in the publisher Markdown. Unlinked pages absent from the sitemap cannot be guaranteed to be included.", "",
        "## Unavailable pages", "",
    ]
    if failures:
        coverage += ["- [" + p["source_url"] + "](" + p["source_url"] + "): " + p["error"] for p in failures]
    else:
        coverage += ["No unavailable pages were found."]
    coverage += ["", "[Collection overview](README.md)", ""]
    atomic_write(root / "COVERAGE.md", "\n".join(coverage).encode("utf-8"))
    return report

def validate(root):
    root = root.resolve()
    report = json.loads((root / "manifest.json").read_text(encoding="utf-8"))
    if report.get("in_progress"):
        raise ValueError("Collection is incomplete or in progress; resume the collector before validating.")
    errors = []
    for row in report["pages"]:
        if row["status"] != "collected":
            continue
        path = (root / row["local_path"]).resolve()
        if not path.is_relative_to(root) or not path.is_file():
            errors.append("Missing or unsafe file: " + row["local_path"])
            continue
        data = path.read_bytes()
        if sha(data) != row["sha256"] or len(data) != row["bytes"]:
            errors.append("Checksum mismatch: " + row["local_path"])
        data.decode("utf-8")
        export = root / row["export_local_path"]
        if not export.is_file() or sha(export.read_bytes()) != row["export_sha256"]:
            errors.append("Shared/native export checksum mismatch: " + row["export_local_path"])
    authored = [root / "README.md", root / "COVERAGE.md", root / "SOURCE-NOTICE.md"]
    authored += list((root / "indexes").glob("*.md"))
    authored += [root / p["local_path"] for p in report["pages"] if p.get("kind") == "shared_export_reference"]
    checked_links = 0
    for path in authored:
        text = path.read_text(encoding="utf-8")
        for href in re.findall(r"\]\(([^)]+)\)", text):
            if href.startswith(("https://", "http://", "#")):
                continue
            checked_links += 1
            destination = (path.parent / href.split("#")[0]).resolve()
            if not destination.is_relative_to(root) or not destination.is_file():
                errors.append("Broken local link in " + str(path.relative_to(root)) + ": " + href)
    if errors:
        raise ValueError("\n".join(errors))
    print(f"Validated {report['collected_pages']} page files, checksums, UTF-8, and {checked_links} authored local links.", flush=True)
    return report

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=SCRIPT_ROOT / "docs" / "qlik-developer-portal")
    parser.add_argument("--workers", type=int, default=6)
    parser.add_argument("--refresh", action="store_true")
    parser.add_argument("--validate-only", action="store_true")
    args = parser.parse_args()
    if not 1 <= args.workers <= 12:
        parser.error("workers must be between 1 and 12")
    root = args.output.resolve()
    if args.validate_only:
        validate(root)
        return
    root.mkdir(parents=True, exist_ok=True)
    old_path = root / "manifest.json"
    previous = json.loads(old_path.read_text(encoding="utf-8")) if old_path.exists() else {}
    urls, sitemaps = discover()
    print("Discovered:", len(urls), "By section:", dict(Counter(urlsplit(u).path.strip('/').split('/')[0] for u in urls)), flush=True)
    collector = Collector(root, previous, args.refresh)
    records = []
    resume_rows = {url: collector.previous.get(url, {
        "source_url": url,
        "section": urlsplit(url).path.strip("/").split("/")[0],
        "status": "pending",
    }) for url in urls}
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        jobs = {pool.submit(collector.collect, url): url for url in urls}
        for job in as_completed(jobs):
            url = jobs[job]
            try:
                records.append(job.result())
            except Exception as error:
                records.append({"source_url": url, "section": urlsplit(url).path.strip("/").split("/")[0], "status": "unavailable", "error": str(error), "checked_at": utc()})
            resume_rows[url] = records[-1]
            if len(records) % 50 == 0:
                failures = sum(p["status"] != "collected" for p in records)
                print(f"Progress {len(records)}/{len(urls)}; unavailable {failures}", flush=True)
                checkpoint = dict(previous)
                checkpoint.update({
                    "collection": "Qlik Developer Portal official Markdown exports",
                    "generated_at": utc(), "in_progress": True,
                    "discovered_pages": len(urls),
                    "collected_pages": sum(p["status"] == "collected" for p in resume_rows.values()),
                    "pages": sorted(resume_rows.values(), key=lambda p: p["source_url"]),
                })
                atomic_write(root / "manifest.json", (json.dumps(checkpoint, ensure_ascii=False, indent=2) + "\n").encode("utf-8"))
    report = write_metadata(root, records, sitemaps)
    validate(root)
    print(json.dumps({k: report[k] for k in ("discovered_pages", "collected_pages", "native_markdown_pages", "shared_export_references", "unavailable_pages")}), flush=True)
    if report["unavailable_pages"]:
        raise SystemExit(2)

if __name__ == "__main__":
    main()
