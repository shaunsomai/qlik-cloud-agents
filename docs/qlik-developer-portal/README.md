# Qlik Developer Portal Markdown repository

Official publisher-provided Markdown exports from Extend, Manage, APIs, and Toolkits.

Coverage: **1443 collected pages**, including **1432 native exports** and **11 references to shared exports**. Unavailable pages: **0**.

| Section | Collected pages | Browse | Official overview |
| --- | ---: | --- | --- |
| Extend | 104 | [Local index](indexes/extend.md) | [Qlik overview](extend.md) |
| Manage | 110 | [Local index](indexes/manage.md) | [Qlik overview](manage.md) |
| APIs | 189 | [Local index](indexes/apis.md) | [Qlik overview](apis.md) |
| Toolkits | 1040 | [Local index](indexes/toolkits.md) | [Qlik overview](toolkits.md) |

## Start building

- [Extension development guidelines](extend/extensions/extension-guidelines.md)
- [Manage key concepts](manage/key-concepts.md)
- [Your first API call](manage/get-started-first-api-call.md)
- [API namespaces](apis/namespaces.md)
- [JavaScript/TypeScript toolkit](toolkits/qlik-api.md)
- [CLI reference index](indexes/toolkits.md)

## File conventions

Native exports are preserved byte-for-byte. Their source metadata, code examples, schemas, and tables remain as Qlik publishes them. Publisher timestamps are included when present; generated API exports do not always include front matter.

Shared-export reference files point to a combined API reference when Qlik's Markdown action serves the same export for multiple web pages. The manifest distinguishes these from native exports.

Local indexes and reference files use local links. Links inside unchanged publisher exports retain their original web targets; resolve relative links against the source page URL recorded in the manifest. Images and external assets remain online.

[Coverage report](COVERAGE.md) | [Source attribution](SOURCE-NOTICE.md) | [Manifest](manifest.json)

## Collect or update

From the repository root:

~~~powershell
python scripts/collect-qlik-dev.py
python scripts/collect-qlik-dev.py --validate-only
python scripts/collect-qlik-dev.py --refresh
~~~

The collector requires Python 3.10+ and requests. Normal runs resume verified existing files and retry unavailable pages. The refresh option explicitly updates the snapshot from the current exports.
