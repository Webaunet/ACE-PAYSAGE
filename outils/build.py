#!/usr/bin/env python3
"""Génère les pages HTML du site ACE Paysage IDF (maquette).

Usage : python3 outils/build.py   (depuis la racine du dépôt)
Le corps de l'accueil est dans outils/pages/index.html ; les autres pages sont composées ici.
Chaque page a son propre contenu, sa propre mise en page et ses propres textes.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HOME = open(os.path.join(ROOT, "outils", "pages", "index.html"), encoding="utf-8").read()

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
           "rx='14' fill='%2316382A'/%3E%3Ctext x='32' y='43' font-family='Arial' font-weight='800' font-size='25' "
           "text-anchor='middle' fill='%23D6E4F6'%3EACE%3C/text%3E%3C/svg%3E")


def header(active):
    links = "\n".join(
        '      <a class="link" href="%s"%s>%s</a>' % (h, ' aria-current="page"' if h == active else "", t) for h, t in NAV)
    return f'''<header class="site-header" id="top">
  <div class="wrap bar">
    <a class="logo" href="https://webaunet.github.io/AR-paysage" aria-label="ACE Paysage IDF, accueil"><b>ACE</b><span>Paysage IDF</span></a>
    <button class="burger" id="burger" type="button" aria-label="Ouvrir le menu" aria-expanded="false" aria-controls="nav">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg>
    </button>
    <nav class="nav" id="nav" aria-label="Navigation principale">
{links}
      <a class="btn btn-sm" href="tel:+33622623186">
        {PHONE_ICON}
        06 22 62 31 86
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
        <a class="logo" href="https://webaunet.github.io/AR-paysage" aria-label="ACE Paysage IDF, accueil"><b>ACE</b><span>Paysage IDF</span></a>
        <p style="margin-top:1rem;max-width:26em">Aménagement paysager aux Alluets-le-Roi et alentours.</p>
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
          <li><a href="tel:+33622623186">06 22 62 31 86</a></li>
          <li><a href="mailto:ace.paysage@hotmail.com" style="overflow-wrap:anywhere">ace.paysage@hotmail.com</a></li>
          <li>Les Alluets-le-Roi (78)</li>
        </ul>
      </div>
    </div>
    <div class="foot-note">
      <span>© 2026 ACE Paysage IDF · Maquette de site</span>
      <span>SARL · SIREN 523 262 624</span>
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
<body{' class="page-home"' if fname == "index.html" else ""}>
{header(fname)}
<main>
{body}
</main>
{footer()}
<script src="main.js"></script>
</body>
</html>
'''


def page_hero(crumb, eyebrow, h1, lead, media="", actions=""):
    head = f'<nav class="crumbs" aria-label="Fil d\'Ariane"><a href="index.html">Accueil</a> / <span>{crumb}</span></nav>'
    if media:
        inner = f'''      {head}
      <div class="page-hero-grid">
        <div>
          <p class="eyebrow">{eyebrow}</p>
          <h1 id="h1">{h1}</h1>
          <p class="lead">{lead}</p>
          {actions}
        </div>
        {media}
      </div>'''
        cls = "page-hero has-media"
    else:
        inner = f'''      {head}
      <p class="eyebrow">{eyebrow}</p>
      <h1 id="h1">{h1}</h1>
      <p class="lead">{lead}</p>'''
        cls = "page-hero"
    return f'''  <section class="{cls}" aria-labelledby="h1">
    <div class="wrap">
{inner}
    </div>
    {WAVE % ""}
  </section>
'''


def phone_block(extra_btn=""):
    return f'''<a class="phone" href="tel:+33622623186" id="phone">06 22 62 31 86</a>
        <div class="cta-actions">
          <a class="btn btn-band" href="tel:+33622623186">Appeler</a>
          <button class="btn btn-ghost" type="button" id="copy">Copier le numéro</button>
          {extra_btn}
          <span class="copied" id="copied" role="status" aria-live="polite"></span>
        </div>'''


def cta_split(eyebrow, heading, lead, img, alt, pos, info="", h="h2", bottom_wave=False):
    """Bandeau de contact avec photo à droite."""
    return f'''  <section class="cta" id="contact" aria-labelledby="h-contact">
    {WAVE % " flip"}
    <div class="wrap cta-grid">
      <div>
        <p class="eyebrow">{eyebrow}</p>
        <{h} id="h-contact">{heading}</{h}>
        <p class="lead">{lead}</p>
        {phone_block()}
        {info}
      </div>
      <figure class="cta-media">
        <img src="img/{img}" width="1376" height="768" loading="lazy" style="object-position:{pos}" alt="{alt}">
      </figure>
    </div>
    {WAVE % "" if bottom_wave else ""}
  </section>
'''


def cta_center(eyebrow, heading, lead, extra_btn="", bg=""):
    """Bandeau de contact centré, sans photo (ou avec un fond photo teinté)."""
    style = ""
    cls = "cta cta-center"
    if bg:
        style = (' style="background-image:linear-gradient(rgba(16,44,32,.84),rgba(16,44,32,.84)),url(img/%s)"' % bg)
        cls += " cta-bg"
    return f'''  <section class="{cls}" aria-labelledby="h-cta"{style}>
    {WAVE % " flip"}
    <div class="wrap">
      <p class="eyebrow">{eyebrow}</p>
      <h2 id="h-cta">{heading}</h2>
      <p class="lead">{lead}</p>
      {phone_block(extra_btn)}
    </div>
  </section>
'''


def swap(s, a, b):
    assert s.count(a) == 1, ("cible absente ou multiple", a[:60], s.count(a))
    return s.replace(a, b)


PAGES = {}

# ------------------------------------------------------------------ Accueil
PAGES["index.html"] = (
    "ACE Paysage IDF",
    "ACE Paysage IDF, aménagement paysager aux Alluets-le-Roi (78) : création de jardin, plantation, entretien.",
    HOME)

# ------------------------------------------------------------------ Prestations
MOSAIC = '''<div class="mosaic">
          <img class="m1" src="img/plantation.jpg" width="1400" height="764" style="object-position:62% 50%" alt="Jardinier qui plante un arbuste dans un massif de terre fraîchement travaillée">
          <img class="m2" src="img/terrassement.jpg" width="1376" height="768" style="object-position:68% 50%" alt="Terre décaissée à la pelle à côté d'une pelouse">
          <img class="m3" src="img/dechets-verts.jpg" width="1408" height="768" style="object-position:55% 50%" alt="Branchages chargés sur une remorque après la taille d'une haie">
        </div>'''
PREST_ACTIONS = '''<div class="hero-actions">
            <a class="btn btn-band" href="#amenager">Aménager</a>
            <a class="btn btn-ghost" href="#entretien">Entretenir</a>
          </div>'''

AMENAGER = [
    ("creation-espace-vert.jpg", "70% 50%", "Création d'espaces verts",
     "Un jardin se pense avant de se planter. Pelouse, massifs, allées et bordures sont organisés pour s'accorder à la maison et à la façon dont vous vivez dehors.",
     "Pelouse aux courbes douces, bordures et paillage autour d'une plantation de graminées"),
    ("plantation.jpg", "62% 50%", "Plantation",
     "Arbustes, vivaces et haies sont installés à leur place, dans une terre préparée, pour bien démarrer et s'épanouir au fil des saisons.",
     "Arbuste planté dans un massif de terre fraîchement travaillée"),
    ("terrassement.jpg", "68% 50%", "Terrassement",
     "Décaissement, remblai et modelage du terrain : la base indispensable avant de semer, de planter ou d'aménager.",
     "Terre décaissée à la pelle, brouette et tas de terre à côté d'une pelouse"),
    ("nivellement.jpg", "45% 50%", "Nivellement et préparation du sol",
     "Un sol aplani et affiné au râteau, prêt à recevoir une pelouse ou de nouvelles plantations.",
     "Terrain nivelé au râteau large avant la remise en pelouse"),
]
ENTRETENIR = [
    ("tonte.jpg", "60% 50%", "Tonte de pelouse", "Des passages réguliers pour une pelouse nette, au rythme de la pousse.", "Tonte d'une pelouse devant une maison aux volets bleus"),
    ("taille-haies.jpg", "40% 50%", "Taille de haies", "Haies taillées à la bonne hauteur, au bon moment, pour rester denses et propres.", "Taille d'une haie de laurier au taille-haie"),
    ("desherbage.jpg", "60% 50%", "Désherbage", "Massifs et allées gravillonnées débarrassés des mauvaises herbes.", "Désherbage d'un massif fleuri le long d'une allée de gravier"),
    ("feuilles.jpg", "68% 50%", "Ramassage de feuilles", "Pelouse, massifs et allées dégagés des feuilles tombées à l'automne.", "Ramassage des feuilles d'automne au râteau"),
    ("dechets-verts.jpg", "55% 50%", "Évacuation des déchets verts", "Tailles, tontes et feuilles chargées et emportées une fois le travail terminé.", "Chargement de branchages sur une remorque"),
]
rows = "\n".join(
    f'''        <article class="row-card">
          <img src="img/{f}" width="1400" height="764" loading="lazy" style="object-position:{pos}" alt="{alt}">
          <div><h3>{t}</h3><p>{d}</p></div>
        </article>''' for f, pos, t, d, alt in AMENAGER)
svcs = "\n".join(
    f'''          <li class="svc">
            <img src="img/{f}" width="400" height="400" loading="lazy" style="object-position:{pos}" alt="{alt}">
            <div><h3>{t}</h3><p>{d}</p></div>
          </li>''' for f, pos, t, d, alt in ENTRETENIR)

PAGES["prestations.html"] = (
    "Prestations · ACE Paysage IDF",
    "Prestations d'ACE Paysage IDF aux Alluets-le-Roi : création d'espaces verts, plantation, terrassement, tonte, taille de haies, désherbage.",
    page_hero("Prestations", "Prestations", "Aménager et entretenir votre jardin.",
              "De la création du jardin à son entretien au fil des saisons, ACE Paysage IDF intervient aux différentes étapes.",
              media=MOSAIC, actions=PREST_ACTIONS)
    + f'''  <section class="section" id="amenager" aria-labelledby="h-amen">
    <div class="wrap">
      <div class="section-head">
        <p class="eyebrow">Aménager</p>
        <h2 id="h-amen">Un terrain prêt, puis un jardin qui prend forme.</h2>
        <p>Les travaux qui donnent au jardin sa structure : le dessin, la terre, les premières plantations.</p>
      </div>
      <div class="rows">
{rows}
      </div>
    </div>
  </section>
  <section class="section band-tint" id="entretien" aria-labelledby="h-entr">
    <div class="wrap svc-wrap">
      <div class="section-head">
        <p class="eyebrow">Entretenir</p>
        <h2 id="h-entr">Le jardin reste soigné, saison après saison.</h2>
        <p>Les gestes réguliers qui gardent la pelouse, les haies et les massifs en ordre.</p>
      </div>
      <ul class="svc-list">
{svcs}
      </ul>
    </div>
  </section>
''' + cta_center("Un projet de jardin ?", "Décrivez-le directement à l'entreprise.",
                 "ACE Paysage IDF répond aux particuliers des Alluets-le-Roi et des environs."))

# ------------------------------------------------------------------ Réalisations
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


POLAROIDS = '''<div class="polaroids">
          <figure class="pola p1"><img src="img/taille-haie-pavillon.jpg" width="1408" height="768" style="object-position:48% 50%" alt="Longue haie taillée devant un pavillon en brique"><figcaption>Haie taillée</figcaption></figure>
          <figure class="pola p2"><img src="img/jardin-ambiance.jpg" width="1408" height="768" style="object-position:55% 50%" alt="Jardin de campagne avec pelouse, massifs et allée de gravier"><figcaption>Jardin et massifs</figcaption></figure>
          <figure class="pola p3"><img src="img/feuilles.jpg" width="1400" height="764" style="object-position:68% 50%" alt="Ramassage des feuilles d'automne au râteau"><figcaption>Jardin en automne</figcaption></figure>
        </div>'''
REAL_ACTIONS = '''<div class="hero-actions">
            <a class="btn btn-band" href="#galerie">Voir la galerie</a>
            <a class="btn btn-ghost" href="prestations.html">Les prestations</a>
          </div>'''

PAGES["realisations.html"] = (
    "Réalisations · ACE Paysage IDF",
    "Aperçu de travaux d'aménagement et d'entretien de jardin par ACE Paysage IDF, aux Alluets-le-Roi.",
    page_hero("Réalisations", "Réalisations", "Des jardins aménagés et entretenus.",
              "Neuf scènes de jardin : pelouses, haies, massifs et terrains en préparation.",
              media=POLAROIDS, actions=REAL_ACTIONS)
    + f'''  <section class="section" id="galerie" aria-label="Galerie">
    <div class="wrap">
      <div class="real-grid">
{fig_html(GALLERY[:6])}
      </div>
    </div>
  </section>
  <section class="section band-tint" aria-label="Galerie, suite">
    <div class="wrap">
      <div class="real-grid real-big">
{fig_html(GALLERY[6:])}
      </div>
    </div>
  </section>
''' + cta_center("Votre jardin", "Et si le prochain, c'était le vôtre ?",
                 "Parlez de votre projet à ACE Paysage IDF par téléphone.",
                 extra_btn='<a class="btn btn-ghost" href="prestations.html">Voir les prestations</a>',
                 bg="entretien-general.jpg"))

# ------------------------------------------------------------------ À propos
APROPOS_MEDIA = '''<div class="mosaic mosaic-one">
          <img class="m1" src="img/entretien-general.jpg" width="1376" height="768" style="object-position:62% 50%" alt="Entretien d'un jardin devant une maison en pierre : tonte de la pelouse et ratissage de la terrasse">
        </div>'''
PAGES["a-propos.html"] = (
    "À propos · ACE Paysage IDF",
    "ACE Paysage IDF, SARL d'aménagement paysager installée aux Alluets-le-Roi (78) depuis 2010.",
    page_hero("À propos", "À propos", "Un paysagiste de proximité.",
              "SARL installée aux Alluets-le-Roi depuis 2010, ACE Paysage IDF aménage et entretient les jardins du secteur.",
              media=APROPOS_MEDIA)
    + '''  <section class="section" id="a-propos" aria-labelledby="h-apropos">
    <div class="wrap about-grid">
      <figure class="about-media">
        <img src="img/dechets-verts.jpg" width="1408" height="768" loading="lazy" style="object-position:55% 50%" alt="Jardinier qui charge des branchages sur une remorque devant une maison en pierre">
      </figure>
      <div class="about-body">
        <p class="eyebrow">L'entreprise</p>
        <h2 id="h-apropos">Du jardin à créer au jardin à entretenir.</h2>
        <p>ACE Paysage IDF est une SARL créée en 2010 aux Alluets-le-Roi, dans les Yvelines. Son activité déclarée : les services d'aménagement paysager.</p>
        <p>Pour un projet ou un entretien régulier, le plus simple est d'en parler directement avec l'entreprise.</p>
        <dl class="id-card">
          <div><dt>Activité</dt><dd>Services d'aménagement paysager</dd></div>
          <div><dt>Forme</dt><dd>SARL</dd></div>
          <div><dt>Depuis</dt><dd>2010</dd></div>
          <div><dt>SIREN</dt><dd>523 262 624</dd></div>
        </dl>
      </div>
    </div>
  </section>
  <section class="section statement" id="zone" aria-labelledby="h-zone">
    <div class="wrap">
      <p class="eyebrow">Zone d'intervention</p>
      <h2 id="h-zone">Les Alluets-le-Roi et alentours.</h2>
      <p>ACE Paysage IDF travaille aux Alluets-le-Roi et dans les communes voisines. Pour savoir si votre jardin est dans le secteur, appelez l'entreprise.</p>
      <a class="btn" href="contact.html">Contacter l'entreprise</a>
    </div>
  </section>
''' + cta_split("Une question ?", "Un projet ou une demande d'intervention ?",
                "Le plus direct reste un appel à l'entreprise.",
                "plantation.jpg", "Jardinier qui plante un arbuste dans un massif de terre", "62% 50%"))

# ------------------------------------------------------------------ Contact
PAGES["contact.html"] = (
    "Contact · ACE Paysage IDF",
    "Contacter ACE Paysage IDF, paysagiste aux Alluets-le-Roi (78) : 06 22 62 31 86.",
    cta_split("Contact", "Parlons de votre jardin.",
              "Une question, un projet, une demande d'intervention : le téléphone est le moyen le plus direct.",
              "feuilles.jpg", "Jardinier qui ratisse les feuilles d'automne dans un jardin", "68% 50%", h="h1", bottom_wave=True)
    + '''  <section class="section" id="formulaire" aria-labelledby="h-coord">
    <div class="wrap about-grid contact-grid">
      <div class="about-body">
        <p class="eyebrow">Votre demande</p>
        <h2 id="h-coord">Décrivez votre jardin et votre besoin.</h2>
        <p>Préparez votre demande ici, puis transmettez-la à l'entreprise par SMS, par e-mail ou par téléphone.</p>
        <dl class="id-card">
          <div><dt>Téléphone</dt><dd><a href="tel:+33622623186">06 22 62 31 86</a></dd></div>
          <div><dt>E-mail</dt><dd><a href="mailto:ace.paysage@hotmail.com" style="overflow-wrap:anywhere">ace.paysage@hotmail.com</a></dd></div>
          <div><dt>Commune</dt><dd>Les Alluets-le-Roi</dd></div>
          <div><dt>Département</dt><dd>Yvelines (78)</dd></div>
        </dl>
      </div>
      <div class="form-card">
        <form id="contact-form" novalidate>
          <h3>Préparer ma demande</h3>
          <p class="form-intro">Quelques lignes suffisent. Les champs marqués * sont nécessaires.</p>
          <div class="field-grid">
            <div class="field">
              <label for="f-nom">Nom *</label>
              <input type="text" id="f-nom" name="nom" autocomplete="name" placeholder="Votre nom">
              <span class="err" id="e-nom" role="alert"></span>
            </div>
            <div class="field">
              <label for="f-tel">Téléphone *</label>
              <input type="tel" id="f-tel" name="tel" autocomplete="tel" inputmode="tel" placeholder="06 00 00 00 00">
              <span class="err" id="e-tel" role="alert"></span>
            </div>
            <div class="field">
              <label for="f-commune">Commune</label>
              <input type="text" id="f-commune" name="commune" autocomplete="address-level2" placeholder="Votre commune">
            </div>
            <div class="field">
              <label for="f-besoin">Je souhaite *</label>
              <div class="select-wrap">
                <select id="f-besoin" name="besoin">
                  <option value="">Choisir…</option>
                  <option>Aménager mon jardin</option>
                  <option>Entretenir mon jardin</option>
                  <option>Aménager et entretenir mon jardin</option>
                  <option>Autre demande</option>
                </select>
              </div>
              <span class="err" id="e-besoin" role="alert"></span>
            </div>
            <div class="field full">
              <span class="lbl" id="l-presta">Prestations concernées</span>
              <div class="pills" role="group" aria-labelledby="l-presta">
              <label class="pill"><input type="checkbox" name="prestations" value="Création d'espaces verts" id="svc-1"><span>Création d'espaces verts</span></label>
              <label class="pill"><input type="checkbox" name="prestations" value="Plantation" id="svc-2"><span>Plantation</span></label>
              <label class="pill"><input type="checkbox" name="prestations" value="Terrassement" id="svc-3"><span>Terrassement</span></label>
              <label class="pill"><input type="checkbox" name="prestations" value="Nivellement" id="svc-4"><span>Nivellement</span></label>
              <label class="pill"><input type="checkbox" name="prestations" value="Tonte" id="svc-5"><span>Tonte</span></label>
              <label class="pill"><input type="checkbox" name="prestations" value="Taille de haies" id="svc-6"><span>Taille de haies</span></label>
              <label class="pill"><input type="checkbox" name="prestations" value="Désherbage" id="svc-7"><span>Désherbage</span></label>
              <label class="pill"><input type="checkbox" name="prestations" value="Ramassage de feuilles" id="svc-8"><span>Ramassage de feuilles</span></label>
              <label class="pill"><input type="checkbox" name="prestations" value="Déchets verts" id="svc-9"><span>Déchets verts</span></label>
              </div>
            </div>
            <div class="field full">
              <label for="f-message">Message</label>
              <textarea id="f-message" name="message" rows="3" placeholder="Surface, état du jardin, période souhaitée…"></textarea>
            </div>
          </div>
          <div class="form-actions">
            <button class="btn" type="submit">Préparer ma demande</button>
            <p class="note">Rien n'est envoyé automatiquement : vous choisissez ensuite comment transmettre votre demande.</p>
          </div>
        </form>
        <div id="recap" hidden>
          <h3>Votre demande est prête</h3>
          <p class="form-intro">Relisez-la, puis transmettez-la à l'entreprise.</p>
          <textarea class="recap-text" id="recap-text" readonly aria-label="Texte de votre demande"></textarea>
          <div class="recap-actions">
            <a class="btn" id="recap-sms" href="sms:+33622623186">Envoyer par SMS</a>
            <a class="btn btn-line" id="recap-mail" href="mailto:ace.paysage@hotmail.com">Envoyer par e-mail</a>
            <button class="btn btn-line" type="button" id="recap-copy">Copier la demande</button>
            <a class="btn btn-line" href="tel:+33622623186">Appeler le 06 22 62 31 86</a>
          </div>
          <p class="recap-note" id="recap-status" role="status" aria-live="polite">Le SMS et l'e-mail s'ouvrent dans votre messagerie. Sinon, copiez la demande ou appelez l'entreprise.</p>
          <p style="margin-top:.8rem"><button class="btn btn-sm btn-line" type="button" id="recap-edit">Modifier ma demande</button></p>
        </div>
      </div>
    </div>
  </section>
''')

for fname, (title, desc, body) in PAGES.items():
    out = page(fname, title, desc, body)
    open(os.path.join(ROOT, fname), "w", encoding="utf-8").write(out)
    print("écrit", fname, len(out))

# Contrôles : liens internes (fichier + ancre) et images existantes
bad = 0
ids = {}
for fname in PAGES:
    html = open(os.path.join(ROOT, fname), encoding="utf-8").read()
    ids[fname] = set(re.findall(r'id="([^"]+)"', html))
for fname in PAGES:
    html = open(os.path.join(ROOT, fname), encoding="utf-8").read()
    for ref in re.findall(r'(?:href|src)="([^"]+)"', html):
        if ref.startswith(("http", "data:", "tel", "mailto", "sms")):
            continue
        path, _, anchor = ref.partition("#")
        target = path or fname
        if not os.path.exists(os.path.join(ROOT, target)):
            print("LIEN CASSÉ", fname, ref); bad += 1
        elif anchor and target.endswith(".html") and anchor not in ids.get(target, set()):
            print("ANCRE ABSENTE", fname, ref); bad += 1
sys.exit(1 if bad else 0)
