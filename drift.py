"""Review differences between desired and observed JSON snapshots."""
import argparse
import json
from pathlib import Path
import sys


def pointer(parent,key):
    return parent+'/'+str(key).replace('~','~0').replace('/','~1')


def compare(expected,actual,ignore=()):
    ignored=set(ignore);changes=[]
    def walk(a,b,path):
        if path in ignored: return
        if type(a) is not type(b): changes.append({'path':path,'change':'modified','expected':a,'actual':b});return
        if isinstance(a,dict):
            for key in sorted(a.keys() | b.keys()):
                child=pointer(path,key)
                if child in ignored: continue
                if key not in a: changes.append({'path':child,'change':'added','actual':b[key]})
                elif key not in b: changes.append({'path':child,'change':'removed','expected':a[key]})
                else: walk(a[key],b[key],child)
        elif a!=b: changes.append({'path':path,'change':'modified','expected':a,'actual':b})
    walk(expected,actual,'');return changes


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('snapshots');p.add_argument('--ignore',action='append',default=[]);a=p.parse_args()
    try:
        value=json.loads(Path(a.snapshots).read_text());changes=compare(value['expected'],value['actual'],a.ignore)
    except (OSError,ValueError,KeyError,TypeError) as e:
        print(json.dumps({'error':str(e)}),file=sys.stderr);return 2
    print(json.dumps({'changes':changes,'in_sync':not changes},indent=2));return int(bool(changes))

if __name__=='__main__': sys.exit(main())
