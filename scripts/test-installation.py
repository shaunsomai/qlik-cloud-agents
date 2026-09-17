"""Run real Claude plugin installation with isolated settings (no model calls)."""
from pathlib import Path
import os,json,subprocess,sys,tempfile,shutil
ROOT=Path(__file__).resolve().parents[1]
def main():
    exe=os.environ.get('CLAUDE_TEST_BINARY') or shutil.which('claude')
    if not exe:raise SystemExit('Install Claude Code or set CLAUDE_TEST_BINARY first.')
    name=json.loads((ROOT/'.claude-plugin/marketplace.json').read_text())['plugins'][0]['name']
    with tempfile.TemporaryDirectory(prefix='qlik-install-') as temp:
        env=os.environ.copy();env['CLAUDE_CONFIG_DIR']=str(Path(temp)/'config');env['DISABLE_AUTOUPDATER']='1';env['CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC']='1'
        for key in ['ANTHROPIC_API_KEY','CLAUDE_CODE_OAUTH_TOKEN']:env.pop(key,None)
        def run(*args):
            result=subprocess.run([exe,*args],cwd=temp,env=env,capture_output=True,encoding='utf-8',timeout=90)
            if result.returncode:raise RuntimeError(result.stdout+'\n'+result.stderr)
            return result.stdout
        run('plugin','validate',str(ROOT))
        run('plugin','validate',str(ROOT/'plugins'/name))
        source='https://github.com/shaunsomai/'+name+'.git' if '--github' in sys.argv else str(ROOT)
        args=['plugin','marketplace','add',source]
        if '--github' in sys.argv:args+=['--sparse','.claude-plugin','plugins']
        run(*args)
        installed=json.loads(run('plugin','install',name+'@'+name+'-marketplace','--json'))
        assert installed['outcome']=='ok',installed
        listed=json.loads(run('plugin','list','--json'))
        matches=[p for p in listed if p.get('id')==name+'@'+name+'-marketplace']
        assert len(matches)==1 and matches[0]['enabled'],listed
        cached=Path(matches[0]['installPath'])
        run('plugin','validate',str(cached))
        for asset in ['LICENSE','SHARING.md','HOUSE-CONVENTIONS.md','skills/qlik-theming/SKILL.md','assets/themes/sales-demo-theme/theme.json']:
            assert (cached/asset).is_file(),asset
        metadata=json.loads((cached/'.claude-plugin/plugin.json').read_text())
        if 'mcpServers' in metadata:
            cfg=metadata['mcpServers']['qlik-desktop']
            entry=cfg['args'][0].replace('${CLAUDE_PLUGIN_ROOT}',str(cached))
            messages=[{'jsonrpc':'2.0','id':1,'method':'initialize','params':{'protocolVersion':'2025-06-18'}},{'jsonrpc':'2.0','id':2,'method':'tools/list'}]
            response=subprocess.run([sys.executable,entry],input='\n'.join(map(json.dumps,messages))+'\n',capture_output=True,encoding='utf-8',timeout=15,check=True,env=env)
            rows=list(map(json.loads,response.stdout.splitlines()))
            assert rows[0]['result']['serverInfo']['name']=='qlik-desktop'
            assert len(rows[1]['result']['tools'])==39
            print('Installed Desktop MCP initializes and exposes 39 tools')
        print(name+': real CLI validation and isolated installation passed')
if __name__=='__main__':main()
