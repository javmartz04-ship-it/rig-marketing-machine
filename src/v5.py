# v5: Javier's round-5 notes. Funnel/closer copy without invented specifics, account built his way,
# funnel psychology, agent photo on the offer opener, and the offer rebuilt as full-color bonuses.
# Runs after v4.py (reads and rewrites src/slides.html).
import re, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(ROOT, 'src/slides.html')
s = open(P, encoding='utf-8').read()

def rep(a, b, count=1):
    global s
    assert a in s, 'missing: ' + a[:80]
    s = s.replace(a, b) if count == 0 else s.replace(a, b, count)

def block(marker_regex, new):
    global s
    pat = re.compile(r'<!-- ═+ ' + marker_regex + r'.*?</section>', re.S)
    assert pat.search(s), 'block not found: ' + marker_regex
    s = pat.sub(lambda m: new, s, count=1)

# ── A2 every ad has a job: no invented behaviours
rep('<p class="hand">clicked, watched, registered → <b>warming ads</b></p>', '<p class="hand">warming up to you → <b>warming ads</b></p>')
rep('<p class="hand">already talked to you → <b>closer ads</b></p>', '<p class="hand">ready to buy → <b>closer ads</b></p>')
rep('"Picture a funnel. At the top, strangers. People who\'ve never heard of you. In the middle, people who are interested: they clicked, watched a video, registered for a class. At the bottom, people who are ready: they already talked to you."',
    '"Picture a funnel. At the top, strangers. People who\'ve never heard of you. In the middle, people who are warming up to you. At the bottom, people who are ready to buy."')

# ── A4 closers
rep('<p class="rb a">These ads talk to people who already know you. Leads who didn\'t book, no-shows, webinar registrants.</p>',
    '<p class="rb a">These ads talk to people who already know you. They\'ve seen your stuff. They\'re lower in the funnel, and closer to signing up with you.</p>')
rep('        <div class="exad a"><span>Example</span>“Mary, your Medicare review is still open. Pick a time that works.”</div>\n', '')
rep('<p class="hand foot3 frag">kill your prospectors, and your closers run out of people to close.</p>',
    '<p class="hand foot3 frag">closers finish what your prospecting started.</p>')
rep('"Bottom of the funnel. These are your closers. They talk to people who already know you. Leads who didn\'t book. No-shows. People who registered for your class."',
    '"Bottom of the funnel. These are your closers. They talk to people who already know you. They\'ve seen your stuff. They\'re lower in the funnel, closer to signing up with you."')
rep('THE LINE: "Your closers only have people to close because your prospectors fed them. Kill the prospectors, and in a couple weeks your closers run out of people."',
    'THE LINE: "Closers finish what your prospecting started. They only have people to close because your prospectors fed them."')

# ── A5 awareness: bottom stage is "ready to buy"
rep('<h3>Already talked to you</h3><p class="awd">Opted in, registered, or no-showed.</p><p class="awh">“Mary, your review is still open. Enrollment closes December 7. Pick a time.”</p>',
    '<h3>Ready to buy</h3><p class="awd">Knows you, trusts you. Just needs the next step.</p><p class="awh">“Ready to get your Medicare handled? Book a 15-minute call.”</p>')
rep('ALREADY TALKED TO YOU: "Now you\'re direct. Their name, a deadline, a calendar link."',
    'READY TO BUY: "Now you\'re direct. One clear next step: book the call."')
rep('Bottom-of-funnel ads talk to people who know your name.', 'Bottom-of-funnel ads talk to people who are ready.')

# ── A6 how the account is built, Javier's way
block(r'A6 · HOW THE ACCOUNT IS BUILT', r'''<!-- ═══════════════════════ A6 · HOW THE ACCOUNT IS BUILT ═══════════════════════ -->
<section data-part="3" class="slide wb s-cs2" data-kicker="03 · Ads · The setup">
  <div class="light"></div>
  <div class="content">
    <h1 class="head a" style="font-size:84px">How to set up <em>the account.</em></h1>
    <div class="c2w a">
      <div class="c2t">
        <div class="c2b frag"><p class="k">Campaign · Leads</p><h3>Budget at the campaign</h3><p>That's CBO. Meta moves the money to the ads that are working.</p></div>
        <div class="c2ln frag"></div>
        <div class="c2b frag"><p class="k">Ad set</p><h3>Broad</h3><p>Your licensed states. Let the ads find the right people.</p></div>
        <div class="c2ln frag"></div>
        <div class="c2ads frag"><span>Ad 1</span><span>Ad 2</span><span>Ad 3</span><span>Ad 4</span><span>Ad 5</span></div>
        <p class="hand c2n frag">low budget? keep it to one ad set with several different ads.</p>
      </div>
      <div class="c2r">
        <p class="k">Rules that never change</p>
        <div class="c2r1 frag"><i>01</i><div><b>Never edit a live ad</b><span>Editing resets what it learned. Launch a new version instead.</span></div></div>
        <div class="c2r1 frag"><i>02</i><div><b>One change at a time</b><span>Change two things and you'll never know which one worked.</span></div></div>
        <div class="c2r1 frag"><i>03</i><div><b>Don't kill your top spender</b><span>It's usually your prospector. Build something better next to it.</span></div></div>
        <div class="c2r1 frag"><i>04</i><div><b>Let it settle</b><span>Wait until the numbers are steady week over week, then decide.</span></div></div>
      </div>
    </div>
  </div>
<script type="text/plain" class="notes">HOW TO SET UP THE ACCOUNT. KEEP IT SIMPLE.

LEFT, TOP TO BOTTOM:
"One leads campaign. Always put the budget at the campaign level. That's called CBO. Meta moves the money to the ads that are working, so you don't have to."

"Under it, your ad set. Go broad. Your licensed states, and let the ads find the right people."

"Inside it, several different ads. If you're on a low budget, keep it to one ad set with several different ads. Don't split a small budget five ways."

RIGHT, THE RULES:
1. "Never edit a live ad. The moment you edit it, it starts over. Duplicate it, change it, launch it as a new ad."
2. "One change at a time. Change the image and the headline together and you'll never know what worked."
3. "Don't kill your top spender because its cost per lead looks high. It's usually the prospector feeding everything."
4. "Let it settle. When the numbers are steady week over week, then you decide."</script>
</section>''')

# ── A7 the four metrics, in plain words
rep('<h1 class="head a">Twenty columns. <em>Four</em> that matter.</h1>', '<h1 class="head a">The four metrics that <em>matter most.</em></h1><p class="sub a" style="font-size:28px;margin-top:18px">When you open your ad data, these are the four to look at first.</p>')
rep('<p class="k">Feels like analysis</p>', '<p class="k">Ignore these for now</p>')
rep('"Open Ads Manager and you get twenty columns. Click-through rate, cost per click, hook rate, ROAS. They feel like analysis. They\'re not the numbers you make decisions with."',
    '"When you open your ad data, there are a ton of numbers. Click-through rate, cost per click, hook rate, ROAS. Ignore those for now. They feel like analysis, but they\'re not the numbers you make decisions with."')
rep('<span class="an">Your review is still open<small>Warm audience</small></span>', '<span class="an">Book your Medicare call<small>Lower funnel</small></span>')

# ── Funnel chapter: psychology
rep('<p class="a">What happens after they click?</p>', '<p class="a">How do you build a funnel that converts?</p>')
rep('<h1 class="head a">What happens <em>after the click.</em></h1>', '<h1 class="head a">Every step is <em>intentional.</em></h1>')
rep('<p class="sub a">Most agents stop thinking at the ad. This is where the money is actually made or lost.</p>',
    '<p class="sub a">A high-converting funnel isn\'t random. Every step of the journey does one job in their head.</p>')
for a, b in [('<h3>Ad</h3><p>One person, one promise.</p>', '<h3>Ad</h3><p><b>Curiosity.</b> Stop the scroll.</p>'),
             ('<h3>Landing page</h3><p>Repeats the promise. One button.</p>', '<h3>Landing page</h3><p><b>Relevance.</b> “This is for me.”</p>'),
             ('<h3>Form</h3><p>Name, phone, email, one question.</p>', '<h3>Form</h3><p><b>A small yes.</b> Easy to say.</p>'),
             ('<h3>Thank-you page</h3><p>Not “thanks.” “Book your time.”</p>', '<h3>Thank-you page</h3><p><b>Momentum.</b> Book while it\'s warm.</p>'),
             ('<h3>Calendar</h3><p>They pick the time. You don\'t chase.</p>', '<h3>Calendar</h3><p><b>Control.</b> They pick the time.</p>'),
             ('<h3>Text + email</h3><p>Fires in minutes, automatically.</p>', '<h3>Text + email</h3><p><b>Trust.</b> They know who\'s calling.</p>'),
             ('<h3>Appoint&shy;ment</h3><p>A conversation they asked for.</p>', '<h3>Appoint&shy;ment</h3><p><b>Commitment.</b> They asked for it.</p>')]:
    rep(a, b)
s = re.sub(r'(MECHANISM: THE PATH AFTER THE CLICK\.).*?(</script>)', lambda m: '''FUNNEL PSYCHOLOGY: EVERY STEP IS INTENTIONAL.

"A high-converting funnel isn't a bunch of pages. Every step of the journey does one job in the person's head. Nothing is random."

Walk it left to right, and say the word in bold each time:
"The ad: curiosity. Stop the scroll.
The landing page: relevance. The second they land, they have to think 'this is for me.'
The form: a small yes. Short and easy to say yes to.
The thank-you page: momentum. They're the most interested they'll ever be. Ask them to book right now.
The calendar: control. They pick the time, so they own the appointment.
The text and email: trust. When you call, you're not a stranger.
The appointment: commitment. They asked for this call."

"Miss one of these and you lose people at that step. That's why most funnels leak."''' + m.group(2), s, count=1, flags=re.S)

block(r'15 MECHANISM · PAGE JOBS', r'''<!-- ═══════════════════════ 15 FUNNEL · THE PSYCHOLOGY ═══════════════════════ -->
<section data-part="4" class="slide wb s-psy" data-kicker="04 · Funnel · The psychology">
  <div class="light"></div>
  <div class="content">
    <h1 class="head a" style="font-size:84px">The psychology behind <em>each page.</em></h1>
    <div class="psg a">
      <div class="ps frag"><p class="k">Landing page</p><h3>Message match</h3><p>Say exactly what the ad promised. If it doesn't match, they feel tricked and leave.</p></div>
      <div class="ps frag"><p class="k">Form</p><h3>Small yes first</h3><p>A short form is an easy yes. Every extra field is one more reason to stop.</p></div>
      <div class="ps frag"><p class="k">Thank-you page</p><h3>Strike while it's warm</h3><p>This is the most interested they will ever be. Ask for the call now, not later.</p></div>
      <div class="ps frag"><p class="k">Calendar</p><h3>Let them choose</h3><p>When they pick the time, it's their appointment. Show the next few days only.</p></div>
      <div class="ps frag"><p class="k">Confirmation</p><h3>No strangers</h3><p>Text them right away from your number, so your call isn't a surprise.</p></div>
      <div class="ps gold frag"><p class="k">The whole funnel</p><h3>One next step</h3><p>Every page asks for one thing. More choices means fewer people choose.</p></div>
    </div>
  </div>
<script type="text/plain" class="notes">THE PSYCHOLOGY BEHIND EACH PAGE.

"This is what separates a funnel that converts from a funnel that just exists."

MESSAGE MATCH: "If your ad says 'three decisions before you turn 65' and your page says 'Welcome to ABC Insurance,' they feel tricked. Say exactly what the ad promised."
SMALL YES FIRST: "A short form is an easy yes. Every extra field is one more reason to stop."
STRIKE WHILE IT'S WARM: "The thank-you page is the most interested they'll ever be. Most agents put 'thanks, we'll be in touch.' Ask for the call right there."
LET THEM CHOOSE: "When they pick the time, it's their appointment, not yours. Show the next few days only."
NO STRANGERS: "Text them right away from your number, so when you call, they know who it is."
ONE NEXT STEP: "Every page asks for one thing. The more choices you give, the fewer people choose."</script>
</section>''')

# ── offer opener: agents, not seniors
rep('<img src="assets/ch-offer.jpg" alt="" style="object-position:62% 40%">', '<img src="assets/ch-offer2.jpg" alt="" style="object-position:66% 30%">')

# ═══ THE OFFER, AS BONUSES, FULL COLOR ═══
TOTALS = ['$3,000', '$5,500', '$7,000', '$8,164', '$9,164', '$14,164']
def tally(n):
    segs = ''.join(f'<i class="{"on" if k < n else ""}"></i>' for k in range(7))
    return f'<div class="bt frag"><p class="l">Total value so far</p><span class="seg">{segs}</span><p class="c">{n} of 7</p><p class="v">{TOTALS[n-1]}</p></div>'

def bonus(n, name_html, value, value_sub, lead, rows, visual, note, kicker_title):
    lis = ''.join(f'<li class="frag"><b>{t}</b>{d}</li>' for t, d in rows)
    return f'''<!-- ═══════════════════════ BONUS {n:02d} · {kicker_title} ═══════════════════════ -->
<section class="slide wb s-bn" data-kicker="Bonus {n} of 7">
  <div class="light"></div>
  <div class="content">
    <div class="bnw">
      <div class="bnl">
        <div class="bnt a"><span class="gift"><svg viewBox="0 0 40 40"><rect x="6" y="16" width="28" height="18" rx="2"/><rect x="4" y="11" width="32" height="7" rx="2"/><path d="M20 11v23M20 11c-3-6-10-6-9-1 1 3 9 1 9 1zM20 11c3-6 10-6 9-1-1 3-9 1-9 1z"/></svg></span>Bonus #{n}</div>
        <h1 class="head a">{name_html}</h1>
        <p class="rb a">{lead}</p>
        <ul class="bl a">{lis}</ul>
      </div>
      <div class="bnr a">{visual}<div class="stamp"><b>{value}</b><span>{value_sub}</span></div></div>
    </div>
    {tally(n)}
  </div>
<script type="text/plain" class="notes">{note}</script>
</section>'''

BOOK = '''<div class="pbw"><div class="book"><div class="cv"><img src="assets/logo.webp" alt=""><p class="k">The Real Insurance Group</p><h4>The Medicare<br>Marketing<br><em>Playbook.</em></h4><p class="au">Johnny Brock</p></div><div class="pg"></div></div>
<div class="toc"><p class="k">Inside</p><p><i>01</i>Market</p><p><i>02</i>Message</p><p><i>03</i>Ads</p><p><i>04</i>Funnel</p><p><i>05</i>Backend</p></div></div>'''

LIB = '<div class="lib">' + ''.join(f'<div class="cc"><div class="ct {c}"><span>{t}</span></div><small>Course · Included</small></div>' for t, c in
       [('Cross-Selling', 'c1'), ('Medicare Supplement', 'c2'), ('Sales Training', 'c3'), ('Technology', 'c4'), ('Facebook Ads', 'c5'), ('Annuities', 'c6')]) + '</div>'

CAL = '''<div class="shot"><div class="frame live"><div class="bar"><i></i><i></i><i></i><span>skool.com · Calendar</span></div><video muted loop playsinline preload="auto" poster="assets/training-calendar-poster.jpg" src="assets/training-calendar.mp4"></video></div>
<div class="wkc">''' + ''.join(f'<span><b>{d}</b>{t}</span>' for d, t in [('Mon', 'Marketing'), ('Tue', 'Sales + annuity'), ('Wed', 'Marketing, AI, sales'), ('Thu', 'Sales'), ('Fri', 'Marketing')]) + '</div></div>'

GHL = '''<div class="g4">''' + ''.join(f'<div class="frame live"><div class="bar"><i></i><i></i><i></i><span>{t}</span></div><img src="assets/{f}" alt="{t}"></div>' for t, f in
       [('Automation', 'crm-auto.jpg'), ('Funnels', 'crm-funnels.jpg'), ('Sites', 'crm-sites.jpg'), ('A live page', 'crm-livepage.jpg')]) + '</div>'

CALLCARD = '''<div class="callc"><div class="vid"><span class="av">D</span><p class="nm">David<small>Tech team · The Real Insurance Group</small></p><span class="live">Onboarding call</span></div>
<div class="ck">''' + ''.join(f'<p><i>✓</i>{t}</p>' for t in ['Your account set up, with you', 'A2P approved, so your texts land', 'Your phone number connected', 'Your email connected', 'Your calendar connected']) + '</div></div>'

SNAP = '''<div class="snap"><div class="frame live"><div class="bar"><i></i><i></i><i></i><span>Your account · day one</span></div><img src="assets/crm-funnels.jpg" alt="Funnel steps already built" style="object-fit:cover;object-position:24% 40%;transform:scale(1.3);transform-origin:24% 40%"></div>
<div class="pgs"><span>Registration page</span><span>Thank-you page</span><span>Booking page</span><span>Confirmation page</span><span class="g">+ every text and email behind them</span></div></div>'''

B = {
 1: bonus(1, 'The Medicare Marketing <em>Playbook.</em>', '$3,000', 'value',
          'Everything you saw tonight, step by step. How to create the opportunity, from the first ad to the renewal.',
          [('Market and message', 'picking your person and writing the ad'), ('Running the ads', 'from a dead stop to a running account'), ('The funnel', 'every page, built to convert'), ('The backend', 'follow-up, nurture, pipeline, cross-sell')],
          BOOK, 'BONUS #1: THE MEDICARE MARKETING PLAYBOOK. $3,000.\n\n"First bonus. Tonight was the overview. The playbook is the whole thing, step by step. The five parts you just learned: market, message, ads, funnel, backend."\n\nSay the value once and move on. Point at the tally at the bottom: it climbs on every slide from here.', 'PLAYBOOK'),
 2: bonus(2, 'The Complete Training <em>Library.</em>', '$2,500', 'value',
          'Marketing isn\'t the only gap you\'ll hit. The lead books, and now you need to sell, cross-sell and quote.',
          [('Cross-selling', 'dental, hospital, cancer, home health'), ('Medicare Supplement', 'start to finish'), ('Sales training', 'my method, from thousands of policies'), ('Technology', 'the right sites to quote seniors')],
          LIB, 'BONUS #2: THE COMPLETE TRAINING LIBRARY. $2,500.\n\n"Marketing isn\'t the only gap you\'ll hit. The lead books, and now you need to sell. They say yes to Medicare, and now you need the cross-sell. Hundreds of hours of training, all unlocked the day you join."\n\nRunning value: $5,500.', 'TRAINING LIBRARY'),
 3: bonus(3, 'The Private Medicare Agent <em>Community.</em>', '$1,500', 'per year',
          'You never get stuck alone. Live training every business day with Johnny, the team, and agents doing the work.',
          [('Live every business day', 'marketing, sales, AI, annuities'), ('Same-day answers', 'post in the morning, answer by lunch'), ('Agents doing the work', 'wins, scripts, what\'s working this week')],
          CAL, 'BONUS #3: THE PRIVATE MEDICARE AGENT COMMUNITY. $1,500 A YEAR.\n\n"Courses age on a shelf. Marketing changes, AI changes. On these calls you hear what\'s working this week. You\'re never more than 24 hours from a real answer."\n\n$1,500 a year, about $125 a month. Running value: $7,000.', 'COMMUNITY'),
 4: bonus(4, 'Your Complete GoHighLevel <em>Account.</em>', '$97', 'per month',
          'Training doesn\'t run itself. The system does. This is where the whole back end you saw tonight lives.',
          [('Every lead in one place', 'texts, calls and emails in one inbox'), ('Booking pages', 'they pick a time without you'), ('The follow-up, automatic', 'every step fires on its own'), ('You own the list', 'your account, your contacts')],
          GHL, 'BONUS #4: YOUR COMPLETE GOHIGHLEVEL ACCOUNT. $97 A MONTH.\n\n"Remember the back end? Speed to lead, nurture, reminders, the pipeline. This is where all of it lives."\n\nPoint at the four screens. $97 a month, $1,164 a year. Running: $8,164.', 'GHL ACCOUNT'),
 5: bonus(5, 'Done-For-You <em>Onboarding.</em>', '$1,000', 'value',
          'You don\'t switch it on alone. A one-on-one call with David, my tech guy, who sets it up with you.',
          [('Set up live, with you', 'so you actually know where things are'), ('A2P approved', 'so your texts land instead of silently dying'), ('Everything connected', 'number, email and calendar, switched on')],
          CALLCARD, 'BONUS #5: DONE-FOR-YOU ONBOARDING. $1,000.\n\n"A one-on-one call with David. Not a chatbot, not a help article."\n\nStop on A2P: "That\'s the registration that decides whether your texts land or silently die. None of the follow-up works without it."\n\nRunning: $9,164.', 'ONBOARDING'),
 6: bonus(6, 'Medicare Automation <em>Snapshots.</em>', '$5,000', 'what I paid',
          'The exact campaign running for me right now, refined on more than $100,000 of my own ad spend, loaded into your account.',
          [('The whole funnel', 'every page from tonight, already built'), ('Every automation behind it', 'texts, reminders, no-show, 90-day follow-up'), ('Change the name, turn it on', 'live on day one')],
          SNAP, 'BONUS #6: MEDICARE AUTOMATION SNAPSHOTS. $5,000.\n\n"I know this is worth five thousand dollars, because that\'s what I paid to have it built. And I refined it on more than a hundred thousand dollars of my own ad spend."\n\nCHECK BEFORE GOING LIVE: only say $100,000 if that\'s genuinely what\'s behind these funnels.\n\nRunning: $14,164. Then STOP. Don\'t reveal bonus 7 yet.', 'SNAPSHOTS'),
}
for n, mk in [(1, '26 STACK 01'), (2, '27 STACK 02'), (3, '28 STACK 03'), (4, '29 STACK 04'), (5, '30 STACK 05'), (6, '31 STACK 06')]:
    block(mk, B[n])

# the rest of the offer goes full color too; the reveal and the Q&A stay dark for contrast
for cls in ['s-was paper', 's-gap', 's-hats', 's-spec', 's-delta2', 's-offer paper', 's-full2', 's-cap', 's-math', 's-next', 's-three3']:
    rep(f'<section class="slide {cls}"', f'<section class="slide wb {cls}"')
rep('<section class="slide wb s-was paper"', '<section class="slide wb s-was"')
rep('<section class="slide wb s-offer paper"', '<section class="slide wb s-offer"')
rep('<p class="k a">Part 07 &nbsp;·&nbsp; New</p>', '<p class="k a">Bonus #7 &nbsp;·&nbsp; New</p>')
s = s.replace('data-kicker="How we help · 07"', 'data-kicker="Bonus 7 of 7"')
rep('<div>Medicare Marketing Playbook <span>$3,000</span></div>', '<div><i>01</i>Medicare Marketing Playbook <span>$3,000</span></div>')
rep('<div>Complete Training Library <span>$2,500</span></div>', '<div><i>02</i>Complete Training Library <span>$2,500</span></div>')
rep('<div>Private Medicare Agent Community <span>$1,500/yr</span></div>', '<div><i>03</i>Private Medicare Agent Community <span>$1,500/yr</span></div>')
rep('<div>Complete GoHighLevel Account <span>$97/mo</span></div>', '<div><i>04</i>Complete GoHighLevel Account <span>$97/mo</span></div>')
rep('<div>Done-For-You Onboarding <span>$1,000</span></div>', '<div><i>05</i>Done-For-You Onboarding <span>$1,000</span></div>')
rep('<div>Medicare Automation Snapshots <span>$5,000</span></div>', '<div><i>06</i>Medicare Automation Snapshots <span>$5,000</span></div>')
s = s.replace('Part 01 · Medicare Marketing Playbook', 'Bonus #1 · Medicare Marketing Playbook')

open(P, 'w', encoding='utf-8').write(s)
print('sections', s.count('<section'), 'wb', s.count('class="slide wb'))
