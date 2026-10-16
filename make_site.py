"""Build the searchable Studio Book web app.
   python3 make_site.py repo <dir>      -> index.html + img/ + PDF for GitHub Pages
   python3 make_site.py artifact <file> -> one self-contained page (images inlined)"""
import json, os, sys, base64, shutil
HERE = os.path.dirname(os.path.abspath(__file__))
mode, dest = sys.argv[1], sys.argv[2]
SITE = "/home/claude/toad-site"
book = json.load(open(os.path.join(SITE, "book.json")))
tpl = open(os.path.join(HERE, "site_template.html")).read()

def data_uri(rel):
    return "data:image/png;base64," + base64.b64encode(open(os.path.join(SITE, rel), "rb").read()).decode()

book["cover"] = "img/cover.png"
if mode == "artifact":
    book["cover"] = data_uri("img/cover.png")
    for s in book["sections"]:
        for b in s["blocks"]:
            if b["type"] == "img":
                b["src"] = data_uri(b["src"])
    page = tpl.replace("<!--PDFLINK-->", "")
else:
    page = tpl.replace("<!--PDFLINK-->", '<a class="btn" href="Studio_Book_Complete.pdf" target="_blank" rel="noopener">PDF</a>')
data = json.dumps(book, ensure_ascii=False).replace("</", "<\\/")
page = page.replace("/*BOOK*/", data)

if mode == "artifact":
    open(dest, "w").write(page)
else:
    os.makedirs(dest, exist_ok=True)
    head, rest = page.split("<style>", 1)
    full = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
            '<meta name="description" content="Toad Studio: the searchable studio book for a Mackie 24-8 home studio.">\n'
            + head + "<style>\n:root { padding-top: env(safe-area-inset-top, 0px); padding-bottom: env(safe-area-inset-bottom, 0px) }\nbody { margin: 0 }\nimg { max-width: 100% }\n[hidden] { display: none !important }\n"
            + rest.replace("</style>", "</style>\n</head>\n<body>", 1) + "\n</body>\n</html>\n")
    open(os.path.join(dest, "index.html"), "w").write(full)
    if os.path.exists(os.path.join(dest, "img")):
        shutil.rmtree(os.path.join(dest, "img"))
    shutil.copytree(os.path.join(SITE, "img"), os.path.join(dest, "img"))
    shutil.copy("/mnt/user-data/outputs/Studio_Book_Complete.pdf", dest)
print("wrote", dest, os.path.getsize(dest if mode == "artifact" else os.path.join(dest, "index.html")))
