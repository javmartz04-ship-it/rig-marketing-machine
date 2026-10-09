# v10: no "build it yourself" anywhere, and the price is said once, high to low.
# The $147 price slide and the $147 → $300 bars are gone; the recap shows value so far, not a price.
# The stack lists keep $147/mo as the Skool group's stand-alone value, like every other item's value.
# Runs after v9.py (reads and rewrites src/slides.html).
import re, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(ROOT, 'src/slides.html')
s = open(P, encoding='utf-8').read()

def rep(a, b, n=1):
    global s
    assert a in s, 'missing: ' + a[:90]
    s = s.replace(a, b, n)

def drop(opener):
    global s
    a = s.index(opener)
    b = s.index('</section>', a) + len('</section>')
    s = s[:a] + s[b:].lstrip('\n')

# ── no DIY lines ──
rep("Who to target, what to say, where to run it, what happens after the click. Take it and build it yourself.",
    "Who to target, what to say, where to run it, and what happens after the click.")
rep(" Until then, this is marketing. Real marketing. If you never talk to me again after tonight, you should still be able to go build this.\"",
    " Until then, this is marketing. Real marketing.\"")
rep('<div class="foot2 frag">You can build all of it yourself. <span>Or we can help you build it.</span> Here\'s how.</div>',
    '<div class="foot2 frag">That\'s exactly what we <span>help you build.</span> Here\'s how.</div>')
rep('"So everything I just showed you, you can absolutely build yourself. To do it you need three things.',
    '"So to run everything I just showed you, you need three things.')

# ── price once, high to low ──
drop('<section class="slide wb s-offer s-corep"')
drop('<section class="slide wb s-delta2"')
rep('(Javier is sending a better video of the wins feed. When it lands, it goes on this slide.)</script>',
    '(Javier is sending a better video of the wins feed. When it lands, it goes on this slide.)\n\nDON\'T SAY A PRICE YET. The price comes once, at the very end.\n\nThen: "And because you stayed with me tonight, I want to do something just for you." Click to the gift slide.</script>')
rep('''      <p class="k">You pay</p>
      <div class="v">$147<small>/mo</small></div>
      <p>That alone is the best deal in Medicare.</p>''',
    '''      <p class="k">Value so far</p>
      <div class="v">$9,000<small>+ $244/mo</small></div>
      <p>And I haven't told you the price yet.</p>''')
rep('''"So if you join today: the community, the playbook, your GoHighLevel account, onboarding with David, and the snapshots. All for a hundred and forty-seven a month."

"That alone is the best deal in Medicare."''',
    '''"So if you join today: the community, the playbook, your GoHighLevel account, onboarding with David, and the snapshots. That's nine thousand dollars of value, plus two hundred forty-four a month."

"And I haven't even told you the price yet." Don't say a number here. The price comes once, at the end.''')
rep('<div class="core"><i>★</i>The Real Insurance Group community <span>$147/mo</span></div>',
    '<div class="core"><i>★</i>Our Skool group <span>$147/mo</span></div>')
rep('Every three or four questions, flip back to the whole-offer slide or the $147 to $300 bars.',
    'Every three or four questions, flip back to the whole-offer slide.')

assert 's-corep' not in s and 's-delta2' not in s
assert 'yourself' not in s.lower(), [m.start() for m in re.finditer('yourself', s, re.I)]
open(P, 'w', encoding='utf-8').write(s)
print('v10 ok, slides', s.count('<section '))
