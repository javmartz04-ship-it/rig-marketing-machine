# v8: David's face everywhere he's named in the offer; the 15-minute timer auto-starts on "How we help".
# Runs after v7.py (reads and rewrites src/slides.html).
import re, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(ROOT, 'src/slides.html')
s = open(P, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert a in s, 'missing: ' + a[:90]
    s = s.replace(a, b, n)

# David (and Christopher) on the one-screen summary and the outcome
rep('<div class="f3c"><p class="k">Bonus #3</p><h3>Onboarding with David</h3><b>$1,000</b></div>',
    '<div class="f3c face"><img class="av" src="assets/david.png" alt="David"><p class="k">Bonus #3</p><h3>Onboarding with David</h3><b>$1,000</b></div>')
rep('<div class="f3c spec"><p class="k">Bonus #5 · Only today</p>', '<div class="f3c spec face"><img class="av" src="assets/christopher.jpg" alt="Christopher"><p class="k">Bonus #5 · Only today</p>')
rep('<div class="ot frag"><i>01</i><h3>Onboarding with David</h3>', '<div class="ot frag"><img class="oav" src="assets/david.png" alt="David"><i>01</i><h3>Onboarding with David</h3>')
rep('<div class="ot frag"><i>02</i><h3>Your specialist builds it</h3>', '<div class="ot frag"><img class="oav" src="assets/christopher.jpg" alt="Christopher"><i>02</i><h3>Your specialist builds it</h3>')

# the timer: visible from "How we help" on, and it starts itself there
rep('<section class="slide s-ch" data-kicker="How we help">', '<section class="slide s-ch" data-timer data-timer-start data-kicker="How we help">')
for k in ['s-core1', 's-class', 's-live', 's-offer s-corep']:
    s = re.sub(r'<section class="slide wb ' + re.escape(k) + r'"', lambda m: m.group(0) + ' data-timer', s, count=1)
s = s.replace('THE OFFER OPENS.\n\n', 'THE OFFER OPENS. THE 15-MINUTE CLOCK STARTS BY ITSELF ON THIS SLIDE (top right).\n\n', 1)
rep('<p class="hand a">the clock starts now: 10 minutes. and we\'re only taking 12 people today.</p>',
    '<p class="hand a">the clock in the corner is already running. and we\'re only taking 12 people today.</p>')
rep('PRESS T (or click the timer in the corner) to start the 10-minute clock. It keeps running through every slide to the end.',
    'THE CLOCK IS ALREADY RUNNING. It started on its own on the "How we help" slide. Point at it. (T pauses it, Shift+T resets it.)')
rep('The clock starts now: ten minutes.', 'See the clock in the corner? It\'s already running.')
open(P, 'w', encoding='utf-8').write(s)
print('timer slides', s.count('data-timer'), 'autostart', s.count('data-timer-start'))
s = open(P, encoding='utf-8').read()
s = s.replace('<div class="f3c core"><p class="k">The main thing</p><h3>The Real Insurance Group community</h3><p>The classroom, live calls every business day, and the wins.</p>',
              '<div class="f3c core"><p class="k">Our Skool group</p><h3>Launch your first campaign</h3><p>The community, the courses, live calls every business day, and the wins.</p>')
s = s.replace('"The community, the main thing. Bonus one', '"Our Skool group. Bonus one')
open(P, 'w', encoding='utf-8').write(s)
s = open(P, encoding='utf-8').read()
s = s.replace('<div class="t">The community<small>The main thing</small></div>', '<div class="t">Our Skool group<small>On its own</small></div>')
open(P, 'w', encoding='utf-8').write(s)
