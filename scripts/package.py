from pathlib import Path
import json,re,sys,subprocess,zipfile,tempfile,hashlib
ROOT=Path(__file__).resolve().parents[1]
def validate(root):
 m=json.loads((root/'.claude-plugin/marketplace.json').read_text()); assert len(m['plugins'])==1
 i=m['plugins'][0]; p=(root/i['source']).resolve(); assert p.is_relative_to(root.resolve())
 meta=json.loads((p/'.claude-plugin/plugin.json').read_text()); assert meta['name']==i['name']; assert meta['version']=='2.1.0'
 names=[]
 for f in (p/'agents').glob('*.md'):
  t=f.read_text(encoding='utf-8'); assert t.startswith('---\n'); h=t.split('---',2)[1]; n=re.search(r'^name:\s*(.+)$',h,re.M).group(1).strip(); assert n==f.stem; assert 'description:' in h; names.append(n)
 assert len(names)==len(set(names)); assert len(names)==(5 if 'desktop' in meta['name'] else 6)
 for f in ['LICENSE','SHARING.md','HOUSE-CONVENTIONS.md','skills/qlik-theming/SKILL.md']:assert (p/f).is_file()
 for f in (p/'assets/themes').rglob('*.json'):json.loads(f.read_text())
 for f in (p/'assets/themes').rglob('*.qext'):assert json.loads(f.read_text())['type']=='theme'
 for f in [root/'README.md',p/'README.md']:
  for link in re.findall(r'\[[^\]]+\]\(([^)]+)\)',f.read_text(encoding='utf-8')):
   if not link.startswith(('https://','http://','#')):assert (f.parent/link.split('#')[0]).exists(),(f,link)
 if 'mcpServers' in meta:
  cfg=meta['mcpServers']['qlik-desktop']; entry=cfg['args'][0].replace('${CLAUDE_PLUGIN_ROOT}',str(p)); assert Path(entry).is_file()
  for f in (p/'mcp-server').glob('*.py'):compile(f.read_text(encoding='utf-8'),str(f),'exec')
  msgs=[{'jsonrpc':'2.0','id':1,'method':'initialize','params':{'protocolVersion':'2025-06-18'}},{'jsonrpc':'2.0','method':'notifications/initialized'},{'jsonrpc':'2.0','id':2,'method':'tools/list'},{'jsonrpc':'2.0','id':3,'method':'ping'}]
  res=subprocess.run([sys.executable,entry],input='\n'.join(map(json.dumps,msgs))+'\n',text=True,capture_output=True,check=True,timeout=15); rows=list(map(json.loads,res.stdout.splitlines())); assert [x['id'] for x in rows]==[1,2,3]; assert rows[0]['result']['serverInfo']['name']=='qlik-desktop'; assert rows[2]['result']=={}
  tools=rows[1]['result']['tools']; assert len(tools)==len({t['name'] for t in tools})
  for t in tools:
   s=t['inputSchema']; assert s['type']=='object'; assert set(s.get('required',[]))<=set(s.get('properties',{}))
  print('MCP handshake, ping and',len(tools),'tool schemas passed')
 print(meta['name'],': manifests, agents, themes and links passed'); return p,meta
def main():
 p,meta=validate(ROOT)
 if '--validate-only' in sys.argv:return
 dest=ROOT/'dist'; dest.mkdir(exist_ok=True); archive=dest/(meta['name']+'-'+meta['version']+'.zip')
 with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED) as z:
  for f in sorted(p.rglob('*')):
   if f.is_file() and '__pycache__' not in f.parts and f.suffix!='.pyc':z.write(f,Path(meta['name'])/f.relative_to(p))
 with tempfile.TemporaryDirectory() as temp:
  test=Path(temp)
  with zipfile.ZipFile(archive) as z:assert z.testzip() is None; z.extractall(test)
  (test/'.claude-plugin').mkdir(); m=json.loads((ROOT/'.claude-plugin/marketplace.json').read_text()); m['plugins'][0]['source']='./'+meta['name']; (test/'.claude-plugin/marketplace.json').write_text(json.dumps(m)); (test/'README.md').write_text('# Extracted package\n'); validate(test)
 digest=hashlib.sha256(archive.read_bytes()).hexdigest(); archive.with_suffix('.zip.sha256').write_text(digest+'  '+archive.name+'\n'); print('ZIP extracted and validated:',archive.name,digest)
if __name__=='__main__':main()
