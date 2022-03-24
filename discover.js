const SUBREDDIT=document.querySelector('template#subreddit').content.children[0]
const SUBS=new Set()

async function get(){
  let all=await fetch('https://www.reddit.com/r/all/new/.json')
  all=await all.json()
  for(let post of all['data']['children']){
    post=post['data']
    let name=post['subreddit']
    if(SUBS.has(name)||name.indexOf('u_')==0||post['over_18'])
      continue
    SUBS.add(name)
    let s=SUBREDDIT.cloneNode(true)
    let a=s.querySelector('a')
    a.href=`https://reddit.com/r/${name}/top/?sort=top&t=month`
    a.innerHTML=name
    document.body.appendChild(s)
  }
  run()
}

export function run(){setTimeout(get,3000)}
