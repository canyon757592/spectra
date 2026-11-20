"""Ajoute ?v=<empreinte> à style.css et app.js dans toutes les pages HTML.
À lancer avant chaque publication : python3 tools/stamp.py
Le navigateur est ainsi obligé de recharger un fichier modifié, même s'il l'avait gardé en mémoire."""
import hashlib, re, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
hashes = {n: hashlib.sha1((root / n).read_bytes()).hexdigest()[:8] for n in ("style.css", "app.js")}
total = 0
for page in sorted(root.glob("*.html")):
    html = page.read_text(encoding="utf-8")
    for name, h in hashes.items():
        pat = re.compile(r'((?:href|src)="/)' + re.escape(name) + r'(?:\?v=[0-9a-f]+)?(")')
        html, n = pat.subn(r'\g<1>' + name + "?v=" + h + r'\g<2>', html)
        total += n
    page.write_text(html, encoding="utf-8")
print("empreintes mises à jour :", hashes, "(", total, "références )")
