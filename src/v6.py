# v6: the offer rebuilt around the core (Skool community, $147/mo), a gift slide that starts a
# 15-minute timer, Hormozi-style bonus build-up, Chris (onboarding) + Christopher (GHL specialist),
# "outside this webinar it's all separate", 12 seats; whole deck in the light style; agent photos.
# Runs after v5.py (reads and rewrites src/slides.html).
import re, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(ROOT, 'src/slides.html')
s = open(P, encoding='utf-8').read()

def rep(a, b):
    global s
    assert a in s, 'missing: ' + a[:80]
    s = s.replace(a, b, 1)

# ── split off the offer tail and index its blocks
OPEN = '<!-- ═══════════════════════ CHAPTER · How we help'
i = s.index(OPEN)
head, tail = s[:i], s[i:]
parts = re.split(r'\n\s*(?=<!-- ═+ )', tail)
blk = {}
for p in parts:
    m = re.match(r'<!-- ═+ (.*?) ═', p)
    if m: blk[m.group(1).strip()] = p.strip()
need = ['CHAPTER · How we help', '33 THE GAP', '34 SIX PEOPLE', '37 THE DELTA', '38 THE PRICE', '41 THE MATH', '42 WHAT HAPPENS NEXT', '43 AMA']
for n in need: assert n in blk, n

# ═══ THE CORE ═══
THUMBS = [('start', 'Start Here'), ('fb', 'Facebook Ads'), ('anc', 'Ancillary Sales'), ('sales', 'Sales 101'),
          ('comp', 'Compliance Mastery'), ('calls', 'Live Recorded Trainings'), ('scripts', 'Scripts'), ('annuity', 'Annuity Course')]
CORE = f'''<!-- ═══════════════════════ CORE 1 · THE COMMUNITY ═══════════════════════ -->
<section class="slide wb s-core1" data-kicker="How we help · The main thing">
  <div class="light"></div>
  <div class="content">
    <div class="c1w">
      <div class="c1l">
        <span class="mainpill a">The main thing</span>
        <h1 class="head a">The Real Insurance Group <em>community.</em></h1>
        <p class="rb a">Everything you need to market, sell and grow a Medicare business, in one place, with people who are doing it right now.</p>
        <div class="c1p a">
          <div class="frag"><b>The classroom</b><span>Hundreds of hours of training, unlocked on day one.</span></div>
          <div class="frag"><b>Live every business day</b><span>Marketing, sales, AI and annuities, live.</span></div>
          <div class="frag"><b>The wins</b><span>Agents posting results every day.</span></div>
        </div>
      </div>
      <div class="c1r a"><div class="frame live"><div class="bar"><i></i><i></i><i></i><span>skool.com · The Real Insurance Group</span></div><video muted loop playsinline preload="auto" poster="assets/skool-feed-poster.jpg" src="assets/skool-feed.mp4"></video></div><p class="hand">this is what you log into, today.</p></div>
    </div>
  </div>
<script type="text/plain" class="notes">THE CORE. THE COMMUNITY IS THE PRODUCT.

"So here's how we help. It starts with the main thing: the Real Insurance Group community, on Skool."

"Three things live inside it. The classroom: hundreds of hours of training, unlocked the day you join. Live calls every business day. And the wins: agents posting results every single day."

Talk over the video: "This is what you log into. Not a screenshot from a good week. Today."</script>
</section>

<!-- ═══════════════════════ CORE 2 · THE CLASSROOM ═══════════════════════ -->
<section class="slide wb s-class" data-kicker="How we help · The classroom">
  <div class="light"></div>
  <div class="content">
    <h1 class="head a" style="font-size:80px">Every course, <em>unlocked on day one.</em></h1>
    <div class="thg a">''' + ''.join(f'<div class="th frag"><img src="assets/courses/{f}.jpg" alt="{t}"><p>{t}</p></div>' for f, t in THUMBS) + '''</div>
    <p class="hand foot3 frag">+ 9 more courses. medicare basics, marketing, tech, VAs, reels, GHL help... all unlocked.</p>
  </div>
<script type="text/plain" class="notes">THE CLASSROOM.

"This is the classroom. Every one of these is a full course, and they all unlock the day you join. Not drip-fed. All of it."

Point at a few: "Start Here is your 90-day roadmap. Facebook Ads. Ancillary sales: that's the cross-sell from tonight. Sales 101. Compliance. Scripts. Annuities. Even how to hire a virtual assistant."

"Whatever you don't know how to do yet, there's already a course for it."</script>
</section>

<!-- ═══════════════════════ CORE 3 · LIVE + WINS ═══════════════════════ -->
<section class="slide wb s-live" data-kicker="How we help · The community">
  <div class="light"></div>
  <div class="content">
    <h1 class="head a" style="font-size:80px">Live every business day. <em>Wins every day.</em></h1>
    <div class="lvw a">
      <div class="lvk">
        <div class="dy frag"><i>Mon</i><p>Marketing, with Johnny</p></div>
        <div class="dy frag"><i>Tue</i><p>Sales and annuity</p></div>
        <div class="dy frag"><i>Wed</i><p>Marketing, AI and sales</p></div>
        <div class="dy frag"><i>Thu</i><p>Sales training</p></div>
        <div class="dy frag"><i>Fri</i><p>Marketing, and running an agency</p></div>
        <p class="hand">never more than 24 hours from a real answer.</p>
      </div>
      <div class="wins">
        <div class="wn frag"><b>$10,000</b><p>“He made me roughly $10,000 from June to the middle of July, and I've not even scratched the surface yet.”</p><span>Jill Coates</span></div>
        <div class="wn frag"><b>Full calendar</b><p>“I started running Facebook ads, hired a virtual assistant, and now have a full calendar year-round.”</p><span>Mindy Baron</span></div>
        <div class="wn frag"><b>Secret weapon</b><p>“In the wild world of Medicare, Johnny Brock is my secret weapon.”</p><span>Thomas Key</span></div>
      </div>
    </div>
  </div>
<script type="text/plain" class="notes">LIVE CALLS AND WINS.

"You're not buying a course that sits on a shelf. There's a live call every business day. Monday marketing with me. Tuesday sales and annuity. Wednesday marketing, AI and sales. Thursday sales. Friday marketing and running an agency."

"And the wins." Read one: Jill, ten thousand dollars June to mid-July. Mindy, full calendar year-round. Thomas: "Johnny Brock is my secret weapon."

(Javier is sending a better video of the wins feed. When it lands, it goes on this slide.)</script>
</section>

<!-- ═══════════════════════ CORE 4 · THE PRICE OF THE CORE ═══════════════════════ -->
<section class="slide wb s-offer s-corep" data-kicker="How we help · The community">
  <div class="light"></div>
  <div class="wrap">
    <p class="lead a">The community. Everything inside it.</p>
    <h1 class="price a">$147<small>/mo</small></h1>
    <p class="all a">Nothing up front. No contract. Cancel anytime.</p>
    <p class="less a">That's the main thing. If that's all you ever got, it would already be worth it.</p>
  </div>
<script type="text/plain" class="notes">THE PRICE OF THE CORE.

"The community, everything inside it: a hundred and forty-seven dollars a month. Nothing up front, cancel anytime."

"That's the main thing. And honestly, if that's all you ever got, it would be worth it."

Pause. Then go to the gift slide. That's where the build-up starts.</script>
</section>

<!-- ═══════════════════════ GIFT · FOR STAYING ═══════════════════════ -->
<section class="slide wb s-gift" data-timer data-kicker="A gift for staying">
  <div class="light"></div>
  <div class="content">
    <div class="gfw">
      <div class="gfl">
        <p class="eb a">Because you stayed to the end</p>
        <h1 class="head a">We have a <em>special gift</em> for you.</h1>
        <p class="rb a">Join on this webinar today, and you get every bonus I'm about to show you. They're not on the website. They're not in the follow-up email. <b>They're only for the people here right now.</b></p>
        <p class="hand a">the clock starts now. you have 15 minutes.</p>
      </div>
      <div class="gfr a"><div class="tile gold big gbox"><svg viewBox="0 0 120 120"><rect x="22" y="52" width="76" height="52" rx="4"/><rect x="16" y="38" width="88" height="16" rx="4" class="f2"/><path d="M60 38v66"/><path d="M60 38c-8-16-30-18-28-4 2 9 28 4 28 4zM60 38c8-16 30-18 28-4-2 9-28 4-28 4z"/></svg></div></div>
    </div>
  </div>
<script type="text/plain" class="notes">THE GIFT. START THE TIMER HERE.

PRESS T (or click the timer in the corner) to start the 15-minute clock. It keeps running through every slide to the end.

"Because you stayed to the end, we have a special gift for you. If you join on this webinar today, you get every bonus I'm about to show you."

"They're not on the website. They're not in the follow-up email. They're only for the people here right now. And the clock starts now: fifteen minutes."

Then: "Not only do you get the community. If you join today, you also get..." Go.</script>
</section>'''

# ═══ BONUSES ═══
TOT = ['$3,000', '$4,164', '$5,164', '$10,164']
def tally(n):
    segs = ''.join(f'<i class="{"on" if k < n else ""}"></i>' for k in range(5))
    return f'<div class="bt frag"><p class="l">Bonus value so far</p><span class="seg s5">{segs}</span><p class="c">{n} of 5</p><p class="v">{TOT[n-1]}</p></div>'
GIFTSVG = '<span class="gift"><svg viewBox="0 0 40 40"><rect x="6" y="16" width="28" height="18" rx="2"/><rect x="4" y="11" width="32" height="7" rx="2"/><path d="M20 11v23M20 11c-3-6-10-6-9-1 1 3 9 1 9 1zM20 11c3-6 10-6 9-1-1 3-9 1-9 1z"/></svg></span>'
def bonus(n, name, value, vsub, lead, rows, visual, note):
    lis = ''.join(f'<li class="frag"><b>{t}</b>{d}</li>' for t, d in rows)
    return f'''<!-- ═══════════════════════ BONUS {n} ═══════════════════════ -->
<section class="slide wb s-bn" data-timer data-kicker="Join today · Bonus {n} of 5">
  <div class="light"></div>
  <div class="content">
    <div class="bnw">
      <div class="bnl">
        <p class="also a">{'Not only do you get the community.' if n == 1 else 'And if you join today, you also get'}</p>
        <div class="bnt a">{GIFTSVG}Bonus #{n}</div>
        <h1 class="head a">{name}</h1>
        <p class="rb a">{lead}</p>
        <ul class="bl a">{lis}</ul>
      </div>
      <div class="bnr a">{visual}<div class="stamp"><b>{value}</b><span>{vsub}</span></div></div>
    </div>
    {tally(n)}
  </div>
<script type="text/plain" class="notes">{note}</script>
</section>'''

BOOK = '''<div class="pbw"><div class="book"><div class="cv"><img src="assets/logo.webp" alt=""><p class="k">The Real Insurance Group</p><h4>The Medicare<br>Marketing<br><em>Playbook.</em></h4><p class="au">Johnny Brock</p></div><div class="pg"></div></div>
<div class="toc"><p class="k">Inside</p><p><i>01</i>Market</p><p><i>02</i>Message</p><p><i>03</i>Ads</p><p><i>04</i>Funnel</p><p><i>05</i>Backend</p></div></div>'''
GHL = '<div class="g4">' + ''.join(f'<div class="frame live"><div class="bar"><i></i><i></i><i></i><span>{t}</span></div><img src="assets/{f}" alt="{t}"></div>' for t, f in
       [('Automation', 'crm-auto.jpg'), ('Funnels', 'crm-funnels.jpg'), ('Sites', 'crm-sites.jpg'), ('A live page', 'crm-livepage.jpg')]) + '</div>'
CHRIS = '''<div class="pcard"><div class="ph"><img src="assets/david.png" alt="Chris"></div><div class="pi"><p class="k">Your onboarding specialist</p><h3>Meet Chris.</h3>
<div class="ck">''' + ''.join(f'<p><i>✓</i>{t}</p>' for t in ['Sets your account up, live, with you', 'Gets you A2P approved, so texts land', 'Connects your number, email and calendar']) + '</div></div></div>'
SNAP = '''<div class="snap"><div class="frame live"><div class="bar"><i></i><i></i><i></i><span>Your account · day one</span></div><img src="assets/crm-funnels.jpg" alt="Funnel steps already built" style="object-fit:cover;object-position:24% 40%;transform:scale(1.3);transform-origin:24% 40%"></div>
<div class="pgs"><span class="g">Webinar snapshot</span><span>Registration</span><span>Reminders</span><span>Replay</span><span>Lead funnels</span><span>Booking</span><span class="g">+ every text and email behind them</span></div></div>'''

BON = [
 bonus(1, 'The Medicare Marketing <em>Playbook.</em>', '$3,000', 'value',
       'Everything you saw tonight, step by step. How to create the opportunity, from the first ad to the renewal.',
       [('Market and message', 'picking your person and writing the ad'), ('Running the ads', 'from a dead stop to a running account'), ('The funnel', 'every page, built to convert'), ('The backend', 'follow-up, nurture, pipeline, cross-sell')],
       BOOK, 'BONUS #1: THE MEDICARE MARKETING PLAYBOOK. $3,000.\n\n"Not only do you get the community. If you join today, you also get the Medicare Marketing Playbook. Tonight was the overview. The playbook is the whole thing, step by step: market, message, ads, funnel, backend."\n\nSay the value once. Point at the bar at the bottom: it climbs on every slide from here.'),
 bonus(2, 'Your GoHighLevel <em>Account.</em>', '$97', 'per month',
       'This is the back end for your ads. Every lead, every follow-up and every booking, in one place.',
       [('Every lead in one place', 'texts, calls and emails in one inbox'), ('Booking pages', 'they pick a time without you'), ('The follow-up, automatic', 'every step from tonight, firing on its own'), ('You own the list', 'your account, your contacts')],
       GHL, 'BONUS #2: YOUR GOHIGHLEVEL ACCOUNT. $97 A MONTH.\n\n"And if you join today, you also get your GoHighLevel account. This is the back end for your ads. Remember speed to lead, nurture, reminders, the pipeline? This is where all of it lives."\n\n$97 a month, $1,164 a year. Bonus value so far: $4,164.'),
 bonus(3, 'Done-For-You <em>Onboarding.</em>', '$1,000', 'value',
       'You don\'t switch it on alone. A one-on-one call with Chris, your onboarding specialist, who sets it up with you.',
       [('Set up live, with you', 'so you actually know where things are'), ('A2P approved', 'so your texts land instead of silently dying'), ('Everything connected', 'number, email and calendar, switched on')],
       CHRIS, 'BONUS #3: DONE-FOR-YOU ONBOARDING. $1,000.\n\n"And you don\'t set it up alone. Meet Chris, your onboarding specialist. He gets on a call with you and builds it, live, so you know where everything is."\n\nStop on A2P: "That\'s the registration that decides whether your texts land or silently die. None of the follow-up works without it."\n\nBonus value so far: $5,164.'),
 bonus(4, 'Medicare Automation <em>Snapshots.</em>', '$5,000', 'what I paid',
       'The exact funnels running for me right now, refined on more than $100,000 of my own ad spend, loaded into your account.',
       [('Webinar snapshots', 'registration, reminders and replay, built'), ('Lead funnels', 'every page from tonight, already built'), ('Every automation behind them', 'texts, reminders, no-show, 90-day follow-up')],
       SNAP, 'BONUS #4: MEDICARE AUTOMATION SNAPSHOTS. $5,000.\n\n"And you get the snapshots. The webinar funnel, registration, reminders and replay. The lead funnels. And every automation behind them. I know it\'s worth five thousand dollars because that\'s what I paid to have it built."\n\nCHECK: only say $100,000 if that\'s genuinely the ad spend behind these funnels.\n\nBonus value so far: $10,164. Then go to the recap.'),
]

RECAP = '''<!-- ═══════════════════════ RECAP · WHAT YOU GET TODAY ═══════════════════════ -->
<section class="slide wb s-was" data-timer data-kicker="Join today">
  <div class="light"></div>
  <div class="wrap">
    <div>
      <h1 class="head a">Here's what you get <em>if you join today.</em></h1>
      <div class="lst a">
        <div class="core"><i>★</i>The Real Insurance Group community <span>$147/mo</span></div>
        <div><i>01</i>Medicare Marketing Playbook <span>$3,000</span></div>
        <div><i>02</i>Your GoHighLevel Account <span>$97/mo</span></div>
        <div><i>03</i>Done-For-You Onboarding with Chris <span>$1,000</span></div>
        <div><i>04</i>Medicare Automation Snapshots <span>$5,000</span></div>
      </div>
    </div>
    <div class="pr a">
      <p class="k">You pay</p>
      <div class="v">$147<small>/mo</small></div>
      <p>That alone is the best deal in Medicare.</p>
      <p class="turn frag">But there's still one problem.</p>
    </div>
  </div>
<script type="text/plain" class="notes">THE RECAP. LET IT SIT.

"So if you join today: the community, the playbook, your GoHighLevel account, onboarding with Chris, and the snapshots. All for a hundred and forty-seven a month."

"That alone is the best deal in Medicare."

Then reveal the last line, slowly: "But there's still one problem."</script>
</section>'''

GAP = '''<!-- ═══════════════════════ 33 THE GAP ═══════════════════════ -->
<section class="slide wb s-gap2" data-timer data-kicker="The one problem">
  <div class="light"></div>
  <div class="content">
    <h1 class="head a" style="font-size:84px">Knowing what to build is not the same as <em>getting it built.</em></h1>
    <div class="g10 a">''' + ''.join(f'<div class="gs frag{" have" if k == 0 else ""}"><b class="ck">{"✓" if k == 0 else ""}</b><i>{k+1:02d}</i><h3>{t}</h3></div>' for k, t in enumerate(
        ['Campaign idea', 'Landing page', 'Form', 'Pipeline', 'Calendar', 'Text sequence', 'Email sequence', 'Automations', 'Testing', 'Launch'])) + '''
      <div class="ring2 frag"><p class="hand">somebody still has to build all of this.</p></div>
    </div>
    <p class="hand foot3 frag">you have the idea. that's step one of ten. <small>that's where agents get stuck.</small></p>
  </div>
<script type="text/plain" class="notes">THE IMPLEMENTATION GAP.

"Most agents don't fail because they can't understand what I teach. They fail in the gap between knowing what to do and actually getting everything connected."

"You have the campaign idea. That's step one. Then somebody has to build the landing page. The form. The pipeline. The calendar. The text sequence. The email sequence. The automations. Test it. Launch it."

"Somebody still has to build all of this. That's where agents get stuck."</script>
</section>'''

HATICON = {
 'Agent': '<svg viewBox="0 0 60 60"><circle cx="30" cy="20" r="10"/><path d="M12 52c2-12 9-18 18-18s16 6 18 18"/></svg>',
 'Media buyer': '<svg viewBox="0 0 60 60"><path d="M10 26v10l26 10V16z"/><path d="M36 22c6 0 10 4 10 9s-4 9-10 9"/><path d="M16 38l4 12h6l-3-10"/></svg>',
 'Funnel builder': '<svg viewBox="0 0 60 60"><path d="M10 12h40L34 32v14l-8 4V32z"/></svg>',
 'Automation expert': '<svg viewBox="0 0 60 60"><circle cx="30" cy="30" r="8"/><path d="M30 10v6M30 44v6M10 30h6M44 30h6M16 16l4 4M40 40l4 4M16 44l4-4M40 20l4-4"/></svg>',
 'CRM admin': '<svg viewBox="0 0 60 60"><ellipse cx="30" cy="16" rx="16" ry="6"/><path d="M14 16v28c0 3 7 6 16 6s16-3 16-6V16M14 30c0 3 7 6 16 6s16-3 16-6"/></svg>',
 'Tech support': '<svg viewBox="0 0 60 60"><path d="M40 12a10 10 0 0 0-12 12L12 40a4 4 0 0 0 6 6l16-16a10 10 0 0 0 12-12l-6 6-6-2-2-6z"/></svg>',
}
HATS = '''<!-- ═══════════════════════ 34 SIX PEOPLE ═══════════════════════ -->
<section class="slide wb s-hats2" data-timer data-kicker="The one problem">
  <div class="light"></div>
  <div class="content">
    <h1 class="head a">So now you're trying to be <em>six people.</em></h1>
    <div class="h6 a">''' + ''.join(f'<div class="hh frag{" me" if t == "Agent" else ""}"><div class="hi">{HATICON[t]}</div><h3>{t}</h3><p>{d}</p>{"<span class=\'you\'>you signed up for this one</span>" if t == "Agent" else ""}</div>' for t, d in [
        ('Agent', 'Talking to clients. Writing policies.'), ('Media buyer', 'Running and testing the ads.'), ('Funnel builder', 'Pages, forms, calendars.'),
        ('Automation expert', 'Texts, emails, triggers, no-shows.'), ('CRM admin', 'Pipelines, tags, the dashboard.'), ('Tech support', 'When something breaks at 9pm.')]) + '''</div>
    <p class="hand foot3 frag">not because you don't want it. because it's six jobs. so we solved that too.</p>
  </div>
<script type="text/plain" class="notes">SIX PEOPLE.

"This is where agents get stuck. Not because they don't want it. Because now they're trying to be the agent, the media buyer, the funnel builder, the automation expert, the CRM admin, and tech support."

"You signed up for one of those."

Then, slowly: "So we solved that too." Click, and stop talking for a beat.</script>
</section>'''

REVEAL = '''<!-- ═══════════════════════ 35 THE REVEAL ═══════════════════════ -->
<section class="slide wb s-reveal" data-timer data-kicker="Join today · Bonus 5 of 5">
  <div class="light"></div>
  <div class="glow2"></div>
  <div class="wrap">
    <p class="k a">But today, we're adding one more thing</p>
    <div class="bnt a" style="margin:0 auto 34px">''' + GIFTSVG + '''Bonus #5 · Only today</div>
    <h1 class="a">Your Dedicated<br>GoHighLevel <em>Specialist.</em></h1>
    <p class="a">Not a course. Not a ticket. Not a Facebook group. A specialist attached to your business.</p>
  </div>
<script type="text/plain" class="notes">THE REVEAL. ALMOST NO TALKING.

"But today, we're adding one more thing."

Click. Wait two seconds.

"Your dedicated GoHighLevel specialist. Not a course. Not a support ticket. Not a Facebook group where you ask somebody how to do something. A specialist attached to your business, who builds it."</script>
</section>'''

SPEC1 = '''<!-- ═══════════════════════ 36 MEET CHRISTOPHER ═══════════════════════ -->
<section class="slide wb s-meet" data-timer data-kicker="Join today · Bonus 5 of 5">
  <div class="light"></div>
  <div class="content">
    <div class="mtw">
      <div class="mtp a"><div class="ph"><img src="assets/christopher.jpg" alt="Christopher"></div><p class="nm">Christopher<small>GoHighLevel Specialist</small></p></div>
      <div class="mtr">
        <p class="eb a">The specialist behind Real Insurance Group</p>
        <h1 class="head a">Meet <em>Christopher.</em></h1>
        <p class="rb a">He lives inside GoHighLevel accounts: building the funnels, wiring the automations, cleaning up the pipelines and fixing what breaks. And he knows the insurance side, not just the software.</p>
        <div class="mts a">
          <div class="frag"><b>800+</b><span>Webinar funnels launched</span></div>
          <div class="frag"><b>1,000+</b><span>Accounts on his automation</span></div>
          <div class="frag"><b>6–7</b><span>Figure businesses he runs GHL for</span></div>
        </div>
      </div>
    </div>
    <div class="stamp big2s frag"><b>$1,500</b><span>a month, on its own</span></div>
  </div>
<script type="text/plain" class="notes">MEET CHRISTOPHER.

"This is Christopher. He's the GoHighLevel specialist behind the Real Insurance Group."

"He's launched more than 800 webinar funnels. The webinar automation he built is running in over a thousand accounts. He runs GoHighLevel for six and seven-figure businesses. And he knows the insurance side, not just the software."

"A specialist like this costs fifteen hundred dollars a month, on its own. That's what we charge for it by itself."

JOHNNY, CONFIRM BEFORE GOING LIVE: is every member's dedicated specialist Christopher himself, or his team? Say it the true way. These numbers are from his booking page.</script>
</section>

<!-- ═══════════════════════ 36B WHAT THE SPECIALIST BUILDS ═══════════════════════ -->
<section class="slide wb s-req" data-timer data-kicker="Join today · Bonus 5 of 5">
  <div class="light"></div>
  <div class="content">
    <h1 class="head a" style="font-size:80px">You say what you want. <em>It gets built.</em></h1>
    <div class="rqw a">
      <div class="chat">
        <div class="ch-top"><span class="dot"></span>Your specialist<small>Real Insurance Group</small></div>
        <p class="m me frag">I want to run a Part B delay campaign this month.</p>
        <p class="m sp frag">On it. I'll build the landing page, the form, the calendar and the follow-up, and get it ready to launch.</p>
        <div class="sts frag"><span>Landing page ✓</span><span>Form ✓</span><span>Calendar ✓</span><span>Follow-up ✓</span><span class="g">Ready to launch</span></div>
      </div>
      <div class="bl6">''' + ''.join(f'<div class="frag"><i>{k+1:02d}</i><b>{t}</b><span>{d}</span></div>' for k, (t, d) in enumerate([
        ('Webinar funnels', 'registration, reminders and replays'), ('Landing pages & calendars', 'built on what converts for agents now'), ('Follow-up & automations', 'speed to lead, reminders, no-show recovery'),
        ('Back-end systems', 'pipelines, tags, calendars, integrations'), ('Cross-sell & retention', 'dental, vision, final expense, referrals'), ('Old-lead reactivation', 'wake up the leads already in your CRM')])) + '''</div>
    </div>
  </div>
<script type="text/plain" class="notes">WHAT THE SPECIALIST BUILDS.

Left: "This is how it works. You say what you want. 'I want to run a Part B delay campaign this month.' Your specialist builds the landing page, the form, the calendar and the follow-up, and gets it ready to launch."

Right, walk the six: webinar funnels; landing pages and calendars; follow-up and automations; back-end systems; cross-sell and retention; old-lead reactivation.

"Every single thing I taught you tonight, built for you."

BEFORE GOING LIVE: have the internal scope written down (requests per month, turnaround, what's extra). If someone asks "is it unlimited?", answer with the real scope. The chat on the left is an illustration.</script>
</section>'''

DELTA = '''<!-- ═══════════════════════ 37 THE DELTA ═══════════════════════ -->
<section class="slide wb s-delta2" data-timer data-kicker="The math that matters">
  <div class="light"></div>
  <div class="content">
    <h1 class="head a">Here's the only math<br>that <em>matters.</em></h1>
    <div class="bars a">
      <div class="br frag"><div class="t">The community<small>The main thing</small></div><div class="tr"><i class="base" style="width:9.8%"></i></div><div class="v">$147<small>/mo</small></div></div>
      <div class="br frag"><div class="t">Today, the full package<small>Every bonus, plus your specialist</small></div><div class="tr"><i class="base" style="width:9.8%"></i><i class="add" style="width:10.2%"><em>+$153</em></i></div><div class="v g">$300<small>/mo</small></div></div>
      <div class="br frag dim"><div class="t">A GHL specialist on its own<small>What we charge for it alone</small></div><div class="tr"><i class="ext" style="width:100%"></i></div><div class="v">$1,500<small>/mo</small></div></div>
    </div>
    <div class="foot2 frag">For <span>$153 more</span>, you get the piece that costs <span>$1,500 a month</span> on its own.</div>
  </div>
<script type="text/plain" class="notes">THE DECISION MATH.

"The community is a hundred and forty-seven a month. Today, the full package, every bonus plus your own specialist, is three hundred."

Point at the gold sliver: "That gold piece is the difference. A hundred and fifty-three dollars."

"And here's what we charge for a GoHighLevel specialist on its own: fifteen hundred a month."

Pause. Let the picture do the work.</script>
</section>

<!-- ═══════════════════════ SEPARATE · OUTSIDE THIS WEBINAR ═══════════════════════ -->
<section class="slide wb s-sep" data-timer data-kicker="Only on this webinar">
  <div class="light"></div>
  <div class="content">
    <h1 class="head a">Outside this webinar, <em>it's all separate.</em></h1>
    <div class="spw2 a">
      <div class="spl2">
        <p class="k">Bought separately</p>
        <div class="r frag"><span>The community</span><b>$147<small>/mo</small></b></div>
        <div class="r frag"><span>Dedicated GoHighLevel Specialist</span><b>$1,500<small>/mo</small></b></div>
        <div class="r frag"><span>GoHighLevel Account</span><b>$97<small>/mo</small></b></div>
        <div class="r frag"><span>Medicare Marketing Playbook</span><b>$3,000</b></div>
        <div class="r frag"><span>Done-For-You Onboarding</span><b>$1,000</b></div>
        <div class="r frag"><span>Medicare Automation Snapshots</span><b>$5,000</b></div>
        <div class="tot frag"><span>Total</span><b>$9,000 <small>+ $1,744/mo</small></b></div>
      </div>
      <div class="spr2 frag">
        <p class="k">On this webinar only</p>
        <h3>The full package</h3>
        <div class="big">$300<small>/mo</small></div>
        <p class="hand">everything on the left. one price. only today.</p>
      </div>
    </div>
  </div>
<script type="text/plain" class="notes">OUTSIDE THIS WEBINAR, IT'S ALL SEPARATE.

"Here's the thing. Outside of this webinar, all of this is separate. The community is one-forty-seven. The specialist is fifteen hundred a month. The account, ninety-seven. The playbook, the onboarding, the snapshots, nine thousand dollars."

"On this webinar only, you get the full package. Everything on the left. Three hundred dollars a month."

JOHNNY: only say this if it's how it will actually be sold after tonight.</script>
</section>'''

PRICE = '''<!-- ═══════════════════════ 38 THE PRICE ═══════════════════════ -->
<section class="slide wb s-offer" data-timer data-kicker="The price">
  <div class="light"></div>
  <div class="wrap">
    <p class="lead a">The community, every bonus, and your specialist.</p>
    <h1 class="price a">$300<small>/mo</small></h1>
    <p class="all a">Nothing up front. No contract. Cancel anytime.</p>
    <p class="less a">We teach you the Medicare marketing. We give you the software and the systems. And we give you the person who builds it. <b>Only on this webinar.</b></p>
  </div>
<script type="text/plain" class="notes">THE PRICE.

"The community. Every bonus. And your specialist. Three hundred dollars a month. Only on this webinar."

JOHNNY: confirm the terms are true for the $300 version before going live (nothing up front, no contract, cancel anytime).</script>
</section>

<!-- ═══════════════════════ SEATS · 12 THIS WEEK ═══════════════════════ -->
<section class="slide wb s-seats" data-timer data-kicker="Why there's a limit">
  <div class="light"></div>
  <div class="content">
    <h1 class="head a">We're only opening <em><span data-spots>12</span> seats.</em></h1>
    <div class="stw a">
      <div class="seatg">''' + ''.join('<i></i>' for _ in range(12)) + '''</div>
      <div class="stx">
        <div class="ln frag"><i>01</i><p><b>That's our onboarding capacity this week.</b> Chris sets up every account personally, live, one on one.</p></div>
        <div class="ln frag"><i>02</i><p><b>Every seat gets a real specialist.</b> That only works if each one has a manageable number of agents.</p></div>
        <div class="ln frag"><i>03</i><p><b>When the seats are gone, the bonuses go with them.</b> Same as when the timer hits zero.</p></div>
      </div>
    </div>
  </div>
<script type="text/plain" class="notes">12 SEATS. REAL SCARCITY.

"We're only opening twelve seats. That's our onboarding capacity this week: Chris sets up every account personally, live, one on one. And every seat gets a real specialist."

"When the seats are gone, the bonuses go with them. Same as when that timer hits zero."

THE NUMBER MUST BE REAL. Change it in one place: the SPOTS line at the top of the deck script.

As people join during Q&A, call it out: "Two gone. Ten left."</script>
</section>'''

FULL = '''<!-- ═══════════════════════ 39 EVERYTHING, ONE SCREEN ═══════════════════════ -->
<section class="slide wb s-full3" data-timer data-kicker="Everything, on one screen">
  <div class="light"></div>
  <div class="content">
    <h1 class="head a">Everything you get <em>if you join today.</em></h1>
    <div class="f3 a">
      <div class="f3c core"><p class="k">The main thing</p><h3>The Real Insurance Group community</h3><p>The classroom, live calls every business day, and the wins.</p><b>$147<small>/mo</small></b></div>
      <div class="f3c"><p class="k">Bonus #1</p><h3>Medicare Marketing Playbook</h3><b>$3,000</b></div>
      <div class="f3c"><p class="k">Bonus #2</p><h3>Your GoHighLevel Account</h3><b>$97<small>/mo</small></b></div>
      <div class="f3c"><p class="k">Bonus #3</p><h3>Onboarding with Chris</h3><b>$1,000</b></div>
      <div class="f3c"><p class="k">Bonus #4</p><h3>Automation Snapshots</h3><b>$5,000</b></div>
      <div class="f3c spec"><p class="k">Bonus #5 · Only today</p><h3>Dedicated GoHighLevel Specialist</h3><b>$1,500<small>/mo</small></b></div>
    </div>
    <div class="f3bar a">
      <div><p class="k">Separately</p><div class="was">$9,000 + $1,744/mo</div></div>
      <div><p class="k">Today</p><div class="now">$300<small>/mo</small></div></div>
      <div class="jn"><p class="k">How to join</p><div class="url">The link is in the chat.</div></div>
    </div>
  </div>
<script type="text/plain" class="notes">THE WHOLE OFFER, ONE SCREEN. THE SLIDE PEOPLE SCREENSHOT.

Let them read for a few seconds.

"The community, the main thing. Bonus one, the playbook. Bonus two, your GoHighLevel account. Bonus three, onboarding with Chris. Bonus four, the snapshots. And bonus five, only today, your own GoHighLevel specialist."

"Separately, nine thousand dollars plus seventeen hundred a month. Today, three hundred."

Say it twice: "The link is in the chat." Come back to this slide during Q&A.</script>
</section>'''

# the rest keeps its content, gets the timer and Chris
MATH = blk['41 THE MATH'].replace('<section class="slide wb s-math"', '<section class="slide wb s-math" data-timer')
NEXT = blk['42 WHAT HAPPENS NEXT'].replace('<section class="slide wb s-next"', '<section class="slide wb s-next" data-timer').replace('David', 'Chris')
NEXT = NEXT.replace('<h1 class="head a">Here\'s what happens next.<br><em>The link is in the chat.</em></h1>', '<h1 class="head a">Here\'s what happens next.<br><em>The link is in the chat.</em></h1>')
AMA = blk['43 AMA'].replace('<section class="slide s-ama"', '<section class="slide wb s-ama" data-timer').replace('Specialist accounts go in the order people join.', 'Seats and bonuses go in the order people join.')

tail_new = '\n\n'.join([blk['CHAPTER · How we help'], CORE] + BON + [RECAP, GAP, HATS, REVEAL, SPEC1, DELTA, PRICE, FULL, MATH, NEXT, AMA])
s = head + tail_new + '\n'

# ── whole deck in the light style
for a in ['<section class="slide s-title"', '<section class="slide" data-kicker="Before we start"', '<section class="slide s-who"', '<section class="slide s-why"',
          '<section class="slide s-five"', '<section class="slide s-proof"']:
    rep(a, a.replace('class="slide', 'class="slide wb'))
s = s.replace('class="slide s-loop"', 'class="slide wb s-loop"')
# ── agents, not only seniors, on the openers
rep('<img src="assets/ch-media.jpg" alt="" style="object-position:66% 40%">', '<img src="assets/ch-ads2.jpg" alt="" style="object-position:62% 40%">')
rep('<img src="assets/ch-mechanism.jpg" alt="" style="object-position:64% 40%">', '<img src="assets/ch-funnel2.jpg" alt="" style="object-position:66% 35%">')
rep('"Part three. Ads. Your clients are on their phones every day, just like him. I\'m going to show you how to run the ads, and how to read them like a pro."',
    '"Part three. Ads. I\'m going to show you how to run the ads, and how to read them like a pro."')

# ── the 30-day proof slide, the focal point of the Ads chapter
P30 = """<!-- ═══════════════════════ PROOF · LAST 30 DAYS ═══════════════════════ -->
<section data-part="3" class="slide wb s-p30" data-kicker="03 · Ads · Our numbers">
  <div class="light"></div>
  <div class="content">
    <div class="p30top a"><span class="date">Last 30 days · Sep 6 – Oct 5, 2026</span><span class="src">Straight out of Ads Manager</span></div>
    <h1 class="head a">3,459 leads at <em>$1.64 each.</em></h1>
    <div class="p30s a">
      <div class="frag big"><b><span class="count" data-to="3459" data-comma="1">3,459</span></b><span>Leads</span></div>
      <div class="frag big g"><b><span class="count" data-to="1.64" data-prefix="$" data-decimals="2">$1.64</span></b><span>Cost per lead</span></div>
      <div class="frag"><b><span class="count" data-to="5672.92" data-prefix="$" data-decimals="2" data-comma="1">$5,672.92</span></b><span>Total spent</span></div>
      <div class="frag"><b><span class="count" data-to="168330" data-comma="1">168,330</span></b><span>People reached</span></div>
    </div>
    <div class="p30shot frag"><img src="assets/ads-30d-row.jpg" alt="Ads Manager, last 30 days"></div>
    <p class="hand p30n frag">frequency 1.38: still mostly new people. that's a prospector doing its job.</p>
  </div>
<script type="text/plain" class="notes">OUR NUMBERS. THE FOCAL POINT. SLOW DOWN.

"This is our ad account, last thirty days. September 6th to October 5th."

Let the counters run, then read them out:
"Three thousand four hundred fifty-nine leads. A dollar sixty-four a lead. Fifty-six hundred dollars spent. A hundred and sixty-eight thousand people reached."

Then tie it to what you just taught: "Look at the frequency. 1.38. That means it's still reaching mostly new people. That's a prospector doing its job, and that's why we leave it alone."

JOHNNY, SAY WHAT IT IS: this is the "Veteran Video Ads" campaign (lead forms). If anyone asks, say so plainly. Don't call it a Medicare campaign unless it is.</script>
</section>"""
s = s.replace('<!-- ═══════════════════════ 12 MEDIA · THE AD ACCOUNT', P30 + '\n\n<!-- ═══════════════════════ 12 MEDIA · THE AD ACCOUNT', 1)

open(P, 'w', encoding='utf-8').write(s)
print('sections', s.count('<section'), 'wb', s.count('class="slide wb'), 'timer', s.count('data-timer'))
