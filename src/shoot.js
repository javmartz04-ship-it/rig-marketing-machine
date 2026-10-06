const { chromium } = require('playwright');
(async()=>{
  const b = await chromium.launch(); const p = await b.newPage({viewport:{width:1920,height:1080}});
  const errs=[]; p.on('pageerror', e=>errs.push(e.message)); p.on('console', m=>{ if(m.type()==='error') errs.push(m.text()); });
  await p.goto('file://'+process.argv[2]+'/index.html#1'); await p.waitForTimeout(800);
  const N = await p.evaluate(()=>window.__deck.N);
  for(let i=0;i<N;i++){
    await p.evaluate(i=>{ window.__instant=true; window.__deck.show(i,{force:true}); window.__deck.revealAll(); }, i);
    await p.evaluate(()=>document.querySelectorAll('.slide.active .a').forEach(e=>{e.style.animation='none'}));
    await p.waitForTimeout(700);
    // overflow check: any element inside .content extending past the content box
    const over = await p.evaluate(()=>{ const s=document.querySelector('.slide.active'); const c=s.querySelector('.content')||s; const cr=c.getBoundingClientRect(); const bad=[];
      s.querySelectorAll('.content *').forEach(e=>{ const r=e.getBoundingClientRect(); if(r.width&&r.height&&(r.bottom>cr.bottom+4||r.right>cr.right+4)) bad.push((e.className||e.tagName)+' '+Math.round(r.bottom-cr.bottom)+'/'+Math.round(r.right-cr.right)); });
      return bad.slice(0,4); });
    if(over.length) console.log('slide', i+1, 'overflow', JSON.stringify(over));
    await p.screenshot({path:`${process.argv[2]}/shots/${String(i+1).padStart(2,'0')}.png`});
  }
  console.log('errors', errs); await b.close();
})();
