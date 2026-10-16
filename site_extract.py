"""Turn the Studio Book's section sources into book.json + diagram images for the searchable web app."""
import json, os, re, subprocess, sys, html
sys.path.insert(0, os.path.dirname(__file__))
from common import *
from reportlab.platypus import Table, KeepTogether, Paragraph
import summary, setupmap, gain, lists, needs, guide, comp, eq, power, monitor, tascam, reaper, flstudio, protools, garageband, mics, altsetups
from pypdf import PdfReader

SITE = sys.argv[1] if len(sys.argv) > 1 else "/home/claude/toad-site"
IMG = os.path.join(SITE, "img")
os.makedirs(IMG, exist_ok=True)

def clean(t):
    t = t.replace("&bull;&nbsp;&nbsp;", "", 1) if t.startswith("&bull;&nbsp;&nbsp;") else t
    t = re.sub(r"<font[^>]*>|</font>", "", t)
    t = t.replace("<br/>", "<br>")
    return t.strip()

def is_bullet(p):
    return p.text.startswith("&bull;&nbsp;&nbsp;")

def cell_text(v):
    if isinstance(v, Paragraph):
        return clean(v.text)
    if isinstance(v, (list, tuple)):
        return " ".join(cell_text(x) for x in v)
    return "" if v is None else html.escape(str(v))

def walk(flows, out):
    for f in flows:
        if isinstance(f, KeepTogether):
            walk(f._content, out)
        elif isinstance(f, Paragraph):
            sn = f.style.name
            if sn == 't':
                continue
            if is_bullet(f):
                if out and out[-1]["type"] == "ul":
                    out[-1]["items"].append(clean(f.text))
                else:
                    out.append({"type": "ul", "items": [clean(f.text)]})
            elif sn == 'h':
                out.append({"type": "h", "text": clean(f.text)})
            elif sn == 's':
                out.append({"type": "lead", "text": clean(f.text)})
            elif sn == 'n':
                out.append({"type": "note", "text": clean(f.text)})
            else:
                out.append({"type": "p", "text": clean(f.text)})
        elif isinstance(f, Table):
            cv = f._cellvalues
            if cv and cv[0] and isinstance(cv[0][0], eq.Strip):
                rows = [s.row for r in cv for s in r if isinstance(s, eq.Strip)]
                out.append({"type": "eq", "rows": [list(r[:10]) for r in rows]})
                continue
            rows = [[cell_text(v) for v in r] for r in cv]
            if len(rows[0]) == 2 and rows[0][1] == "" and len(rows) > 1:  # a gear card
                out.append({"type": "card", "title": rows[0][0], "fields": rows[1:]})
                continue
            hdr = any(isinstance(v, Paragraph) and v.style.name == 'hd' for v in cv[0]) if cv else False
            if not hdr:  # plain_tbl tables use bold first rows
                hdr = len(cv) > 1 and all(isinstance(v, Paragraph) and v.style.name == 'cb' for v in cv[0] if isinstance(v, Paragraph))
            out.append({"type": "table", "head": rows[0] if hdr else None, "rows": rows[1:] if hdr else rows})
    return out

def pdf_pages_to_png(pdf, first, last, stem):
    subprocess.run(["pdftoppm", "-r", "110", "-f", str(first), "-l", str(last), "-png", pdf, os.path.join(IMG, stem)], check=True)
    files = sorted(x for x in os.listdir(IMG) if x.startswith(stem + "-"))
    r = PdfReader(pdf)
    res = []
    for i, fn in enumerate(files):
        txt = r.pages[first - 1 + i].extract_text() or ""
        lines = [l.strip() for l in txt.splitlines() if l.strip() and "TOAD STUDIO" not in l]
        res.append({"type": "img", "src": "img/" + fn, "title": lines[0] if lines else stem, "alt": " ".join(lines)})
    return res

for f in os.listdir(IMG):
    os.remove(os.path.join(IMG, f))

vstory, _ = lists.values()
SECTIONS = [
    ("summary", "Studio Build Summary", "Everything decided, capacity, aux sends, deals, shopping totals, open items", "Overview", summary.story()),
    ("setup-map", "Studio Setup Map", "Rack order, 24-channel map, four snakes, clock, wiring, cable list", "Setup", setupmap.story()),
    ("connection-diagram", "Studio Connection Diagram", "Signal flow; power, instrument chains and snake colors", "Setup", "diagram:Studio_Connection_Diagram.pdf"),
    ("monitoring", "Monitoring: Outputs and Routes", "Every console output, monitor and phones sections, talkback, setups per session", "Setup", monitor.story()),
    ("power", "Power: Start-Up and Shutdown", "Furman outlets, switch-on order, shutdown order", "Setup", power.story()),
    ("gain", "Gain Staging Guide", "Setting levels on every channel and piece of gear", "Sound", gain.story()),
    ("compression", "Setting Compression Levels", "Dialing in the 76-KT (and the dbx alternatives)", "Sound", comp.story()),
    ("eq", "EQ Settings, Channel by Channel", "What each EQ knob does, and a starting point for all 24 channels", "Sound", eq.story()),
    ("mics", "Mic Placement", "Where each mic goes, how far and aimed at what", "Sound", mics.story()),
    ("tascam", "Tascam 246: Setup and Recording", "Connections, levels, recording passes, bouncing", "Recording", tascam.story()),
    ("reaper", "Reaper Setup", "Driver, 16 ins and outs, the track template, playback, MIDI", "Recording", reaper.story()),
    ("fl-studio", "FL Studio Setup", "The same studio in FL Studio", "Recording", flstudio.story()),
    ("pro-tools", "Pro Tools Setup", "The same studio in Pro Tools", "Recording", protools.story()),
    ("garageband", "GarageBand Setup", "The same studio on a Mac in GarageBand", "Recording", garageband.story()),
    ("panning", "Panning Guide", "Console pans for tracking; Reaper pans for the mix", "Sound", "diagram:Studio_Panning_Guide.pdf"),
    ("alternate-setups", "Alternate Setups", "A: all direct outs; B: stereo playback on two outputs", "Setup", altsetups.story()),
    ("equipment", "Studio Equipment List", "Everything you own", "Gear", lists.equipment()),
    ("needs", "Studio Gear Needs List", "What's still missing, with prices", "Gear", needs.story()),
    ("goal", "Goal Studio Diagram", "Where every planned purchase plugs in", "Gear", "diagram:Studio_Goal_Diagram.pdf"),
    ("values", "Studio Equipment Values", "Rough used-market value, with totals", "Gear", vstory),
    ("how-it-works", "How Each Piece Works", "What each piece of gear does and how it connects", "Gear", guide.story()),
]

book = {"title": "TOAD STUDIO", "subtitle": "The Studio Book", "revised": "October 15, 2026", "sections": []}
for sid, t, desc, group, src in SECTIONS:
    if isinstance(src, str):
        pdf = OUT + src.split(":", 1)[1]
        n = len(PdfReader(pdf).pages)
        blocks = pdf_pages_to_png(pdf, 1, n, sid)
        if sid == "panning":
            blocks.append({"type": "h", "text": "Console pan map (text version)"})
            blocks.append({"type": "table", "head": ["Ch", "Source", "Pan", "Records to"],
                           "rows": [[r[0], r[1], r[3], r[5]] for r in CH]})
    else:
        blocks = walk(src, [])
        if sid == "alternate-setups":
            pdf = OUT + "Studio_Alternate_Setups.pdf"
            n = len(PdfReader(pdf).pages)
            blocks.append({"type": "h", "text": "Alternate Setups: Connection Diagram"})
            blocks += pdf_pages_to_png(pdf, n, n, sid)
    book["sections"].append({"id": sid, "title": t, "desc": desc, "group": group, "blocks": blocks})

subprocess.run(["pdftoppm", "-r", "90", "-png", "-singlefile", "/home/claude/studio/title.pdf", os.path.join(IMG, "cover")], check=True)
with open(os.path.join(SITE, "book.json"), "w") as fh:
    json.dump(book, fh, ensure_ascii=False)
print("sections", len(book["sections"]), "blocks", sum(len(s["blocks"]) for s in book["sections"]))
print(sorted(os.listdir(IMG)))
