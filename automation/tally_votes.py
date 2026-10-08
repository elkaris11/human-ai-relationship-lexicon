#!/usr/bin/env python3
import json, os, urllib.request
repo=os.environ['GITHUB_REPOSITORY']; token=os.environ['GITHUB_TOKEN']
headers={'Authorization':f'Bearer {token}','Accept':'application/vnd.github+json','X-GitHub-Api-Version':'2022-11-28'}
def api(url,method='GET',data=None):
 req=urllib.request.Request(url,headers=headers,method=method,data=json.dumps(data).encode() if data else None)
 with urllib.request.urlopen(req) as r: return json.load(r) if r.length else {}
issues=api(f'https://api.github.com/repos/{repo}/issues?state=open&labels=proposal&per_page=100')
for issue in issues:
 reactions=api(issue['reactions']['url']+'?per_page=100')
 up=sum(1 for r in reactions if r['content']=='+1'); down=sum(1 for r in reactions if r['content']=='-1'); total=up+down; net=up-down; ratio=(down/total if total else 0)
 eligible=total>=7 and net>=3 and ratio<=.40
 labels=[x['name'] for x in issue['labels'] if x['name']!='stage: ready-for-harvest']
 if eligible: labels.append('stage: ready-for-harvest')
 api(f"https://api.github.com/repos/{repo}/issues/{issue['number']}",'PATCH',{'labels':labels})
 print(json.dumps({'issue':issue['number'],'up':up,'down':down,'net':net,'opposition_ratio':round(ratio,3),'eligible_for_review':eligible}))
