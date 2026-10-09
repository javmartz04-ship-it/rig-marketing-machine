# Assembles index.html for The Marketing Machine from the Renewal Book engine (read-only source).
import re, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.expanduser('~/Desktop/Jarvis/trig-webinar-deck/index.html')
s = open(SRC, encoding='utf-8').read()
css_end = s.index('</style>')
head = s[:css_end]
head = head.replace('<title>The Renewal Book · Johnny Brock · The Real Insurance Group</title>',
                    '<title>The Marketing Machine · Johnny Brock · The Real Insurance Group</title>')
new_css = open(os.path.join(ROOT, 'src/new.css'), encoding='utf-8').read() + open(os.path.join(ROOT, 'src/v2.css'), encoding='utf-8').read() + open(os.path.join(ROOT, 'src/v3.css'), encoding='utf-8').read() + open(os.path.join(ROOT, 'src/v4.css'), encoding='utf-8').read() + open(os.path.join(ROOT, 'src/v5.css'), encoding='utf-8').read() + open(os.path.join(ROOT, 'src/v6.css'), encoding='utf-8').read() + open(os.path.join(ROOT, 'src/v7.css'), encoding='utf-8').read() + open(os.path.join(ROOT, 'src/v9.css'), encoding='utf-8').read()
slides = open(os.path.join(ROOT, 'src/slides.html'), encoding='utf-8').read()
tail = s[s.index('<div class="grain"></div>') + len('<div class="grain"></div>'):]
# notes: read from each slide's <script type="text/plain" class="notes">
a = tail.index('const NOTES = {'); b = tail.index('};', a) + 2
tail = tail[:a] + 'const NOTES = {};' + tail[b:]
tail = tail.replace("const SEATS = { now: 245, cap: 250 };", "const SPOTS = 12;  /* seats opening on this webinar (onboarding capacity this week): set to the REAL number */")
tail = re.sub(r"  document\.querySelectorAll\('\[data-seat\]'\).*?\n  \{ const m = .*?\n.*?\n", 
              "  document.querySelectorAll('[data-spots]').forEach(el=>{ el.textContent = SPOTS; });\n", tail, flags=re.S)
tail = tail.replace("     Check skool.com/realinsurancegroup for the current member count.\n     Everything on slides 24, 26, 32, 34 and 36 updates from here.     */",
                    "     Specialist capacity shown on the 'Why there's a limit' slide.     */")
tail = tail.replace("new BroadcastChannel('trig-renewal-book')", "new BroadcastChannel('trig-marketing-machine')")
tail = tail.replace("'trig-speaker'", "'trig-mm-speaker'")
tail = tail.replace('<span class="l">The Renewal Book</span>', '<span class="l">The Marketing Machine</span>')
tail = tail.replace("<h3>The Renewal Book · controls</h3>", "<h3>The Marketing Machine · controls</h3>")
tail = tail.replace("  addEventListener('storage', e=>{ if(e.key===TKEY) updateChip(); });\n", "")
tail = tail.replace("NOTES[i+1] || ''", "(slides[i]?.querySelector('script.notes')?.textContent || '').trim()")
TRACK = '''<script>
/* 15-minute offer timer (resets on every page load, starts itself on the data-timer-start slide): T starts/pauses, Shift+T resets, or click it. Shows on slides with data-timer. */
(function(){
  const KEY='mm-offer-timer', DUR=15*60*1000;
  const stage=document.getElementById('stage'); if(!stage) return;
  const el=document.createElement('div'); el.id='otimer';
  el.innerHTML='<span class="pl"><svg viewBox="0 0 20 20"><path d="M5 3l12 7-12 7z"/></svg></span><span class="lb"></span><b>15:00</b>';
  stage.appendChild(el);
  let st={end:null,left:DUR}, lastA=null; /* every fresh open starts a full, unstarted clock */
  const save=()=>{ try{ localStorage.setItem(KEY, JSON.stringify(st)); }catch(e){} };
  const remain=()=> st.end ? Math.max(0, st.end-Date.now()) : st.left;
  const fmt=ms=>{ const s=Math.ceil(ms/1000); return String(Math.floor(s/60)).padStart(2,'0')+':'+String(s%60).padStart(2,'0'); };
  function tick(){
    const r=remain();
    el.querySelector('b').textContent=fmt(r);
    el.classList.toggle('run', !!st.end && r>0);
    el.classList.toggle('zero', r<=0);
    el.querySelector('.lb').textContent = r<=0 ? "Tonight's bonuses are closed" : (st.end ? "Tonight's bonuses end in" : "Press play to start the clock");
    const a=document.querySelector('.slide.active');
    el.classList.toggle('on', !!(a && a.hasAttribute('data-timer')));
    if (a !== lastA){ lastA = a; if (a && a.hasAttribute('data-timer-start') && !st.end && st.left===DUR) start(); }
  }
  const start=()=>{ if(st.end || st.left<=0) return; st.end=Date.now()+st.left; save(); tick(); };
  const pause=()=>{ if(!st.end) return; st.left=remain(); st.end=null; save(); tick(); };
  const reset=()=>{ st={end:null,left:DUR}; save(); tick(); };
  el.addEventListener('click', e=>{ e.stopPropagation(); st.end ? pause() : start(); });
  addEventListener('keydown', e=>{ if(e.metaKey||e.ctrlKey||e.altKey) return; if(e.key==='t') (st.end ? pause() : start()); else if(e.key==='T') reset(); });
  setInterval(tick, 250); tick();
})();

/* framework tracker: replaces the brand label on teaching slides */
(function(){ const P=['Market','Message','Ads','Funnel','Backend'];
  document.querySelectorAll('.slide[data-part]').forEach(s=>{ const cur=+s.dataset.part, b=s.querySelector('.c-brand'); if(!b) return;
    const t=document.createElement('div'); t.className='c-track';
    t.innerHTML=P.map((n,i)=>`<span class="${i+1===cur?'on':(i+1<cur?'done':'')}">${n}</span>`).join('');
    b.replaceWith(t); }); })();
</script>
'''
tail = tail.replace('<tr><td>A</td><td>Reveal all steps on this slide</td></tr>', '<tr><td>A</td><td>Reveal all steps on this slide</td></tr>\n    <tr><td>T</td><td>Start / pause the 15-minute offer timer (Shift+T resets). It starts itself on How we help.</td></tr>')
tail = tail.replace("show(h>=1&&h<=N ? h-1 : 0, {force:true});", "show(0, {force:true}); /* always open on slide 1, whatever the URL says */")
tail = tail.replace('</body>', TRACK + '</body>')
out = head + new_css + '\n' + '</style>\n</head>\n<body>\n\n<div id="stage">\n' + slides + '\n' + tail
for must in ['Renewal Book', 'SEATS', 'data-seat', 'TKEY']:
    if must in out: print('LEFTOVER:', must, out.count(must))
open(os.path.join(ROOT, 'index.html'), 'w', encoding='utf-8').write(out)
print('index.html', len(out), 'slides', out.count('<section class="slide'))
