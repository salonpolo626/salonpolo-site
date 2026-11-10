#!/usr/bin/env python3
"""
Salon Polo static site generator.

Run from the repository root:   python3 _src/build.py

It writes pre-rendered HTML for every page (each in its own folder, so
URLs are clean: /services/skin-fades/), plus sitemap.xml and robots.txt.
All text, titles, descriptions, canonical URLs and structured data are in
the HTML itself; JavaScript is only used for the live Google rating.

When salonpolo.com is switched over to GitHub Pages, change BASE_PATH to "/"
and run this again.
"""
import datetime
import html
import json
import os

# --------------------------------------------------------------------------
# Settings
# --------------------------------------------------------------------------
SITE_URL = "https://www.salonpolo.com"     # the real domain (used for canonical URLs)
BASE_PATH = "/salonpolo-site/"             # where the site is served right now ("/" after the domain switch)
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TODAY = datetime.date.today().isoformat()

BOOK = "https://phorest.com/book/salons/salonpolobarbershop"
PHONE_DISPLAY = "(443) 949-9786"
PHONE_TEL = "+14439499786"
EMAIL = "contact@salonpolo.com"
INSTAGRAM = "https://www.instagram.com/salonpolo/"
FACEBOOK = "https://www.facebook.com/thesalonpolo/"
MAPS = ("https://www.google.com/maps/place/Salon+Polo+%26+Barbershop/@38.9945079,-76.5322495,17z/"
        "data=!3m1!4b1!4m6!3m5!1s0x89b7f75372734adb:0x7365693d55a7aa5b!8m2!3d38.9945079!4d-76.5322495")
DIRECTIONS = "https://www.google.com/maps/dir/?api=1&destination=Salon+Polo+%26+Barbershop+626+Admiral+Dr+Suite+E+Annapolis+MD+21401"
GEO = (38.9945079, -76.5322495)
STREET, CITY, REGION, ZIP = "626 Admiral Drive, Suite E", "Annapolis", "MD", "21401"
HOURS = [("Monday", None), ("Tuesday", ("10:00", "19:00")), ("Wednesday", ("10:00", "19:00")),
         ("Thursday", ("10:00", "19:00")), ("Friday", ("10:00", "19:00")),
         ("Saturday", ("09:00", "14:00")), ("Sunday", None)]
SALON_ID = SITE_URL + "/#salon"


def esc(s):
    return html.escape(s, quote=True)


def hour12(t):
    h, m = map(int, t.split(":"))
    suffix = "AM" if h < 12 else "PM"
    h = h % 12 or 12
    return f"{h}{'' if m == 0 else ':%02d' % m} {suffix}"


def hours_short(span):
    if not span:
        return "Closed"
    a, b = span
    return f"{hour12(a)} – {hour12(b)}"


# --------------------------------------------------------------------------
# Content: services
# --------------------------------------------------------------------------
SERVICES = [
    {
        "slug": "mens-haircuts",
        "name": "Men's Haircuts",
        "short": "Short, medium and long cuts, scissor work and undercuts.",
        "title": "Men's Haircuts in Annapolis, MD | Salon Polo",
        "description": "Men's haircuts in Annapolis, MD: short, medium and long cuts, tailored scissor work and undercuts. Book online with Alexis, Amber or Colette at Salon Polo.",
        "h1": "Men's haircuts <em>in Annapolis.</em>",
        "lead": "Short, medium and long cuts, tailored to your head shape and the way your hair grows.",
        "body": [
            "Every men's haircut at Salon Polo starts with a conversation: how you wear your hair, how much time you spend styling it, and how you want it to grow out. From there we build the shape with clippers, scissors or both, cut to your head shape and growth pattern rather than a one-size template.",
            "We cut every length. Short, clean cuts. Medium-length cuts with texture and movement. Longer styles, cut dry so we can see exactly how your hair falls. We also do undercuts, and quick neckline cleanups to keep a cut sharp between visits.",
            "Every cut is finished with Kevin Murphy products, and we'll show you how to recreate the look at home with what you actually need.",
        ],
        "menu": ["Short haircut", "Medium length dry cut", "Long dry cut", "Undercut", "Neckline cleanup", "Fringe / face framing only"],
        "who": ["alexis", "amber", "colette"],
        "who_note": {"colette": "Short &amp; medium cuts"},
        "photos": ["scissor", "waves", "mullet"],
    },
    {
        "slug": "skin-fades",
        "name": "Skin Fades & Tapers",
        "short": "Skin fades and taper fades, blended clean.",
        "title": "Skin Fades & Taper Fades in Annapolis, MD | Salon Polo",
        "description": "Skin fades and taper fades in Annapolis, MD. Clean blends and a shaped top from Salon Polo's barber and stylists. Book online with Alexis, Amber or Colette.",
        "h1": "Skin fades &amp; tapers <em>in Annapolis.</em>",
        "lead": "A skin fade all the way down or a soft taper at the temples, blended so there's no line to find.",
        "body": [
            "A good fade is all in the blend. Whether you want a skin fade that takes the sides all the way down or a softer taper at the temples and neckline, we blend it clean, then shape the top so the whole cut works together.",
            "Fades are a favorite here. Colette, our licensed barber, says tapers and skin fades are her favorite cuts to do, and Alexis's favorite cut is a skin fade: in her words, it's soooo satisfying.",
            "Tell us how high you like it, how short you want the top, and how often you come in, and we'll set the fade up so it still looks right a few weeks later.",
        ],
        "menu": ["Skin fade", "Taper fade", "Neckline cleanup"],
        "who": ["colette", "alexis", "amber"],
        "who_note": {"colette": "Tapers &amp; skin fades are her favorite", "alexis": "Her favorite cut: a skin fade"},
        "photos": ["fade", "slick", "texture"],
    },
    {
        "slug": "hot-towel-shaves",
        "name": "Hot Towel Shaves",
        "short": "Traditional straight-razor shaves and head shaves.",
        "title": "Hot Towel Shaves in Annapolis, MD | Salon Polo",
        "description": "Traditional hot towel shaves and hot towel head shaves in Annapolis, MD with Colette, Salon Polo's licensed barber. Book online.",
        "h1": "Hot towel shaves <em>in Annapolis.</em>",
        "lead": "A traditional straight-razor shave, done slowly and properly, with Colette.",
        "body": [
            "A traditional hot towel shave is the slow way to a clean finish. Hot towels soften the hair and relax the skin, then the shave is done with a straight razor, with care taken around the neck and jawline.",
            "We also offer a hot towel head shave for a smooth, clean scalp.",
            "Hot towel shaves at Salon Polo are done by Colette, our licensed barber.",
        ],
        "menu": ["Traditional hot towel shave", "Hot towel head shave"],
        "who": ["colette"],
        "who_note": {},
        "photos": ["shave"],
    },
    {
        "slug": "beard-trims",
        "name": "Beard Trims & Sculpting",
        "short": "Beard and goatee shaping, from express tidy-ups to full sculpting.",
        "title": "Beard Trims & Beard Sculpting in Annapolis, MD | Salon Polo",
        "description": "Beard trims, goatee shaping and beard sculpting in Annapolis, MD. Express tidy-ups or a premium hot towel beard sculpt at Salon Polo. Book online.",
        "h1": "Beard trims &amp; sculpting <em>in Annapolis.</em>",
        "lead": "Clean lines, balanced length and a shape that suits your face.",
        "body": [
            "A beard looks its best when the lines are deliberate. We shape the cheek line and neckline, balance the length to your face, and tidy the edges, whether you wear a goatee, a short beard or a full one.",
            "The premium goatee and beard sculpting service includes a hot towel. The express version is a quicker tidy-up, ideal between haircuts.",
            "Beard work is done by Alexis, Amber and Colette, so you can add it to your haircut with whoever you already book.",
        ],
        "menu": ["Hot towel premium goatee / beard sculpting", "Express goatee / beard sculpting"],
        "who": ["alexis", "amber", "colette"],
        "who_note": {},
        "photos": ["beard", "slick"],
    },
    {
        "slug": "gray-blending",
        "name": "Men's Gray Blending",
        "short": "Softened gray that still looks like you.",
        "title": "Men's Gray Blending in Annapolis, MD | Salon Polo",
        "description": "Men's gray blending and gloss / tone refresh in Annapolis, MD at Salon Polo. Softer, natural-looking gray with Alexis or Amber. Book online.",
        "h1": "Men's gray blending <em>in Annapolis.</em>",
        "lead": "Gray softened, not erased, so you look like yourself.",
        "body": [
            "Men's gray blending tones gray down so it looks natural instead of colored. The goal isn't to hide every gray hair. It's to soften it, so the change is noticeable to you and nobody can quite tell why.",
            "A gloss / tone refresh adds shine and evens out tone between visits.",
            "Gray blending at Salon Polo is done by Alexis and Amber, and pairs well with a haircut in the same visit.",
        ],
        "menu": ["Men's gray blending", "Gloss / tone refresh"],
        "who": ["alexis", "amber"],
        "who_note": {},
        "photos": [],
    },
]
SVC = {s["slug"]: s for s in SERVICES}

# The full menu (names only, no prices)
MENU = [
    ("The Cut", "Haircuts", ["Short haircut", "Skin fade", "Medium length dry cut", "Long dry cut", "Undercut",
                             "Neckline cleanup", "Fringe / face framing only", "Child's haircut, 10 &amp; under"],
     ["mens-haircuts", "skin-fades"]),
    ("The Groom", "Barbering", ["Traditional hot towel shave", "Hot towel head shave",
                                "Hot towel premium goatee / beard sculpting", "Express goatee / beard sculpting"],
     ["hot-towel-shaves", "beard-trims"]),
    ("The Color", "Gray blending &amp; gloss", ["Men's gray blending", "Gloss / tone refresh"], ["gray-blending"]),
]

# --------------------------------------------------------------------------
# Content: team
# --------------------------------------------------------------------------
TEAM = [
    {
        "slug": "alexis",
        "name": "Alexis",
        "role": "Stylist",
        "license": "Licensed cosmetologist",
        "photo": "team/alexis.jpg",
        "alt": "Alexis, stylist at Salon Polo, in front of the Kevin Murphy wall",
        "book": "https://www.phorest.com/salon/salonpolobarbershop/book/services?staffId=8HZcPC7pnCw_wKK3vLH13w",
        "accepting": True,
        "does": "Short to long cuts · Fades &amp; tapers · Beard work · Gray blending",
        "services": ["mens-haircuts", "skin-fades", "beard-trims", "gray-blending"],
        "title": "Alexis, Stylist at Salon Polo in Annapolis, MD",
        "description": "Book with Alexis at Salon Polo in Annapolis, MD. Licensed cosmetologist for 7+ years specializing in clipper and scissor cuts, skin fades and beard work.",
        "h1": "Alexis",
        "lead": "Licensed cosmetologist for over seven years, specializing in clipper and scissor cuts.",
        "bio": [
            "Hi, I’m Alexis! I’ve been a licensed cosmetologist for over seven years, specializing in clipper and scissor cuts. I love building new connections and helping people feel confident in the reflection they see in the mirror.",
            "When I’m not behind the chair, you’ll find me crocheting, going to the gym, spending time outdoors. I am fascinated by marine wildlife and ocean conservation. I can’t wait to welcome you to my chair and help you achieve a look you’ll love.",
        ],
        "qa": [
            ("Favorite cut to do?", "“A skin fade! It’s soooo satisfying.”"),
            ("What do you love most about being a stylist?", "“Connecting with people and doing transformations.”"),
            ("Something people might not know about you?", "“I used to drive dump trucks.”"),
        ],
        "review": ("Alexis cut my husband’s hair and did an awesome job! They also carry Kevin Murphy products, which not everyone does and it’s great to have a place nearby to get these. The salon is clean and organized. Highly recommend.", "Lauran P., Google review"),
        "work": None,
    },
    {
        "slug": "amber",
        "name": "Amber",
        "role": "Stylist",
        "license": "Licensed cosmetologist",
        "photo": "team/amber.jpg",
        "alt": "Amber, stylist at Salon Polo, in front of the Kevin Murphy wall",
        "book": "https://www.phorest.com/salon/salonpolobarbershop/book/services?staffId=X1TsNiO8WNYVHWTYorO8gQ",
        "accepting": True,
        "does": "Short to long cuts · Fades &amp; tapers · Beard work · Gray blending",
        "services": ["mens-haircuts", "skin-fades", "beard-trims", "gray-blending"],
        "title": "Amber, Stylist at Salon Polo in Annapolis, MD",
        "description": "Book with Amber at Salon Polo in Annapolis, MD. Licensed cosmetologist for 7 years specializing in men's grooming: cuts, fades, beards and gray blending.",
        "h1": "Amber",
        "lead": "Licensed cosmetologist for 7 years, specializing in men's grooming.",
        "bio": [
            "Hi, I'm Amber! I've been a licensed cosmetologist for 7 years and specialize in men's grooming while also offering women's haircuts and blowouts. My goal is to help every guest leave my chair looking great and feeling confident.",
            "When I'm not behind the chair, you'll usually find me spending time with my fur babies, exploring the outdoors, or enjoying a festival. I look forward to meeting you and helping you achieve a look that makes you feel your best!",
        ],
        "qa": [],
        "review": ("Amber did an amazing job! She is great at knowing what’s would look best for me and suggesting how to style it.", "Peter S., Google review"),
        "work": ("work/amber.jpg", "Amber smiling as she finishes a guest's slicked-back cut", 1100, 1100),
    },
    {
        "slug": "colette",
        "name": "Colette",
        "role": "Barber",
        "license": "Licensed barber",
        "photo": "team/colette.jpg",
        "alt": "Colette, barber at Salon Polo, in front of the Kevin Murphy wall",
        "book": "https://www.phorest.com/salon/salonpolobarbershop/book/services?staffId=4P5LVSoCJaKDknl80Vjzyg",
        "accepting": True,
        "does": "Tapers &amp; skin fades · Short &amp; medium cuts · Hot towel shaves · Beard work",
        "services": ["skin-fades", "mens-haircuts", "hot-towel-shaves", "beard-trims"],
        "title": "Colette, Barber at Salon Polo in Annapolis, MD",
        "description": "Book with Colette, licensed barber at Salon Polo in Annapolis, MD. Tapers, skin fades, short and medium cuts, hot towel shaves and beard work.",
        "h1": "Colette",
        "lead": "Licensed barber, cutting hair since she was 17. Tapers and skin fades are her favorites.",
        "bio": [
            "Hi, I’m Colette! I'm a licensed barber and I’ve been cutting hair since I was 17. My favorite cuts to do are tapers and skin fades, but I enjoy working with all hair types and styles.",
            "Outside of the shop, I love spending time with my family, especially my twin brother and my dog. I also enjoy walking shelter dogs at the SPCA.",
            "At Salon Polo, I want every client to be comfortable and leave feeling their absolute best, while maintaining a fun and lighthearted experience. I also love cutting kids’ hair, and I even have a treasure box filled with toys for them to pick from after doing such a great job! I’m excited to meet you and have you in my chair!",
        ],
        "qa": [],
        "review": ("Colette is very professional and keeps attention to detail definitely recommend!", "Scott, Google review"),
        "work": ("work/colette.jpg", "Colette finishing a short fade on a smiling guest", 1600, 800),
    },
]
TM = {t["slug"]: t for t in TEAM}
HENRY = {
    "name": "Henry", "role": "Owner &amp; Stylist", "photo": "team/henry.jpg",
    "alt": "Henry, owner of Salon Polo, finishing a skin fade at his chair",
    "book": "https://www.phorest.com/salon/salonpolobarbershop/book/services?staffId=kJTIY_2ESmKxqZ6ShLrVsw",
}

WORK = [  # (file, alt, w, h, css class, inline style)
    ("texture", "Men's textured cut with movement on top and a soft taper", 1100, 1100, "", ""),
    ("scissor", "All-scissor layered men's cut with natural movement", 1100, 1098, "", ""),
    ("beyond", "Profile of a tailored men's cut with length left at the back", 825, 825, "", ""),
    ("fade", "Profile of a short men's cut with a skin fade and textured top", 796, 1100, "", "object-position: 50% 32%"),
    ("shave", "Barber detailing a guest's beard line with a straight razor", 1400, 1400, "big", ""),
    ("beard", "Short textured men's cut with a full, shaped beard", 1100, 1100, "", ""),
    ("waves", "Men's medium-length cut with natural waves swept back", 1100, 1100, "", ""),
    ("mullet", "Profile of a textured modern mullet with a taper fade", 1100, 1100, "", ""),
    ("pixie", "Short silver pixie cut with soft texture on top", 1100, 1100, "", ""),
    ("wavy", "Men's textured cut with natural waves and a soft, longer back", 700, 1490, "tall", "object-position: 50% 0%"),
    ("fringe", "Shaggy textured cut with a heavy fringe", 1100, 1100, "", ""),
    ("slick", "Slicked-back men's cut with a tapered side and full beard", 1100, 1100, "", ""),
    ("crop", "Short textured crop with choppy layers and a soft fringe", 1100, 1100, "", ""),
    ("amber", "Stylist Amber smiling as she finishes a guest's slicked-back cut", 1100, 1100, "", ""),
    ("stylist", "Stylist shaping a guest's textured cut with shears", 1400, 1400, "big", ""),
    ("colette", "Barber Colette finishing a short fade on a smiling guest", 1600, 800, "wide", ""),
]
WK = {w[0]: w for w in WORK}

# --------------------------------------------------------------------------
# Structured data helpers
# --------------------------------------------------------------------------
def abs_url(path):
    return SITE_URL + "/" + path


def img_url(p):
    return SITE_URL + "/assets/img/" + p


def opening_hours():
    out = []
    for day, span in HOURS:
        if span:
            out.append({"@type": "OpeningHoursSpecification", "dayOfWeek": day, "opens": span[0], "closes": span[1]})
    return out


def address_ld():
    return {"@type": "PostalAddress", "streetAddress": STREET, "addressLocality": CITY,
            "addressRegion": REGION, "postalCode": ZIP, "addressCountry": "US"}


def salon_ld(full=False):
    d = {
        "@type": "HairSalon",
        "@id": SALON_ID,
        "name": "Salon Polo & Barbershop",
        "url": SITE_URL + "/",
        "telephone": PHONE_TEL,
        "address": address_ld(),
        "image": img_url("salon-floor.jpg"),
    }
    if full:
        d.update({
            "alternateName": "Salon Polo",
            "description": "A modern barbershop and hair salon in Annapolis, Maryland: tailored scissor cuts, skin fades and tapers, hot towel shaves, beard sculpting and men's gray blending.",
            "logo": img_url("logo-badge.png"),
            "email": EMAIL,
            "geo": {"@type": "GeoCoordinates", "latitude": GEO[0], "longitude": GEO[1]},
            "hasMap": MAPS,
            "openingHoursSpecification": opening_hours(),
            "areaServed": {"@type": "City", "name": "Annapolis, Maryland"},
            "foundingDate": "2020",
            "acceptsReservations": True,
            "sameAs": [INSTAGRAM, FACEBOOK],
            "potentialAction": {"@type": "ReserveAction", "target": {"@type": "EntryPoint", "urlTemplate": BOOK,
                                "actionPlatform": ["http://schema.org/DesktopWebPlatform", "http://schema.org/MobileWebPlatform"]},
                                "result": {"@type": "Reservation", "name": "Salon appointment"}},
            "employee": [{"@id": abs_url(f"team/{t['slug']}/#person")} for t in TEAM],
            "hasOfferCatalog": {
                "@type": "OfferCatalog", "name": "Services",
                "itemListElement": [{"@type": "Offer", "itemOffered": {"@id": abs_url(f"services/{s['slug']}/#service")}} for s in SERVICES],
            },
        })
    return d


def person_ld(t):
    return {
        "@type": "Person",
        "@id": abs_url(f"team/{t['slug']}/#person"),
        "name": t["name"],
        "jobTitle": html.unescape(t["role"]),
        "url": abs_url(f"team/{t['slug']}/"),
        "image": img_url(t["photo"]),
        "worksFor": {"@id": SALON_ID},
        "knowsAbout": [html.unescape(SVC[s]["name"]) for s in t["services"]],
        "hasCredential": {"@type": "EducationalOccupationalCredential", "credentialCategory": "license", "name": t["license"]},
    }


def service_ld(s):
    return {
        "@type": "Service",
        "@id": abs_url(f"services/{s['slug']}/#service"),
        "name": html.unescape(s["name"]),
        "serviceType": html.unescape(s["name"]),
        "description": s["description"],
        "url": abs_url(f"services/{s['slug']}/"),
        "provider": {"@id": SALON_ID},
        "areaServed": {"@type": "City", "name": "Annapolis, Maryland"},
        "hasOfferCatalog": {"@type": "OfferCatalog", "name": html.unescape(s["name"]),
                            "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": html.unescape(m)}} for m in s["menu"]]},
    }


def crumbs_ld(crumbs):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": html.unescape(name), "item": abs_url(path)}
        for i, (name, path) in enumerate(crumbs)]}


def jsonld(nodes):
    data = {"@context": "https://schema.org", "@graph": nodes}
    s = json.dumps(data, ensure_ascii=False, indent=1).replace("</", "<\\/")
    return f'<script type="application/ld+json">\n{s}\n</script>'


# --------------------------------------------------------------------------
# Page chrome
# --------------------------------------------------------------------------
NAV = [("Services", "services/"), ("Work", "#work"), ("Team", "team/"), ("Visit", "contact/")]


def nav_html(R, current):
    items = []
    for label, path in NAV:
        href = (R + path) if not path.startswith("#") else (R + path if R else path)
        if path == "#work":
            href = (R or "./") + "#work"
        cur = ' aria-current="page"' if current == path else ""
        items.append(f'<a href="{href}"{cur}>{label}</a>')
    links = "\n      ".join(items)
    mlinks = "\n          ".join(items)
    return f'''<nav class="nav" aria-label="Main">
  <div class="wrap">
    <a class="brand" href="{R or './'}"><img src="{R}assets/img/logo-nav.png" alt="Salon Polo &amp; Barbershop, Annapolis" width="600" height="209"></a>
    <div class="nav-right">
      <div class="links">
      {links}
      <a class="btn" href="{BOOK}" target="_blank" rel="noopener">Book</a>
      </div>
      <details class="mnav">
        <summary>Menu</summary>
        <div class="panel">
          <a href="{R or './'}">Home</a>
          {mlinks}
        </div>
      </details>
    </div>
  </div>
</nav>'''


def footer_html(R):
    hours = "".join(f"<span>{d[:3]}</span><span>{hours_short(s)}</span>" for d, s in HOURS)
    svc = "".join(f'<li><a href="{R}services/{s["slug"]}/">{s["name"]}</a></li>' for s in SERVICES)
    team = "".join(f'<li><a href="{R}team/{t["slug"]}/">{t["name"]}, {t["role"]}</a></li>' for t in TEAM)
    return f'''<footer class="sitefoot">
  <div class="wrap">
    <div class="cols">
      <div>
        <div class="fbrand"><img src="{R}assets/img/logo-badge.png" alt="Salon Polo, est. 2020" width="140" height="49" loading="lazy"></div>
        <address>Salon Polo &amp; Barbershop<br>{STREET}<br>{CITY}, {REGION} {ZIP}</address>
        <p style="margin:12px 0 0"><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a><br><span style="user-select:all">{EMAIL}</span></p>
        <p style="margin:12px 0 0"><a href="{DIRECTIONS}" target="_blank" rel="noopener">Get directions</a> · <a href="{BOOK}" target="_blank" rel="noopener">Book online</a></p>
      </div>
      <div>
        <h2>Services</h2>
        <ul><li><a href="{R}services/">All services</a></li>{svc}</ul>
      </div>
      <div>
        <h2>Team</h2>
        <ul><li><a href="{R}team/">Meet the team</a></li>{team}<li><a href="{R}join-our-team/">Join our team</a></li></ul>
      </div>
      <div>
        <h2>Hours</h2>
        <div class="fhours">{hours}</div>
      </div>
    </div>
    <div class="legal">
      <span>© {datetime.date.today().year} Salon Polo &amp; Barbershop · Annapolis, Maryland</span>
      <span><a href="{R}contact/#policy">Cancellation policy</a> · <a href="{R}privacyterms/">Privacy &amp; terms</a> · <a href="{INSTAGRAM}" target="_blank" rel="noopener">Instagram</a> · <a href="{FACEBOOK}" target="_blank" rel="noopener">Facebook</a></span>
    </div>
  </div>
</footer>'''


def bookband(R, heading="Ready when <em>you are.</em>", text=None, book=BOOK, label="Book online"):
    text = text or f"Book online in a minute, or call us at {PHONE_DISPLAY}."
    return f'''<section class="bookband">
  <div class="wrap">
    <div>
      <h2>{heading}</h2>
      <p>{text}</p>
    </div>
    <div class="cta">
      <a class="btn light" href="{book}" target="_blank" rel="noopener">{label}</a>
      <a class="btn ghost light" href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a>
    </div>
  </div>
</section>'''


def crumbs_html(R, crumbs):
    items = []
    for i, (name, path) in enumerate(crumbs):
        if i == len(crumbs) - 1:
            items.append(f'<li aria-current="page">{name}</li>')
        else:
            items.append(f'<li><a href="{R + path if path else (R or "./")}">{name}</a></li>')
    return f'<ol class="crumbs" aria-label="Breadcrumb">{"".join(items)}</ol>'


def write_page(path, *, title, description, body, ld_nodes, R, current="", og_type="website",
               image="salon-floor.jpg", image_alt="Inside Salon Polo in Annapolis", head_extra="", scripts="", robots=None):
    canonical = abs_url(path)
    og_image = img_url(image)
    robots_tag = f'\n<meta name="robots" content="{robots}">' if robots else ""
    doc = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<link rel="canonical" href="{canonical}">{robots_tag}
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="Salon Polo &amp; Barbershop">
<meta property="og:locale" content="en_US">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{og_image}">
<meta property="og:image:alt" content="{esc(image_alt)}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#FBFAF8">
<link rel="icon" type="image/png" sizes="32x32" href="{R}assets/favicon-32.png">
<link rel="apple-touch-icon" href="{R}assets/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&amp;family=DM+Sans:opsz,wght@9..40,300;9..40,400;9..40,500&amp;display=swap">
<link rel="stylesheet" href="{R}assets/site.css">{head_extra}
{jsonld(ld_nodes)}
</head>
<body>
{nav_html(R, current)}
<main id="main">
{body}
</main>
{footer_html(R)}{scripts}
</body>
</html>
'''
    out = os.path.join(ROOT, path, "index.html") if not path.endswith(".html") else os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(doc)
    return path


def rel(path):
    depth = 0 if path == "" else path.strip("/").count("/") + 1
    return "../" * depth


# --------------------------------------------------------------------------
# Shared fragments
# --------------------------------------------------------------------------
def who_count(slugs):
    roles = [TM[s]["role"] for s in slugs]
    parts = []
    for role in ("Stylist", "Barber"):
        n = roles.count(role)
        if n:
            parts.append(f"{n} {role.lower()}{'s' if n > 1 else ''}")
    return " · ".join(parts)


def chair_card(R, t, heading="h3", show_profile=True):
    tag = '<span class="tag">Accepting new guests</span>' if t.get("accepting") else ""
    prof = f'<a class="soft" href="{R}team/{t["slug"]}/">Meet {t["name"]}</a>' if show_profile else ""
    return f'''      <article class="chair">
        <a href="{R}team/{t["slug"]}/" tabindex="-1" aria-hidden="true"><img src="{R}assets/img/{t["photo"]}" alt="{t["alt"]}" width="800" height="1000" loading="lazy"></a>
        <div class="who"><{heading}><a href="{R}team/{t["slug"]}/">{t["name"]}</a></{heading}><span class="role">{t["role"]}</span></div>
        <p class="does">{t["does"]}</p>
        {tag}
        <div class="links2"><a href="{t["book"]}" target="_blank" rel="noopener">Book with {t["name"]}</a>{prof}</div>
      </article>'''


def henry_card(R, heading="h3"):
    h = HENRY
    return f'''      <article class="chair">
        <img src="{R}assets/img/{h["photo"]}" alt="{h["alt"]}" width="800" height="1000" loading="lazy">
        <div class="who"><{heading}>{h["name"]}</{heading}><span class="role">{h["role"]}</span></div>
        <a class="bk" href="{h["book"]}" target="_blank" rel="noopener">Current guests: book with Henry</a>
        <p class="closed">Not accepting new guests</p>
      </article>'''


def shot(R, key, lazy=True, plain=False):
    f, alt, w, h, cls, style = WK[key]
    if plain:
        cls = ""
    c = f' class="{cls}"' if cls else ""
    st = f' style="{style}"' if style else ""
    return f'<figure{c}><img src="{R}assets/img/work/{f}.jpg"{st} alt="{alt}" width="{w}" height="{h}"{" loading=\"lazy\"" if lazy else ""} decoding="async"></figure>'


# --------------------------------------------------------------------------
# Pages
# --------------------------------------------------------------------------
def build_home():
    R = ""
    menu = []
    for title, small, items, links in MENU:
        more = " ".join(f'<a class="more" href="{R}services/{s}/">{SVC[s]["name"]}</a>' for s in links)
        lis = "".join(f"<li>{i}</li>" for i in items)
        menu.append(f'''      <div class="course">
        <h3>{title} <small>{small}</small></h3>
        <ul class="items">{lis}</ul>
        <div style="display:flex;flex-wrap:wrap;gap:6px 18px">{more}</div>
      </div>''')
    menu = "\n".join(menu)
    shots = "\n      ".join(shot(R, w[0]) for w in WORK)
    chairs = "\n".join(chair_card(R, t) for t in TEAM) + "\n" + henry_card(R)
    hours_rows = "\n".join(
        f'        <tr{" class=\"closed\"" if not s else ""}><td>{d}</td><td>{"Closed" if not s else hours_short(s)}</td></tr>' for d, s in HOURS)
    body = f'''<header id="top" class="hero">
  <img class="photo" src="{R}assets/img/salon-floor.jpg" alt="Inside Salon Polo in Annapolis: black styling stations, a gloss-black front desk, Kevin Murphy shelves and the Salon Polo sign" width="1536" height="916" fetchpriority="high">
  <div class="hero-text">
    <div class="wrap">
      <h1>A modern <em>barbershop</em> &amp; salon in Annapolis.</h1>
      <p class="sub">Tailored scissor cuts, precision fades and hot towel shaves.</p>
      <div class="cta">
        <a class="btn light" href="{BOOK}" target="_blank" rel="noopener">Book a chair</a>
        <a class="btn ghost light" href="{R}services/">The menu</a>
      </div>
    </div>
  </div>
</header>

<section class="letter">
  <div class="wrap grid">
    <div>
      <p class="eyebrow">From the chair</p>
      <h2>The art of a <em>proper cut.</em></h2>
    </div>
    <div class="copy">
      <p>I opened Salon Polo in 2020 because I wanted a shop where a men's cut got real attention. Not a quick buzz and out the door, but scissor work shaped to how your hair grows, fades blended clean, and a hot towel shave that takes the time it should. We cut women's hair too, with the same care.</p>
      <p>There are four chairs here, and that's deliberate. Nobody's rushing to the next client, you get a real conversation, and by your second visit your stylist or barber knows your hair. We use Kevin Murphy products, and we'll only send you home with what you'll actually use.</p>
      <p class="sig">Henry, owner &amp; stylist</p>
    </div>
  </div>
</section>

<section class="carte" id="services">
  <div class="wrap">
    <header>
      <div>
        <p class="eyebrow">The Menu</p>
        <h2>Services, <em>à la carte</em></h2>
      </div>
      <p>Every visit starts with a conversation about your hair and beard, your routine, and how you want to look walking out. Then we get to work.</p>
    </header>
    <div class="menu">
{menu}
    </div>
    <div class="foot">
      <span class="km">Proud Kevin Murphy salon</span>
      <div style="display:flex;gap:10px;flex-wrap:wrap"><a class="btn ghost" href="{R}services/">All services</a><a class="btn" href="{BOOK}" target="_blank" rel="noopener">Book a service</a></div>
    </div>
  </div>
</section>

<section class="work" id="work">
  <div class="wrap">
    <header>
      <div>
        <p class="eyebrow">The Work</p>
        <h2>Every cut, <em>considered.</em></h2>
      </div>
      <p>Shaped to your head, your growth pattern and the way you actually wear it.</p>
    </header>
    <div class="shots">
      {shots}
    </div>
    <a class="ig" href="{INSTAGRAM}" target="_blank" rel="noopener">See more on Instagram · @salonpolo</a>
  </div>
</section>

<section class="team" id="team">
  <div class="wrap">
    <header>
      <div>
        <p class="eyebrow">The Team</p>
        <h2>Behind <em>the chair</em></h2>
      </div>
      <p>Every cut, color and shave at Salon Polo comes from one of these chairs. Choose your stylist or barber when you book.</p>
    </header>
    <div class="chairs">
{chairs}
    </div>
  </div>
</section>

<section class="quote" id="reviews">
  <div class="wrap">
    <div class="rv-top">
      <p class="eyebrow">Overheard</p>
      <a class="rv-sum" id="rv-link" href="{MAPS}" target="_blank" rel="noopener">
        <b id="rv-rating">5.0</b><span class="stars" id="rv-stars" aria-hidden="true">★★★★★</span><span id="rv-count">202 Google reviews</span>
      </a>
    </div>
    <blockquote id="rv-lead">“{TM["alexis"]["review"][0]}”</blockquote>
    <div class="meta"><span class="stars" aria-label="5 out of 5 stars">★★★★★</span><span>{TM["alexis"]["review"][1]}</span></div>
    <div class="rv-grid">
      <article class="rv-card">
        <span class="stars" aria-label="5 out of 5 stars">★★★★★</span>
        <p>{TM["amber"]["review"][0]}</p>
        <div class="rv-who"><span>{TM["amber"]["review"][1].split(",")[0]}</span><span>· Google review</span></div>
      </article>
      <article class="rv-card">
        <span class="stars" aria-label="5 out of 5 stars">★★★★★</span>
        <p>{TM["colette"]["review"][0]}</p>
        <div class="rv-who"><span>{TM["colette"]["review"][1].split(",")[0]}</span><span>· Google review</span></div>
      </article>
    </div>
    <div class="rv-foot">
      <a href="{MAPS}" id="rv-all" target="_blank" rel="noopener">Read all reviews on Google</a>
    </div>
  </div>
</section>

<section class="floor" id="salon">
  <div class="wrap floor-grid">
    <div class="txt">
      <p class="eyebrow">The Salon</p>
      <h2>A space built <em>for the work.</em></h2>
      <p>Four chairs, plenty of natural light, and a full wall of Kevin Murphy. It's a calm, comfortable room where you can settle in, talk, or just switch off while we take care of the rest.</p>
    </div>
    <figure>
      <div class="pic"><div class="pic-img" role="img" aria-label="A black Belmont barber chair with chrome frame on the salon floor"></div></div>
      <figcaption><span>The chair</span><span>Belmont</span></figcaption>
    </figure>
  </div>
</section>

<section class="visit" id="visit">
  <div class="wrap grid">
    <div>
      <p class="eyebrow">Visit &amp; Book</p>
      <h2>Your chair is <em>waiting.</em></h2>
      <div style="margin-top:30px;display:flex;gap:10px;flex-wrap:wrap"><a class="btn" href="{BOOK}" target="_blank" rel="noopener">Book online</a><a class="btn ghost" href="{R}contact/">Visit &amp; policies</a></div>
    </div>
    <div class="block">
      <h3>Find us</h3>
      <address>{STREET}<br>{CITY}, {REGION} {ZIP}</address>
      <a class="phone" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a><br>
      <span style="display:block;margin-top:6px;color:var(--mute);user-select:all">{EMAIL}</span>
      <a class="dir" href="{DIRECTIONS}" target="_blank" rel="noopener">Get directions</a>
    </div>
    <div class="block">
      <h3>Hours</h3>
      <table class="hours">
{hours_rows}
      </table>
    </div>
  </div>
</section>'''
    website = {"@type": "WebSite", "@id": SITE_URL + "/#website", "url": SITE_URL + "/",
               "name": "Salon Polo & Barbershop", "publisher": {"@id": SALON_ID}}
    head_extra = f'\n<link rel="preload" as="image" href="{R}assets/img/salon-floor.jpg" fetchpriority="high">'
    return write_page("", R=R,
                      title="Salon Polo | Barbershop & Hair Salon in Annapolis, MD",
                      description="Modern barbershop & salon in Annapolis, MD: tailored scissor cuts, skin fades and tapers, hot towel shaves, beard sculpting and gray blending. Book online.",
                      body=body, ld_nodes=[salon_ld(True), website] + [person_ld(t) for t in TEAM],
                      head_extra=head_extra,
                      scripts=f'\n<script src="{R}assets/reviews.js" defer></script>')


def build_services():
    path = "services/"
    R = rel(path)
    cards = "\n".join(
        f'''      <a class="svc" href="{R}services/{s["slug"]}/"><h3>{s["name"]} <span>{who_count(s["who"])}</span></h3><p>{s["short"]} Booked with {", ".join(TM[w]["name"] for w in s["who"])}.</p></a>'''
        for s in SERVICES)
    menu = []
    for title, small, items, links in MENU:
        more = " ".join(f'<a class="more" href="{R}services/{s}/">{SVC[s]["name"]}</a>' for s in links)
        menu.append(f'''      <div class="course">
        <h3>{title} <small>{small}</small></h3>
        <ul class="items">{"".join(f"<li>{i}</li>" for i in items)}</ul>
        <div style="display:flex;flex-wrap:wrap;gap:6px 18px">{more}</div>
      </div>''')
    crumbs = [("Home", ""), ("Services", path)]
    body = f'''<header class="phead">
  <div class="wrap">
    {crumbs_html(R, crumbs)}
    <h1>Services <em>at Salon Polo.</em></h1>
    <p class="lead">Men's haircuts, skin fades and tapers, hot towel shaves, beard sculpting and men's gray blending, in Annapolis, Maryland. Every visit starts with a conversation about how you want to look walking out.</p>
    <div class="cta"><a class="btn" href="{BOOK}" target="_blank" rel="noopener">Book online</a><a class="btn ghost" href="{R}team/">Choose a stylist</a></div>
  </div>
</header>

<section class="sec">
  <div class="wrap">
    <p class="eyebrow">What we do</p>
    <h2>Find your <em>service.</em></h2>
    <div class="svc-grid">
{cards}
    </div>
  </div>
</section>

<section class="carte">
  <div class="wrap">
    <header>
      <div>
        <p class="eyebrow">The Menu</p>
        <h2>The full <em>menu.</em></h2>
      </div>
      <p>Prices depend on who you book with and the service, and are shown when you book online.</p>
    </header>
    <div class="menu">
{chr(10).join(menu)}
    </div>
  </div>
</section>

{bookband(R)}'''
    item_list = {"@type": "ItemList", "name": "Services at Salon Polo",
                 "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": abs_url(f"services/{s['slug']}/"),
                                      "name": html.unescape(s["name"])} for i, s in enumerate(SERVICES)]}
    return write_page(path, R=R, current="services/",
                      title="Haircuts, Fades, Shaves & Beard Trims | Salon Polo Annapolis",
                      description="Salon Polo services in Annapolis, MD: men's haircuts, skin fades and tapers, hot towel shaves, beard trims and men's gray blending. Book online.",
                      body=body, ld_nodes=[salon_ld(), item_list, crumbs_ld(crumbs)])


def build_service(s):
    path = f"services/{s['slug']}/"
    R = rel(path)
    crumbs = [("Home", ""), ("Services", "services/"), (s["name"], path)]
    paras = "\n".join(f"      <p>{p}</p>" for p in s["body"])
    menu = "".join(f"<li>{m}</li>" for m in s["menu"])
    who_cards = []
    for slug in s["who"]:
        t = dict(TM[slug])
        note = s["who_note"].get(slug)
        if note:
            t["does"] = note
        who_cards.append(chair_card(R, t))
    who_cls = "chairs three" if len(s["who"]) > 1 else "chairs three"
    photos = ""
    if s["photos"]:
        figs = "\n      ".join(shot(R, k, plain=True) for k in s["photos"])
        n = len(s["photos"])
        width = "max-width:520px;" if n == 1 else ""
        photos = f'''
<section class="sec">
  <div class="wrap">
    <p class="eyebrow">The Work</p>
    <h2>From <em>our chairs.</em></h2>
    <div class="shots" style="margin-top:36px;grid-template-columns:repeat({n},1fr);{width}">
      {figs}
    </div>
  </div>
</section>'''
    others = "\n".join(
        f'      <a class="svc" href="{R}services/{o["slug"]}/"><h3>{o["name"]}</h3><p>{o["short"]}</p></a>'
        for o in SERVICES if o["slug"] != s["slug"])
    book = TM[s["who"][0]]["book"] if len(s["who"]) == 1 else BOOK
    book_label = f'Book with {TM[s["who"][0]]["name"]}' if len(s["who"]) == 1 else "Book online"
    body = f'''<header class="phead">
  <div class="wrap">
    {crumbs_html(R, crumbs)}
    <h1>{s["h1"]}</h1>
    <p class="lead">{s["lead"]}</p>
    <div class="cta"><a class="btn" href="{book}" target="_blank" rel="noopener">{book_label}</a><a class="btn ghost" href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a></div>
  </div>
</header>

<section class="sec">
  <div class="wrap two">
    <div>
      <p class="eyebrow">On the menu</p>
      <h2>What you <em>can book.</em></h2>
      <ul class="items" style="margin-top:24px;max-width:420px">{menu}</ul>
      <p class="intro">Prices are shown when you book online.</p>
    </div>
    <div class="prose">
{paras}
      <p>Salon Polo is at {STREET}, {CITY}, {REGION} {ZIP}. <a href="{R}contact/">Hours, directions and booking policy</a>.</p>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <p class="eyebrow">Who to book</p>
    <h2>{"Book with" if len(s["who"]) == 1 else "Pick your"} <em>{TM[s["who"][0]]["name"] if len(s["who"]) == 1 else "chair."}</em></h2>
    <div class="{who_cls}" style="margin-top:40px">
{chr(10).join(who_cards)}
    </div>
  </div>
</section>
{photos}
<section class="sec">
  <div class="wrap">
    <p class="eyebrow">More services</p>
    <h2>Also <em>at Salon Polo.</em></h2>
    <div class="svc-grid">
{others}
    </div>
  </div>
</section>

{bookband(R, book=book, label=book_label)}'''
    image = f"work/{s['photos'][0]}.jpg" if s["photos"] else "salon-floor.jpg"
    image_alt = WK[s["photos"][0]][1] if s["photos"] else "Inside Salon Polo in Annapolis"
    return write_page(path, R=R, current="services/", title=s["title"], description=s["description"],
                      body=body, image=image, image_alt=image_alt,
                      ld_nodes=[salon_ld(), service_ld(s), crumbs_ld(crumbs)])


def build_team():
    path = "team/"
    R = rel(path)
    crumbs = [("Home", ""), ("Team", path)]
    chairs = "\n".join(chair_card(R, t, heading="h2") for t in TEAM) + "\n" + henry_card(R, heading="h2")
    body = f'''<header class="phead">
  <div class="wrap">
    {crumbs_html(R, crumbs)}
    <h1>Meet <em>the team.</em></h1>
    <p class="lead">Licensed stylists and a licensed barber, cutting in Annapolis. Alexis, Amber and Colette are all accepting new guests.</p>
  </div>
</header>

<section class="team" style="padding-block:clamp(48px,7vw,96px)">
  <div class="wrap">
    <div class="chairs">
{chairs}
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap two">
    <div>
      <p class="eyebrow">Who we are</p>
      <h2>Dream big, <em>put in the work.</em></h2>
    </div>
    <div class="prose">
      <p>What started as a dream in 2017 has now become a reality. In 2020, Salon Polo opened its doors as a suite in Annapolis, MD, with a vision to offer exceptional service and build lasting relationships. While no one could have anticipated the challenges of a global pandemic, it only strengthened our commitment to providing the care and respect every guest deserves.</p>
      <p>In September 2024, we proudly opened Salon Polo at our new Annapolis location, {STREET}, with a mission to create meaningful employment opportunities for like-minded professionals who share our passion for helping others and providing the best service in the industry.</p>
      <p>Your trust and support mean everything to us. We deeply value the personal connections we build with every guest, and our team is here to make sure you feel like family from the moment you walk through our doors.</p>
      <p><a href="{R}join-our-team/">Interested in joining the team?</a></p>
    </div>
  </div>
</section>

{bookband(R, heading="Pick your <em>chair.</em>", text="Choose Alexis, Amber or Colette when you book online, or call and we'll match you.")}'''
    return write_page(path, R=R, current="team/",
                      title="Our Team: Stylists & Barber | Salon Polo, Annapolis MD",
                      description="Meet the team at Salon Polo in Annapolis, MD: stylists Alexis and Amber and barber Colette, all accepting new guests. Book online with Alexis, Amber or Colette.",
                      body=body, ld_nodes=[salon_ld()] + [person_ld(t) for t in TEAM] + [crumbs_ld(crumbs)],
                      image="team/alexis.jpg", image_alt="The Salon Polo team")


def build_person(t):
    path = f"team/{t['slug']}/"
    R = rel(path)
    crumbs = [("Home", ""), ("Team", "team/"), (t["name"], path)]
    bio = "\n".join(f"      <p>{p}</p>" for p in t["bio"])
    chips = "".join(f'<li><a href="{R}services/{s}/">{SVC[s]["name"]}</a></li>' for s in t["services"])
    qa = ""
    if t["qa"]:
        rows = "".join(f"<div><dt>{q}</dt><dd>{a}</dd></div>" for q, a in t["qa"])
        qa = f'''
      <h2>Get to know <em>{t["name"]}.</em></h2>
      <dl class="qa" style="margin-top:20px">{rows}</dl>'''
    work = ""
    if t["work"]:
        f, alt, w, h = t["work"]
        work = f'''
      <figure class="inline-shot" style="margin-top:40px"><img src="{R}assets/img/{f}" alt="{alt}" width="{w}" height="{h}" loading="lazy" decoding="async"></figure>'''
    others = "\n".join(chair_card(R, o) for o in TEAM if o["slug"] != t["slug"])
    body = f'''<header class="phead">
  <div class="wrap">
    {crumbs_html(R, crumbs)}
    <p class="eyebrow">{t["role"]} · Salon Polo, Annapolis</p>
    <h1 style="margin-top:12px">{t["h1"]}</h1>
    <p class="lead">{t["lead"]}</p>
    <div class="cta"><a class="btn" href="{t["book"]}" target="_blank" rel="noopener">Book with {t["name"]}</a><a class="btn ghost" href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a></div>
  </div>
</header>

<section class="sec">
  <div class="wrap profile">
    <figure class="portrait">
      <img src="{R}assets/img/{t["photo"]}" alt="{t["alt"]}" width="800" height="1000" fetchpriority="high">
      <figcaption>{t["license"]} · Accepting new guests</figcaption>
    </figure>
    <div class="prose">
      <p class="eyebrow">About {t["name"]}</p>
{bio}
      <h2>What {t["name"]} <em>does.</em></h2>
      <ul class="chips">{chips}</ul>{qa}
      <figure class="pull" style="margin-top:44px">
        <blockquote>“{t["review"][0]}”</blockquote>
        <figcaption><span class="stars" style="color:var(--ink)" aria-label="5 out of 5 stars">★★★★★</span> {t["review"][1]}</figcaption>
      </figure>{work}
    </div>
  </div>
</section>

{bookband(R, heading=f"Book with <em>{t['name']}.</em>", text=f"{t['name']} is accepting new guests. Pick a time online, or call {PHONE_DISPLAY}.", book=t["book"], label=f"Book with {t['name']}")}

<section class="sec">
  <div class="wrap">
    <p class="eyebrow">The team</p>
    <h2>Also <em>behind the chair.</em></h2>
    <div class="chairs pair" style="margin-top:40px">
{others}
    </div>
  </div>
</section>'''
    profile = {"@type": "ProfilePage", "@id": abs_url(path) + "#page", "url": abs_url(path),
               "name": t["title"], "mainEntity": {"@id": abs_url(f"team/{t['slug']}/#person")}}
    return write_page(path, R=R, current="team/", og_type="profile", title=t["title"], description=t["description"],
                      body=body, image=t["photo"], image_alt=t["alt"],
                      ld_nodes=[salon_ld(), person_ld(t), profile, crumbs_ld(crumbs)])


FAQ = [
    ("How do I book an appointment?", f"Book online through our booking page, where you can choose your stylist or barber and see available times, or call us at {PHONE_DISPLAY}."),
    ("What is your cancellation policy?", f"Please cancel or reschedule at least 24 hours before your appointment, using the link in your confirmation email and text or by calling {PHONE_DISPLAY}. After two no-call, no-shows, you will no longer be able to book future appointments."),
    ("What are your hours?", "Tuesday to Friday, 10 AM to 7 PM, and Saturday, 9 AM to 2 PM. We're closed Sunday and Monday."),
    ("Where are you located?", f"Salon Polo & Barbershop is at {STREET}, {CITY}, {REGION} {ZIP}."),
    ("Who does hot towel shaves?", "Hot towel shaves and head shaves are done by Colette, our licensed barber."),
    ("What products do you use?", "We use and carry Kevin Murphy hair and grooming products."),
]


def build_contact():
    path = "contact/"
    R = rel(path)
    crumbs = [("Home", ""), ("Visit & Contact", path)]
    hours_rows = "\n".join(
        f'        <tr{" class=\"closed\"" if not s else ""}><td>{d}</td><td>{"Closed" if not s else hours_short(s)}</td></tr>' for d, s in HOURS)
    faq = "\n".join(f"      <details><summary>{q}</summary><p>{a}</p></details>" for q, a in FAQ)
    body = f'''<header class="phead">
  <div class="wrap">
    {crumbs_html(R, crumbs)}
    <h1>Visit <em>Salon Polo.</em></h1>
    <p class="lead">Salon Polo &amp; Barbershop, {STREET}, {CITY}, {REGION} {ZIP}. Open Tuesday to Saturday.</p>
    <div class="cta"><a class="btn" href="{BOOK}" target="_blank" rel="noopener">Book online</a><a class="btn ghost" href="{DIRECTIONS}" target="_blank" rel="noopener">Get directions</a></div>
  </div>
</header>

<section class="visit" style="border-top:0">
  <div class="wrap grid">
    <div class="block">
      <h2 style="font-family:var(--body);font-size:.7rem;letter-spacing:.26em;text-transform:uppercase;color:var(--oak);font-weight:500;margin:0 0 14px">Address</h2>
      <address>Salon Polo &amp; Barbershop<br>{STREET}<br>{CITY}, {REGION} {ZIP}</address>
      <a class="dir" href="{MAPS}" target="_blank" rel="noopener">Open in Google Maps</a>
    </div>
    <div class="block">
      <h2 style="font-family:var(--body);font-size:.7rem;letter-spacing:.26em;text-transform:uppercase;color:var(--oak);font-weight:500;margin:0 0 14px">Phone &amp; email</h2>
      <a class="phone" style="margin-top:0" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a><br>
      <span style="display:block;margin-top:6px;user-select:all">{EMAIL}</span>
    </div>
    <div class="block">
      <h2 style="font-family:var(--body);font-size:.7rem;letter-spacing:.26em;text-transform:uppercase;color:var(--oak);font-weight:500;margin:0 0 14px">Hours</h2>
      <table class="hours">
{hours_rows}
      </table>
    </div>
  </div>
</section>

<section class="sec" id="policy">
  <div class="wrap two">
    <div>
      <p class="eyebrow">Booking policy</p>
      <h2>Cancellation <em>policy.</em></h2>
    </div>
    <div class="prose">
      <h3>Canceling and rescheduling</h3>
      <p>At Salon Polo, we value your time and the time of our staff and other guests. If you need to cancel or reschedule your appointment, please do so at least 24 hours before your scheduled time. You can easily make changes using the link provided in your confirmation email and text or by calling our salon at <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>.</p>
      <h3>No-call, no-show policy</h3>
      <p>After two instances of a no-call, no-show, you will no longer be eligible to book future appointments with Salon Polo.</p>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap two">
    <div>
      <p class="eyebrow">Questions</p>
      <h2>Good to <em>know.</em></h2>
    </div>
    <div class="faq">
{faq}
    </div>
  </div>
</section>

{bookband(R)}'''
    faq_ld = {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}
    contact_page = {"@type": "ContactPage", "@id": abs_url(path) + "#page", "url": abs_url(path), "about": {"@id": SALON_ID}}
    return write_page(path, R=R, current="contact/",
                      title="Hours, Directions & Contact | Salon Polo, Annapolis MD",
                      description=f"Salon Polo, {STREET}, {CITY}, {REGION} {ZIP}. Open Tue–Fri 10–7, Sat 9–2. Call {PHONE_DISPLAY}, get directions or read our cancellation policy.",
                      body=body, ld_nodes=[salon_ld(True), contact_page, faq_ld, crumbs_ld(crumbs)])


def build_join():
    path = "join-our-team/"
    R = rel(path)
    crumbs = [("Home", ""), ("Team", "team/"), ("Join our team", path)]
    body = f'''<header class="phead">
  <div class="wrap">
    {crumbs_html(R, crumbs)}
    <h1>Join <em>our team.</em></h1>
    <p class="lead">We're growing, and we're always glad to hear from licensed stylists and barbers who care about the craft and the people in their chair.</p>
    <div class="cta"><a class="btn" href="{INSTAGRAM}" target="_blank" rel="noopener">Send us a DM</a></div>
  </div>
</header>

<section class="sec">
  <div class="wrap two">
    <div>
      <p class="eyebrow">Working here</p>
      <h2>Let's work <em>together.</em></h2>
    </div>
    <div class="prose">
      <p>Salon Polo opened at its own Annapolis location in September 2024 with a clear mission: to create meaningful employment opportunities for like-minded professionals who share our passion for helping others and providing the best service in the industry.</p>
      <ul>
        <li>An employee position, not booth rental.</li>
        <li>A guaranteed hourly floor or level-based commission, whichever is higher, calculated weekly.</li>
        <li>A 90-day performance review.</li>
        <li>Kevin Murphy products, and a bright, four-chair salon.</li>
      </ul>
      <p>Interested? Send us a message on <a href="{INSTAGRAM}" target="_blank" rel="noopener">Instagram</a>, or email <span style="user-select:all">{EMAIL}</span> with a little about yourself and your work.</p>
    </div>
  </div>
</section>'''
    return write_page(path, R=R, current="team/",
                      title="Join Our Team: Stylist & Barber Jobs in Annapolis | Salon Polo",
                      description="Stylist and barber jobs at Salon Polo in Annapolis, MD. Employee position with a guaranteed hourly floor or level-based commission, whichever is higher.",
                      body=body, ld_nodes=[salon_ld(), crumbs_ld(crumbs)])


def build_privacy():
    path = "privacyterms/"
    R = rel(path)
    crumbs = [("Home", ""), ("Privacy & Terms", path)]
    body = f'''<header class="phead">
  <div class="wrap">
    {crumbs_html(R, crumbs)}
    <h1>Privacy <em>&amp; terms.</em></h1>
  </div>
</header>

<section class="sec">
  <div class="wrap">
    <div class="prose">
      <h2>Privacy policy</h2>
      <p>At Salon Polo, we respect your privacy and are committed to protecting your personal information. When you book an appointment, contact us, or communicate with us through our website or messaging services, we may collect basic information such as your name, phone number, email address, and appointment history.</p>
      <p>This information is used to:</p>
      <ul><li>Schedule and manage appointments</li><li>Communicate regarding services or bookings</li><li>Send appointment confirmations and reminders</li><li>Respond to inquiries or customer service requests</li><li>Improve our services and client experience</li></ul>
      <p>If you choose to communicate with us through SMS or messaging, message frequency may vary depending on your interaction with our salon. Standard message and data rates may apply.</p>
      <p>Salon Polo does not sell, rent, or share your personal information with third parties for marketing purposes. Your information may be shared with trusted service providers used to operate our business systems, such as booking software or messaging platforms.</p>
      <p>You may opt out of SMS communications at any time by replying STOP to any text message.</p>
      <h2>Terms of service</h2>
      <p>By contacting Salon Polo or opting into messaging through our website or booking platform, you agree to receive communications from Salon Polo related to your appointments and salon services. These communications may include:</p>
      <ul><li>Appointment confirmations</li><li>Appointment reminders</li><li>Responses to inquiries</li><li>Follow-up messages related to services</li><li>Occasional promotions or updates</li></ul>
      <p>Message frequency may vary. Message and data rates may apply depending on your mobile carrier. You may opt out of SMS communications at any time by replying STOP to any text message. For assistance, contact the salon directly.</p>
      <p>Salon Polo is not responsible for delays in message delivery caused by mobile carriers or service providers.</p>
      <h2>Contact information</h2>
      <p>Salon Polo<br>{STREET}<br>{CITY}, {REGION} {ZIP}<br>Phone: <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a><br>Email: {EMAIL}</p>
    </div>
  </div>
</section>'''
    return write_page(path, R=R, title="Privacy & Terms | Salon Polo, Annapolis MD",
                      description="Salon Polo's privacy policy and SMS terms of service: what information we collect, how we use it, and how to opt out of text messages.",
                      body=body, ld_nodes=[salon_ld(), crumbs_ld(crumbs)])


def build_redirect(old, new):
    """Keep an old Squarespace URL working by sending visitors (and Google) to its new page."""
    R = rel(old)
    target = abs_url(new)
    doc = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Moved | Salon Polo</title>
<link rel="canonical" href="{target}">
<meta name="robots" content="noindex, follow">
<meta http-equiv="refresh" content="0; url={R}{new}">
</head>
<body>
<p>This page has moved to <a href="{R}{new}">{target}</a>.</p>
</body>
</html>
'''
    out = os.path.join(ROOT, old, "index.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(doc)


def build_404():
    B = BASE_PATH
    body = f'''<header class="phead">
  <div class="wrap">
    <h1>That page <em>isn't here.</em></h1>
    <p class="lead">It may have moved when we rebuilt the site. Try one of these instead.</p>
    <div class="cta"><a class="btn" href="{B}">Home</a><a class="btn ghost" href="{B}services/">Services</a><a class="btn ghost" href="{B}team/">Team</a><a class="btn ghost" href="{B}contact/">Visit</a></div>
  </div>
</header>'''
    # 404 can be served at any depth, so it uses absolute paths.
    doc_path = os.path.join(ROOT, "404.html")
    write_page("404.html", R=B, title="Page not found | Salon Polo", description="This page could not be found.",
               body=body, ld_nodes=[salon_ld()], robots="noindex")
    return doc_path


def build_sitemap(paths):
    pri = {"": "1.0"}
    urls = []
    for p in paths:
        priority = pri.get(p, "0.8" if p.startswith(("services/", "team/")) else "0.5")
        urls.append(f"  <url><loc>{abs_url(p)}</loc><lastmod>{TODAY}</lastmod><priority>{priority}</priority></url>")
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(urls) + "\n</urlset>\n"
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(xml)
    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n")


def main():
    pages = [build_home(), build_services()]
    pages += [build_service(s) for s in SERVICES]
    pages.append(build_team())
    pages += [build_person(t) for t in TEAM]
    pages += [build_contact(), build_join(), build_privacy()]
    build_redirect("ourteam/", "team/")
    build_404()
    build_sitemap(pages)
    print(f"Built {len(pages)} pages + 404, redirects, sitemap.xml, robots.txt")
    for p in pages:
        print("  /" + p)


if __name__ == "__main__":
    main()
