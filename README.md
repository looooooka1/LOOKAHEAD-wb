# Lookahead — Site web

Site vitrine statique (HTML / CSS / JavaScript) pour Lookahead : agents IA vocaux, chatbots et automatisation pour PME. Aucune dépendance, aucun build. Publiable tel quel sur GitHub Pages.

## Structure du projet

```
lookahead-site/
├── index.html                 # Page d'accueil (toutes les sections)
├── reserver.html              # Page de réservation (widget de booking)
├── mentions-legales.html      # Mentions légales
├── cgv.html                   # Conditions générales de vente
├── cgu.html                   # Conditions générales d'utilisation
├── confidentialite.html       # Politique de confidentialité
├── cookies.html               # Politique de cookies
├── .nojekyll                  # Désactive le traitement Jekyll de GitHub Pages
├── assets/
│   ├── css/styles.css         # Toute la feuille de style
│   ├── js/main.js             # Toutes les animations et interactions
│   ├── img/favicon.svg        # Favicon
│   └── fonts/                 # (polices chargées via Google Fonts)
└── _legal_src/                # Sources texte des pages légales (pour ré-édition)
    └── _build_legal.py        # Générateur des pages légales (optionnel)
```

> Les polices (Plus Jakarta Sans + Instrument Serif) sont chargées via Google Fonts
> (balise `<link>` dans chaque page). Aucune installation requise.

## Tester en local

Double-cliquez sur `index.html`, ou lancez un petit serveur :

```bash
cd lookahead-site
python3 -m http.server 8000
# puis ouvrez http://localhost:8000
```

## Publier sur GitHub Pages

1. Créez un dépôt sur GitHub (ex. `lookahead-site`).
2. Depuis le dossier du projet :

   ```bash
   cd lookahead-site
   git init
   git add .
   git commit -m "Site Lookahead"
   git branch -M main
   git remote add origin https://github.com/VOTRE-COMPTE/lookahead-site.git
   git push -u origin main
   ```

3. Sur GitHub : **Settings → Pages → Build and deployment**
   - Source : **Deploy from a branch**
   - Branch : **main** / dossier **/ (root)** → **Save**
4. Le site est en ligne sous quelques minutes à l'adresse
   `https://VOTRE-COMPTE.github.io/lookahead-site/`.

### Domaine personnalisé (lookahead.fr)

Dans **Settings → Pages → Custom domain**, saisissez `lookahead.fr`, puis
chez votre registrar ajoutez un enregistrement CNAME (ou les A records GitHub
Pages) pointant vers GitHub. Un fichier `CNAME` sera créé automatiquement.

## Modifier le contenu

- **Textes / sections** : `index.html`
- **Couleurs, espacements, styles** : `assets/css/styles.css` (variables en haut du fichier)
- **Animations (démos, apparitions)** : `assets/js/main.js`
- **Pages légales** : éditez les `.txt` dans `_legal_src/` puis relancez
  `python3 _build_legal.py` pour régénérer les pages HTML.
- **Lien de réservation** : iframe dans `reserver.html`.

## Couleur d'accent

`#4B49EC` (définie via la variable CSS `--accent` dans `styles.css`).
