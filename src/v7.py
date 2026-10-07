# v7: round-7 notes. $1.64 client account is the focal proof, $5.92 demoted; automations video moves to
# Backend ("this is where GoHighLevel comes in"); campaign-types slide; the offer re-led by the Skool group
# outcome; 10-minute timer; 12 people today; a real-looking GHL account; Meet David; outcome slide;
# final full-stack slide after Q&A. Runs after v6.py (reads and rewrites src/slides.html).
import re, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(ROOT, 'src/slides.html')
s = open(P, encoding='utf-8').read()

def rep(a, b, n=1):
    global s
    assert a in s, 'missing: ' + a[:90]
    s = s.replace(a, b, n) if n else s.replace(a, b)

def take(marker):
    """remove a block by its comment marker and return it"""
    global s
    m = re.search(r'<!-- ═+ ' + re.escape(marker) + r' ═.*?</section>\s*', s, re.S)
    assert m, 'block: ' + marker
    s = s[:m.start()] + s[m.end():]
    return m.group(0).strip()

def put_after(marker, html):
    global s
    m = re.search(r'<!-- ═+ ' + re.escape(marker) + r' ═.*?</section>', s, re.S)
    assert m, 'anchor: ' + marker
    s = s[:m.end()] + '\n\n' + html + s[m.end():]

def put_before(marker, html):
    global s
    i = s.index('<!-- ═══════════════════════ ' + marker)
    s = s[:i] + html + '\n\n' + s[i:]

# ═══ 1. the proof: $1.64 is the focal point, $5.92 is "another one" ═══
rep('<span class="src">Straight out of Ads Manager</span>', '<span class="src">one of our clients\' accounts · targeting veterans</span>')
rep('data-kicker="03 · Ads · Our numbers"', 'data-kicker="03 · Ads · Client results"')
rep('"This is our ad account, last thirty days. September 6th to October 5th."',
    '"This is one of our clients\' accounts. Last thirty days, September 6th to October 5th. This client is specifically targeting veterans."')
rep('JOHNNY, SAY WHAT IT IS: this is the "Veteran Video Ads" campaign (lead forms). If anyone asks, say so plainly. Don\'t call it a Medicare campaign unless it is.',
    'SAY WHAT IT IS: one of our clients\' accounts, the "Veteran Video Ads" campaign, lead forms, targeting veterans. Then go to the next slide: "Here\'s another one."')
rep('<h1 class="head a" style="font-size:64px">Here\'s the account. Now, <em>what built it.</em></h1>',
    '<h1 class="head a" style="font-size:72px">Here\'s another one. <em>Different audience, different numbers.</em></h1>')
rep('<p class="sub a" style="margin-top:12px;font-size:24px">Straight out of Ads Manager. A mix of webinars, Medicare Supplement and dental.</p>',
    '<p class="sub a" style="margin-top:12px;font-size:24px">Webinars, Medicare Supplement and dental. What a lead costs depends on who you\'re talking to.</p>')
s = re.sub(r'THE AD ACCOUNT\. PROOF, THEN LESSON\..*?(</script>)', lambda m: '''ANOTHER ACCOUNT. DIFFERENT AUDIENCE, DIFFERENT NUMBERS.

"Here's another one. This account runs webinars, Medicare Supplement and dental. Different audience, different numbers."

"That's the point. What you pay for a lead depends on who you're talking to and which campaign you run. Veterans on a lead form cost one thing. A Med Supp webinar costs another. You match the campaign to your ICP, and then you read the numbers the way I just showed you."

Don't make this number the focus. The $1.64 slide is the headline.''' + m.group(1), s, count=1, flags=re.S)
rep('<h1 class="head a" style="font-size:80px">What built <em>$5.92</em> a lead.</h1>', '<h1 class="head a" style="font-size:80px">What builds <em>numbers like these.</em></h1>')
rep('<b>The average is the skill</b><span>$5.92 isn\'t one lucky ad. It\'s a full team of ads, each doing its job.</span>',
    '<b>The average is the skill</b><span>Good numbers aren\'t one lucky ad. They\'re a full team of ads, each doing its job.</span>')
rep('WHAT BUILT $5.92. THE HONEST VERSION.', 'WHAT BUILDS NUMBERS LIKE THESE. THE HONEST VERSION.')
s = s.replace('The average is $5.92 because the account works as a team.', 'The average is good because the account works as a team.')

# ── the math examples stop leaning on $5.92: a round $10 example lead
rep('<div class="t">Leads<small>at $5.92 each</small></div>', '<div class="t">Leads<small>at $10 each</small></div>')
rep('<div class="c">$592 spent</div>', '<div class="c">$1,000 spent</div>')
rep('<p class="k">Cost to get each client</p><div class="big">$74</div>', '<p class="k">Cost to get each client</p><div class="big">$125</div>')
rep('"A hundred leads at $5.92 is $592. Thirty book. Twenty-one show. Eight become clients. At $694 first-year on Medicare Advantage, that\'s $5,552. So each client cost you about seventy-four dollars."',
    '"Say your leads cost ten dollars. A hundred leads is a thousand dollars. Thirty book. Twenty-one show. Eight become clients. At $694 first-year on Medicare Advantage, that\'s $5,552. So each client cost you about a hundred and twenty-five dollars."')
rep('<p class="sub a">The client cost $74. Watch what the same person is worth when you do it right.</p>', '<p class="sub a">The client cost $125. Watch what the same person is worth when you do it right.</p>')
s = s.replace('"The lead cost seventy-four dollars.', '"The client cost a hundred and twenty-five dollars.')

# ═══ 2. the automations video leaves the Funnel chapter and lands in Backend ═══
vid = take('16 MECHANISM · BUILT (VIDEO)')
vid = vid.replace('data-part="4"', 'data-part="5"').replace('data-kicker="04 · Funnel · Built"', 'data-kicker="05 · Backend · The system"')
vid = vid.replace('<h1 class="head a" style="font-size:72px">This is what it looks like built.</h1>', '<h1 class="head a" style="font-size:76px">This is where <em>GoHighLevel</em> comes in.</h1>')
vid = vid.replace('<p class="sub a" style="margin-top:16px;font-size:26px">The same seven steps, live in an account. Pages in front, automations behind.</p>',
                  '<p class="sub a" style="margin-top:16px;font-size:26px">Every piece of the back end you just saw runs inside one system.</p>')
vid = vid.replace('<div class="row"><h4>Four pages</h4><p>Registration, thank-you, booking, confirmation.</p></div>', '<div class="row"><h4>The follow-up, on autopilot</h4><p>Speed to lead, nurture, reminders, no-shows.</p></div>')
vid = vid.replace('<div class="row"><h4>Automations behind them</h4><p>The text four minutes after someone registers. The reminder the night before.</p></div>', '<div class="row"><h4>The pipeline</h4><p>Every lead in one place, and who needs you today.</p></div>')
vid = re.sub(r'<script type="text/plain" class="notes">.*?</script>', lambda m: '''<script type="text/plain" class="notes">THIS IS WHERE GOHIGHLEVEL COMES IN.

"Everything I just showed you on the back end: speed to lead, the nurture sequence, reminders, no-shows, the pipeline. This is where it lives. GoHighLevel."

Talk over the video: "These are the automations, firing whether you're at your desk or not. Nothing on this screen depends on you remembering."

Don't sell it yet. You're showing what the back end looks like when it's built.</script>''', vid, flags=re.S)
put_after('B5 · THE PIPELINE', vid)

# ═══ 3. the campaigns you can run, matched to your ICP ═══
CAMPS = [('T65', 'Turning 65', 'Ad → T65 guide or checklist → call', 'People turning 65 in the next few months.'),
         ('WEB', 'Webinars', 'Ad → register → live class → book', 'People who want to learn before they talk.'),
         ('FORM', 'Straight lead forms', 'Ad → instant form → you call fast', 'Volume. Needs fast follow-up.'),
         ('VSL', 'VSL funnels', 'Ad → video page → book a call', 'People who need trust before a call.'),
         ('BOOK', 'Opt-in + book a call', 'Ad → opt-in page → calendar', 'People who are ready to talk now.')]
CAMP = '''<!-- ═══════════════════════ MARKET · THE CAMPAIGNS ═══════════════════════ -->
<section data-part="1" class="slide wb s-camp" data-kicker="01 · Market · The campaigns">
  <div class="light"></div>
  <div class="content">
    <h1 class="head a" style="font-size:80px">There's more than one way to <em>run Medicare marketing.</em></h1>
    <p class="sub a" style="font-size:27px;margin-top:16px">Different campaigns work for different people. Pick the one that fits your ICP: your ideal client.</p>
    <div class="cpg a">''' + ''.join(f'<div class="cp frag"><span class="tg">{t}</span><h3>{n}</h3><p class="fl">{f}</p><p class="bf"><b>Best for</b>{b}</p></div>' for t, n, f, b in CAMPS) + '''</div>
    <p class="hand foot3 frag">the campaign that works for your ICP is the one you run first.</p>
  </div>
<script type="text/plain" class="notes">THE CAMPAIGNS YOU CAN RUN. THIS IS WHERE YOU SOUND LIKE THE EXPERT.

"Most agents think Medicare marketing is one thing. It's not. There are different campaigns, and they work for different people."

Walk the five:
"Turning 65: an ad, a guide or a checklist, then a call. For people turning 65 in the next few months."
"Webinars: they register, they come to a live class, then they book. For people who want to learn before they talk to anyone."
"Straight lead forms: they fill out a form right inside Facebook and you call them fast. Volume. But you have to be fast."
"VSL funnels: a video page, then they book. For people who need to trust you before a call."
"Opt-in and book a call: a simple page and a calendar. For people who are ready to talk now."

"The question isn't which one is best. It's which one works for YOUR ideal client. That's the one you run first."

Johnny: adjust the "best for" lines to how you actually use each one.</script>
</section>'''
put_after('07 MARKET · NOBODY IS CALLING', CAMP)

# ═══ 4. the offer, led by the Skool group's outcome ═══
rep('<section class="slide wb s-core1" data-kicker="How we help · The main thing">', '<section class="slide wb s-core1" data-kicker="How we help · Our Skool group">')
rep('<span class="mainpill a">The main thing</span>', '<span class="mainpill a">How we help</span>')
rep('<h1 class="head a">The Real Insurance Group <em>community.</em></h1>', '<h1 class="head a">Our Skool group helps you <em>launch your first campaign.</em></h1>')
rep('<p class="rb a">Everything you need to market, sell and grow a Medicare business, in one place, with people who are doing it right now.</p>',
    '<p class="rb a">Start to finish. The community, the courses and the live calls behind it, all pointed at one outcome.</p>')
rep('<div class="frag"><b>The classroom</b><span>Hundreds of hours of training, unlocked on day one.</span></div>', '<div class="frag"><b>Launch your first campaign</b><span>From picking your person to the first booked call.</span></div>')
rep('<div class="frag"><b>Live every business day</b><span>Marketing, sales, AI and annuities, live.</span></div>', '<div class="frag"><b>Cross-sell your existing book</b><span>The money already sitting in the clients you have.</span></div>')
rep('<div class="frag"><b>The wins</b><span>Agents posting results every day.</span></div>', '<div class="frag"><b>Build a book of business</b><span>One that renews, and keeps paying you.</span></div>')
s = re.sub(r'THE CORE\. THE COMMUNITY IS THE PRODUCT\..*?(</script>)', lambda m: '''HOW WE HELP: OUR SKOOL GROUP.

"So how do we help you? It starts with our Skool group."

"And here's what it's for. It helps you launch your first campaign, start to finish. Not only launch it: it teaches you to cross-sell the book you already have, and to build a book of business that renews."

"Behind it there's the community, the courses, and the live calls. Let me show you each one."

Talk over the video: "This is what you log into. Today."''' + m.group(1), s, count=1, flags=re.S)
rep('<section class="slide wb s-class" data-kicker="How we help · The classroom">', '<section class="slide wb s-class" data-kicker="Our Skool group · The courses">')
rep('<section class="slide wb s-live" data-kicker="How we help · The community">', '<section class="slide wb s-live" data-kicker="Our Skool group · The community">')
rep('<section class="slide wb s-offer s-corep" data-kicker="How we help · The community">', '<section class="slide wb s-offer s-corep" data-kicker="Our Skool group">')
rep('<p class="lead a">The community. Everything inside it.</p>', '<p class="lead a">Our Skool group. Everything inside it.</p>')
rep('<p class="less a">That\'s the main thing. If that\'s all you ever got, it would already be worth it.</p>',
    '<p class="less a">That alone helps you launch your first campaign. <b>But I\'m not stopping there.</b></p>')
s = re.sub(r'THE PRICE OF THE CORE\..*?(</script>)', lambda m: '''THE PRICE OF THE SKOOL GROUP. THEN THE TURN.

"Our Skool group, everything inside it: a hundred and forty-seven dollars a month. Nothing up front, cancel anytime. That alone helps you launch your first campaign."

Then lean in: "But I'm not stopping there. Because you stayed with me tonight, I want to do something just for you."

Click to the gift slide.''' + m.group(1), s, count=1, flags=re.S)

# gift: 10 minutes, and a first, small mention of the 12
rep('<p class="hand a">the clock starts now. you have 15 minutes.</p>', '<p class="hand a">the clock starts now: 10 minutes. and we\'re only taking 12 people today.</p>')
rep('PRESS T (or click the timer in the corner) to start the 15-minute clock.', 'PRESS T (or click the timer in the corner) to start the 10-minute clock.')
rep('"They\'re not on the website. They\'re not in the follow-up email. They\'re only for the people here right now. And the clock starts now: fifteen minutes."',
    '"They\'re not on the website. They\'re not in the follow-up email. They\'re only for the people here right now. The clock starts now: ten minutes. And we\'re only taking twelve people today. I\'ll tell you why in a minute."')

# ── bonus #2: a GoHighLevel account that looks like one
NAV = ['Launchpad', 'Dashboard', 'Conversations', 'Calendars', 'Contacts', 'Opportunities', 'Marketing', 'Automation', 'Sites', 'Reporting']
GHL = '''<div class="ghl"><div class="gs"><div class="gl"><i></i>Real Insurance CRM</div>''' + ''.join(f'<p class="{"on" if n == "Opportunities" else ""}"><i></i>{n}</p>' for n in NAV) + '''</div>
<div class="gm"><div class="gt"><b>Opportunities</b><span>Medicare pipeline</span><u>+ Add opportunity</u></div>
<div class="gk"><div><small>New leads</small><b>42</b></div><div><small>Booked</small><b>18</b></div><div><small>Clients</small><b>9</b></div></div>
<div class="gp">''' + ''.join(f'<div class="gc"><p>{c}</p>' + ''.join('<i></i>' for _ in range(k)) + '</div>' for c, k in [('New lead', 4), ('Contacted', 3), ('Booked', 3), ('Showed', 2), ('Client', 2)]) + '''</div></div></div>'''
s = re.sub(r'<div class="g4">.*?</div>(?=<div class="stamp"><b>\$97)', lambda m: GHL, s, count=1, flags=re.S)
rep('<p class="rb a">This is the back end for your ads. Every lead, every follow-up and every booking, in one place.</p>',
    '<p class="rb a">Your own account. It\'s everything: the back end of everything we talked about tonight, in one place.</p>')

# ── bonus #3: Meet David
DAVID = '''<div class="pcard"><div class="ph mono"><span>D</span></div><div class="pi"><p class="k">Your onboarding specialist</p><h3>Meet David.</h3>
<div class="ck">''' + ''.join(f'<p><i>✓</i>{t}</p>' for t in ['Sets your account up, live, with you', 'Gets you A2P approved, so texts land', 'Connects your number, email and calendar']) + '</div></div></div>'
s = re.sub(r'<div class="pcard"><div class="ph"><img src="assets/chris.png".*?</div></div></div>', lambda m: DAVID, s, count=1, flags=re.S)
rep('<p class="rb a">You don\'t switch it on alone. A one-on-one call with Chris, your onboarding specialist, who sets it up with you.</p>',
    '<p class="rb a">Typically a $1,000 setup. A one-on-one call with David, who sets it up live with you and gets everything connected.</p>')
rep('"And you don\'t set it up alone. Meet Chris, your onboarding specialist. He gets on a call with you and builds it, live, so you know where everything is."',
    '"And you don\'t set it up alone. Meet David. Onboarding is typically a thousand dollars. He gets on a call with you, sets it up live, and gets everything connected."')
s = re.sub(r'\bChris\b', 'David', s)

# ── bonus #4: webinar + lead gen snapshots
s = s.replace('<li class="frag"><b>Lead funnels</b>every page from tonight, already built</li>', '<li class="frag"><b>Lead gen snapshots</b>lead forms, opt-ins and booking pages, built</li>')
s = s.replace('<span>Lead funnels</span>', '<span>Lead gen snapshot</span>')

# ═══ 5. Christopher knows the front end too ═══
rep('<p class="rb a">He lives inside GoHighLevel accounts: building the funnels, wiring the automations, cleaning up the pipelines and fixing what breaks. And he knows the insurance side, not just the software.</p>',
    '<p class="rb a">He builds the funnels, wires the automations and fixes what breaks. And because he\'s launched so many webinars and funnels, he knows the front end too, not just the software.</p>')

# ═══ 6. 12 people today ═══
rep('<h1 class="head a">We\'re only opening <em><span data-spots>12</span> seats.</em></h1>', '<h1 class="head a">We\'re only accepting <em><span data-spots>12</span> people today.</em></h1>')
rep('<b>When the seats are gone, the bonuses go with them.</b> Same as when the timer hits zero.', '<b>When the 12 are gone, the bonuses go with them.</b> Same as when the timer hits zero.')
rep('"We\'re only opening twelve seats. That\'s our onboarding capacity this week: David sets up every account personally, live, one on one. And every seat gets a real specialist."',
    '"We\'re only accepting twelve people today. That\'s our onboarding capacity this week: David sets up every account personally, live, one on one. And every one of you gets a real specialist."')

# ═══ 7. the outcome ═══
NEXT_NEW = '''<!-- ═══════════════════════ 42 WHAT HAPPENS NEXT ═══════════════════════ -->
<section class="slide wb s-out" data-timer data-kicker="The outcome">
  <div class="light"></div>
  <div class="content">
    <h1 class="head a">The outcome: <em>your campaign, launched.</em></h1>
    <p class="rb a">You launch and build your campaign, with someone who builds the funnels, walks you through the back end, and knows the front end because he's built hundreds of them.</p>
    <div class="otw a">
      <div class="ot frag"><i>01</i><h3>Onboarding with David</h3><p>Your account set up live, A2P approved, everything connected.</p></div>
      <div class="ot frag"><i>02</i><h3>Your specialist builds it</h3><p>The funnel, the calendar, the follow-up, the automations.</p></div>
      <div class="ot frag"><i>03</i><h3>You launch</h3><p>Your first campaign, live, with the playbook and the live calls behind you.</p></div>
      <div class="ot gold frag"><i>04</i><h3>You build the book</h3><p>Cross-sell what you have. Add clients who renew.</p></div>
    </div>
  </div>
  <div class="rail"><div class="p">$300<small>/mo</small></div><div class="d"></div><div class="u"><small>How to join</small>The link is in the chat.</div></div>
<script type="text/plain" class="notes">THE OUTCOME. MAKE IT CONCRETE.

"Here's what actually happens when you join. First, onboarding with David: your account set up live, everything connected. Then your specialist builds it: the funnel, the calendar, the follow-up. Then you launch your first campaign, with the playbook and the live calls behind you. And then you build the book: cross-sell what you have, add clients who renew."

"You're not buying information. You're getting your campaign launched, with someone who builds it and knows the front end too."

"The link is in the chat."</script>
</section>'''
s = re.sub(r'<!-- ═+ 42 WHAT HAPPENS NEXT ═.*?</section>', lambda m: NEXT_NEW, s, count=1, flags=re.S)

# ═══ 8. the final slide: the whole stack, visually, with the timer ═══
MINI_BOOK = '<div class="mbk"><b>The Medicare<br>Marketing<br><em>Playbook.</em></b></div>'
FINAL = '''<!-- ═══════════════════════ FINAL · THE FULL STACK ═══════════════════════ -->
<section class="slide wb s-final" data-timer data-kicker="Everything you get today">
  <div class="light"></div>
  <div class="content">
    <h1 class="head a">Everything you get <em>if you join today.</em></h1>
    <div class="fg a">
      <div class="fc core"><div class="fv"><img src="assets/skool-feed-poster.jpg" alt=""></div><p class="k">Our Skool group</p><h3>Community, courses, live calls</h3><b>$147<small>/mo</small></b></div>
      <div class="fc"><div class="fv bk">''' + MINI_BOOK + '''</div><p class="k">Bonus #1</p><h3>Medicare Marketing Playbook</h3><b>$3,000</b></div>
      <div class="fc"><div class="fv ui"><span></span><span></span><span></span><span></span><span></span></div><p class="k">Bonus #2</p><h3>Your GoHighLevel Account</h3><b>$97<small>/mo</small></b></div>
      <div class="fc"><div class="fv mono2"><span>D</span></div><p class="k">Bonus #3</p><h3>Onboarding with David</h3><b>$1,000</b></div>
      <div class="fc"><div class="fv"><img src="assets/crm-funnels.jpg" alt="" style="object-position:24% 40%"></div><p class="k">Bonus #4</p><h3>Webinar + lead gen snapshots</h3><b>$5,000</b></div>
      <div class="fc spec"><div class="fv"><img src="assets/christopher.jpg" alt="" style="object-position:center 25%"></div><p class="k">Bonus #5 · Only today</p><h3>Dedicated GoHighLevel Specialist</h3><b>$1,500<small>/mo</small></b></div>
    </div>
    <div class="fbar a">
      <div><p class="k">Separately</p><div class="was">$9,000 + $1,744/mo</div></div>
      <div><p class="k">Today only</p><div class="now">$300<small>/mo</small></div></div>
      <div><p class="k">Only</p><div class="seats"><span data-spots>12</span> people today</div></div>
      <div class="jn"><p class="k">How to join</p><div class="url">The link is in the chat.</div></div>
    </div>
  </div>
<script type="text/plain" class="notes">THE FULL STACK. LEAVE THIS UP FOR THE REST OF THE CALL.

This is the last slide. It stays on screen while you take questions, with the timer running in the corner.

Every few questions, walk it again: "Our Skool group. The playbook. Your GoHighLevel account. Onboarding with David. The snapshots. And today only, your own GoHighLevel specialist. Separately, nine thousand dollars plus seventeen hundred a month. Today, three hundred. Twelve people. The link is in the chat."

Call the count as people join: "Two gone. Ten left."</script>
</section>'''
put_after('43 AMA', FINAL)

open(P, 'w', encoding='utf-8').write(s)
print('sections', s.count('<section'), 'timer', s.count('data-timer'), 'chris left', len(re.findall(r'\bChris\b', s)))
