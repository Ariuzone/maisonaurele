# -*- coding: utf-8 -*-
"""Assemble les pages HTML de Maison Aurèle à partir des fragments."""
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).parent
IMG_TOKEN_RE = re.compile(r"\{\{IMG:([^|}]+)\|([^|}]*)\|?([^|}]*)\|?(eager)?\}\}")
BASE = "https://www.maison-aurele.fr/"

SCHEMA_RESTAURANT = {
    "@context": "https://schema.org",
    "@type": "Restaurant",
    "name": "Maison Aurèle",
    "url": BASE,
    "image": [BASE + "og-image.jpg", BASE + "assets/img/hero-accueil.jpg"],
    "logo": BASE + "assets/icons/logo-full.svg",
    "description": ("Maison de gastronomie française contemporaine fondée en 1929 "
                    "sur les quais de la Saône, à Lyon. Cuisine de saison signée "
                    "par le chef Kenji Tanaka."),
    "servesCuisine": "Française contemporaine",
    "priceRange": "€€€€",
    "currenciesAccepted": "EUR",
    "paymentAccepted": "Carte bancaire, espèces",
    "address": {
        "@type": "PostalAddress",
        "streetAddress": "17 quai Saint-Vincent",
        "postalCode": "69001",
        "addressLocality": "Lyon",
        "addressRegion": "Auvergne-Rhône-Alpes",
        "addressCountry": "FR",
    },
    "geo": {"@type": "GeoCoordinates", "latitude": 45.7668, "longitude": 4.8287},
    "openingHoursSpecification": [
        {"@type": "OpeningHoursSpecification",
         "dayOfWeek": ["Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
         "opens": "12:00", "closes": "13:45"},
        {"@type": "OpeningHoursSpecification",
         "dayOfWeek": ["Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
         "opens": "19:30", "closes": "22:30"},
    ],
    "acceptsReservations": BASE + "reservation.html",
    "hasMenu": BASE + "carte.html",
    "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.9",
                        "reviewCount": "312", "bestRating": "5"},
}

SCHEMA_ORG = {
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": "Matrice Studio",
    "url": "https://www.example.com/",
    "email": "matricestudio@protonmail.com",
    "description": "Studio de création de sites web — démonstration Maison Aurèle.",
}

# Métadonnées par page : canon, titre, description, image og, fil d'ariane
PAGES = {
    "index": {
        "title": "Maison Aurèle — Restaurant gastronomique à Lyon, quais de Saône",
        "desc": ("Maison Aurèle, table gastronomique lyonnaise depuis 1929. Cuisine "
                 "française contemporaine de saison par le chef Kenji Tanaka. "
                 "Réservation en ligne, privatisation, bons cadeaux."),
        "og_type": "website",
        "img": "og-image.jpg",
        "crumbs": [],
    },
    "maison": {
        "title": "La Maison — Histoire, chef et équipe | Maison Aurèle, Lyon",
        "desc": ("Depuis 1929, sur les quais de la Saône : l'histoire de la Maison "
                 "Aurèle, le parcours du chef Kenji Tanaka et l'équipe qui fait "
                 "vivre la table chaque soir."),
        "og_type": "article",
        "img": "assets/img/lyon-saone.webp",
        "crumbs": [["La Maison", "maison.html"]],
    },
    "carte": {
        "title": "La Carte — Menus et vins | Maison Aurèle, Lyon",
        "desc": ("Menus Sillon et Carte blanche, carte de saison et carte des vins "
                 "de plus de 400 références : découvrez la table de la Maison "
                 "Aurèle, restaurant gastronomique à Lyon."),
        "og_type": "article",
        "img": "assets/img/plat-signe.webp",
        "crumbs": [["La Carte", "carte.html"]],
        "extra_schema": [{
            "@context": "https://schema.org",
            "@type": "Menu",
            "name": "Carte de la Maison Aurèle",
            "hasMenuSection": [
                {"@type": "MenuSection", "name": "Le Sillon (déjeuner, 5 temps)",
                 "offers": {"@type": "Offer", "price": "95", "priceCurrency": "EUR"}},
                {"@type": "MenuSection", "name": "Carte blanche (dîner, 8 temps)",
                 "offers": {"@type": "Offer", "price": "165", "priceCurrency": "EUR"}},
                {"@type": "MenuSection", "name": "La Table d'Aurèle (samedi midi)",
                 "offers": {"@type": "Offer", "price": "65", "priceCurrency": "EUR"}},
                {"@type": "MenuSection", "name": "À la carte",
                 "hasMenuItem": [
                     {"@type": "MenuItem", "name": "Huîtres de Doëlan n°3",
                      "description": "Mignonette au poivre de Timut, pain de seigle maison",
                      "offers": {"@type": "Offer", "price": "22", "priceCurrency": "EUR"}},
                     {"@type": "MenuItem", "name": "Turbot sauvage de ligne",
                      "description": "Beurre nacré aux algues, poireau brûlé",
                      "offers": {"@type": "Offer", "price": "58", "priceCurrency": "EUR"}},
                     {"@type": "MenuItem", "name": "Pigeonneau des Monts du Lyonnais",
                      "description": "Jus corsé, betterave fumée, cromesquis de sabot",
                      "offers": {"@type": "Offer", "price": "54", "priceCurrency": "EUR"}},
                     {"@type": "MenuItem", "name": "Le chocolat de Tain",
                      "description": "Ganache 70 % caramel au beurre demi-sel, glace malt",
                      "offers": {"@type": "Offer", "price": "17", "priceCurrency": "EUR"}}
                 ]},
                {"@type": "MenuSection", "name": "Carte des vins",
                 "description": "400 références vieillies en cave voûtée, 60 références au verre."}
            ]
        }],
    },
    "privatisation": {
        "title": "Privatisation, événements et bons cadeaux | Maison Aurèle",
        "desc": ("Salons privés et cave voûtée du XVIIᵉ siècle au cœur de Lyon : "
                 "déjeuners d'affaires, réceptions et mariages jusqu'à 36 convives. "
                 "Bons cadeaux valables 18 mois."),
        "og_type": "article",
        "img": "assets/img/salle.webp",
        "crumbs": [["Privatisation & bons cadeaux", "privatisation.html"]],
    },
    "galerie": {
        "title": "Galerie — La Maison en images | Maison Aurèle, Lyon",
        "desc": ("La salle, la cuisine, la cave et les assiettes de la Maison "
                 "Aurèle en images : galerie photographique du restaurant "
                 "gastronomique lyonnais."),
        "og_type": "article",
        "img": "assets/img/table-dressee.webp",
        "crumbs": [["Galerie", "galerie.html"]],
    },
    "reservation": {
        "title": "Réserver une table | Maison Aurèle, Lyon",
        "desc": ("Réservez votre table en ligne à la Maison Aurèle, Lyon : "
                 "déjeuner et dîner du mardi au samedi, confirmation par e-mail "
                 "sous 24 heures."),
        "og_type": "website",
        "img": "assets/img/salle-claire.webp",
        "crumbs": [["Réserver", "reservation.html"]],
    },
    "contact": {
        "title": "Contact et informations pratiques | Maison Aurèle, Lyon",
        "desc": ("Adresse, horaires, accès métro et parking : toutes les "
                 "informations pratiques pour venir à la Maison Aurèle, "
                 "17 quai Saint-Vincent, Lyon 1ᵉʳ. Écrivez-nous."),
        "og_type": "website",
        "img": "assets/img/lyon-saone.webp",
        "crumbs": [["Contact", "contact.html"]],
    },
    "mentions-legales": {
        "title": "Mentions légales | Maison Aurèle",
        "desc": "Mentions légales du site de la Maison Aurèle, restaurant fictif de démonstration réalisé par Matrice Studio.",
        "og_type": "article",
        "img": "og-image.jpg",
        "crumbs": [["Mentions légales", "mentions-legales.html"]],
        "plain": True,
    },
    "confidentialite": {
        "title": "Politique de confidentialité | Maison Aurèle",
        "desc": "Politique de confidentialité du site de la Maison Aurèle : données collectées, durée de conservation, droits des personnes (RGPD).",
        "og_type": "article",
        "img": "og-image.jpg",
        "crumbs": [["Politique de confidentialité", "confidentialite.html"]],
        "plain": True,
    },
    "plan-du-site": {
        "title": "Plan du site | Maison Aurèle",
        "desc": "Plan du site de la Maison Aurèle : toutes les pages du restaurant, de la carte à la réservation en ligne.",
        "og_type": "article",
        "img": "og-image.jpg",
        "crumbs": [["Plan du site", "plan-du-site.html"]],
        "plain": True,
    },
    "404": {
        "title": "Page introuvable (404) | Maison Aurèle",
        "desc": "La page que vous cherchez n'existe pas. Retournez à l'accueil de la Maison Aurèle, restaurant gastronomique à Lyon.",
        "og_type": "website",
        "img": "og-image.jpg",
        "crumbs": [],
        "plain": True,
    },
}

HEAD_TMPL = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="generator" content="Matrice Studio">
<link rel="canonical" href="{base}{canon}">
<meta name="theme-color" content="#14100D">
<meta property="og:site_name" content="Maison Aurèle">
<meta property="og:type" content="{og_type}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{base}{canon}">
<meta property="og:image" content="{base}{img}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="fr_FR">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{base}{img}">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="icon" href="favicon-32.png" sizes="32x32" type="image/png">
<link rel="icon" href="favicon.ico" sizes="any">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="manifest" href="site.webmanifest">
<link rel="preload" href="assets/fonts/cormorant-normal-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/montserrat-normal-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/css/main.css">
{schema}
</head>
<body class="{body_class}">
"""

PAGE_HERO_TMPL = """<section class="page-hero on-dark{hero_cls}">
  {bg}
  <div class="container">
    <nav class="breadcrumbs" aria-label="Fil d'Ariane">
      <a href="index.html">Accueil</a>
      {sep}<span aria-current="page">{crumb}</span>
    </nav>
    <p class="eyebrow">{eyebrow}</p>
    <h1 class="display-lg reveal">{h1}</h1>
    {sub}
  </div>
</section>
"""

def picture(name, alt, cls="", eager=False, sizes=None):
    w_attr = ' width="1920" height="1280"' if name == "hero-accueil" else ""
    loading = ' fetchpriority="high"' if eager else ' loading="lazy"'
    dim = ""
    if name in DIMS and not eager:
        dim = DIMS[name]
    return ('<picture><source type="image/webp" srcset="assets/img/{n}.webp">'
            '<img src="assets/img/{n}.jpg" alt="{alt}"{dim}{load}{cls}>'
            '</picture>').format(n=name, alt=alt, dim=dim, load=loading,
                                 cls=(' class="%s"' % cls) if cls else "")

DIMS = {
    "lyon-saone": ' width="1600" height="1200"',
    "salle": ' width="1600" height="1067"',
    "salle-claire": ' width="1400" height="933"',
    "cuisine": ' width="909" height="1400"',
    "cuisine-passe": ' width="1400" height="933"',
    "chef-portrait": ' width="1200" height="1200"',
    "plat-signe": ' width="1050" height="1400"',
    "plat-atelier": ' width="933" height="1400"',
    "dessert-chocolat": ' width="1120" height="1400"',
    "dessert-framboise": ' width="1120" height="1400"',
    "vin-verres": ' width="1400" height="933"',
    "vin-cave": ' width="1400" height="933"',
    "vin-degustation": ' width="1400" height="932"',
    "vignoble": ' width="1600" height="726"',
    "table-dressee": ' width="1400" height="933"',
    "ambiance-bougie": ' width="1400" height="933"',
    "terrasse": ' width="1600" height="1200"',
    "bar": ' width="1050" height="1400"',
}

def build_page(slug, meta, fragment):
    canon = "index.html" if slug == "index" else slug + ".html"
    schema_extra = []
    if meta["crumbs"]:
        items = [{"@type": "ListItem", "position": 1, "name": "Accueil", "item": BASE}]
        for i, (name, href) in enumerate(meta["crumbs"], start=2):
            items.append({"@type": "ListItem", "position": i, "name": name,
                          "item": BASE + href})
        schema_extra.append({"@context": "https://schema.org", "@type": "BreadcrumbList",
                             "itemListElement": items})
    schemas = [{"@context": "https://schema.org", "@graph": [SCHEMA_RESTAURANT, SCHEMA_ORG]}]
    schemas += schema_extra
    schemas += meta.get("extra_schema", [])
    schema_html = "\n".join(
        '<script type="application/ld+json">%s</script>' % json.dumps(s, ensure_ascii=False)
        for s in schemas)

    html = HEAD_TMPL.format(title=meta["title"], desc=meta["desc"], base=BASE,
                            canon=canon, og_type=meta["og_type"], img=meta["img"],
                            schema=schema_html,
                            body_class=meta.get("body_class", ""))
    html += header_html
    # gestion aria-current
    html = html.replace('data-page="%s"' % slug,
                        'data-page="%s" aria-current="page"' % slug)
    html += '<main id="contenu">\n' + fragment + '\n</main>\n'
    html += footer_html
    html += '\n<script src="assets/js/main.js" defer></script>\n</body>\n</html>\n'
    out = ROOT / ("index.html" if slug == "index" else slug + ".html")
    out.write_text(html, encoding="utf-8")
    print("OK", out.name, len(html))

def page_hero(slug, eyebrow, h1, sub_html, bg_name, bg_alt):
    bg = ('<img class="page-hero__bg" src="assets/img/%s.jpg" alt="%s" width="1600" '
          'height="1200" fetchpriority="high">' % (bg_name, bg_alt)) if bg_name else ""
    crumbs = PAGES[slug]["crumbs"]
    crumb = crumbs[0][0] if crumbs else ""
    return PAGE_HERO_TMPL.format(hero_cls="", bg=bg, crumb=crumb,
                                 sep='<span class="sep" aria-hidden="true">/</span>' if crumbs else "",
                                 eyebrow=eyebrow, h1=h1, sub=sub_html)

if __name__ == "__main__":
    header_html = (ROOT / "templates/header.html").read_text(encoding="utf-8")
    footer_html = (ROOT / "templates/footer.html").read_text(encoding="utf-8")
    pages_dir = ROOT / "pages"
    for f in sorted(pages_dir.glob("*.html")):
        slug = f.stem
        if slug not in PAGES:
            print("IGNORÉ (pas de meta):", slug)
            continue
        frag = f.read_text(encoding="utf-8")
        # placeholder PICTURE() côté fragment
        frag = IMG_TOKEN_RE.sub(lambda m: picture(m.group(1), m.group(2), m.group(3) or "",
                                                  eager=m.group(4) == "eager"), frag)
        build_page(slug, PAGES[slug], frag)
