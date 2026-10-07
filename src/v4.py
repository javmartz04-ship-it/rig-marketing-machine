# v4: whiteboard teaching register, Ads chapter rebuilt one idea per slide, Backend chapter.
# Runs after v2.py (reads and rewrites src/slides.html).
import re, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(ROOT, 'src/slides.html')
s = open(P, encoding='utf-8').read()

def sub1(pat, rep, flags=re.S):
    global s
    new, n = re.subn(pat, lambda m: rep, s, count=1, flags=flags)
    assert n == 1, 'not found: ' + pat[:70]
    s = new

def rep(a, b):
    global s
    assert a in s, 'missing: ' + a[:70]
    s = s.replace(a, b)

rep('Here\'s the account. Now let me show you what built it.', 'Here\'s the account. Now, <em>what built it.</em>')
# ── names
s = s.replace('data-kicker="03 · Media', 'data-kicker="03 · Ads').replace('data-kicker="04 · Mechanism', 'data-kicker="04 · Funnel').replace('data-kicker="05 · Monetization', 'data-kicker="05 · Backend')
rep('<h3>Media</h3><p>How do you put it in front of them?</p>', '<h3>Ads</h3><p>How do you run them, and read them?</p>')
rep('<h3>Mechanism</h3><p>What gets them to raise their hand and book?</p>', '<h3>Funnel</h3><p>What happens after they click?</p>')
rep('<h3>Monetization</h3><p>What happens after the lead comes in?</p>', '<h3>Backend</h3><p>What turns a lead into money?</p>')
rep("Most agents only ever work on one of these, usually media.", "Most agents only ever work on one of these, usually the ads.")
s = s.replace('Everything from the mechanism section, already built.', 'Everything from the funnel section, already built.')
s = s.replace('The pages from the mechanism section, built for your campaign.', 'The pages from the funnel section, built for your campaign.')
s = s.replace('Everything I showed you in the mechanism section.', 'Everything I showed you in the funnel section.')
s = s.replace('The number from the monetization section.', 'The number from the backend section.')

ICON = {
 'spend': '<svg viewBox="0 0 120 120"><path d="M22 92h76M26 80h68M30 68h60" /><rect x="30" y="50" width="60" height="18" rx="3"/><path d="M52 59h16"/><circle cx="84" cy="36" r="13"/><path d="M84 29v14M80 32.5c1-2 7-2 8 0s-8 4-7 6.5 7 2 8 0"/></svg>',
 'cpm': '<svg viewBox="0 0 120 120"><circle cx="60" cy="60" r="40"/><circle cx="46" cy="52" r="8"/><circle cx="74" cy="52" r="8"/><path d="M32 80c3-9 9-13 14-13s11 4 14 13M60 80c3-9 9-13 14-13s11 4 14 13"/><circle cx="60" cy="40" r="6" class="f"/></svg>',
 'freq': '<svg viewBox="0 0 120 120"><path d="M92 46a36 36 0 1 0 4 22"/><path d="M96 30v18H78"/><path d="M52 44l24 16-24 16z" class="f"/></svg>',
 'cpr': '<svg viewBox="0 0 120 120"><circle cx="56" cy="64" r="38"/><circle cx="56" cy="64" r="24"/><circle cx="56" cy="64" r="9" class="f"/><path d="M56 64L96 24M84 22h14v14"/></svg>',
 'door': '<svg viewBox="0 0 120 120"><path d="M30 98V20h56v78"/><path d="M30 98l28-8V28L30 20" class="f2"/><circle cx="50" cy="62" r="3" class="f"/><path d="M20 98h80"/><path d="M92 50l10-6M94 62h12M92 74l10 6"/></svg>',
 'cal': '<svg viewBox="0 0 120 120"><rect x="20" y="28" width="80" height="70" rx="8"/><path d="M20 46h80M40 20v16M80 20v16"/><path d="M44 72l10 10 22-22"/></svg>',
 'clock': '<svg viewBox="0 0 120 120"><circle cx="60" cy="64" r="40"/><path d="M60 40v24l16 10"/><path d="M50 16h20M60 16v8M92 30l6-6"/></svg>',
 'bucket': '<svg viewBox="0 0 120 120"><path d="M24 36h72l-10 64H34z"/><ellipse cx="60" cy="36" rx="36" ry="8"/><path d="M40 70v10M60 78v12M80 66v10" class="drip"/></svg>',
}
def tile(name, color):
    return f'<div class="tile {color}">{ICON[name]}</div>'

ADS = r'''<!-- ═══════════════════════ A1 · THE WRONG QUESTION ═══════════════════════ -->
<section data-part="3" class="slide s-q2" data-kicker="03 · Ads">
  <div class="light"></div>
  <div class="content">
    <div class="q2w">
      <p class="lbl a">Stop asking</p>
      <p class="strike a">“Is this ad working?”</p>
      <p class="lbl b a">Start asking</p>
      <h1 class="head a">“What <em>job</em> is this ad doing?”</h1>
      <p class="hand a">every ad in your account has a different job. judge it by that.</p>
    </div>
  </div>
<script type="text/plain" class="notes">THE WRONG QUESTION. SLOW DOWN HERE.

"Most agents open Ads Manager, look at one ad, and ask one question: is this ad working? That's the wrong question."

"The right question is: what JOB is this ad doing? Because every ad in a good account has a different job. Once you see that, everything else in this section makes sense."</script>
</section>

<!-- ═══════════════════════ A2 · EVERY AD HAS A JOB ═══════════════════════ -->
<section data-part="3" class="slide s-job" data-kicker="03 · Ads · The funnel">
  <div class="light"></div>
  <div class="content">
    <h1 class="head a">Every ad has <em>a job.</em></h1>
    <p class="sub a">It depends on where the person is in the funnel.</p>
    <div class="fun a">
      <div class="lv frag"><div class="bd b1"><b>Top</b><span>Strangers</span></div><p class="hand">never heard of you → <b>prospecting ads</b></p></div>
      <div class="lv frag"><div class="bd b2"><b>Middle</b><span>Interested</span></div><p class="hand">clicked, watched, registered → <b>warming ads</b></p></div>
      <div class="lv frag"><div class="bd b3"><b>Bottom</b><span>Ready</span></div><p class="hand">already talked to you → <b>closer ads</b></p></div>
    </div>
  </div>
<script type="text/plain" class="notes">EVERY AD HAS A JOB.

"Picture a funnel. At the top, strangers. People who've never heard of you. In the middle, people who are interested: they clicked, watched a video, registered for a class. At the bottom, people who are ready: they already talked to you."

"You need different ads for each level. Top-of-funnel ads are called prospecting ads. Bottom-of-funnel ads are called closers. Let me show you both."</script>
</section>

<!-- ═══════════════════════ A3 · PROSPECTORS ═══════════════════════ -->
<section data-part="3" class="slide s-role" data-kicker="03 · Ads · Top of funnel">
  <div class="light"></div>
  <div class="content">
    <div class="rw">
      <div class="rt">
        <p class="eb a">Top of funnel</p>
        <h1 class="head a">Prospectors <em>open the door.</em></h1>
        <p class="rb a">These ads talk to people who have never heard of you. Their job is to find new people and get a hand raised.</p>
        <ul class="ar a">
          <li class="frag">They get <b>most of your budget</b></li>
          <li class="frag">They reach <b>new people every day</b></li>
          <li class="frag">They're <b>cheap to show</b></li>
          <li class="frag">Their cost per lead <b>looks higher. That's normal.</b></li>
        </ul>
        <div class="exad a"><span>Example</span>“Turning 65 this year? There are 3 Medicare decisions to make first.”</div>
      </div>
      <div class="ri a">''' + tile('door', 'blue') + r'''<p class="hand">the door-opener</p></div>
    </div>
  </div>
<script type="text/plain" class="notes">PROSPECTORS.

"Top of the funnel. These are your prospecting ads. They talk to people who have never heard of you. Their only job is to find new people and get a hand raised."

Walk the four:
"They get most of your budget. They reach new people every single day. They're cheap to show. And their cost per lead will look higher than your other ads. That is normal. They're talking to strangers."

"The biggest mistake I see: an agent turns this ad off because the cost per lead looks high. Two weeks later, nothing works. Because this was the ad feeding everything else."</script>
</section>

<!-- ═══════════════════════ A4 · CLOSERS ═══════════════════════ -->
<section data-part="3" class="slide s-role" data-kicker="03 · Ads · Bottom of funnel">
  <div class="light"></div>
  <div class="content">
    <div class="rw">
      <div class="rt">
        <p class="eb a">Bottom of funnel</p>
        <h1 class="head a">Closers <em>book the call.</em></h1>
        <p class="rb a">These ads talk to people who already know you. Leads who didn't book, no-shows, webinar registrants.</p>
        <ul class="ar a">
          <li class="frag">They get <b>a small budget, on purpose</b></li>
          <li class="frag">They show to <b>the same people again</b></li>
          <li class="frag">They <b>cost more to show</b></li>
          <li class="frag">They get <b>the cheapest booked calls</b></li>
        </ul>
        <div class="exad a"><span>Example</span>“Mary, your Medicare review is still open. Pick a time that works.”</div>
      </div>
      <div class="ri a">''' + tile('cal', 'gold') + r'''<p class="hand">the closer</p></div>
    </div>
    <p class="hand foot3 frag">kill your prospectors, and your closers run out of people to close.</p>
  </div>
<script type="text/plain" class="notes">CLOSERS.

"Bottom of the funnel. These are your closers. They talk to people who already know you. Leads who didn't book. No-shows. People who registered for your class."

"Small budget, on purpose, because there are only so many warm people. They show to the same people again and again. They cost more to show. And they get you the cheapest booked calls in the account."

THE LINE: "Your closers only have people to close because your prospectors fed them. Kill the prospectors, and in a couple weeks your closers run out of people."

If someone says "my ad got tired": "Most of the time it's not tired. It's doing the wrong job."</script>
</section>

<!-- ═══════════════════════ A5 · WHERE THEY ARE ═══════════════════════ -->
<section data-part="3" class="slide s-aw" data-kicker="03 · Ads · The message">
  <div class="light"></div>
  <div class="content">
    <h1 class="head a" style="font-size:80px">Talk to people <em>where they are.</em></h1>
    <p class="sub a" style="font-size:27px;margin-top:18px">The same person needs a different ad depending on how much they already know.</p>
    <div class="awg a">
      <div class="aws frag" style="--lift:0px"><p class="awt">Top</p><h3>Unaware</h3><p class="awd">Doesn't know they have a decision to make.</p><p class="awh">“Turning 65 this year? There are 3 Medicare decisions you have to make first.”</p></div>
      <div class="aws frag" style="--lift:34px"><p class="awt">Top</p><h3>Problem aware</h3><p class="awd">Knows it's confusing. Doesn't know who to trust.</p><p class="awh">“Parts A, B, C, D, G, N. Here's what actually matters, in plain English.”</p></div>
      <div class="aws frag" style="--lift:68px"><p class="awt">Middle</p><h3>Solution aware</h3><p class="awd">Knows they need a plan, or an agent. Comparing.</p><p class="awh">“Plan G or Plan N? Join Thursday's 30-minute class and bring your questions.”</p></div>
      <div class="aws frag hot" style="--lift:102px"><p class="awt">Bottom</p><h3>Already talked to you</h3><p class="awd">Opted in, registered, or no-showed.</p><p class="awh">“Mary, your review is still open. Enrollment closes December 7. Pick a time.”</p></div>
    </div>
  </div>
<script type="text/plain" class="notes">AWARENESS. WHAT MAKES THE MESSAGE MATCH THE FUNNEL.

"You don't say the same thing to a stranger that you say to someone who already filled out your form."

UNAWARE: "They don't know they have a decision to make. Lead with the decision."
PROBLEM AWARE: "They know it's confusing. Make it simple."
SOLUTION AWARE: "They know they need a plan or an agent. Give them the comparison and an easy next step, like a class."
ALREADY TALKED TO YOU: "Now you're direct. Their name, a deadline, a calendar link."

"Top-of-funnel ads talk to strangers. Bottom-of-funnel ads talk to people who know your name. Mix those up and both ads look broken."

Annual Enrollment runs October 15 to December 7.</script>
</section>

<!-- ═══════════════════════ A6 · HOW THE ACCOUNT IS BUILT ═══════════════════════ -->
<section data-part="3" class="slide s-cs" data-kicker="03 · Ads · The setup">
  <div class="light"></div>
  <div class="content">
    <h1 class="head a" style="font-size:80px">How the account is <em>actually built.</em></h1>
    <div class="csg a">
      <div class="cstree">
        <div class="csbox top frag"><p class="csk">Campaign</p><h3>One objective: Leads</h3><p>Names and phone numbers, not likes.</p></div>
        <div class="csarms frag"><i></i></div>
        <div class="cspair">
          <div class="csbox frag"><p class="csk">Ad set · Prospecting</p><h3>Broad, cold</h3><p>Your licensed states. Most of the budget.</p><div class="csads"><i></i><i></i><i></i><i></i><i></i><i></i></div></div>
          <div class="csbox cl frag"><p class="csk">Ad set · Closers</p><h3>Warm, narrow</h3><p>Leads, engagers, registrants. Small on purpose.</p><div class="csads"><i></i><i></i><i></i><i></i></div></div>
        </div>
        <p class="csnote hand frag">4 to 8 ads per ad set. more than that and none of them learn.</p>
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
<script type="text/plain" class="notes">HOW THE ACCOUNT IS BUILT.

"One campaign, one objective: leads. Under it, two ad sets. Prospecting: broad, your licensed states, most of the budget. Closers: warm and narrow, people who already raised their hand. Small on purpose. Four to eight ads in each."

THE FOUR RULES:
1. "Never edit a live ad. The moment you edit it, it starts over. Duplicate it, change it, launch it as a new ad."
2. "One change at a time. Change the image and the headline together and you'll never know what worked."
3. "Don't kill your top spender because its cost per lead looks high. It's usually the prospector feeding everything."
4. "Let it settle. When the numbers are steady week over week, then you decide."</script>
</section>

<!-- ═══════════════════════ A7 · FOUR NUMBERS ═══════════════════════ -->
<section data-part="3" class="slide s-4n" data-kicker="03 · Ads · Your numbers">
  <div class="light"></div>
  <div class="content">
    <h1 class="head a">Twenty columns. <em>Four</em> that matter.</h1>
    <div class="fnw a">
      <div class="nope frag"><p class="k">Feels like analysis</p><span>Click-through rate</span><span>Cost per click</span><span>Hook rate</span><span>Conversion rate</span><span>ROAS</span></div>
      <div class="yes">
        <div class="mi frag">''' + tile('spend', 'blue') + r'''<b>Spend</b><p class="hand">what Meta chooses</p></div>
        <div class="mi frag">''' + tile('cpm', 'yellow') + r'''<b>CPM</b><p class="hand">who it reaches</p></div>
        <div class="mi frag">''' + tile('freq', 'green') + r'''<b>Frequency</b><p class="hand">where in the funnel</p></div>
        <div class="mi frag">''' + tile('cpr', 'pink') + r'''<b>Cost per result</b><p class="hand">is it doing its job</p></div>
      </div>
    </div>
  </div>
<script type="text/plain" class="notes">TWENTY COLUMNS, FOUR THAT MATTER.

"Open Ads Manager and you get twenty columns. Click-through rate, cost per click, hook rate, ROAS. They feel like analysis. They're not the numbers you make decisions with."

"There are four. Spend, CPM, frequency, and cost per result. Let me give you each one in one sentence."</script>
</section>

<!-- ═══════════════════════ A8 · SPEND ═══════════════════════ -->
<section data-part="3" class="slide s-met" data-kicker="03 · Ads · Number 1 of 4">
  <div class="light"></div>
  <div class="content">
    <div class="mw">
      <div class="mt">
        <p class="eb a">01 · Spend</p>
        <h1 class="big1 a">Spend.</h1>
        <p class="mq a">What <em>Meta chooses.</em></p>
        <p class="rb a">Meta never splits your money evenly. The ad getting the most money is the ad Meta trusts the most.</p>
        <ul class="ar a"><li class="frag">The top spender is <b>usually your prospector</b></li><li class="frag">Don't turn it off just because <b>its cost per lead looks high</b></li></ul>
      </div>
      <div class="mv a">''' + tile('spend', 'blue big') + r'''</div>
    </div>
    <p class="hand foot3 frag">if one ad gets 70% and another gets 3%, that's not random. that's Meta talking.</p>
  </div>
<script type="text/plain" class="notes">SPEND. WHAT META CHOOSES.

"Spend is where Meta is putting your money. And Meta never splits it evenly. If one ad gets seventy percent and another gets three, that's not random. That's Meta telling you which ad it trusts."

"The ad with the most spend is usually your prospector. Do not turn it off because the cost per lead looks high."</script>
</section>

<!-- ═══════════════════════ A9 · CPM ═══════════════════════ -->
<section data-part="3" class="slide s-met" data-kicker="03 · Ads · Number 2 of 4">
  <div class="light"></div>
  <div class="content">
    <div class="mw">
      <div class="mt">
        <p class="eb a">02 · CPM</p>
        <h1 class="big1 a">CPM.</h1>
        <p class="mq a">Who <em>you reach.</em></p>
        <p class="rb a">What it costs to show your ad 1,000 times. The price tells you what kind of people you're reaching.</p>
        <ul class="ar a"><li class="frag down"><b>Low CPM:</b> broad, cold, new people</li><li class="frag up"><b>High CPM:</b> warm people who already know you</li></ul>
      </div>
      <div class="mv a">''' + tile('cpm', 'yellow big') + r'''</div>
    </div>
    <p class="hand foot3 frag">a high CPM on a closer isn't a problem. it's the design.</p>
  </div>
<script type="text/plain" class="notes">CPM. WHO YOU REACH.

"CPM is what it costs to show your ad a thousand times. It's not good or bad by itself. It tells you who you're reaching."

"Low CPM: broad, cold, new people. That's your prospector. High CPM: warm people who already know you. That's your closer. So when your closer has a high CPM, that's not a problem. That's the design."</script>
</section>

<!-- ═══════════════════════ A10 · FREQUENCY ═══════════════════════ -->
<section data-part="3" class="slide s-met" data-kicker="03 · Ads · Number 3 of 4">
  <div class="light"></div>
  <div class="content">
    <div class="mw">
      <div class="mt">
        <p class="eb a">03 · Frequency</p>
        <h1 class="big1 a">Frequency.</h1>
        <p class="mq a">Where it sits <em>in the funnel.</em></p>
        <p class="rb a">How many times one person sees your ad. Always look at it <b>by the day</b>, not the month.</p>
      </div>
      <div class="ladder a">
        <p class="k">Daily frequency</p>
        <div class="lr frag"><b>1.05</b><span class="bar"><i style="width:12%"></i></span><em>brand-new people</em></div>
        <div class="lr frag"><b>1.15</b><span class="bar"><i style="width:28%"></i></span><em>mostly prospecting</em></div>
        <div class="lr frag gz"><b>1.25</b><span class="bar"><i style="width:50%"></i></span><em>the gray zone</em></div>
        <div class="lr frag hot"><b>1.50</b><span class="bar"><i style="width:76%"></i></span><em>people who know you</em></div>
      </div>
    </div>
    <p class="hand foot3 frag">higher frequency = lower in the funnel.</p>
  </div>
<script type="text/plain" class="notes">FREQUENCY. WHERE IT SITS IN THE FUNNEL.

"Frequency is how many times one person sees your ad. And here's the trick most people miss: look at it BY THE DAY. In Ads Manager, break it down by day."

Walk the ladder:
"Around 1.05 a day, almost everybody is seeing it for the first time. Brand-new people. Up to about 1.15, it's mostly prospecting. Around 1.25 is the gray zone. Once you're at 1.5, it's mostly showing to people who already know you. That's closer territory."

"Higher frequency means lower in the funnel. That one number tells you what job the ad is doing."

These are guidelines, not hard rules. Your own account average is the real baseline.</script>
</section>

<!-- ═══════════════════════ A11 · COST PER RESULT ═══════════════════════ -->
<section data-part="3" class="slide s-met" data-kicker="03 · Ads · Number 4 of 4">
  <div class="light"></div>
  <div class="content">
    <div class="mw">
      <div class="mt">
        <p class="eb a">04 · Cost per result</p>
        <h1 class="big1 a">Cost per result.</h1>
        <p class="mq a">Is it <em>doing its job?</em></p>
        <p class="rb a">What you pay for a lead, or better, for a booked call. This is the number that tells you if the ad is working.</p>
        <ul class="ar a"><li class="frag">Judge it <b>against the ad's job</b>, not against other ads</li><li class="frag">A prospector at $7 can be doing <b>better work than a closer at $3</b></li></ul>
      </div>
      <div class="mv a">''' + tile('cpr', 'pink big') + r'''</div>
    </div>
    <p class="hand foot3 frag">the number that pays you: cost per booked call.</p>
  </div>
<script type="text/plain" class="notes">COST PER RESULT. IS IT DOING ITS JOB?

"Cost per result is what you pay for a lead, or even better, for a booked call. This is the one that tells you if the ad is doing its job."

"But judge it against its JOB, not against other ads. A prospector at seven dollars a lead can be doing better work than a closer at three, because the prospector is creating the people the closer converts."

"And if you can, track cost per booked call. That's the number that actually pays you."</script>
</section>

<!-- ═══════════════════════ A12 · TOGETHER ═══════════════════════ -->
<section data-part="3" class="slide s-rd" data-kicker="03 · Ads · Read the account">
  <div class="light"></div>
  <div class="content">
    <h1 class="head a" style="font-size:72px">Alone, each number says nothing. <em>Together,</em> they tell the story.</h1>
    <div class="rdt a">
      <div class="rdh"><span>Ad</span><span>Spend</span><span>Freq / day</span><span>CPM</span><span>Cost / lead</span><span>Verdict</span></div>
      <div class="rdr frag"><span class="an">Turning 65 · 3 decisions<small>Static image</small></span><span>$1,840<small>62% of spend</small></span><span>1.08</span><span>$9</span><span>$7.40</span><span class="vd ok"><b>Prospector</b>Leave it. It feeds everything.</span></div>
      <div class="rdr frag"><span class="an">Your review is still open<small>Warm audience</small></span><span>$310<small>10% of spend</small></span><span>1.62</span><span>$31</span><span>$3.10</span><span class="vd ok"><b>Closer</b>Leave it. It's meant to be small.</span></div>
      <div class="rdr frag bad"><span class="an">Plan G static v2<small>Static image</small></span><span>$95<small>3% of spend</small></span><span>1.31</span><span>$28</span><span>$19.80</span><span class="vd no"><b>No job</b>Not earning spend. Launch a new version.</span></div>
    </div>
    <p class="rdx a">Example account</p>
    <p class="hand foot3 frag">sort by spend. read each ad left to right. then decide.</p>
  </div>
<script type="text/plain" class="notes">PUT THE FOUR TOGETHER. THE DEMO THAT MAKES YOU THE EXPERT.

"Here's how I read an account in about sixty seconds. Sort by spend, highest to lowest. Read every ad left to right."

ROW 1: "Sixty-two percent of the spend. Frequency 1.08 a day: new people. CPM nine dollars: cheap and broad. $7.40 a lead. A beginner turns this off. That's the worst thing you could do. It's the prospector. It feeds everything."

ROW 2: "Ten percent of the spend. Frequency 1.6, CPM thirty-one: warm people. $3.10 a lead. It's the closer. It's supposed to be small. Leave it."

ROW 3: "Three percent of the spend, almost twenty bucks a lead. Meta can't find a job for it. Don't edit it. Launch a new version and let it earn spend."

These are example numbers for teaching. Say so if anyone asks.</script>
</section>'''

sub1(r'<!-- ═+ 11 MEDIA · THE 20% ═+ -->.*?</section>', ADS)

rep('<b>Kill, then feed</b><span>Turn off what doesn\'t work. Move the money to what does. Every week.</span>',
    '<b>Replace, don\'t just kill</b><span>An ad with no job gets a new version. The top spender stays.</span>')
rep('<b>The average is the skill</b><span>$5.92 isn\'t one lucky ad. It\'s what\'s left after you cut the losers.</span>',
    '<b>The average is the skill</b><span>$5.92 isn\'t one lucky ad. It\'s a full team of ads, each doing its job.</span>')
rep('"Some of these ads cost fifteen, twenty-three dollars a lead. I lost money on them. The average is $5.92 because I killed those and fed the ones that worked. That IS the skill."',
    '"Some of these ads cost fifteen, twenty-three dollars a lead. Some were prospectors doing their job, some had no job and got replaced. The average is $5.92 because the account works as a team. That IS the skill."')

BACK1 = r'''<!-- ═══════════════════════ B1 · FRONT END VS BACK END ═══════════════════════ -->
<section data-part="5" class="slide s-fb" data-kicker="05 · Backend">
  <div class="light"></div>
  <div class="content">
    <h1 class="head a">The back end is <em>just as important</em> as the front end.</h1>
    <div class="fbw a">
      <div class="fbp frag"><p class="k">The front end</p><h3>Gets you the lead.</h3><div class="chips"><span>Market</span><span>Message</span><span>Ads</span><span>Funnel</span></div><p class="hand">where most agents spend 100% of their time</p></div>
      <div class="fbeq frag">=</div>
      <div class="fbp gold frag"><p class="k">The back end</p><h3>Turns the lead into money.</h3><div class="chips"><span>Speed to lead</span><span>Nurture</span><span>Reminders</span><span>No-show recovery</span><span>Pipeline</span><span>Reactivation</span><span>Cross-sell</span><span>Referrals</span></div><p class="hand">where the money actually gets made</p></div>
    </div>
  </div>
<script type="text/plain" class="notes">FRONT END VS BACK END. THIS IS THE BIG IDEA OF THE BACKEND SECTION.

"Everything we've talked about so far: market, message, ads, funnel. That's the front end. It gets you the lead. And that's where almost every agent spends a hundred percent of their time."

"But the lead isn't money. The back end is what turns the lead into money. Speed to lead. Nurture. Reminders. Getting no-shows back. A pipeline so nobody gets forgotten. Reactivating old leads. The cross-sell. Referrals."

"The back end is just as important as the front end. Let me prove it."</script>
</section>

<!-- ═══════════════════════ B2 · SAME LEADS, TWO AGENTS ═══════════════════════ -->
<section data-part="5" class="slide s-ab" data-kicker="05 · Backend · Why it matters">
  <div class="light"></div>
  <div class="content">
    <h1 class="head a" style="font-size:76px">Same ad. Same 100 leads.<br><em>Four times the clients.</em></h1>
    <div class="abw a">
      <div class="abh"></div><div class="abh"><p class="k">Agent A</p><h3>No back end</h3></div><div class="abh gold"><p class="k">Agent B</p><h3>With a back end</h3></div>
      <div class="abm frag">Called in 5 minutes</div><div class="abv frag"><i class="x">✕</i>Calls the next day</div><div class="abv g frag"><i class="ok">✓</i>Text in 1 minute, call in 5</div>
      <div class="abm frag">Reminders</div><div class="abv frag"><i class="x">✕</i>None</div><div class="abv g frag"><i class="ok">✓</i>Night before + morning of</div>
      <div class="abm frag">No-shows</div><div class="abv frag"><i class="x">✕</i>Gone</div><div class="abv g frag"><i class="ok">✓</i>Rebook text in minutes</div>
      <div class="abm frag">Not ready yet</div><div class="abv frag"><i class="x">✕</i>Forgotten</div><div class="abv g frag"><i class="ok">✓</i>Nurtured for 90 days</div>
      <div class="abm tot frag">New clients</div><div class="abv tot frag"><b>2</b><small>$1,388</small></div><div class="abv g tot frag"><b>8</b><small>$5,552</small></div>
    </div>
    <p class="hand foot3 frag">the ad didn't change. the back end did. <small>(example numbers)</small></p>
  </div>
<script type="text/plain" class="notes">SAME LEADS, TWO AGENTS. THE PROOF THAT THE BACK END MATTERS.

"Two agents. Same ad. Same hundred leads."

Walk the rows:
"Agent A calls the next day. Agent B's system texts in one minute, and B calls in five."
"Agent A sends no reminders. Agent B's go out the night before and the morning of."
"Agent A's no-shows are gone. Agent B sends a rebook text within minutes."
"Agent A forgets the people who weren't ready. Agent B nurtures them for ninety days."

"Agent A gets two clients. Agent B gets eight. Same ad. Same leads. Four times the clients. The ad didn't change. The back end did."

These are example numbers (the same rates as the math slide coming up: 30 booked, 21 showed, 8 clients at $694). Say so if asked.</script>
</section>

<!-- ═══════════════════════ B3 · SPEED TO LEAD ═══════════════════════ -->
<section data-part="5" class="slide s-spd" data-kicker="05 · Backend · Speed to lead">
  <div class="light"></div>
  <div class="content">
    <div class="spw">
      <div class="spl">
        <h1 class="head a">The first <em>five minutes</em> decide the lead.</h1>
        <p class="rb a">The system handles the first minute. You make the call.</p>
        <div class="spt a">
          <div class="st1 frag"><b>0:00</b><p>Mary fills out your form</p></div>
          <div class="st1 frag"><b>0:01</b><p>She gets a text: <em>“Hi Mary, got your request. Calling you in a few minutes.”</em></p></div>
          <div class="st1 frag"><b>0:01</b><p>Your phone buzzes with a new-lead alert</p></div>
          <div class="st1 gold frag"><b>0:05</b><p><strong>You call.</strong> She still remembers filling it out.</p></div>
          <div class="st1 late frag"><b>Tomorrow</b><p>You're calling a stranger.</p></div>
        </div>
      </div>
      <div class="ri a">''' + tile('clock', 'green big') + r'''<p class="hand">speed to lead</p></div>
    </div>
  </div>
<script type="text/plain" class="notes">SPEED TO LEAD.

"The first five minutes decide the lead."

Walk the clock:
"Zero: Mary fills out your form. One minute: she gets a text from you, automatically. 'Hi Mary, got your request, calling you in a few minutes.' At the same time your phone buzzes with a lead alert. Five minutes: you call. She still remembers filling it out."

"Call her tomorrow, and you're calling a stranger. She's filled out three other forms since then."

"The system handles the first minute. You make the call."</script>
</section>

<!-- ═══════════════════════ B4 · THE NURTURE SEQUENCE ═══════════════════════ -->
<section data-part="5" class="slide s-nur" data-kicker="05 · Backend · Nurture">
  <div class="light"></div>
  <div class="content">
    <h1 class="head a" style="font-size:80px">The nurture sequence: <em>trust on autopilot.</em></h1>
    <p class="sub a" style="font-size:27px;margin-top:18px">For everyone who didn't book yet. Every message has one job.</p>
    <div class="nuw a">
      <div class="nu frag"><p class="d">Day 0 · Text + email</p><p class="m">“Here's your checklist, and my calendar if you want help.”</p><p class="j">Deliver the promise</p></div>
      <div class="nu frag"><p class="d">Day 1 · Email</p><p class="m">“The 3 Medicare mistakes that cost people the most.”</p><p class="j">Teach</p></div>
      <div class="nu frag"><p class="d">Day 2 · Email</p><p class="m">A real story from one of your own clients.</p><p class="j">Proof</p></div>
      <div class="nu frag"><p class="d">Day 3 · Text</p><p class="m">“Any questions so far? Just reply here.”</p><p class="j">Start a conversation</p></div>
      <div class="nu frag"><p class="d">Day 5 · Email</p><p class="m">“What to have ready for your Medicare review.”</p><p class="j">Remove the friction</p></div>
      <div class="nu gold frag"><p class="d">Day 7 · Text</p><p class="m">“Still want help? Here's my calendar.”</p><p class="j">Ask for the booking</p></div>
    </div>
    <p class="hand foot3 frag">write it once. it works every night while you sleep.</p>
  </div>
<script type="text/plain" class="notes">THE NURTURE SEQUENCE.

"Most of your leads won't book on day one. That doesn't mean they're not interested. It means they don't trust you yet. The nurture sequence builds that trust automatically."

Walk the six, and say the job of each:
"Day zero: deliver what you promised, plus your calendar. Day one: teach them something. Day two: a real story from one of your clients. Day three: a simple text, 'any questions?' That one starts conversations. Day five: tell them what to have ready, so booking feels easy. Day seven: ask for the booking."

"You write it once. It runs every night while you sleep, for every single lead."</script>
</section>'''

PIPE = r'''<!-- ═══════════════════════ B5 · THE PIPELINE ═══════════════════════ -->
<section data-part="5" class="slide s-kb" data-kicker="05 · Backend · Pipeline">
  <div class="light"></div>
  <div class="content">
    <h1 class="head a" style="font-size:80px">Know where <em>every lead</em> is.</h1>
    <p class="sub a" style="font-size:27px;margin-top:18px">A pipeline is just a board. Every lead sits in one column, and you can see who needs you today.</p>
    <div class="kbw a">
      <div class="col frag"><p class="h">New lead <i>3</i></p><div class="cd"><b>Mary H.</b><span>Turning 65 · checklist</span></div><div class="cd"><b>Robert K.</b><span>Part B delay</span></div><div class="cd"><b>Linda P.</b><span>Dental</span></div></div>
      <div class="col frag"><p class="h">Contacted <i>2</i></p><div class="cd"><b>James W.</b><span>Called · left voicemail</span></div><div class="cd"><b>Carol S.</b><span>Texted back</span></div></div>
      <div class="col frag"><p class="h">Booked <i>2</i></p><div class="cd"><b>Ann M.</b><span>Tue 10:00</span></div><div class="cd"><b>Frank D.</b><span>Wed 2:30</span></div></div>
      <div class="col frag"><p class="h">No-show <i>1</i></p><div class="cd warn"><b>Paul R.</b><span>Rebook text sent</span></div></div>
      <div class="col frag"><p class="h">Client <i>2</i></p><div class="cd ok"><b>Susan T.</b><span>Plan G</span></div><div class="cd ok"><b>Gary L.</b><span>Advantage</span></div></div>
      <div class="col frag gold"><p class="h">Cross-sell <i>1</i></p><div class="cd ok"><b>Susan T.</b><span>Hospital indemnity</span></div></div>
    </div>
    <p class="hand foot3 frag">if it's not in the pipeline, you will forget them.</p>
  </div>
<script type="text/plain" class="notes">THE PIPELINE.

"A pipeline sounds technical. It's not. It's a board. Every lead sits in one column: new, contacted, booked, no-show, client, cross-sell."

"Every morning you look at it and you know exactly who needs you today. Paul no-showed? The system already sent the rebook text. Susan became a client? She moves to cross-sell, and that's where the hospital indemnity conversation happens."

"If it's not in the pipeline, you will forget them. And the person you forget is the money you already paid for."

The names on this board are made up for the example.</script>
</section>'''

# backend: drop the old ledger slide, add the new ones around the follow-up schedule
sub1(r'<!-- ═+ 22 THE BACKEND ═+ -->.*?</section>\s*', '')
sub1(r'(<!-- ═+ 18 FOLLOW-UP · THE SCHEDULE ═+ -->.*?</section>)', BACK1 + '\n\n' + '\\1' + '\n\n' + PIPE)
# the regex replacement above inserted a literal \1; put the follow-up slide back
m = re.search(r'(<!-- ═+ 18 FOLLOW-UP · THE SCHEDULE ═+ -->.*?</section>)', open(P, encoding='utf-8').read(), re.S)
s = s.replace('\\1', m.group(1))

# whiteboard register on every teaching slide (not the chapter openers, not the machine loop)
def wb(mo):
    tag = mo.group(0)
    if 's-loop' in tag: return tag
    return tag.replace('class="slide', 'class="slide wb', 1)
s = re.sub(r'<section data-part="\d" class="slide[^"]*"', wb, s)

s = s.replace('data-kicker="05 · Monetization', 'data-kicker="05 · Backend')
open(P, 'w', encoding='utf-8').write(s)
print('sections', s.count('<section'), 'wb', s.count('class="slide wb'))
