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
        assert installed['outcome']=='installed',installed
        listed=json.loads(run('plugin','list','--json'))
        assert any(p.get('id')==name+'@'+name+'-marketplace' for p in listed),listed
        print(name+': real CLI validation and isolated installation passed')
if __name__=='__main__':main()
