# v3: the Media chapter becomes campaign structure + reading the numbers.
# Runs after v2.py (reads and rewrites src/slides.html).
import re, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(ROOT, 'src/slides.html')
s = open(P, encoding='utf-8').read()

NEW = r'''<!-- ═══════════════════════ M1 · EVERY AD HAS A JOB ═══════════════════════ -->
<section data-part="3" class="slide s-fz" data-kicker="03 · Media · Campaign structure">
  <div class="light"></div>
  <div class="content">
    <h1 class="head a" style="font-size:80px">Every ad has a <em>job.</em></h1>
    <p class="sub a" style="font-size:27px;margin-top:18px">Before you judge an ad, know where it sits in the funnel and who it's talking to.</p>
    <div class="fzg a">
      <div class="fzband frag"><div class="fzshape t1"><b>Top</b><span>Prospecting</span></div>
        <div class="fzinfo"><p class="fzk">Who</p><p>People who've never heard of you. Turning 65, retiring, confused.</p></div>
        <div class="fzinfo"><p class="fzk">The ad's job</p><p>Open the door. Teach something, get a hand raised.</p></div>
        <div class="fzinfo"><p class="fzk">Budget</p><p class="fzv">Most of it</p></div></div>
      <div class="fzband frag"><div class="fzshape t2"><b>Middle</b><span>Warming</span></div>
        <div class="fzinfo"><p class="fzk">Who</p><p>They watched, clicked, or registered, but haven't booked.</p></div>
        <div class="fzinfo"><p class="fzk">The ad's job</p><p>Build trust. Proof, comparisons, the webinar replay.</p></div>
        <div class="fzinfo"><p class="fzk">Budget</p><p class="fzv">Some</p></div></div>
      <div class="fzband frag"><div class="fzshape t3"><b>Bottom</b><span>Closers</span></div>
        <div class="fzinfo"><p class="fzk">Who</p><p>People who already know you. Leads, no-shows, past clients.</p></div>
        <div class="fzinfo"><p class="fzk">The ad's job</p><p>Get the call booked. Deadlines, reminders, “pick a time.”</p></div>
        <div class="fzinfo"><p class="fzk">Budget</p><p class="fzv">A little, on purpose</p></div></div>
    </div>
  </div>
<script type="text/plain" class="notes">EVERY AD HAS A JOB. THIS IS WHERE YOU SOUND LIKE A MARKETER.

"Most agents run one ad and ask one question: is it working? Wrong question. Every ad has a job, and the job depends on where it sits in the funnel."

TOP, PROSPECTING: "These are people who have never heard of you. Somebody turning 65 who doesn't know what Part B is. The ad's job is to open the door. This gets most of your budget."

MIDDLE, WARMING: "They watched a video, clicked, registered for a class, but haven't booked. The job here is trust. Proof, a Plan G versus Plan N comparison, the replay."

BOTTOM, CLOSERS: "People who already know you. Leads who didn't book, no-shows, your past clients. Small budget, on purpose. The job is one thing: get the call on the calendar."

Land it: "Your closers only have people to close because your prospecting ads fed them. Turn off the top, and the bottom dries up in a couple of weeks."</script>
</section>

<!-- ═══════════════════════ M2 · PROSPECTORS VS CLOSERS ═══════════════════════ -->
<section data-part="3" class="slide s-pc" data-kicker="03 · Media · Campaign structure">
  <div class="light"></div>
  <div class="content">
    <h1 class="head a" style="font-size:72px">Door-openers and closers<br>look <em>completely different.</em></h1>
    <div class="pcg a">
      <div class="pch"></div>
      <div class="pch op"><p class="pck">Top of funnel</p><h3>The Prospector</h3><p>Opens the door</p></div>
      <div class="pch cl"><p class="pck">Bottom of funnel</p><h3>The Closer</h3><p>Books the call</p></div>
      <div class="pcm frag">Spend</div><div class="pcv frag"><span class="gauge"><i style="width:88%"></i></span>The most. Meta gives it the budget.</div><div class="pcv frag"><span class="gauge"><i style="width:22%"></i></span>Less. Small audience, small spend.</div>
      <div class="pcm frag">Frequency <small>per day</small></div><div class="pcv frag"><span class="gauge"><i style="width:18%"></i></span>Low. Under 1.15. New people every day.</div><div class="pcv frag"><span class="gauge"><i style="width:78%"></i></span>High. 1.25 and up. The same people again.</div>
      <div class="pcm frag">CPM</div><div class="pcv frag"><span class="gauge"><i style="width:22%"></i></span>Low. Broad, cold, cheap to reach.</div><div class="pcv frag"><span class="gauge"><i style="width:80%"></i></span>High. Narrow, warm, worth more.</div>
      <div class="pcm frag">Cost per result</div><div class="pcv frag"><span class="gauge"><i style="width:68%"></i></span>Higher. That's expected.</div><div class="pcv frag"><span class="gauge g"><i style="width:26%"></i></span>Lower. This is how you judge it.</div>
    </div>
    <div class="foot2 frag">“Ad fatigue” is usually a closer asked to knock on doors, <span>or a door-opener asked to close.</span></div>
  </div>
<script type="text/plain" class="notes">PROSPECTORS VS CLOSERS. READ ACROSS, ROW BY ROW.

"Here are two ads in the same account doing two different jobs."

SPEND: "The prospector gets most of the money. Meta is putting it there because it's finding new people. The closer spends less, because there are only so many warm people to show it to."

FREQUENCY, PER DAY: "Look at frequency by the DAY, not lifetime. Under about 1.15 a day means it's mostly reaching new people. Over 1.25 a day, it's hitting people who already know you. That one number tells you where the ad lives in the funnel."

CPM: "That's what it costs to show your ad a thousand times. Cheap means broad and cold. Expensive means narrow and warm. A high CPM on a closer isn't a problem. It's the design."

COST PER RESULT: "The prospector's cost per lead will look worse. That's normal, it's talking to strangers. The closer's will look better. You judge each one against its own job, not against each other."

THE KILLER LINE: "When people say an ad 'got tired,' most of the time they asked a closer to go find new people, or a door-opener to close. Wrong job, not a tired ad."</script>
</section>

<!-- ═══════════════════════ M3 · TALK TO WHERE THEY ARE ═══════════════════════ -->
<section data-part="3" class="slide s-aw" data-kicker="03 · Media · Campaign structure">
  <div class="light"></div>
  <div class="content">
    <h1 class="head a" style="font-size:76px">Talk to people <em>where they are.</em></h1>
    <p class="sub a" style="font-size:26px;margin-top:18px">The same person needs a different ad depending on how much they already know.</p>
    <div class="awg a">
      <div class="aws frag" style="--lift:0px"><p class="awt">Top</p><h3>Unaware</h3><p class="awd">Doesn't know they have a decision to make.</p><p class="awh">“Turning 65 this year? There are 3 Medicare decisions you have to make first.”</p></div>
      <div class="aws frag" style="--lift:34px"><p class="awt">Top</p><h3>Problem aware</h3><p class="awd">Knows it's confusing. Doesn't know who to trust.</p><p class="awh">“Parts A, B, C, D, G, N. Here's what actually matters, in plain English.”</p></div>
      <div class="aws frag" style="--lift:68px"><p class="awt">Middle</p><h3>Solution aware</h3><p class="awd">Knows they need a plan, or an agent. Comparing.</p><p class="awh">“Plan G or Plan N? Join Thursday's 30-minute class and bring your questions.”</p></div>
      <div class="aws frag hot" style="--lift:102px"><p class="awt">Bottom</p><h3>Already talked to you</h3><p class="awd">Opted in, registered, or no-showed.</p><p class="awh">“Mary, your review is still open. Enrollment closes December 7. Pick a time.”</p></div>
    </div>
  </div>
<script type="text/plain" class="notes">AWARENESS. THIS IS WHAT MAKES THE MESSAGE MATCH THE FUNNEL.

"You don't say the same thing to a stranger that you say to someone who already filled out your form."

Walk up the stairs, left to right:

UNAWARE: "They don't even know they have a decision to make. You lead with the decision. 'Three decisions before you turn 65.'"

PROBLEM AWARE: "They know it's confusing. You make it simple. 'Here's what actually matters, in plain English.'"

SOLUTION AWARE: "They know they need a plan or an agent, they're comparing. Give them the comparison and an easy next step, like a class."

ALREADY TALKED TO YOU: "They opted in, registered, or no-showed. Now you're direct. Their name, a deadline, a calendar link."

The rule: "Top-of-funnel ads talk to strangers. Bottom-of-funnel ads talk to people who already know your name. Mix those up and both ads look broken."

Annual Enrollment runs October 15 to December 7.</script>
</section>

<!-- ═══════════════════════ M4 · HOW THE ACCOUNT IS BUILT ═══════════════════════ -->
<section data-part="3" class="slide s-cs" data-kicker="03 · Media · Campaign structure">
  <div class="light"></div>
  <div class="content">
    <h1 class="head a" style="font-size:76px">How the account is <em>actually built.</em></h1>
    <div class="csg a">
      <div class="cstree">
        <div class="csbox top frag"><p class="csk">Campaign</p><h3>One objective: Leads</h3><p>You want names and phone numbers, not likes.</p></div>
        <div class="csarms frag"><i></i></div>
        <div class="cspair">
          <div class="csbox frag"><p class="csk">Ad set · Prospecting</p><h3>Broad, cold</h3><p>Your licensed states. Most of the budget.</p><div class="csads"><i></i><i></i><i></i><i></i><i></i><i></i></div></div>
          <div class="csbox cl frag"><p class="csk">Ad set · Closers</p><h3>Warm, narrow</h3><p>Leads, engagers, registrants. Small on purpose.</p><div class="csads"><i></i><i></i><i></i><i></i></div></div>
        </div>
        <p class="csnote frag">4 to 8 ads per ad set. More than that, and none of them get enough to learn.</p>
      </div>
      <div class="csrules">
        <p class="csk">The rules that never change</p>
        <div class="csr frag"><i>01</i><div><b>Never edit a live ad</b><span>Editing resets what it learned. Launch a new version instead.</span></div></div>
        <div class="csr frag"><i>02</i><div><b>One change at a time</b><span>Change two things and you'll never know which one worked.</span></div></div>
        <div class="csr frag"><i>03</i><div><b>Don't kill your top spender</b><span>It's usually feeding the closers. Build something better next to it.</span></div></div>
        <div class="csr frag"><i>04</i><div><b>Let it settle</b><span>Wait until the numbers are steady week over week, then decide.</span></div></div>
      </div>
    </div>
  </div>
<script type="text/plain" class="notes">HOW THE ACCOUNT IS BUILT. KEEP IT SIMPLE, SOUND LIKE YOU'VE DONE IT A THOUSAND TIMES.

LEFT, THE TREE:
"One campaign, one objective: leads. Underneath it, two ad sets. Prospecting: broad, your licensed states, most of the budget. Closers: warm and narrow, people who already raised their hand. Small on purpose."

"Four to eight ads in each ad set. Put twenty ads in there and none of them get enough budget to learn anything."

RIGHT, THE FOUR RULES. These are what separate people who've actually run accounts from people who've watched a YouTube video:

1. "Never edit a live ad. The moment you edit it, it starts over. Duplicate it, change the copy, launch it as a new ad."
2. "One change at a time. Change the image and the headline together and you'll never know what worked."
3. "Don't kill your top spender because its cost per lead looks high. It's usually the prospector feeding everything else. Build a better one next to it and let them fight."
4. "Let it settle. Don't make decisions on one day. When the numbers are steady week over week, then you decide."</script>
</section>

<!-- ═══════════════════════ M5 · THE FOUR NUMBERS ═══════════════════════ -->
<section data-part="3" class="slide s-n4" data-kicker="03 · Media · Your numbers">
  <div class="light"></div>
  <div class="content">
    <h1 class="head a" style="font-size:76px">Four numbers. <em>Ignore the rest.</em></h1>
    <p class="sub a" style="font-size:26px;margin-top:18px">Ads Manager gives you twenty columns. These four tell you what's really going on.</p>
    <div class="n4g a">
      <div class="n4c frag"><p class="n4i">01</p><h3>Spend</h3><p class="n4d">Where Meta is putting your money.</p><div class="n4viz"><span class="sp"><i style="width:70%">70%</i><i class="lo" style="width:3%"></i></span></div><p class="n4t"><b>Tells you</b>which ads Meta trusts. The top spender is usually your prospector.</p></div>
      <div class="n4c frag"><p class="n4i">02</p><h3>CPM</h3><p class="n4d">What it costs to show your ad 1,000 times.</p><div class="n4viz"><span class="scale"><em>Cold, broad</em><u></u><em>Warm, narrow</em></span></div><p class="n4t"><b>Tells you</b>who it's reaching. Low is new people. High is people who know you.</p></div>
      <div class="n4c frag"><p class="n4i">03</p><h3>Frequency</h3><p class="n4d">How many times one person sees it, per day.</p><div class="n4viz"><span class="fq"><i>1.0</i><i class="m">1.15</i><i class="m">1.25</i><i>1.5+</i></span></div><p class="n4t"><b>Tells you</b>where it sits. Under 1.15 is prospecting. Over 1.25 is closing.</p></div>
      <div class="n4c frag gold"><p class="n4i">04</p><h3>Cost per result</h3><p class="n4d">What you pay for a lead, or a booked call.</p><div class="n4viz"><span class="cpr"><b>$7.40</b><small>prospector</small><b class="g">$3.10</b><small>closer</small></span></div><p class="n4t"><b>Tells you</b>if it's doing its job. Judge it against its job, not other ads.</p></div>
    </div>
    <div class="foot2 frag">Spend and frequency tell you the ad's <span>job.</span> CPM and cost per result tell you if it's <span>doing it.</span></div>
  </div>
<script type="text/plain" class="notes">THE FOUR NUMBERS. SAY EACH ONE IN ONE SENTENCE.

"Ads Manager gives you twenty columns. Click-through rate, cost per click, hook rate. They feel like analysis. They're not decision numbers. There are four that matter."

SPEND: "Where Meta is putting your money. Meta never splits money evenly. If one ad gets seventy percent and another gets three, that's Meta telling you which one it trusts."

CPM: "What it costs to show your ad a thousand times. Low means you're reaching new, cold people. High means you're reaching warm people who already know you. Neither is good or bad on its own."

FREQUENCY: "How many times one person sees it, per DAY. Always look at it by the day. Under 1.15, it's finding new people. Over 1.25, it's showing to people who already know you."

COST PER RESULT: "What you pay for a lead, or better, a booked call. This is the only one that says if the ad is doing its job. But you judge it against its job. A prospector at seven dollars can be doing better work than a closer at three."

LAND IT: "Spend and frequency tell you the ad's job. CPM and cost per result tell you if it's doing it."

The $7.40 and $3.10 are example numbers.</script>
</section>

<!-- ═══════════════════════ M6 · READ THE ACCOUNT ═══════════════════════ -->
<section data-part="3" class="slide s-rd" data-kicker="03 · Media · Your numbers">
  <div class="light"></div>
  <div class="content">
    <h1 class="head a" style="font-size:72px">Read any account in <em>sixty seconds.</em></h1>
    <p class="sub a" style="font-size:25px;margin-top:16px">Sort by spend. Read each ad left to right. Then decide.</p>
    <div class="rdt a">
      <div class="rdh"><span>Ad</span><span>Spend</span><span>Freq / day</span><span>CPM</span><span>Cost / lead</span><span>Verdict</span></div>
      <div class="rdr frag"><span class="an">Turning 65 · 3 decisions<small>Static image</small></span><span>$1,840<small>62%</small></span><span>1.08</span><span>$9</span><span>$7.40</span><span class="vd ok"><b>Prospector</b>Leave it. It feeds everything.</span></div>
      <div class="rdr frag"><span class="an">Your review is still open<small>Warm audience</small></span><span>$310<small>10%</small></span><span>1.62</span><span>$31</span><span>$3.10</span><span class="vd ok"><b>Closer</b>Leave it. It's meant to be small.</span></div>
      <div class="rdr frag bad"><span class="an">Plan G static v2<small>Static image</small></span><span>$95<small>3%</small></span><span>1.31</span><span>$28</span><span>$19.80</span><span class="vd no"><b>No job</b>Not earning spend. Launch a new version.</span></div>
    </div>
    <p class="rdx a">Example account</p>
    <div class="foot2 frag">Stop asking “which ad has the best cost per lead?” <span>Ask “what job is this ad doing?”</span></div>
  </div>
<script type="text/plain" class="notes">READ THE ACCOUNT. THIS IS THE DEMO THAT MAKES YOU THE EXPERT.

"Here's how I read an account in about sixty seconds. Sort by spend, highest to lowest, then read every ad left to right."

ROW 1: "Sixty-two percent of the spend. Frequency 1.08 a day, so it's finding new people. CPM nine bucks, cheap and broad. Cost per lead $7.40, the highest of the good ones. A beginner turns this off. That's the worst thing you could do. It's the prospector. It feeds everything."

ROW 2: "Ten percent of the spend. Frequency 1.6, CPM thirty-one, so it's hitting warm people. Cost per lead $3.10. It's the closer. It's supposed to be small. Leave it alone."

ROW 3: "Three percent of the spend, high CPM, frequency all over the place, and almost twenty bucks a lead. Meta can't find a job for it. Don't edit it. Launch a new version and let it earn spend."

THE LINE: "Stop asking which ad has the best cost per lead. Ask what job each ad is doing, and whether it's doing it."

These are example numbers for teaching. Say so if anyone asks.</script>
</section>'''

# replace the old "20% that matters" slide with the new chapter
pat = re.compile(r'<!-- ═+ 11 MEDIA · THE 20% ═+ -->.*?</section>', re.S)
assert pat.search(s), 'media 20% slide not found'
s = pat.sub(lambda m: NEW, s, count=1)

# align the "what built $5.92" rules with the new chapter
s = s.replace('<b>Kill, then feed</b><span>Turn off what doesn\'t work. Move the money to what does. Every week.</span>',
              '<b>Replace, don\'t just kill</b><span>An ad with no job gets a new version. The top spender stays.</span>')
s = s.replace('<b>The average is the skill</b><span>$5.92 isn\'t one lucky ad. It\'s what\'s left after you cut the losers.</span>',
              '<b>The average is the skill</b><span>$5.92 isn\'t one lucky ad. It\'s a full team of ads, each doing its job.</span>')
s = s.replace('"Some of these ads cost fifteen, twenty-three dollars a lead. I lost money on them. The average is $5.92 because I killed those and fed the ones that worked. That IS the skill."',
              '"Some of these ads cost fifteen, twenty-three dollars a lead. Some of those were prospectors doing their job, some had no job and got replaced. The average is $5.92 because the account works as a team. That IS the skill."')
open(P, 'w', encoding='utf-8').write(s)
print('ok', s.count('<section'))
