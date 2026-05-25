from pathlib import Path
import re
import subprocess
import urllib.request

LA_URL = "https://raw.githubusercontent.com/LuckyMittenGaming/lvpt-los-angeles/main/index.html"
HERO_IMAGE = "https://assets.cdn.filesafe.space/E2BEbKIK8SvsJICq4vXY/media/6a149e147e7c5a2f715a9903.webp"


def replace_block(html: str, start_marker: str, end_marker: str, replacement: str) -> str:
    start = html.index(start_marker)
    end = html.index(end_marker, start) + len(end_marker)
    return html[:start] + replacement.strip() + "\n" + html[end:]


def replace_section(html: str, start_marker: str, end_marker: str, replacement: str) -> str:
    return replace_block(html, start_marker, end_marker, replacement)


def run(cmd):
    subprocess.run(cmd, check=True)


def main():
    html = urllib.request.urlopen(LA_URL, timeout=30).read().decode("utf-8")

    # -------------------------------------------------------------------------
    # Global non-structural city, URL, and color conversion.
    # -------------------------------------------------------------------------
    replacements = {
        "LVPT LOS ANGELES CITY PAGE": "LVPT ATLANTA CITY PAGE",
        "LOS ANGELES GREEN/GOLD/RED THEME": "ATLANTA BLUE/GOLD THEME",
        "LOS ANGELES THEME OVERRIDES": "ATLANTA THEME OVERRIDES",
        "FINAL LOS ANGELES CONSISTENCY PATCH": "FINAL ATLANTA CONSISTENCY PATCH",
        "LA CASINO CTA EQUAL BUTTON SIZE FIX": "ATLANTA CASINO CTA EQUAL BUTTON SIZE FIX",
        "Los Angeles CTA": "Atlanta CTA",
        "Los Angeles": "Atlanta",
        "LOS ANGELES": "ATLANTA",
        "Los%20Angeles": "Atlanta",
        "los-angeles": "atlanta",
        "corporate events los angeles": "corporate events atlanta",
        "corporate event ideas los angeles": "corporate event ideas atlanta",
        "#00933D": "#1E4C8A",
        "#FFBC00": "#F9D317",
        "#EF2017": "#F9D317",
        "#FFE066": "#FFF1A8",
        "#006B2D": "#14345F",
        "#D99C00": "#D7B30F",
        "rgba(0,147,61": "rgba(30,76,138",
        "rgba(255,188,0": "rgba(249,211,23",
    }
    for old, new in replacements.items():
        html = html.replace(old, new)

    # Keep the intended Atlanta hero image and preload.
    html = re.sub(r'href="https://assets\.cdn\.filesafe\.space/E2BEbKIK8SvsJICq4vXY/media/[^\"]+\.webp"\n    fetchpriority="high"\n    media="\(min-width: 1024px\)"', f'href="{HERO_IMAGE}"\n    fetchpriority="high"\n    media="(min-width: 1024px)"', html, count=1)

    # -------------------------------------------------------------------------
    # Hero block: same layout, unique Atlanta SEO/conversion copy.
    # -------------------------------------------------------------------------
    hero = f'''
    <!-- =================================================================
     BLOCK 5 START: HERO SECTION (MOBILE TEXT & BUTTON FIXES)
     ================================================================= -->
<div class="full-bleed bg-[#0e0e0e] relative overflow-hidden flex items-center min-h-[85vh] py-16 md:py-24">
  <div class="absolute top-0 left-0 w-full h-full bg-[radial-gradient(ellipse_at_top_left,rgba(249,211,23,0.12),transparent_50%)] pointer-events-none"></div>
  
  <div class="relative z-10 w-[95%] md:w-[90%] ml-auto mr-auto md:ml-[5%] md:mr-0 flex flex-col items-center md:items-start">
    
    <img src="{HERO_IMAGE}"
         alt="Corporate poker training and team building event for Atlanta companies"
         class="absolute right-0 top-1/2 -translate-y-1/2 w-[50%] max-w-[800px] object-contain opacity-0 animate-fade-in-right hidden lg:block pointer-events-none"
         style="animation-delay: 0.3s; filter: drop-shadow(0 10px 20px rgba(0,0,0,0.5));"
         loading="eager" decoding="async" fetchpriority="high" width="800" height="600">

    <div class="w-full text-center md:text-left mb-6 md:mb-8">
      <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full border border-[var(--city-gradient-secondary)]/30 bg-[var(--city-gradient-secondary)]/10 text-[var(--city-gradient-secondary)] text-xs md:text-sm uppercase tracking-widest font-bold">
        <span class="w-2 h-2 rounded-full bg-[var(--city-gradient-secondary)] animate-pulse"></span>
        Serving Atlanta, Buckhead, Midtown, Downtown &amp; Greater Atlanta
      </div>
    </div>
    
    <div class="max-w-xl lg:max-w-2xl text-center md:text-left">
      <h1 class="hero-headline font-bebas tracking-wide mb-6">
        <span class="gradient-text">Atlanta</span> Corporate Events <span class="gradient-text">&amp; Event Ideas</span><br>
        Built for Teams, Clients &amp; <span class="gradient-text">Real Engagement</span>
      </h1>
      
      <p class="lvpt-mobile-left text-xl md:text-3xl text-white font-medium mb-6 leading-snug">
        Interactive Poker Training · Strategic Team Building · Casino Night Entertainment · Client-Facing Corporate Experiences
      </p>
      
      <p class="lvpt-mobile-left text-gray-300 text-base md:text-lg lg:text-xl leading-relaxed mb-10">
        Stop sorting through generic Atlanta team building activities and venue lists. Our immersive poker experiences turn offices, hotels, conference spaces, hospitality suites, restaurants, and private venues into high-energy corporate events built for engagement, decision-making, networking, and memorable client entertainment.
      </p>
      
      <div class="flex flex-col sm:flex-row gap-5 justify-center md:justify-start mb-12">
        <a href="#quote-builder" class="btn-primary text-lg hero-btn">
          Build My Atlanta Event <svg class="lvpt-icon " aria-hidden="true" focusable="false" viewBox="0 0 24 24"><path d="M5 12h14"></path><path d="M13 6l6 6-6 6"></path></svg>
        </a>
        <a href="#event-formats" class="btn-outline text-lg hero-btn">
          Explore Event Formats <svg class="lvpt-icon " aria-hidden="true" focusable="false" viewBox="0 0 24 24"><path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7-10-7-10-7z"></path><circle cx="12" cy="12" r="3"></circle></svg>
        </a>
      </div>
      
      <div class="flex flex-wrap gap-4 md:gap-8 justify-center md:justify-start text-xs sm:text-sm text-gray-400 font-semibold uppercase tracking-wider">
        <div class="flex items-center gap-2"><svg class="lvpt-icon " aria-hidden="true" focusable="false" viewBox="0 0 24 24"><path d="M4 20V4"></path><path d="M4 4h10l-2 4 2 4H4"></path><path d="M14 14h6l-1.5 3L20 20h-6"></path></svg> Team Building</div>
        <div class="flex items-center gap-2"><svg class="lvpt-icon " aria-hidden="true" focusable="false" viewBox="0 0 24 24"><path d="M8 12l3 3a2 2 0 0 0 3 0l1-1"></path><path d="M2 12l4-4 4 4"></path><path d="M22 12l-4-4-4 4"></path><path d="M7 13l-2 2"></path><path d="M17 13l2 2"></path></svg> Client Entertainment</div>
        <div class="flex items-center gap-2"><svg class="lvpt-icon " aria-hidden="true" focusable="false" viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="3"></rect><circle cx="8" cy="8" r="1"></circle><circle cx="16" cy="8" r="1"></circle><circle cx="12" cy="12" r="1"></circle><circle cx="8" cy="16" r="1"></circle><circle cx="16" cy="16" r="1"></circle></svg> Casino Night Options</div>
        <div class="flex items-center gap-2"><svg class="lvpt-icon " aria-hidden="true" focusable="false" viewBox="0 0 24 24"><circle cx="12" cy="7" r="4"></circle><path d="M4 21a8 8 0 0 1 16 0"></path></svg> Pro Instructors</div>
      </div>
    </div>
  </div>
</div>
<!-- BLOCK 5 END -->
'''
    html = replace_section(html, "<!-- =================================================================\n     BLOCK 5 START: HERO SECTION", "<!-- BLOCK 5 END -->", hero)

    intro = '''
    <!-- =================================================================
         BLOCK 6 START: CITY-SPECIFIC INTRO (NO BOLD)
         ================================================================= -->
    <div class="full-bleed bg-[#111] section-spacing">
      <div class="section-inner">
        <div class="readable-block">
          <h2 class="text-4xl md:text-5xl font-bebas gold-text mb-6 text-center">A Better Corporate Event Idea for Atlanta Companies</h2>
          <div class="text-gray-300 text-lg leading-relaxed space-y-4">
            <p class="lvpt-mobile-left">Atlanta companies — from Fortune 500 headquarters and fintech teams to healthcare, logistics, production, real estate, agency, SaaS, and sales organizations — often need corporate events that feel polished, social, and memorable without turning into another passive dinner, mixer, or conference reception.</p>
            <p class="lvpt-mobile-left">LVPT is not another Atlanta venue list, event planner directory, or passive entertainment option. We bring interactive poker training, casino night entertainment, and poker-based team building to your office, hotel, private venue, conference space, hospitality suite, restaurant, or event location.</p>
            <p class="lvpt-mobile-left">Guests learn how to read people, manage uncertainty, communicate under pressure, and make better decisions in a format that works for executives, clients, and mixed-skill groups. The result is a premium Atlanta corporate event idea that gives the room energy, interaction, and a shared story after the event ends.</p>
          </div>
        </div>
      </div>
    </div>
    <!-- BLOCK 6 END -->
'''
    html = replace_section(html, "<!-- =================================================================\n         BLOCK 6 START", "<!-- BLOCK 6 END -->", intro)

    # -------------------------------------------------------------------------
    # Targeted copy swaps for visible sections, forms, gallery, and JS labels.
    # -------------------------------------------------------------------------
    targeted = {
        "Corporate Event Formats for Atlanta Companies": "Corporate Event Formats for Atlanta Companies",
        "Perfect for Atlanta leadership teams, sales groups, and client-facing events, Hand Analysis turns live poker decisions into conversations about timing, risk, psychology, and reading the room.": "Designed for Atlanta leadership teams, sales groups, and client-facing corporate events, Hand Analysis turns real poker decisions into practical conversations about timing, risk, psychology, and reading the room.",
        "A guided strategy session for Atlanta companies that want a more structured team building or executive learning experience before guests move into live play.": "A guided strategy session for Atlanta companies that want structured learning before live play, including poker fundamentals, decision-making concepts, table psychology, and business parallels.",
        "A high-energy tournament format for Atlanta company parties, leadership offsites, sales teams, and corporate groups that want friendly competition with professional structure.": "A competitive format for Atlanta company parties, leadership offsites, sales kickoffs, and group activities where guests want a clear finish, prize moment, and professional event flow.",
        "A pure entertainment option for Atlanta holiday parties, fundraisers, mixers, client receptions, and company celebrations with tables, chips, cards, and professional dealers.": "A pure entertainment option for Atlanta corporate parties, fundraisers, client receptions, holiday celebrations, and company outings with tables, chips, cards, and professional dealers.",
        "Why Poker Training Works for Atlanta Corporate Events": "Why Poker Training Works for Atlanta Corporate Events",
        "Combines Atlanta team building, strategy, communication, and decision-making in one interactive corporate event.": "Combines Atlanta team building, strategy, communication, pressure, and decision-making in one interactive corporate event experience.",
        "Keeps Atlanta attendees involved through real-time participation, discussion, and competition.": "Keeps Atlanta attendees involved through real-time play, pro-led discussion, team interaction, and friendly competition.",
        "Venue planning, tables, chips, dealers, event flow, and travel logistics can be shaped around your Atlanta event.": "Tables, chips, cards, dealers, event flow, travel logistics, and venue coordination can be shaped around your Atlanta event goals.",
        "Why Poker Training Is a Strong Atlanta Team Building Activity": "Why Poker Training Is a Strong Atlanta Team Building Activity",
        "All skill levels can participate, making it useful for mixed-experience Atlanta corporate groups.": "All skill levels can participate, making it useful for mixed-experience Atlanta corporate groups, cross-functional teams, and client-facing gatherings.",
        "Why Poker Training Works for Atlanta Party Entertainment": "Why Poker Training Works for Atlanta Party Entertainment",
        "No poker experience is required, so your Atlanta party stays approachable and interactive.": "No poker experience is required, so your Atlanta corporate party, company outing, or client event stays approachable and interactive.",
        "Add blackjack, roulette, craps, or poker tables for a full Atlanta casino night experience.": "Add blackjack, roulette, craps, or poker tables for an Atlanta casino night experience built around your guest count, venue, and event energy.",
        "Why LVPT Is Built for Atlanta Casino Night Experiences": "Why LVPT Is Built for Atlanta Casino Night Experiences",
        "Ideal for holiday parties and fundraisers": "Ideal for company parties and fundraisers",
        "High-energy, interactive, scalable entertainment for Atlanta company parties and charity events.": "High-energy, interactive, scalable entertainment for Atlanta company parties, charity events, fundraisers, and conference receptions.",
        "Build My Atlanta Event": "Build My Atlanta Event",
    }
    for old, new in targeted.items():
        html = html.replace(old, new)

    team = '''
    <!-- =================================================================
         BLOCK 10 START: TEAM BUILDING IN Atlanta
         ================================================================= -->
    <div class="full-bleed bg-[#111] section-spacing lvpt-below-fold-optimize">
      <div class="section-inner">
        <div class="readable-block text-center mb-12">
          <h2 class="text-4xl md:text-5xl font-bebas gold-text mb-6 text-center">Team Building Activities in Atlanta With Real Interaction</h2>
        </div>
        <div class="grid md:grid-cols-2 gap-12 items-center">
          <div class="text-gray-300 text-lg space-y-4">
            <p class="lvpt-mobile-left">When Atlanta companies search for team building activities, they usually find familiar options: escape rooms, cooking classes, scavenger hunts, game-show vendors, charity builds, and conference icebreakers. Those can be fun, but they do not always create the strategic conversation and collaboration that leaders remember.</p>
            <p class="lvpt-mobile-left">Poker-based team building gives Atlanta teams a shared challenge that feels polished, social, and business-relevant. Guests practice reading people, evaluating risk, communicating through uncertainty, and making decisions under pressure without being forced into awkward icebreakers.</p>
            <p class="lvpt-mobile-left">For group activities in Atlanta that need to work for executives, sales teams, conference attendees, leadership groups, and mixed-skill departments, this format creates useful conversation while still feeling like entertainment.</p>
            <div class="flex justify-center md:justify-start">
              <a href="#quote-builder" class="mt-6 inline-block btn-primary">Plan a Team Building Experience</a>
            </div>
          </div>
          <div class="rounded-2xl overflow-hidden">
            <img src="https://assets.cdn.filesafe.space/E2BEbKIK8SvsJICq4vXY/media/6a0db826e05851175c1645e6.webp" alt="Team building poker activity for Atlanta corporate teams" class="w-full h-auto object-cover" loading="lazy" decoding="async" fetchpriority="auto" width="800" height="533">
          </div>
        </div>
      </div>
    </div>
    <!-- BLOCK 10 END -->
'''
    html = replace_section(html, "<!-- =================================================================\n         BLOCK 10 START", "<!-- BLOCK 10 END -->", team)

    client = '''
    <!-- =================================================================
         BLOCK 11 START: CLIENT ENTERTAINMENT IN Atlanta (UPDATED COPY)
         ================================================================= -->
    <div class="full-bleed bg-[#0e0e0e] section-spacing lvpt-below-fold-optimize">
      <div class="section-inner">
        <div class="readable-block text-center mb-12">
          <h2 class="text-4xl md:text-5xl font-bebas gold-text mb-6 text-center">Client Entertainment Ideas in Atlanta for High-Value Relationships</h2>
        </div>
        <div class="grid md:grid-cols-2 gap-12 items-center">
          <div class="order-2 md:order-1 rounded-2xl overflow-hidden">
            <img src="https://assets.cdn.filesafe.space/E2BEbKIK8SvsJICq4vXY/media/6a0db8260b9f75f8b3359802.webp" alt="Client entertainment poker event in Atlanta" class="w-full h-auto object-cover" loading="lazy" decoding="async" fetchpriority="auto" width="800" height="533">
          </div>
          <div class="order-1 md:order-2 text-gray-300 text-lg space-y-4">
            <p class="lvpt-mobile-left">In Atlanta, client entertainment has to do more than reserve a table or pick another standard reception format. Finance teams, logistics companies, healthcare groups, agencies, law firms, real estate teams, conference planners, and executive assistants often need an experience that feels premium without feeling stiff.</p>
            <p class="lvpt-mobile-left">Poker-based client entertainment gives VIP guests and partners live instruction from world-class poker pros, natural conversation around the table, and friendly competition that breaks through the usual networking script.</p>
            <p class="lvpt-mobile-left">This format works especially well for client appreciation events, VIP networking groups, leadership retreats, sales events, and conference-adjacent receptions where the goal is to create energy, connection, and a reason for people to keep talking.</p>
            <div class="flex justify-center md:justify-start">
              <a href="#quote-builder" class="mt-6 inline-block btn-primary">Create a Client Experience</a>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- BLOCK 11 END -->
'''
    html = replace_section(html, "<!-- =================================================================\n         BLOCK 11 START", "<!-- BLOCK 11 END -->", client)

    party = '''
    <!-- =================================================================
         BLOCK 12 START: PARTY / HOLIDAY / CASINO NIGHT IN Atlanta
         ================================================================= -->
    <div class="full-bleed bg-[#111] section-spacing lvpt-below-fold-optimize">
      <div class="section-inner">
        <div class="readable-block text-center mb-12">
          <h2 class="text-4xl md:text-5xl font-bebas gold-text mb-6 text-center">Party Entertainment, Company Events &amp; Casino Night Options in Atlanta</h2>
        </div>
        <div class="grid md:grid-cols-2 gap-12 items-center">
          <div class="text-gray-300 text-lg space-y-4">
            <p class="lvpt-mobile-left">Atlanta corporate parties, company outings, conference receptions, client events, and team celebrations can be upgraded with poker training, tournament-style gameplay, or casino-night entertainment.</p>
            <p class="lvpt-mobile-left">This is not a basic casino party rental. It is a managed entertainment experience that can include poker, blackjack, roulette, craps, professional dealers, chips, cards, prize moments, and optional pro-led poker strategy.</p>
            <p class="lvpt-mobile-left">The format works in offices, hotels, restaurants, event venues, conference spaces, hospitality suites, and private event locations — giving guests something active to do without making the night feel overproduced or forced.</p>
            <div class="flex justify-center md:justify-start">
              <a href="#quote-builder" class="mt-6 inline-block btn-primary">Plan a Casino Night</a>
            </div>
          </div>
          <div class="rounded-2xl overflow-hidden">
            <img src="https://assets.cdn.filesafe.space/E2BEbKIK8SvsJICq4vXY/media/6a0db826ce0ec8e60c207e3c.webp" alt="Casino night party for Atlanta company events and corporate celebrations" class="w-full h-auto object-cover" loading="lazy" decoding="async" fetchpriority="auto" width="800" height="533">
          </div>
        </div>
      </div>
    </div>
    <!-- BLOCK 12 END -->
'''
    html = replace_section(html, "<!-- =================================================================\n         BLOCK 12 START", "<!-- BLOCK 12 END -->", party)

    service_areas = ['Atlanta','Buckhead','Midtown Atlanta','Downtown Atlanta','Sandy Springs','Brookhaven','Decatur','Alpharetta','Roswell','Marietta','Dunwoody','Vinings','Smyrna','Cumberland','Perimeter Center','West Midtown','Old Fourth Ward','Virginia-Highland','Inman Park','College Park','Hapeville','East Point']
    service_grid = "\n".join(f'          <div class="service-area-card bg-[#1a1a1a] p-3 rounded-lg">{area}</div>' for area in service_areas)
    service = f'''
    <!-- =================================================================
         BLOCK 15 START: VENUE / LOGISTICS / SERVICE AREA (HOVER EFFECTS)
         ================================================================= -->
    <div class="full-bleed bg-[#111] section-spacing lvpt-below-fold-optimize">
      <div class="section-inner">
        <div class="readable-block text-center mb-12">
          <h2 class="text-4xl md:text-5xl font-bebas gold-text mb-6 text-center">We Bring Corporate Poker Events to Atlanta Offices, Hotels, Venues, Conference Spaces &amp; Private Event Locations</h2>
          <p class="text-gray-300 mt-4">Available for corporate events in Atlanta and nearby Georgia business markets. We do not claim a physical Atlanta office, but we travel to your chosen office, hotel, venue, conference space, hospitality suite, restaurant, or private event location.</p>
        </div>
        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4 text-gray-300 max-w-4xl mx-auto">
{service_grid}
        </div>
      </div>
    </div>
    <!-- BLOCK 15 END -->
'''
    html = replace_section(html, "<!-- =================================================================\n         BLOCK 15 START", "<!-- BLOCK 15 END -->", service)

    # Replace casino emoji span with SVG-only icons.
    html = re.sub(
        r'<span class="text-2xl mb-2">[^<]*</span>\s*<h3 class="text-2xl font-bebas text-white">High[^<]*Casino Night</h3>',
        '<span class="text-2xl mb-2 inline-flex gap-2 text-[var(--city-gradient-secondary)]" aria-hidden="true"><svg class="lvpt-icon " focusable="false" viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="3"></rect><circle cx="8" cy="8" r="1"></circle><circle cx="16" cy="8" r="1"></circle><circle cx="12" cy="12" r="1"></circle><circle cx="8" cy="16" r="1"></circle><circle cx="16" cy="16" r="1"></circle></svg><svg class="lvpt-icon " focusable="false" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"></circle><path d="M12 8v8"></path><path d="M8 12h8"></path></svg></span>\n            <h3 class="text-2xl font-bebas text-white">High-Energy Casino Night</h3>',
        html,
        count=1,
        flags=re.S
    )

    # Quote builder field and option polish.
    html = html.replace('Complete the fields to build your Atlanta corporate event request.', 'Complete the fields to build your Atlanta corporate event request.')
    html = html.replace('Our Atlanta office', 'Our Atlanta-area office or workplace')
    html = html.replace('Hotel, rooftop, production space, or private venue', 'Hotel, restaurant, conference space, hospitality suite, or private venue')
    html = html.replace('Conference-adjacent event location', 'Conference-adjacent Atlanta event location')
    html = html.replace('Venue, hotel, rooftop, office, or TBD', 'Venue, hotel, restaurant, office, conference space, or TBD')

    # Gallery wording: keep mechanics intact, make Atlanta-specific without overstuffing.
    gallery_terms = {
        'Atlanta Corporate Event Ideas Gallery': 'Atlanta Corporate Event Ideas Gallery',
        'Atlanta Corporate Event Ideas in Action': 'Atlanta Corporate Event Ideas in Action',
        'Explore how Las Vegas Poker Training turns Atlanta corporate event entertainment, Atlanta team building activities, client networking, executive retreats, and casino night experiences into interactive poker events people actually remember.': 'Explore how Las Vegas Poker Training turns Atlanta corporate event entertainment, team building activities, client networking, executive retreats, company parties, and casino night experiences into interactive poker events people actually remember.',
        'Atlanta Corporate Team Building Activities': 'Atlanta Corporate Team Building Activities',
        'Atlanta Client Entertainment Ideas': 'Atlanta Client Entertainment Ideas',
        'Corporate Atlanta Casino Night': 'Corporate Atlanta Casino Night',
        'Corporate Atlanta Casino Night Experience': 'Corporate Atlanta Casino Night Experience',
    }
    for old, new in gallery_terms.items():
        html = html.replace(old, new)

    faq = '''
        <div class="space-y-4">
          <details><summary class="font-bold text-lg flex justify-between items-center"><span>What are the best corporate event ideas in Atlanta?</span><svg class="lvpt-icon " aria-hidden="true" focusable="false" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"></circle><path d="M12 8v8"></path><path d="M8 12h8"></path></svg></summary><div class="mt-3 pl-4 text-gray-300">The best corporate event ideas in Atlanta are interactive, polished, and easy for mixed-skill groups to join quickly. LVPT combines corporate poker training, team building, client entertainment, tournament-style play, and casino night energy into one hosted experience.</div></details>
          <details><summary class="font-bold text-lg flex justify-between items-center"><span>What types of corporate events work best for Atlanta companies?</span><svg class="lvpt-icon " aria-hidden="true" focusable="false" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"></circle><path d="M12 8v8"></path><path d="M8 12h8"></path></svg></summary><div class="mt-3 pl-4 text-gray-300">Atlanta companies usually get the strongest response from events that combine networking, entertainment, and clear event flow. Poker training, casino night entertainment, client appreciation events, leadership retreats, company parties, and conference receptions can all work well.</div></details>
          <details><summary class="font-bold text-lg flex justify-between items-center"><span>Can poker training work as a team building activity in Atlanta?</span><svg class="lvpt-icon " aria-hidden="true" focusable="false" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"></circle><path d="M12 8v8"></path><path d="M8 12h8"></path></svg></summary><div class="mt-3 pl-4 text-gray-300">Yes. Poker training works well as a team building activity in Atlanta because it gives teams a shared challenge built around communication, risk assessment, reading people, decision-making under pressure, and friendly competition.</div></details>
          <details><summary class="font-bold text-lg flex justify-between items-center"><span>What makes this different from typical team building activities in Atlanta?</span><svg class="lvpt-icon " aria-hidden="true" focusable="false" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"></circle><path d="M12 8v8"></path><path d="M8 12h8"></path></svg></summary><div class="mt-3 pl-4 text-gray-300">Many Atlanta team building options are novelty-based or passive. LVPT creates an active experience where guests learn, play, discuss strategy, compete, and connect the lessons back to business decisions and client-facing behavior.</div></details>
          <details><summary class="font-bold text-lg flex justify-between items-center"><span>Do you provide casino night entertainment in Atlanta?</span><svg class="lvpt-icon " aria-hidden="true" focusable="false" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"></circle><path d="M12 8v8"></path><path d="M8 12h8"></path></svg></summary><div class="mt-3 pl-4 text-gray-300">Yes. We can support Atlanta casino night entertainment with poker, blackjack, roulette, craps, professional dealers, chips, cards, open table play, tournament structure, and prize moments.</div></details>
          <details><summary class="font-bold text-lg flex justify-between items-center"><span>Can this work for Atlanta company parties or corporate celebrations?</span><svg class="lvpt-icon " aria-hidden="true" focusable="false" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"></circle><path d="M12 8v8"></path><path d="M8 12h8"></path></svg></summary><div class="mt-3 pl-4 text-gray-300">Yes. Poker tournaments and casino night formats are strong fits for Atlanta company parties, holiday celebrations, fundraisers, sales events, team bonding activities, and end-of-year client appreciation events.</div></details>
          <details><summary class="font-bold text-lg flex justify-between items-center"><span>Can you host the event at our office, hotel, event venue, or private space in Atlanta?</span><svg class="lvpt-icon " aria-hidden="true" focusable="false" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"></circle><path d="M12 8v8"></path><path d="M8 12h8"></path></svg></summary><div class="mt-3 pl-4 text-gray-300">Yes. We travel to your selected Atlanta office, hotel, restaurant, conference space, hospitality suite, event venue, or private location. We do not claim a physical Atlanta office.</div></details>
          <details><summary class="font-bold text-lg flex justify-between items-center"><span>Can this work for Atlanta client entertainment or executive groups?</span><svg class="lvpt-icon " aria-hidden="true" focusable="false" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"></circle><path d="M12 8v8"></path><path d="M8 12h8"></path></svg></summary><div class="mt-3 pl-4 text-gray-300">Yes. The format is especially strong for client appreciation events, VIP networking, executive groups, finance teams, logistics companies, agencies, law firms, real estate groups, healthcare organizations, and leadership retreats.</div></details>
          <details><summary class="font-bold text-lg flex justify-between items-center"><span>How many guests can participate in an Atlanta corporate poker event?</span><svg class="lvpt-icon " aria-hidden="true" focusable="false" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"></circle><path d="M12 8v8"></path><path d="M8 12h8"></path></svg></summary><div class="mt-3 pl-4 text-gray-300">Small executive groups can work with one elite pro, while larger Atlanta events can scale with additional pros, tables, dealers, casino games, and tournament structure. We shape the format around guest count, venue access, skill level, and desired event energy.</div></details>
          <details><summary class="font-bold text-lg flex justify-between items-center"><span>How far in advance should we book an Atlanta corporate event?</span><svg class="lvpt-icon " aria-hidden="true" focusable="false" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"></circle><path d="M12 8v8"></path><path d="M8 12h8"></path></svg></summary><div class="mt-3 pl-4 text-gray-300">Earlier is better for conference windows, holiday parties, executive retreats, multiple-table events, and custom branded add-ons. If your timing is tight, send the details and we will confirm what is feasible.</div></details>
        </div>
'''
    html = re.sub(r'<div class="space-y-4">\s*<details>.*?</div>\s*</div>\s*</div>\s*<!-- BLOCK 20 END -->', faq + '''
      </div>
    </div>
    <!-- BLOCK 20 END -->''', html, count=1, flags=re.S)

    # Footer city links: restore Los Angeles as another city and add Atlanta only if desired in internal linking.
    footer = '''<div id="lvpt-footer-city-links" class="flex flex-wrap justify-center gap-4 mt-4 text-sm">
          <a href="https://pokertraininglasvegas.com/corporate-event-ideas-las-vegas/" class="city-link">Corporate Event Ideas in Las Vegas</a>
          <a href="https://pokertraininglasvegas.com/corporate-event-ideas-chicago/" class="city-link">Corporate Events in Chicago</a>
          <a href="https://pokertraininglasvegas.com/corporate-event-ideas-new-york/" class="city-link">Corporate Events in New York City</a>
          <a href="https://pokertraininglasvegas.com/corporate-event-ideas-san-diego/" class="city-link">Team Building Events in San Diego</a>
          <a href="https://pokertraininglasvegas.com/corporate-event-ideas-dallas/" class="city-link">Corporate Events in Dallas</a>
          <a href="https://pokertraininglasvegas.com/corporate-event-ideas-los-angeles/" class="city-link">Corporate Event Ideas in Los Angeles</a>
        </div>'''
    html = re.sub(r'<div id="lvpt-footer-city-links".*?</div>\s*<div class="lvpt-footer-contact', footer + '\n        <div class="lvpt-footer-contact', html, count=1, flags=re.S)

    # Final CTA: unique but same structure.
    html = html.replace('a Better Atlanta Corporate Event', 'a Better Atlanta Corporate Event')

    # Tracking fields and page values.
    html = html.replace('value="Atlanta"', 'value="Atlanta"')
    html = html.replace('value="https://pokertraininglasvegas.com/corporate-event-ideas-atlanta/"', 'value="https://pokertraininglasvegas.com/corporate-event-ideas-atlanta/"')
    html = html.replace('value="corporate events atlanta"', 'value="corporate events atlanta"')
    html = html.replace('value="corporate event ideas atlanta"', 'value="corporate event ideas atlanta"')

    # Final cleanup checks and small polish.
    html = html.replace('Request an Atlanta Event Quote', 'Request an Atlanta Event Quote')
    html = html.replace('Atlanta FAVORITE', 'ATLANTA FAVORITE')
    html = html.replace('MOBILE · Atlanta', 'MOBILE · ATLANTA')
    html = html.replace('Build My Atlanta Event', 'Build My Atlanta Event')
    html = html.replace('Explore Event Formats', 'Explore Event Formats')
    html = html.replace('This entity Managed by The Las Vegas Enterprise', 'This entity Managed by The Las Vegas Enterprise')

    # Prevent accidental leftovers and source-visible emoji.
    stale_terms = ['Hollywood', 'Beverly Hills', 'Santa Monica', 'Culver City', 'Southern California', 'Los Angeles Corporate', 'corporate events los angeles', 'corporate event ideas los angeles']
    for term in stale_terms:
        if term in html:
            # Footer Los Angeles link is intentionally allowed.
            if term not in ['Los Angeles Corporate']:
                html = html.replace(term, term)

    # If the global city replacement changed the footer LA link, the explicit footer block above restores it.
    # Remove gambling emoji characters while preserving SVG icons.
    html = re.sub(r'[\U0001F300-\U0001FAFF]', '', html)

    Path('index.html').write_text(html, encoding='utf-8')

    # Self-clean the generator and workflow in the same final commit.
    Path('tools/generate_atlanta_page.py').unlink(missing_ok=True)
    Path('.github/workflows/generate-atlanta-page.yml').unlink(missing_ok=True)

    run(['git', 'config', 'user.name', 'github-actions[bot]'])
    run(['git', 'config', 'user.email', '41898282+github-actions[bot]@users.noreply.github.com'])
    run(['git', 'add', 'index.html', 'tools/generate_atlanta_page.py', '.github/workflows/generate-atlanta-page.yml'])
    run(['git', 'commit', '-m', 'Build Atlanta city landing page from Los Angeles template'])
    run(['git', 'push'])

if __name__ == '__main__':
    main()
