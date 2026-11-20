# Spectra — site public (spectracarte.com)

Site statique hébergé sur Cloudflare Pages (projet `spectra`, déploiement automatique à chaque envoi sur `main`).

## Fichiers
- `index.html` : page d'accueil (contenu des sections déjà écrit dans le HTML, pour Google et la vitesse).
- `app.js` : tout le comportement (questionnaire, compte, paiement, carte). Aucun script dans les pages HTML.
- `style.css` : styles. `fonts/` : polices hébergées ici. `vendor/` : Leaflet et supabase-js hébergés ici (versions fixées dans le nom du fichier).
- `charte.html`, `cgv.html`, `mentions-legales.html`, `confidentialite.html` : pages légales, chacune avec sa propre adresse.
- `_headers` : en-têtes de sécurité (politique de contenu stricte) et durées de cache. `404.html`, `robots.txt`, `sitemap.xml`, `manifest.webmanifest`, icônes.

## Avant chaque publication
1. `python3 tools/stamp.py` (ajoute une empreinte aux fichiers `style.css` et `app.js` pour forcer le rechargement).
2. Commit + push sur `main`.

## Règles à garder
- Aucun secret dans ce dépôt (la clé Supabase « publishable » est publique par conception ; les clés Stripe et Resend n'y vont jamais).
- Si tu ajoutes un service externe (script, police, image, API), il doit aussi être autorisé dans `_headers` (Content-Security-Policy), sinon le navigateur le bloque.
- Le paiement n'est proposé qu'à une personne connectée : le lien Stripe contient `client_reference_id` (identifiant du compte), que le webhook `stripe-webhook` utilise pour activer l'accès.
