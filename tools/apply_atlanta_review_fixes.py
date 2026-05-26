from pathlib import Path
import re
import subprocess


def run(cmd):
    subprocess.run(cmd, check=True)

p = Path('index.html')
s = p.read_text(encoding='utf-8')

# 1) Hero H1 color mapping: same hero structure, only text/span mapping changes.
old_h1 = '''<h1 class="hero-headline font-bebas tracking-wide mb-6">
        <span class="gradient-text">Atlanta</span> Corporate Events <span class="gradient-text">&amp; Event Ideas</span><br>
        Built for Teams, Clients &amp; <span class="gradient-text">Real Engagement</span>
      </h1>'''
new_h1 = '''<h1 class="hero-headline font-bebas tracking-wide mb-6">
        <span class="text-white">Atlanta </span><span class="gradient-text">Corporate Events &amp;</span><br>
        <span class="text-white">Event Ideas Built for </span><span class="gradient-text">Teams, Clients &amp;</span><br>
        <span class="text-white">Real Engagement</span>
      </h1>'''
if old_h1 not in s:
    raise SystemExit('Hero H1 target block not found')
s = s.replace(old_h1, new_h1, 1)

# 2) Gallery front-card "View details" positioning: keep layout/classes, make title/hint block-level.
css_anchor = """#lvpt-corporate-gallery .lvpt-gallery-card-hint { display: inline-flex; align-items: center; gap: 0.42rem; margin-top: 0.9rem; color: rgba(255, 255, 255, 0.74); font-size: clamp(0.78rem, 2.7vw, 0.92rem); font-weight: 700; font-family: 'Inter', sans-serif; }"""
css_patch = css_anchor + """
  #lvpt-corporate-gallery .lvpt-gallery-front-content { display: block; width: 100%; }
  #lvpt-corporate-gallery .lvpt-gallery-card-title { display: block; }
  #lvpt-corporate-gallery .lvpt-gallery-card-hint { display: flex; width: max-content; max-width: 100%; }"""
if css_anchor not in s:
    raise SystemExit('Gallery hint CSS anchor not found')
s = s.replace(css_anchor, css_patch, 1)

# 3) Venetian card back copy: clarify Vegas destination + local poker-room coordination.
old_venetian = "A premium Las Vegas poker room setting can give Atlanta corporate guests an authentic, high-end destination option for client entertainment, executive groups, and VIP team experiences."
new_venetian = "If your Atlanta group is coming to see us in Las Vegas, the Venetian Poker Room experience creates an authentic, high-end destination setting for client entertainment, executive groups, and VIP team events. If you have a suitable poker room near you, we can also help coordinate a pro-led training experience there when venue access and logistics allow."
if old_venetian not in s:
    raise SystemExit('Venetian back-card description not found')
s = s.replace(old_venetian, new_venetian, 1)

# 4) Mobile footer/social clearance above fixed CTA.
footer_css_anchor = "/* BLOCK 107 END */"
footer_patch = """
/* =========================================================
   BLOCK 108 START: ATLANTA MOBILE FOOTER CTA CLEARANCE
   Purpose:
   - Keeps the very bottom footer/social area above the fixed mobile CTA
   - Does not affect desktop layout
   ========================================================= */
@media (max-width: 767px) {
  body {
    padding-bottom: 5.5rem !important;
  }

  #lvpt-corporate-events > .full-bleed:last-of-type {
    padding-bottom: 8rem !important;
  }

  #lvpt-corporate-events .lvpt-footer-contact {
    padding-bottom: 5.5rem !important;
  }
}
/* BLOCK 108 END */
"""
if footer_css_anchor not in s:
    raise SystemExit('Footer CSS anchor not found')
s = s.replace(footer_css_anchor, footer_css_anchor + "\n" + footer_patch, 1)

p.write_text(s, encoding='utf-8')

Path('tools/apply_atlanta_review_fixes.py').unlink(missing_ok=True)
Path('.github/workflows/apply-atlanta-review-fixes.yml').unlink(missing_ok=True)

run(['git', 'config', 'user.name', 'github-actions[bot]'])
run(['git', 'config', 'user.email', '41898282+github-actions[bot]@users.noreply.github.com'])
run(['git', 'add', 'index.html', 'tools/apply_atlanta_review_fixes.py', '.github/workflows/apply-atlanta-review-fixes.yml'])
run(['git', 'commit', '-m', 'Apply Atlanta review fixes'])
run(['git', 'push'])
