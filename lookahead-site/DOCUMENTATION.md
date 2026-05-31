# Documentation du site Lookahead

Cette documentation décrit chaque compartiment du site et les modifications intégrées.

---

## PARTIE 1 — ASSETS (HTML / CSS / JS / polices / images)

### 1.1 HTML (pages)
| Fichier | Rôle |
|--------|------|
| `index.html` | Page d'accueil : nav, hero, avant/après, méthode (timeline), services, voicebot, chatbot, automatisation, pourquoi nous, résultats, tarifs + comparatif + message intuition, lettre du fondateur, témoignages, CTA finale, footer. |
| `reserver.html` | Page de prise de rendez-vous, contient le widget de booking (iframe `appli.lookahead.fr`). |
| `mentions-legales.html`, `cgv.html`, `cgu.html`, `confidentialite.html`, `cookies.html` | Pages légales, générées à partir des sources texte. |

### 1.2 CSS — `assets/css/styles.css`
Une seule feuille de style pour tout le site. Organisée en blocs :
tokens (variables de couleurs, rayons, ombres, polices), reset, layout,
typographie, éléments « stylo / journal », boutons, navigation, hero, cartes,
avant/après, timeline, sections service, démos (voice / chat / automation),
pourquoi nous, résultats, tarifs, tableau comparatif, lettre, témoignages,
CTA, footer, animations, pages légales, page réservation, responsive,
préférence de mouvement réduit.

Variable d'accent : `--accent: #4b49ec;` (en haut du fichier).

### 1.3 JavaScript — `assets/js/main.js`
Gère, sans aucune dépendance : la navigation (état au scroll + menu mobile),
les apparitions au scroll (`.reveal`), les blocs qui apparaissent/disparaissent
selon le sens du scroll (`.fade`), le remplissage de la timeline, les trois
démos animées (voicebot mot par mot, chatbot, automatisation) **avec pause
automatique hors écran**, et l'année du footer.

### 1.4 Polices (`assets/fonts/`)
Chargées via Google Fonts (`<link>` dans chaque page) :
- **Plus Jakarta Sans** : titres et textes.
- **Instrument Serif** (italique) : mots mis en avant.
Le dossier `assets/fonts/` est prévu si vous souhaitez héberger les polices en
local (téléchargez les `.woff2` puis remplacez le `<link>` par un `@font-face`).

### 1.5 Images (`assets/img/`)
- `favicon.svg` : favicon (carré noir, « L » violet).
Le site n'utilise pas de photos : logos en texte, avatars en initiales,
illustrations en SVG inline. Aucun fichier image lourd à héberger.

---

## PARTIE 2 — INDEX (page d'accueil) et navigation

`index.html` est le point d'entrée. La navigation (en-tête flottant) et le
pied de page mènent vers toutes les autres pages :

- **Voicebots / Chatbots / Automatisations / Tarifs / À propos** : ancres
  internes vers les sections de l'accueil.
- **Diagnostic gratuit** (nav, hero, tarifs, sur-mesure, CTA finale,
  « Réserver mon diagnostic », « Nous appeler ») : vers `reserver.html`.
- **Footer / Légal** : vers les 5 pages légales.
- Chaque page secondaire possède un bouton **« Retour au site »** et un lien
  **« Retour à l'accueil »** pour revenir à `index.html`.

---

## Modifications intégrées (par rapport à la version précédente)

1. **Fluidité / anti-bug** : toutes les animations utilisent `transform` et
   `opacity`, avec `will-change`. Les démos se mettent en pause quand elles ne
   sont plus visibles à l'écran (IntersectionObserver).
2. **Mots mis en avant agrandis** : le style `.accent` (police Instrument Serif
   italique) est passé à `font-size: 1.06em` avec `line-height` ajusté, pour ne
   plus paraître plus petit que le titre.
3. **Démos sans décalage de page** : les fenêtres de conversation (voicebot et
   chatbot) ont une **hauteur fixe** avec défilement interne ; les nouveaux
   messages apparaissent en bas, les anciens disparaissent vers le haut. Le
   reste de la page ne bouge plus jamais.
4. **Éléments « stylo / journal »** : soulignement tracé main (« sans vous »),
   cercle au stylo (« différents »), surligneur (« L'IA n'est pas une fin en
   soi »), styles `.rature` disponibles pour barrer un mot.
5. **CTA → réservation** : tous les boutons de diagnostic mènent au widget de
   booking (`reserver.html`).
6. **Liens** : LinkedIn → `linkedin.com/in/luka-gallagher-lookahead`,
   email → `luka@lookahead.fr`.
7. **Pages légales** : mentions légales, CGV, CGU, confidentialité, cookies,
   chacune sur une page dédiée, cohérente avec le design, avec retour arrière.
EOF
