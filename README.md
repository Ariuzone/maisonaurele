# Maison Aurèle — démonstration de site vitrine

Site vitrine fictif d'un restaurant gastronomique lyonnais, réalisé par
**Matrice Studio** comme démonstration de savoir-faire.

- **Établissement** : Maison Aurèle — restaurant gastronomique fictif, Lyon
- **Langue** : français
- **Contact affiché** : matricestudio@protonmail.com (adresse de Matrice Studio)
- **Aucun numéro de téléphone** n'est affiché (volontairement omis, plage
  fictive non utilisable en France).

## Consulter le site

Aucun backend ni build n'est requis pour consulter le site : ouvrez
simplement `index.html` dans un navigateur, ou servez le dossier avec
n'importe quel serveur statique :

```bash
python -m http.server 8080
# puis http://localhost:8080/
```

## Structure

```
index.html … 404.html   Pages HTML générées (livrables)
pages/*.html            Fragments de contenu (source)
templates/              En-tête et pied de page partagés (source)
build.py                Générateur : assemble pages/ + templates/ → HTML
assets/css/main.css     Design system complet (jetons, composants)
assets/js/main.js       Interactions (nav, révélations, lightbox, formulaires)
assets/img/             Photos optimisées (WebP + JPG)
assets/fonts/           Polices locales (Cormorant, Montserrat, sous-ensemble latin)
assets/icons/           Logo SVG et icônes
favicon.*  site.webmanifest  robots.txt  sitemap.xml  og-image.jpg
SOURCES.md              Sources et licences des ressources tierces
```

Après modification d'un fragment (`pages/*.html`) ou d'un partiel, régénérer :

```bash
python build.py
```

## Notes techniques

- **Performance** : polices locales préchargées, images redimensionnées et
  servies en WebP avec repli JPG (`<picture>`), chargement différé sous la
  ligne de flottaison, dimensions d'images déclarées (CLS maîtrisé).
- **Accessibilité** : lien d'évitement, navigation clavier, `aria-current`,
  focus visible, contrastes vérifiés (WCAG AA), `prefers-reduced-motion`
  respecté, lightbox en `<dialog>` accessible, formulaires avec erreurs
  explicites et zones `aria-live`.
- **SEO** : `lang="fr"`, titres et méta descriptions uniques, canoniques,
  Open Graph + Twitter Card, données structurées Schema.org (Restaurant,
  Menu, BreadcrumbList, Organization), sitemap.xml, robots.txt.
- **Formulaires** : validation côté interface uniquement (aucun backend).
  Le formulaire de contact pré-remplit un `mailto:`.

© 2026 Matrice Studio. Tous droits réservés.
