# Assembles index.html for The Marketing Machine from the Renewal Book engine (read-only source).
import re, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.expanduser('~/Desktop/Jarvis/trig-webinar-deck/index.html')
s = open(SRC, encoding='utf-8').read()
css_end = s.index('</style>')
head = s[:css_end]
head = head.replace('<title>The Renewal Book · Johnny Brock · The Real Insurance Group</title>',
                    '<title>The Marketing Machine · Johnny Brock · The Real Insurance Group</title>')
new_css = open(os.path.join(ROOT, 'src/new.css'), encoding='utf-8').read() + open(os.path.join(ROOT, 'src/v2.css'), encoding='utf-8').read()
slides = open(os.path.join(ROOT, 'src/slides.html'), encoding='utf-8').read()
tail = s[s.index('<div class="grain"></div>') + len('<div class="grain"></div>'):]
# notes: read from each slide's <script type="text/plain" class="notes">
a = tail.index('const NOTES = {'); b = tail.index('};', a) + 2
tail = tail[:a] + 'const NOTES = {};' + tail[b:]
tail = tail.replace("const SEATS = { now: 245, cap: 250 };", "const SPOTS = 10;  /* specialist accounts opening on this webinar: set to the REAL number */")
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
/* framework tracker: replaces the brand label on teaching slides */
(function(){ const P=['Market','Message','Media','Mechanism','Monetization'];
  document.querySelectorAll('.slide[data-part]').forEach(s=>{ const cur=+s.dataset.part, b=s.querySelector('.c-brand'); if(!b) return;
    const t=document.createElement('div'); t.className='c-track';
    t.innerHTML=P.map((n,i)=>`<span class="${i+1===cur?'on':(i+1<cur?'done':'')}">${n}</span>`).join('');
    b.replaceWith(t); }); })();
</script>
'''
tail = tail.replace('</body>', TRACK + '</body>')
out = head + new_css + '\n' + '</style>\n</head>\n<body>\n\n<div id="stage">\n' + slides + '\n' + tail
for must in ['Renewal Book', 'SEATS', 'data-seat', 'TKEY']:
    if must in out: print('LEFTOVER:', must, out.count(must))
open(os.path.join(ROOT, 'index.html'), 'w', encoding='utf-8').write(out)
print('index.html', len(out), 'slides', out.count('<section class="slide'))
