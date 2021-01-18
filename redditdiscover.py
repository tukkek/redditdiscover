#!/usr/bin/python3
import requests,time

HTML='''
<title>reddit discover</title>
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<style>
  .subreddit{margin:.5em;display:inline-block;}
</style>
'''
HEADER={'User-agent':'redditdiscover'}
SUBS={}#keys used as ordered Set

def generate():
  with open('output.html','w') as html:
    print(HTML,file=html)
    for s in dict.fromkeys(SUBS):
      a=f'<a href="https://reddit.com/r/{s}" target="_blank">{s}</a>'
      print(f'<div class="subreddit">{a}</div>',file=html)

while True:
  print('fetching more...')
  new=requests.get('https://www.reddit.com/r/all/new/.json',headers=HEADER).json()
  for post in new['data']['children']:
    s=post['data']['subreddit']
    if not s.startswith('u_'):
      SUBS[s]=None
  generate()
  time.sleep(3)
  
