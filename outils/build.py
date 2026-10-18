#!/usr/bin/env python3
"""Génère les pages HTML du site A.R Paysage (maquette).

Usage : python3 outils/build.py   (depuis la racine du dépôt)
Source de l'accueil : outils/pages/index.html (contenu de <main>, avec marqueurs
<!--GROUPS-->, <!--SEASONS-->, <!--ABOUT-->, <!--CTA--> réutilisés par les autres pages).
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HOME = open(os.path.join(ROOT, "outils", "pages", "index.html"), encoding="utf-8").read()


def part(name):
    m = re.search(r"<!--%s-->\n(.*?)<!--/%s-->" % (name, name), HOME, re.S)
    assert m, "marqueur absent : " + name
    return m.group(1)


PREST, SEASONS, ABOUT, CTA = (part(n) for n in ("PREST", "SEASONS", "ABOUT", "CTA"))

NAV = [
    ("index.html", "Accueil"),
    ("prestations.html", "Prestations"),
    ("realisations.html", "Réalisations"),
    ("a-propos.html", "À propos"),
    ("contact.html", "Contact"),
]

PHONE_ICON = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" '
              'stroke-linejoin="round"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 '
              '0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 '
              '2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2Z"/></svg>')
WAVE = ('<svg class="wave%s" viewBox="0 0 1440 60" preserveAspectRatio="none" aria-hidden="true">'
        '<path d="M0 60V32C220 2 430 58 700 30S1180 4 1440 34V60Z" fill="currentColor"/></svg>')
FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' "
           "rx='14' fill='%2316382A'/%3E%3Ctext x='32' y='43' font-family='Arial' font-weight='800' font-size='30' "
           "text-anchor='middle' fill='%23D6E4F6'%3EA.R%3C/text%3E%3C/svg%3E")


def header(active):
    links = "\n".join(
        '      <a class="link" href="%s"%s>%s</a>' % (h, ' aria-current="page"' if h == active else "", t) for h, t in NAV)
    return f'''<header class="site-header" id="top">
  <div class="wrap bar">
    <a class="logo" href="index.html" aria-label="A.R Paysage, accueil"><b>A.R</b><span>Paysage</span></a>
    <button class="burger" id="burger" type="button" aria-label="Ouvrir le menu" aria-expanded="false" aria-controls="nav">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg>
    </button>
    <nav class="nav" id="nav" aria-label="Navigation principale">
{links}
      <a class="btn btn-sm" href="tel:+33699201849">
        {PHONE_ICON}
        06 99 20 18 49
      </a>
    </nav>
  </div>
</header>
'''


def footer():
    items = "\n".join('          <li><a href="%s">%s</a></li>' % (h, t) for h, t in NAV)
    return f'''<footer class="site-footer">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <a class="logo" href="index.html" aria-label="A.R Paysage, accueil"><b>A.R</b><span>Paysage</span></a>
        <p style="margin-top:1rem;max-width:26em">Aménagement paysager au Val-Saint-Germain et alentours.</p>
      </div>
      <div>
        <h5>Navigation</h5>
        <ul>
{items}
        </ul>
      </div>
      <div>
        <h5>Contact</h5>
        <ul>
          <li><a href="tel:+33699201849">06 99 20 18 49</a></li>
          <li>Le Val-Saint-Germain (91)</li>
        </ul>
      </div>
    </div>
    <div class="foot-note">
      <span>© 2026 A.R Paysage · Maquette de site</span>
      <span>SARL · SIREN 791 175 508</span>
    </div>
  </div>
</footer>
'''


def page(fname, title, desc, body):
    return f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="{FAVICON}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Albert+Sans:wght@400;500;600&family=Bricolage+Grotesque:opsz,wght@12..96,500..800&display=swap">
<link rel="stylesheet" href="style.css">
</head>
<body>
{header(fname)}
<main>
{body}
</main>
{footer()}
<script src="main.js"></script>
</body>
</html>
'''


def page_hero(crumb, eyebrow, h1, lead):
    return f'''  <section class="page-hero" aria-labelledby="h1">
    <div class="wrap">
      <nav class="crumbs" aria-label="Fil d'Ariane"><a href="index.html">Accueil</a> / <span>{crumb}</span></nav>
      <p class="eyebrow">{eyebrow}</p>
      <h1 id="h1">{h1}</h1>
      <p class="lead">{lead}</p>
    </div>
    {WAVE % ""}
  </section>
'''


def swap(s, a, b):
    assert s.count(a) == 1, ("cible absente ou multiple", a[:60], s.count(a))
    return s.replace(a, b)


PAGES = {}

# Accueil
PAGES["index.html"] = ("A.R Paysage",
                       "A.R Paysage, aménagement paysager au Val-Saint-Germain (91) : création de jardin, plantation, entretien.",
                       HOME.replace("<!--PREST-->\n", "").replace("<!--/PREST-->\n", "")
                       .replace("<!--SEASONS-->\n", "").replace("<!--/SEASONS-->\n", "")
                       .replace("<!--ABOUT-->\n", "").replace("<!--/ABOUT-->\n", "")
                       .replace("<!--CTA-->\n", "").replace("<!--/CTA-->\n", ""))

# Prestations
PAGES["prestations.html"] = (
    "Prestations · A.R Paysage",
    "Prestations d'A.R Paysage au Val-Saint-Germain : création d'espaces verts, plantation, terrassement, tonte, taille de haies, désherbage.",
    page_hero("Prestations", "Prestations", "Aménager et entretenir votre jardin.",
              "De la création du jardin à son entretien au fil des saisons, A.R Paysage intervient aux différentes étapes.")
    + PREST
    + SEASONS + CTA)

# Réalisations
GALLERY = [
    ("jardin-ambiance.jpg", 1408, 768, "55% 50%", "Jardin de campagne avec pelouse, massifs et allée de gravier devant une maison en pierre", "Jardin et massifs", "Pelouse, massifs et allée de gravier"),
    ("creation-espace-vert.jpg", 1408, 768, "72% 50%", "Jardin neuf aux bordures courbes, pelouse, paillage et graminées devant une maison moderne", "Création d'espace vert", "Pelouse, massifs et bordures"),
    ("taille-haie-pavillon.jpg", 1408, 768, "48% 50%", "Longue haie taillée devant un pavillon en brique", "Haie taillée", "Pavillon en brique"),
    ("plantation.jpg", 1400, 764, "62% 50%", "Arbuste planté dans un massif de terre fraîchement travaillée", "Plantation", "Massif en cours de plantation"),
    ("desherbage.jpg", 1400, 764, "60% 50%", "Massif fleuri désherbé le long d'une allée de gravier, devant une maison en pierre", "Massifs entretenus", "Allée de gravier et vivaces"),
    ("nivellement.jpg", 1400, 764, "45% 50%", "Terrain nivelé au râteau large avant la remise en pelouse", "Préparation du sol", "Nivellement avant la pelouse"),
    ("tonte.jpg", 1376, 768, "60% 50%", "Tonte d'une pelouse devant une maison aux volets bleus et massifs d'hortensias", "Pelouse tondue", "Maison aux volets bleus"),
    ("terrassement.jpg", 1376, 768, "68% 50%", "Terre décaissée à la pelle, brouette et tas de terre à côté d'une pelouse", "Terrassement", "Terrain décaissé"),
    ("feuilles.jpg", 1400, 764, "68% 50%", "Ramassage des feuilles d'automne au râteau, avec sac de jardin et brouette", "Jardin en automne", "Ramassage des feuilles"),
]
def fig_html(items):
    return "\n".join(
    f'''        <figure class="real">
          <img src="img/{f}" width="{w}" height="{h}" loading="lazy" style="object-position:{pos}" alt="{alt}">
          <figcaption>{cap}<span>{sub}</span></figcaption>
        </figure>''' for f, w, h, pos, alt, cap, sub in items)


figs = (fig_html(GALLERY[:6]), fig_html(GALLERY[6:]))
PAGES["realisations.html"] = (
    "Réalisations · A.R Paysage",
    "Aperçu de travaux d'aménagement et d'entretien de jardin par A.R Paysage, au Val-Saint-Germain.",
    page_hero("Réalisations", "Réalisations", "Des jardins aménagés et entretenus.",
              "Un aperçu du travail d'aménagement et d'entretien de jardin.")
    + f'''  <section class="section" aria-label="Galerie">
    <div class="wrap">
      <div class="real-grid">
{figs[0]}
      </div>
    </div>
  </section>
  <section class="section band-tint" aria-label="Galerie, suite">
    <div class="wrap">
      <div class="real-grid real-big">
{figs[1]}
      </div>
    </div>
  </section>
''' + CTA)

# À propos
ZONE = '''  <section class="section seasons" id="zone" aria-labelledby="h-zone">
    <div class="wrap about-grid">
      <div class="about-body">
        <p class="eyebrow">Zone d'intervention</p>
        <h2 id="h-zone">Le Val-Saint-Germain et alentours.</h2>
        <p>A.R Paysage travaille au Val-Saint-Germain et dans les communes voisines. Pour savoir si votre jardin est dans le secteur, le plus simple est d'appeler l'entreprise.</p>
        <p style="margin-top:1.6rem"><a class="btn btn-line" href="prestations.html">Voir les prestations</a></p>
      </div>
      <dl class="id-card" style="margin:0">
        <div><dt>Commune</dt><dd>Le Val-Saint-Germain</dd></div>
        <div><dt>Département</dt><dd>Essonne (91)</dd></div>
        <div><dt>Secteur</dt><dd>Le Val-Saint-Germain et alentours</dd></div>
        <div><dt>Téléphone</dt><dd><a href="tel:+33699201849">06 99 20 18 49</a></dd></div>
      </dl>
    </div>
  </section>
'''
ABOUT_PAGE = swap(swap(ABOUT, '<h2 id="h-apropos">', '<h2 id="h-apropos">'), '        <p style="margin-top:1.6rem"><a class="btn btn-line" href="a-propos.html">En savoir plus</a></p>\n', "")
PAGES["a-propos.html"] = (
    "À propos · A.R Paysage",
    "A.R Paysage, SARL d'aménagement paysager installée au Val-Saint-Germain (91) depuis 2013.",
    page_hero("À propos", "À propos", "Un paysagiste de proximité.",
              "SARL installée au Val-Saint-Germain depuis 2013, A.R Paysage aménage et entretient les jardins du secteur.")
    + ABOUT_PAGE + ZONE + CTA)

# Contact
CONTACT_CTA = swap(CTA, '<h2 id="h-contact">Un jardin à créer ou à remettre en ordre ?</h2>', '<h1 id="h-contact">Un jardin à créer ou à remettre en ordre ?</h1>')
CONTACT_CTA = swap(CONTACT_CTA, "  </section>\n", "    " + WAVE % "" + "\n  </section>\n")
PAGES["contact.html"] = (
    "Contact · A.R Paysage",
    "Contacter A.R Paysage, paysagiste au Val-Saint-Germain (91) : 06 99 20 18 49.",
    CONTACT_CTA + '''  <section class="section" aria-labelledby="h-coord">
    <div class="wrap about-grid">
      <div class="about-body">
        <p class="eyebrow">Coordonnées</p>
        <h2 id="h-coord">Les informations de l'entreprise.</h2>
        <p>Le téléphone est le moyen le plus direct pour décrire votre projet à A.R Paysage.</p>
        <p style="margin-top:1.6rem"><a class="btn btn-line" href="prestations.html">Voir les prestations</a></p>
      </div>
      <dl class="id-card" style="margin:0">
        <div><dt>Téléphone</dt><dd><a href="tel:+33699201849">06 99 20 18 49</a></dd></div>
        <div><dt>Commune</dt><dd>Le Val-Saint-Germain (91)</dd></div>
        <div><dt>Secteur</dt><dd>Le Val-Saint-Germain et alentours</dd></div>
        <div><dt>Activité</dt><dd>Services d'aménagement paysager</dd></div>
        <div><dt>Forme</dt><dd>SARL</dd></div>
        <div><dt>SIREN</dt><dd>791 175 508</dd></div>
      </dl>
    </div>
  </section>
''')

for fname, (title, desc, body) in PAGES.items():
    out = page(fname, title, desc, body)
    open(os.path.join(ROOT, fname), "w", encoding="utf-8").write(out)
    print("écrit", fname, len(out))

# Contrôles : fichiers présents, liens internes valides, images existantes
bad = 0
for fname in PAGES:
    html = open(os.path.join(ROOT, fname), encoding="utf-8").read()
    for ref in re.findall(r'(?:href|src)="([^"#:]+?)(?:#[^"]*)?"', html):
        if ref.startswith(("http", "data:", "tel", "mailto")):
            continue
        if not os.path.exists(os.path.join(ROOT, ref)):
            print("LIEN CASSÉ", fname, ref)
            bad += 1
sys.exit(1 if bad else 0)
