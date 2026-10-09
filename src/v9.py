# v9: "make it stronger" pass. The text-only teaching slides become pictures the room can read in one look:
# the 5-part machine as a pipeline, the offer timeline, the market as people, an ad marked up into its four parts,
# four real-looking ads, 100-lead dot grids, three things = the machine, and the two-client math as bars.
# Runs after v8.py (reads and rewrites src/slides.html).
import re, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(ROOT, 'src/slides.html')
s = open(P, encoding='utf-8').read()

def content(opener, html):
    """Swap the .content block of the section whose opening tag starts with `opener`; notes stay."""
    global s
    a = s.index(opener)
    c = s.index('<div class="content">', a)
    e = s.index('<script type="text/plain" class="notes">', a)
    assert c < e, opener
    s = s[:c] + html.strip() + '\n' + s[e:]

def rep(a, b, n=1):
    global s
    assert a in s, 'missing: ' + a[:90]
    s = s.replace(a, b, n)

# ── icons (same hand-drawn stroke family as the .tile set) ──
I = {
 'target':  '<circle cx="56" cy="64" r="38"/><circle cx="56" cy="64" r="24"/><circle class="f" cx="56" cy="64" r="9"/><path d="M56 64L96 24M84 22l12 2 2 12"/>',
 'bubble':  '<path d="M18 26h84v54H54L34 98V80H18z"/><path d="M34 44h52M34 60h34"/>',
 'mega':    '<path d="M22 50v22h16l40 20V30L38 50z"/><path d="M38 72l7 22h13l-7-22"/><path d="M90 46c6 5 6 25 0 30M98 37c12 10 12 38 0 48"/>',
 'funnel':  '<path d="M18 26h84L70 66v24l-20 10V66z"/><path class="f2" d="M30 38h60L68 62H52z"/>',
 'gear':    '<path d="M60 18v12M60 90v12M18 60h12M90 60h12M30 30l9 9M81 81l9 9M30 90l9-9M81 39l9-9" style="stroke-width:13;stroke-linecap:butt"/><circle cx="60" cy="60" r="30" style="fill:#FBE7A8"/><circle cx="60" cy="60" r="11"/>',
 'coin':    '<circle cx="60" cy="60" r="40"/><path d="M73 45c-3-6-26-8-26 4s26 6 26 19-23 12-27 4M60 32v56"/>',
 'gift':    '<rect x="22" y="54" width="76" height="46" rx="4"/><rect x="16" y="38" width="88" height="16" rx="4"/><path d="M60 38v62"/><path d="M60 38c-6-14-26-18-26-6 0 6 14 6 26 6zM60 38c6-14 26-18 26-6 0 6-14 6-26 6z"/>',
 'board':   '<rect x="16" y="20" width="88" height="60" rx="4"/><path d="M30 38h40M30 52h56M30 66h24"/><path d="M40 80l-8 22M80 80l8 22"/>',
 'cake':    '<rect x="16" y="54" width="88" height="48" rx="6"/><path d="M16 72c15 10 29-10 44 0s29-10 44 0"/><path d="M44 54V34M76 54V34"/><path class="f" d="M44 16c-7 7-7 13 0 13s7-6 0-13zM76 16c-7 7-7 13 0 13s7-6 0-13z"/>',
 'brief':   '<rect x="16" y="40" width="88" height="56" rx="6"/><path d="M44 40V28h32v12M16 62h88"/><rect class="f" x="54" y="56" width="12" height="12" rx="2"/>',
 'shield':  '<path d="M60 16l36 12v28c0 24-16 38-36 46-20-8-36-22-36-46V28z"/><path d="M72 50c-2-6-8-8-12-8-8 0-14 6-14 16s6 16 14 16c6 0 12-4 12-12H60" />',
 'heart':   '<path d="M60 98S18 74 18 46c0-14 10-24 23-24 9 0 15 5 19 12 4-7 10-12 19-12 13 0 23 10 23 24 0 28-42 52-42 52z"/><path d="M30 58h16l7-13 10 25 7-12h20"/>',
 'tooth':   '<path d="M38 20c-16 0-22 14-18 30 3 12 9 18 11 34 2 16 14 18 18 2l5-16c2-6 10-6 12 0l5 16c4 16 16 14 18-2 2-16 8-22 11-34 4-16-2-30-18-30-9 0-14 6-22 6s-13-6-22-6z"/>',
 'book':    '<path d="M20 26h28l8 10h44v58H20z"/><path d="M44 66l10 10 20-22"/>',
 'nodes':   '<circle cx="28" cy="32" r="12"/><circle cx="92" cy="32" r="12"/><circle class="f" cx="60" cy="90" r="12"/><path d="M40 32h40M34 43l20 36M86 43L66 79"/>',
 'wrench':  '<path d="M80 18a22 22 0 0 0-24 29L22 81a9 9 0 0 0 13 13l34-34a22 22 0 0 0 29-24L85 49l-11-3-3-11z"/>',
 'machine': '<rect x="16" y="34" width="88" height="56" rx="8"/><circle cx="42" cy="62" r="12"/><circle cx="78" cy="62" r="12"/><path d="M42 50v-6M42 74v6M78 50v-6M78 74v6M30 62h-6M90 62h6M28 100h64M60 34V20M50 20h20"/>',
}
def tile(name, color, cls=''):
    return f'<div class="tile {color} {cls}"><svg viewBox="0 0 120 120">{I[name]}</svg></div>'

# ── 02 · Two things → two cards + the shape of tonight ──
content('<section class="slide wb" data-kicker="Before we start">', f'''
<div class="content">
    <h1 class="head a">Two things, so nobody<br>has to guess.</h1>
    <div class="tw2 a">
      <div class="tc frag">{tile('board','blue')}<div><p class="k">01 · Most of tonight</p><h3>This is pure marketing.</h3><p>Who to target, what to say, where to run it, what happens after the click. Take it and build it yourself.</p></div></div>
      <div class="tc frag">{tile('gift','yellow')}<div><p class="k">02 · At the very end</p><h3>There is an offer.</h3><p>I'll show you how we help agents build it. I'll tell you when it's coming. No sneaking up on you.</p></div></div>
    </div>
    <div class="tline frag">
      <div class="seg learn"><b>The marketing</b><span>Market</span><span>Message</span><span>Ads</span><span>Funnel</span><span>Backend</span></div>
      <div class="seg off"><b>The offer</b></div>
      <p class="hand tl-n">you are here ↓</p>
    </div>
  </div>
''')

# ── 05 · Five parts → the machine as a pipeline ──
steps = [('01','Market','Who, exactly, are you going after?','target','blue'),
         ('02','Message','What makes that person stop and care?','bubble','pink'),
         ('03','Ads','How do you run them, and read them?','mega','yellow'),
         ('04','Funnel','What happens after they click?','funnel','green'),
         ('05','Backend','What turns a lead into money?','gear','gold')]
pipe = ''.join(f'<div class="ms frag">{tile(ic,col)}<i>{n}</i><h3>{nm}</h3><p>{q}</p></div>' for n,nm,q,ic,col in steps)
content('<section class="slide wb s-five"', f'''
<div class="content">
    <h1 class="head a" style="font-size:80px">The Medicare Marketing Machine<br>has <em>five parts.</em></h1>
    <div class="mpipe a">{pipe}<div class="ms end frag"><div class="tile dark">{'<svg viewBox="0 0 120 120">'+I['coin']+'</svg>'}</div><i>=</i><h3>Clients</h3><p>Every part does its job, every month.</p></div></div>
    <p class="hand mp-n frag">most agents only ever work on one of these. usually the ads.</p>
  </div>
''')

# ── 07 · Market → six people, not a table ──
ppl = [('Turning 65','The biggest list, and the most crowded one in the business.','cake','blue',''),
       ('Delayed Part B','Still working past 65. Retiring confused.','brief','pink',''),
       ('Supplement only',"They don't want an Advantage pitch. They want Plan G or N.",'shield','green',''),
       ('Chronic / SNP','Heart conditions, diabetes. Almost nobody speaks to them.','heart','pink',''),
       ('Dental first','An easy front door. The Medicare talk comes later.','tooth','blue',''),
       ('Your own book','The cheapest lead you will ever get. You already paid for it.','book','yellow',' hi')]
cards = ''.join(f'<div class="pc frag{h}">{tile(ic,col)}<div><h3>{t}</h3><p>{d}</p></div></div>' for t,d,ic,col,h in ppl)
content('<section data-part="1" class="slide wb s-seg"', f'''
<div class="content">
    <h1 class="head a">“I sell Medicare” is <em>not a market.</em></h1>
    <p class="sub a">Pick one person. The more specific the person, the easier the message gets.</p>
    <div class="pgrid a">{cards}</div>
    <div class="foot2 frag">One campaign. <span>One person.</span> One problem.</div>
  </div>
''')

# ── 11 · Four parts → one ad, marked up ──
content('<section data-part="2" class="slide wb s-hppc"', '''
<div class="content">
    <h1 class="head a" style="font-size:80px">Every ad that works has<br>the same <em>four parts.</em></h1>
    <div class="anat a">
      <div class="fb">
        <div class="fbh"><i></i><div><b>Your Agency</b><span>Sponsored</span></div></div>
        <div class="fbt"><p class="p1"><u class="pin">1</u>Turning 65 this year?</p><p class="p2"><u class="pin">2</u>There are 3 Medicare decisions you have to make before your birthday month, and most people find out about the third one too late.</p></div>
        <div class="fbi"><img src="assets/ad-good.jpg" alt=""><span class="p3"><u class="pin">3</u><small>Free checklist</small>The 3 Medicare Decisions Before You Turn 65</span></div>
        <div class="fbc"><span>Free checklist · 2 minutes</span><b class="p4"><u class="pin">4</u>Get The Checklist</b></div>
      </div>
      <div class="legend">
        <div class="lg frag"><u class="pin c1">1</u><div><h3>Hook</h3><p>Call out the exact person. If they don't feel spoken to in one line, they scroll.</p></div></div>
        <div class="lg frag"><u class="pin c2">2</u><div><h3>Problem</h3><p>Name the thing they're confused or worried about, in their words, not yours.</p></div></div>
        <div class="lg frag"><u class="pin c3">3</u><div><h3>Promise</h3><p>Tell them what they'll learn or get. Education, not a pitch.</p></div></div>
        <div class="lg frag"><u class="pin c4">4</u><div><h3>Call to action</h3><p>One simple next step. Never two.</p></div></div>
      </div>
    </div>
  </div>
''')

# ── 13 · Four headlines → four real-looking ads ──
ads = [('Delayed Part B','blue','“Still working past 65? Here\'s what happens to your Part B the day you retire.”','Hook: still working. Problem: the retirement gap nobody explained.','See What Changes'),
       ('Supplement only','green','“Already on Original Medicare? See how Plan G and Plan N actually compare.”','Hook: already on Medicare. Promise: a straight comparison, no Advantage pitch.','Compare Plans'),
       ('Dental','pink','“On Medicare and still paying full price at the dentist?”','Hook and problem in one line. The front door to the whole relationship.','Check My Options'),
       ('Webinar','yellow','“A 30-minute Medicare class this Thursday. Bring your questions.”','Promise: education. CTA: register. You teach, they book.','Save My Seat')]
mini = ''.join(f'<div class="mad frag"><div class="mh"><i></i><b>Your Agency</b><span>Sponsored</span><em class="tg {c}">{k}</em></div><p class="h">{h}</p><div class="mf"><span>{w}</span><b>{cta}</b></div></div>' for k,c,h,w,cta in ads)
content('<section data-part="2" class="slide wb s-four"', f'''
<div class="content">
    <h1 class="head a" style="font-size:76px">Same formula. <em>Four different people.</em></h1>
    <p class="sub a" style="font-size:26px;margin-top:20px">Every one of these is a campaign type running in the account I'm about to show you.</p>
    <div class="madg a">{mini}</div>
  </div>
''')

# ── 35 · Same 100 leads → two dot grids ──
def dots(n):
    return '<div class="dg">' + ''.join(f'<i class="{"w" if k < n else ""}"></i>' for k in range(100)) + '</div>'
content('<section data-part="5" class="slide wb s-ab"', f'''
<div class="content">
    <h1 class="head a" style="font-size:76px">Same ad. Same 100 leads.<br><em>Four times the clients.</em></h1>
    <div class="dots2 a">
      <div class="dp frag">
        <div class="dh"><p class="k">Agent A</p><h3>No back end</h3></div>
        <div class="db">{dots(2)}<div class="dl">
          <p><i class="x">✕</i>Calls the next day</p><p><i class="x">✕</i>No reminders</p><p><i class="x">✕</i>No-shows are gone</p><p><i class="x">✕</i>Not ready yet? Forgotten</p>
          <div class="dt"><b>2</b><span>clients<small>$1,388</small></span></div></div></div>
      </div>
      <div class="dp g frag">
        <div class="dh"><p class="k">Agent B</p><h3>With a back end</h3></div>
        <div class="db">{dots(8)}<div class="dl">
          <p><i class="ok">✓</i>Text in 1 minute, call in 5</p><p><i class="ok">✓</i>Night before + morning of</p><p><i class="ok">✓</i>Rebook text in minutes</p><p><i class="ok">✓</i>Nurtured for 90 days</p>
          <div class="dt"><b>8</b><span>clients<small>$5,552</small></span></div></div></div>
      </div>
    </div>
    <p class="hand foot3 frag">every dot is a lead. the ad didn't change. the back end did. <small>(example numbers)</small></p>
  </div>
''')
rep('"Two agents. Same ad. Same hundred leads."', '"Two agents. Same ad. Same hundred leads. Every dot on this slide is one of those leads."')

# ── 46 · Three things → marketing + system + building = the machine ──
content('<section class="slide wb s-three3"', f'''
<div class="content">
    <h1 class="head a">To run this machine,<br>you need <em>three things.</em></h1>
    <div class="eqn a">
      <div class="eq frag">{tile('mega','blue')}<span class="idx">01</span><h3>The Marketing</h3><p>Knowing how to create the opportunity. Everything I taught you tonight.</p></div>
      <b class="op frag">+</b>
      <div class="eq frag">{tile('nodes','green')}<span class="idx">02</span><h3>The System</h3><p>The infrastructure that catches it, follows up, and turns it into a client.</p></div>
      <b class="op frag">+</b>
      <div class="eq hl frag">{tile('wrench','yellow')}<span class="idx">03</span><h3>The Building</h3><p>Somebody who actually gets the thing built and connected.</p></div>
      <b class="op frag">=</b>
      <div class="eq res frag"><div class="tile dark"><svg viewBox="0 0 120 120">{I['machine']}</svg></div><span class="idx">&nbsp;</span><h3>A running machine</h3><p>Leads in, clients out.</p></div>
    </div>
    <div class="foot2 frag">You can build all of it yourself. <span>Or we can help you build it.</span> Here's how.</div>
  </div>
''')

# ── 68 · Two clients → bars ──
content('<section class="slide wb s-math"', '''
<div class="content">
    <h1 class="head a" style="font-size:76px">Two clients. That's it.<br>That's the whole decision.</h1>
    <div class="cbars a">
      <div class="cb frag"><p class="cl">A full year of this<small>$300 × 12 months</small></p><div class="trk"><div class="bar yr" style="width:90%"><b>$3,600</b></div></div></div>
      <div class="cb frag"><p class="cl">Two clients<small>$2,000+ each, from the backend math</small></p><div class="trk"><div class="bar c1" style="width:50%"><b>Client 1 · $2,000</b></div><div class="bar c2" style="width:50%"><b>Client 2 · $2,000</b></div></div></div>
      <div class="cover frag" style="left:calc(360px + (100% - 360px) * .9)"><span>paid for</span></div>
      <div class="cb after frag"><p class="cl">Client 3 and on<small>every one after that</small></p><div class="trk"><div class="bar mine" style="width:100%"><b>Yours</b></div></div></div>
    </div>
    <div class="mfoot frag">You don't need the machine to work all year. <span>You need it to work twice.</span></div>
  </div>
''')

open(P, 'w', encoding='utf-8').write(s)
print('v9 ok', s.count('<section class="slide') + s.count('<section data-part'))
