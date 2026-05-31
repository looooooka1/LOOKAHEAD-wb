# -*- coding: utf-8 -*-
import os, html, re

PAGES = [
    ("mentions-legales.txt", "mentions-legales.html", "Mentions légales"),
    ("cgv.txt", "cgv.html", "Conditions générales de vente"),
    ("cgu.txt", "cgu.html", "Conditions générales d'utilisation"),
    ("confidentialite.txt", "confidentialite.html", "Politique de confidentialité"),
    ("cookies.txt", "cookies.html", "Politique de cookies"),
]

HEAD = '''<!doctype html>
<html lang="fr">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title} | Lookahead</title>
  <meta name="description" content="{title} du site lookahead.fr." />
  <meta name="robots" content="index, follow" />
  <link rel="icon" type="image/svg+xml" href="assets/img/favicon.svg" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Plus+Jakarta+Sans:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="assets/css/styles.css" />
</head>
<body>
  <header class="nav is-scrolled">
    <div class="nav__inner">
      <a href="index.html" class="nav__logo">Look<span>ahead</span></a>
      <div class="nav__actions">
        <a href="index.html" class="btn btn--outline">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
          Retour au site
        </a>
      </div>
    </div>
  </header>

  <main class="legal-hero">
    <div class="container">
      <div class="legal">
        <a href="index.html" class="legal-back">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
          Retour à l'accueil
        </a>
        <h1>{title}</h1>
'''

FOOT = '''      </div>
    </div>
  </main>

  <footer class="footer">
    <div class="container">
      <div class="footer__bottom" style="border:0;padding-top:0;">
        <span>© <span data-year>2025</span> Lookahead. Tous droits réservés.</span>
        <div class="footer__legal">
          <a href="mentions-legales.html">Mentions légales</a>
          <a href="cgv.html">CGV</a>
          <a href="cgu.html">CGU</a>
          <a href="confidentialite.html">Confidentialité</a>
          <a href="cookies.html">Cookies</a>
        </div>
      </div>
    </div>
  </footer>
  <script src="assets/js/main.js"></script>
</body>
</html>
'''

def is_h2(line):
    if re.match(r'^(ARTICLE\s+\d+|PRÉAMBULE|PREAMBULE)', line): return True
    if re.match(r'^\d+\.\s', line) and line.upper() == line: return True
    # ALLCAPS title line
    letters = re.sub(r'[^A-Za-zÀ-ÿ]', '', line)
    if len(letters) >= 4 and letters == letters.upper() and not line.endswith('.') and len(line) < 80:
        return True
    return False

def is_h3(line):
    if line.endswith('.') or line.endswith(':') or len(line) > 70: return False
    if re.match(r'^(Par |Adresse|Email|Site|Téléphone|Médiateur|Version|Coordonnées)', line): return False
    # Title-case short heading, no trailing punctuation
    if line[0:1].isupper() and ' ' in line and len(line.split()) <= 9:
        return True
    return False

def linkify(s):
    s = re.sub(r'(luka@lookahead\.fr|cm2c@cm2c\.net)', r'<a href="mailto:\1">\1</a>', s)
    s = re.sub(r'(?<!@)\b(www\.[a-z0-9.\-]+\.[a-z]{2,})', r'<a href="https://\1" target="_blank" rel="noopener">\1</a>', s)
    return s

for src, out, title in PAGES:
    with open(os.path.join("_legal_src", src), encoding="utf-8") as f:
        lines = [l.rstrip() for l in f.read().split("\n")]
    body = []
    # first non-empty line(s) = dates -> .updated
    i = 0
    dates = []
    while i < len(lines) and lines[i].strip().startswith(("Date d'entrée", "Dernière mise")):
        dates.append(lines[i].strip()); i += 1
    if dates:
        body.append('<p class="updated">' + html.escape(" — ".join(dates)) + '</p>')
    for line in lines[i:]:
        t = line.strip()
        if not t: continue
        esc = linkify(html.escape(t))
        if is_h2(t): body.append("<h2>" + esc + "</h2>")
        elif is_h3(t): body.append("<h3>" + esc + "</h3>")
        else: body.append("<p>" + esc + "</p>")
    with open(out, "w", encoding="utf-8") as f:
        f.write(HEAD.format(title=html.escape(title)) + "\n".join(body) + "\n" + FOOT)
    print("OK ->", out)
