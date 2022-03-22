#!/usr/bin/python3
import requests,time

HTML='''
<title>reddit discover</title>
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<style>
  .subreddit{margin:.5em;display:inline-block;}
  a:focus{border:black solid 1px;}
</style>
'''
HEADER={'User-agent':'redditdiscover'}
SUBS={}#keys used as ordered Set
NSFW=False
USERS=False
SMALL=True

biggest=0

def generate():
  with open('output.html','w') as html:
    print(HTML,file=html)
    for s in dict.fromkeys(SUBS):
      a=f'<a href="https://reddit.com/r/{s}/top/?sort=top&t=month" target="_blank">{s}</a>'
      print(f'<div class="subreddit">{a}</div>',file=html)
      
while True:
  print('fetching more...')
  new=requests.get('https://www.reddit.com/r/all/new/.json',headers=HEADER).json()
  for post in new['data']['children']:
    post=post['data']
    s=post['subreddit']
    if not USERS and s.startswith('u_'):
      continue
    if not NSFW and post['over_18']:
      continue
    subscribers=post['subreddit_subscribers']
    if not SMALL:
      biggest=max(biggest,subscribers)
      if subscribers<biggest/100:
        continue
    SUBS[s]=None
  generate()
  time.sleep(3)
