# SOURCES.md — Ressources tierces du site Maison Aurèle

Démonstration réalisée par Matrice Studio. Chaque ressource locale est listée
avec son URL d'origine pour faciliter son remplacement.

## Logotype & icônes

| Fichier local | Origine |
|---|---|
| `assets/icons/seal.svg`, `assets/icons/logo-full.svg`, `favicon.svg`, monogramme dans les en-têtes/pieds de page, tampon des bons cadeaux | **Création originale Matrice Studio** (monogramme « A » cerclé, dessiné pour cette démonstration) |

## Polices

| Fichier local | Origine | Licence |
|---|---|---|
| `assets/fonts/cormorant-normal-latin.woff2` | Google Fonts — https://fonts.google.com/specimen/Cormorant | SIL OFL 1.1 |
| `assets/fonts/cormorant-italic-latin.woff2` | idem | SIL OFL 1.1 |
| `assets/fonts/montserrat-normal-latin.woff2` | Google Fonts — https://fonts.google.com/specimen/Montserrat | SIL OFL 1.1 |

Sous-ensembles « latin » (variable fonts), servis en local.

## Photographies

Toutes les photographies sont téléchargées en local (`assets/img/`, formats
WebP + JPG optimisés). Auteurs non identifiés pour les images Unsplash ; les
URL CDN ci-dessous pointent vers l'original.

| Fichier local | URL d'origine | Source / auteur | Utilisé pour |
|---|---|---|---|
| `assets/img/hero-accueil.{webp,jpg}` | https://images.unsplash.com/photo-1414235077428-338989a2e8c0 | Unsplash | Héros accueil, galerie, image du lightbox |
| `assets/img/lyon-saone.{webp,jpg}` | https://commons.wikimedia.org/wiki/File:Lyon_-_Vue_sur_la_Sa%C3%B4ne_depuis_le_toit_d%27un_immeuble_mont%C3%A9e_de_l%27Observance_-_Aval_-_Le_soir.jpg | Wikimedia Commons — Romainbehar, licence CC0 | Héros « La Maison » et « Contact », accueil § infos |
| `assets/img/salle.{webp,jpg}` | https://images.unsplash.com/photo-1517248135467-4c7edcad34c4 | Unsplash | Héros privatisation, galerie |
| `assets/img/salle-claire.{webp,jpg}` | https://images.unsplash.com/photo-1552566626-52f8b828add9 | Unsplash | Héros réservation, privatisation, galerie |
| `assets/img/cuisine.{webp,jpg}` | https://images.unsplash.com/photo-1577219491135-ce391730fb2c | Unsplash | Galerie |
| `assets/img/cuisine-passe.{webp,jpg}` | https://images.unsplash.com/photo-1428515613728-6b4607e44363 | Unsplash | Galerie |
| `assets/img/chef-portrait.{webp,jpg}` | https://images.unsplash.com/photo-1583394293214-28ded15ee548 | Unsplash | Page La Maison (chef Kenji Tanaka) |
| `assets/img/plat-signe.{webp,jpg}` | https://images.unsplash.com/photo-1529193591184-b1d58069ecdd | Unsplash | Héros carte, galerie |
| `assets/img/plat-atelier.{webp,jpg}` | https://images.unsplash.com/photo-1551218808-94e220e084d2 | Unsplash | Accueil § cuisine |
| `assets/img/dessert-chocolat.{webp,jpg}` | https://images.unsplash.com/photo-1551024506-0bccd828d307 | Unsplash | Carte § desserts, galerie |
| `assets/img/dessert-framboise.{webp,jpg}` | https://images.unsplash.com/photo-1565958011703-44f9829ba187 | Unsplash | Privatisation § bons cadeaux |
| `assets/img/vin-verres.{webp,jpg}` | https://images.unsplash.com/photo-1510812431401-41d2bd2722f3 | Unsplash | Accueil § bons cadeaux |
| `assets/img/vin-cave.{webp,jpg}` | https://images.unsplash.com/photo-1528823872057-9c018a7a7553 | Unsplash | Carte § vins |
| `assets/img/vin-degustation.{webp,jpg}` | https://images.unsplash.com/photo-1568213816046-0ee1c42bd559 | Unsplash | Accueil teaser galerie, galerie |
| `assets/img/vignoble.{webp,jpg}` | https://images.unsplash.com/photo-1543418219-44e30b057fea | Unsplash (recadrée : ciel réduit) | Accueil teaser, galerie |
| `assets/img/table-dressee.{webp,jpg}` | https://images.unsplash.com/photo-1519690889869-e705e59f72e1 | Unsplash | Héros galerie, accueil teaser |
| `assets/img/ambiance-bougie.{webp,jpg}` | https://images.unsplash.com/photo-1533777857889-4be7c70b33f7 | Unsplash | Galerie |
| `assets/img/terrasse.{webp,jpg}` | https://images.unsplash.com/photo-1559339352-11d035aa65de | Unsplash | Galerie |
| `og-image.jpg` | composition générée localement (Pillow) à partir de `hero-accueil.jpg` + textes | — | Open Graph / Twitter Card |

## Outils utilisés (aucun embarqué dans le livrable)

- Pillow (Python) : recadrage, optimisation WebP/JPG, favicons PNG/ICO, og-image.
- npx playwright (CLI) : captures d'écran de vérification uniquement.
