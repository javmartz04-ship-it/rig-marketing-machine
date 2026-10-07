# v2 design pass: chapter openers, framework tracker, visual teaching slides.
# Reads src/slides.v1.html, writes src/slides.html. Re-runnable.
import re, math, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = open(os.path.join(ROOT, 'src/slides.v1.html'), encoding='utf-8').read()

# split into blocks keyed by the v1 slide number
parts = re.split(r'\n(?=<!-- ═+ \d\d )', src)
blocks = {}
for p in parts:
    m = re.match(r'<!-- ═+ (\d\d) ', p)
    if m: blocks[int(m.group(1))] = p.strip('\n')

PARTS = ['Market', 'Message', 'Ads', 'Funnel', 'Backend']

def rail(cur):
    out = []
    for i, n in enumerate(PARTS, 1):
        cls = 'on' if i == cur else ('done' if i < cur else '')
        out.append(f'<span class="{cls}"><i>0{i}</i>{n}</span>')
    return '<div class="rail5 a">' + ''.join(out) + '</div>'

def opener(no, title, line, img, pos, note, cur=None, kicker=None):
    num = f'<div class="no a">{no}</div>' if no else ''
    r = rail(cur) if cur else ''
    return f'''<!-- ═══════════════════════ CHAPTER · {kicker or title} ═══════════════════════ -->
<section class="slide s-ch" data-kicker="{kicker or ('Part ' + no)}">
  <div class="bg"><img src="assets/{img}" alt="" style="object-position:{pos}"></div>
  <div class="scrim"></div>
  <div class="txt">
    {num}
    <h1 class="a">{title}</h1>
    <p class="a">{line}</p>
  </div>
  {r}
<script type="text/plain" class="notes">{note}</script>
</section>'''

def tag(n, part):
    blocks[n] = blocks[n].replace('<section class="slide', f'<section data-part="{part}" class="slide', 1)

for n in (6, 7): tag(n, 1)
for n in (8, 9, 10): tag(n, 2)
for n in (11, 12, 13): tag(n, 3)
for n in (14, 15, 16): tag(n, 4)
for n in (18, 19, 20, 21, 22): tag(n, 5)

# ── 09 · ad mocks with real photography
b = blocks[9]
b = b.replace('<div class="vis">Stock photo of a smiling couple</div>',
              '<div class="vis"><img src="assets/ad-bad.jpg" alt="" style="object-position:center 30%"></div>')
b = b.replace('<div class="vis">The 3 Medicare Decisions Before You Turn 65</div>',
              '<div class="vis"><img src="assets/ad-good.jpg" alt="" style="object-position:center 35%"><span class="band"><small>Free checklist</small>The 3 Medicare Decisions<br>Before You Turn 65</span></div>')
blocks[9] = b

# ── 14 · the path, with a mini mockup of every step
mk = {
 'Ad': '<div class="mk"><div class="mrow"><i class="av"></i><span class="ln w50"></span></div><span class="ln"></span><span class="ln w70"></span><div class="mimg" style="background-image:url(assets/ad-good.jpg)"></div><span class="mbtn">Get The Checklist</span></div>',
 'Landing page': '<div class="mk"><span class="ln k w40"></span><span class="ln h"></span><span class="ln h w80"></span><span class="ln w90"></span><span class="ln w60"></span><span class="mbtn big">Get The Checklist</span></div>',
 'Form': '<div class="mk"><span class="ln h w70"></span><span class="fld">Name</span><span class="fld">Phone</span><span class="fld">Email</span><span class="fld q">Turning 65 when?</span><span class="mbtn">Send It</span></div>',
 'Thank-you page': '<div class="mk ctr"><span class="chk">✓</span><span class="ln h w80"></span><span class="ln w60"></span><span class="mbtn big">Book Your Time</span></div>',
 'Calendar': '<div class="mk"><span class="ln h w60"></span><div class="cal">' + ''.join(f'<i class="{"g" if k==9 else ("x" if k in (3,11,14) else "")}"></i>' for k in range(15)) + '</div><span class="slot">Tue · 10:00 AM</span></div>',
 'Text + email': '<div class="mk"><span class="bub out">Hi Mary, it\'s Johnny\'s office. You\'re booked for Tue at 10.</span><span class="bub out s">Reply C to confirm.</span><span class="bub in">C 👍</span></div>',
 'Appoint&shy;ment': '<div class="mk ctr win"><span class="ev"><small>Tuesday · 10:00</small>Medicare review<em>Mary H. · confirmed</em></span><span class="chk g">✓</span></div>',
}
b = blocks[14]
for title, html in mk.items():
    b = re.sub(r'(<div class="n frag"><div class="dot">\d\d</div>)(<h3>' + re.escape(title) + '</h3>)', r'\1' + html.replace('\\', '\\\\') + r'\2', b)
b = b.replace('<section data-part="4" class="slide"', '<section data-part="4" class="slide s-path"')
blocks[14] = b

# ── 17 · statement slide folds into the Monetization opener
del blocks[17]

# ── 18 · follow-up: timeline left, the actual text thread right
blocks[18] = '''<!-- ═══════════════════════ 18 FOLLOW-UP · THE SCHEDULE ═══════════════════════ -->
<section data-part="5" class="slide s-fu" data-kicker="05 · Monetization · Follow-up">
  <div class="light"></div>
  <div class="content">
    <h1 class="head a" style="font-size:76px">The follow-up schedule<br>most agents <em>skip.</em></h1>
    <div class="fu a">
      <div class="vt">
        <div class="s frag"><p class="w">First 5 min</p><div><h3>Call, then text</h3><p>They still remember filling out the form.</p></div></div>
        <div class="s frag"><p class="w">First 24 hrs</p><div><h3>Touch again</h3><p>Call, text, email. One attempt is not follow-up.</p></div></div>
        <div class="s frag"><p class="w">Days 2 to 7</p><div><h3>Nurture</h3><p>Answer the questions they were scared to ask.</p></div></div>
        <div class="s frag"><p class="w">No-show</p><div><h3>Recover</h3><p>Text within minutes. Half of them rebook.</p></div></div>
        <div class="s frag"><p class="w">90 days</p><div><h3>Stay close</h3><p>For the ones who weren't ready yet.</p></div></div>
        <div class="s frag"><p class="w">Old leads</p><div><h3>Reactivate</h3><p>The list you already paid for.</p></div></div>
      </div>
      <div class="phone">
        <div class="ph-top"><span class="ph-av">J</span><b>Johnny's Office</b><small>Text message</small></div>
        <div class="thread">
          <p class="ts">Today 9:04 AM</p>
          <p class="m in">Hi Mary, it's Johnny's office. Got your checklist request. Is now a good time for a quick call?</p>
          <p class="m out">Can you call after 3?</p>
          <p class="m in">You got it. Talk at 3:15.</p>
          <p class="ts">Thursday</p>
          <p class="m in">Quick tip: most people miss the Part B window when they retire. Want me to check yours?</p>
          <p class="ts">Tuesday 10:12 AM</p>
          <p class="m in">We missed you at 10. Want to pick a new time? Here's my calendar.</p>
          <p class="m out">Sorry! Tomorrow at 2?</p>
        </div>
      </div>
    </div>
    <div class="fufoot frag">None of this should depend on <span>you remembering.</span></div>
  </div>
<script type="text/plain" class="notes">THE FOLLOW-UP SCHEDULE.

Left is the schedule. Right is what it actually looks like on Mary's phone. Point at the phone.

FIVE MINUTES: "If you call them back tomorrow, you're calling a stranger. Five minutes, they still remember filling out the form."

NO-SHOW: point at the last two bubbles. "We missed you at ten. Want to pick a new time?" And she rebooks. Most agents never send that text.

OLD LEADS: "Every one of you has a list of leads you paid for and gave up on. That's not a dead list. That's a campaign you haven't run yet."

Close: none of this should depend on you remembering. That's the bridge to the backend.</script>
</section>'''

# ── 19 · unit economics as a narrowing funnel
blocks[19] = '''<!-- ═══════════════════════ 19 MONETIZATION · UNIT ECONOMICS ═══════════════════════ -->
<section data-part="5" class="slide s-econ2" data-kicker="05 · Monetization · The math">
  <div class="light"></div>
  <div class="content">
    <h1 class="head a" style="font-size:76px">Know five numbers and you know<br>what a lead is <em>worth.</em></h1>
    <div class="grid a">
      <div class="fn">
        <div class="r frag"><div class="t">Leads<small>at $5.92 each</small></div><div class="tr"><i style="width:100%"></i></div><div class="v">100</div><div class="c">$592 spent</div></div>
        <div class="r frag"><div class="t">Booked<small>30% book a call</small></div><div class="tr"><i style="width:30%"></i></div><div class="v">30</div><div class="c"></div></div>
        <div class="r frag"><div class="t">Showed<small>70% show up</small></div><div class="tr"><i style="width:21%"></i></div><div class="v">21</div><div class="c"></div></div>
        <div class="r frag"><div class="t">Clients<small>40% say yes</small></div><div class="tr"><i class="g" style="width:8%"></i></div><div class="v g">8</div><div class="c">× $694 = $5,552</div></div>
        <p class="ex">Example rates. Plug in your own.</p>
      </div>
      <div class="res">
        <div class="frag"><p class="k">Cost to get each client</p><div class="big">$74</div></div>
        <div class="frag"><p class="k">Worth on day one</p><div class="big w">$694</div></div>
        <p class="frag go">So stop asking if $12 a lead is expensive. Ask <span>what you can afford to pay for a client.</span></p>
      </div>
    </div>
  </div>
<script type="text/plain" class="notes">UNIT ECONOMICS. THE MOST VALUABLE SLIDE TONIGHT.

Say clearly: these are EXAMPLE rates. Their numbers will be different. The point is the method.

Walk the funnel down: "A hundred leads at $5.92 is $592. Thirty book. Twenty-one show. Eight become clients. At $694 first-year on Medicare Advantage, that's $5,552. So each client cost you about seventy-four dollars."

Then the turn: "When you know this, you stop asking 'is $12 a lead expensive?' and start asking 'what can I afford to pay for a client?' That one question changes everything."

Johnny: swap in your own real rates if you have them. Real beats example.</script>
</section>'''
blocks[20] = blocks[20].replace('The lead cost $74.', 'The client cost $74.')

# ── 23 · the machine as a loop
cx, cy, rx, ry = 840, 445, 640, 228
names = ['Market', 'Ad', 'Funnel', 'Follow-up', 'Appointment', 'Sale', 'Cross-sell', 'Renewal', 'Referral']
nodes = []
for k, nm in enumerate(names):
    th = math.radians(-90 + 40 * k)
    x, y = cx + rx * math.cos(th), cy + ry * math.sin(th)
    side = 'up' if y < cy - 20 else 'dn'
    cls = 'nd frag ' + side + (' loop' if nm == 'Referral' else '')
    nodes.append(f'<div class="{cls}" style="left:{x:.0f}px;top:{y:.0f}px"><b></b><span><i>0{k+1}</i>{nm}</span></div>')
blocks[23] = f'''<!-- ═══════════════════════ 23 THE WHOLE MACHINE ═══════════════════════ -->
<section data-part="5" class="slide s-loop" data-kicker="The whole machine">
  <div class="light"></div>
  <div class="content">
    <h1 class="head a" style="font-size:72px">This is Medicare <em>marketing.</em></h1>
    <div class="ring a">
      <svg viewBox="0 0 1680 762" width="1680" height="762"><ellipse class="el" cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}"/><ellipse class="el2" cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" pathLength="100"/>
        <circle r="7" class="runner"><animateMotion dur="14s" repeatCount="indefinite" path="M {cx} {cy-ry} A {rx} {ry} 0 1 1 {cx-0.1} {cy-ry} Z"/></circle></svg>
      {''.join(nodes)}
      <div class="mid frag"><p>Not just ads. Not just a funnel. Not just a CRM.</p><h2>The whole <em>machine.</em></h2><small>Referral feeds the market. It never stops.</small></div>
    </div>
  </div>
<script type="text/plain" class="notes">THE WHOLE MACHINE.

Reveal each one around the loop and name it. Market, ad, funnel, follow-up, appointment, sale, cross-sell, renewal, referral.

Then the middle: "Referral feeds the market. That's why it's a machine, not a campaign. Not just Facebook ads. Not just a funnel. Not just a CRM. The whole machine. That's Medicare marketing."

This is the end of the teaching. Next slide is proof.</script>
</section>'''

# ── 33 · checkboxes: you have the idea, nothing else is built
b = blocks[33]
b = re.sub(r'<div class="st frag"><i>(\d\d)</i>', lambda m: f'<div class="st frag{" have" if m.group(1)=="01" else ""}"><i>{m.group(1)}</i><b class="ck">{"✓" if m.group(1)=="01" else ""}</b>', b)
b = b.replace('<h3>Campaign idea</h3>', '<h3>Campaign idea</h3><small>You have this part.</small>')
blocks[33] = b

# ── 37 · the delta as bars
blocks[37] = '''<!-- ═══════════════════════ 37 THE DELTA ═══════════════════════ -->
<section class="slide s-delta2" data-kicker="The math that matters">
  <div class="light"></div>
  <div class="content">
    <h1 class="head a">Here's the only math<br>that <em>matters.</em></h1>
    <div class="bars a">
      <div class="br frag"><div class="t">Before tonight<small>Everything you just saw</small></div><div class="tr"><i class="base" style="width:9.8%"></i></div><div class="v">$147<small>/mo</small></div></div>
      <div class="br frag"><div class="t">Starting tonight<small>All of it, plus your specialist</small></div><div class="tr"><i class="base" style="width:9.8%"></i><i class="add" style="width:10.2%"><em>+$153</em></i></div><div class="v g">$300<small>/mo</small></div></div>
      <div class="br frag dim"><div class="t">A GHL specialist on your own<small>And they don't know Medicare</small></div><div class="tr"><i class="ext" style="width:100%"></i></div><div class="v">~$1,500<small>/mo</small></div></div>
    </div>
    <div class="foot2 frag">For <span>$153 more</span>, you get the piece that costs about <span>$1,500 a month</span> on its own.</div>
  </div>
<script type="text/plain" class="notes">THE DECISION MATH. THE STRONGEST MOMENT IN THE WEBINAR.

Reveal one bar at a time.

"Before tonight, everything you just saw was a hundred and forty-seven a month." (short bar)
"Starting tonight it's three hundred, and it includes your specialist." Point at the gold sliver. "That gold piece is the difference. A hundred and fifty-three dollars."
"And here's what a GoHighLevel specialist costs on your own." (the long bar) "About fifteen hundred a month. And they don't know Medicare."

Let the picture do the work. Pause. Then the bottom line.</script>
</section>'''

blocks[43] = blocks[43].replace('flip back to slide 39 (the whole offer on one screen) or slide 37 (the $147 to $300 math)', 'flip back to the whole-offer slide or the $147 to $300 bars')

# ── openers
OP = {
 6: opener('01', 'Market', 'Who, exactly, are you going after?', 'ch-market.jpg', '70% 30%',
           'CHAPTER 01 · MARKET\n\nOne breath. Read the question and move on.\n\n"Part one. Market. Who, exactly, are you going after? Because if the answer is \'everybody on Medicare\', nothing after this works."', 1),
 8: opener('02', 'Message', 'What makes that person stop and care?', 'ch-message.jpg', '62% 30%',
           'CHAPTER 02 · MESSAGE\n\n"Part two. You know who. Now, what do you say so they stop scrolling? Look at her face. That\'s confusion. Your message has to name it."', 2),
 11: opener('03', 'Ads', 'How do you run them, and how do you read them?', 'ch-media.jpg', '66% 40%',
           'CHAPTER 03 · ADS\n\n"Part three. Ads. Your clients are on their phones every day, just like him. I\'m going to show you how to run the ads, and how to read them like a pro."', 3),
 14: opener('04', 'Funnel', 'What happens after they click?', 'ch-mechanism.jpg', '64% 40%',
           'CHAPTER 04 · FUNNEL\n\n"Part four. They saw the ad. Now what? This is where most agents lose them."', 4),
 18: opener('05', 'Backend', 'Your ad doesn\'t make you money. <em>Your follow-up does.</em>', 'ch-money.jpg', '58% 35%',
           'CHAPTER 05 · BACKEND\n\nSAY IT, THEN STOP.\n\n"Part five. The back end. Your ad doesn\'t make you money. Your follow-up does."\n\nPause. Most agents think marketing ends when the lead comes in. This is the moment that belief breaks.', 5),
 26: opener('', 'How we help you <em>build it.</em>', 'The marketing, the system, and the person who builds it. Seven parts.', 'ch-offer.jpg', '62% 40%',
           'THE OFFER OPENS.\n\n"I told you at the start there was an offer. Here it is. Seven parts. I\'ll show you each one and what it\'s worth, and then the price."', None, 'How we help'),
}

order = []
for n in sorted(blocks):
    if n in OP: order.append(OP[n])
    order.append(blocks[n])
open(os.path.join(ROOT, 'src/slides.html'), 'w', encoding='utf-8').write('\n\n'.join(order) + '\n')
print('slides', sum(o.count('<section') for o in order))
