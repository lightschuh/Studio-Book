import io, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from common import *
import summary, setupmap, gain, lists, needs, guide, diagrams, comp, eq, power, monitor, tascam, reaper, flstudio, protools, garageband, mics, altsetups, cover as coverpage
from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas as rl_canvas

files = []


def alt_book():
    txt = build("Studio_Alternate_Setups_text.pdf", "Alternate Setups", altsetups.story())
    dia = diagrams.make("Studio_Alternate_Setups_diagram.pdf", "Alternate Setups diagram", [diagrams.alt_diagram])
    w_ = PdfWriter()
    for p_ in (txt, dia):
        for pg_ in PdfReader(p_).pages:
            w_.add_page(pg_)
    out_ = OUT + "Studio_Alternate_Setups.pdf"
    with open(out_, "wb") as f_:
        w_.write(f_)
    for p_ in (txt, dia):
        os.remove(p_)
    return out_

files.append(("Studio Build Summary", "Everything decided, capacity, aux sends, deals, shopping totals, open items", build("Studio_Build_Summary.pdf", "Studio Build Summary", summary.story())))
files.append(("Studio Setup Map", "Rack order, 24-channel map, four snakes, clock, wiring, cable list", build("Studio_Setup_Map.pdf", "Studio Setup Map", setupmap.story())))
files.append(("Studio Connection Diagram", "Signal flow; power, instrument chains and snake colors", diagrams.make("Studio_Connection_Diagram.pdf", "Studio Connection Diagram", [diagrams.signal_flow, diagrams.power_page])))
files.append(("Monitoring: Outputs and Routes", "Every console output, the monitor and phones sections button by button, talkback, and setups per session", build("Studio_Monitoring_Guide.pdf", "Monitoring: Outputs and Routes", monitor.story())))
files.append(("Power: Start-Up and Shutdown", "Furman outlet assignments, the switch-on order, and the shutdown order", build("Studio_Power_Guide.pdf", "Power: Start-Up and Shutdown", power.story())))
files.append(("Gain Staging Guide", "Setting levels on every channel and piece of gear", build("Studio_Gain_Staging_Guide.pdf", "Gain Staging Guide", gain.story())))
files.append(("Setting Compression Levels", "Dialing in the 76-KT (and the dbx alternatives) on a channel insert", build("Studio_Compression_Guide.pdf", "Setting Compression Levels", comp.story())))
files.append(("EQ Settings, Channel by Channel", "What each EQ knob does, and a knob-by-knob starting point for all 24 channels", build("Studio_EQ_Guide.pdf", "EQ Settings", eq.story())))
files.append(("Mic Placement", "Where each mic goes, how far and aimed at what; bleed control; what room dimensions would change", build("Studio_Mic_Placement.pdf", "Mic Placement", mics.story())))
files.append(("Tascam 246: Setup and Recording", "Connections, the 246's own mixer, levels, recording passes, bouncing, four-track use", build("Studio_Tascam_Guide.pdf", "Tascam 246: Setup and Recording", tascam.story())))
files.append(("Reaper Setup", "Driver, 16 ins and outs, the track template, playback to the tape returns, MIDI, recording settings", build("Studio_Reaper_Guide.pdf", "Reaper Setup", reaper.story())))
files.append(("FL Studio Setup", "The same studio in FL Studio: Mixer insert inputs, Auto-map, the recording filter, outputs, MIDI", build("Studio_FL_Studio_Guide.pdf", "FL Studio Setup", flstudio.story())))
files.append(("Pro Tools Setup", "The same studio in Pro Tools: Playback Engine, the I/O Setup paths, the session template, recording, MIDI", build("Studio_Pro_Tools_Guide.pdf", "Pro Tools Setup", protools.story())))
files.append(("GarageBand Setup", "The same studio on a Mac in GarageBand: what it can and can't do, inputs, recording, playback", build("Studio_GarageBand_Guide.pdf", "GarageBand Setup", garageband.story())))
files.append(("Panning Guide", "Console pans for tracking; Reaper pans for the mix", diagrams.make("Studio_Panning_Guide.pdf", "Studio Panning Guide", [diagrams.console_pan, diagrams.reaper_pan])))
files.append(("Alternate Setups", "Other ways to wire the studio; A: all direct outs; B: stereo playback", alt_book()))
files.append(("Studio Equipment List", "Everything you own", build("Studio_Equipment_List.pdf", "Studio Equipment List", lists.equipment())))
files.append(("Studio Gear Needs List", "What's still missing, with prices", build("Studio_Gear_Needs_List.pdf", "Studio Gear Needs List", needs.story())))
files.append(("Goal Studio Diagram", "Prospective map: where every planned purchase plugs in", diagrams.make("Studio_Goal_Diagram.pdf", "Goal Studio Diagram", [diagrams.goal_studio])))
vstory, vtot = lists.values()
files.append(("Studio Equipment Values", "Rough used-market value, with totals", build("Studio_Equipment_Values.pdf", "Studio Equipment Values", vstory)))
files.append(("How Each Piece Works", f"What each piece of gear does and how it connects to the {B}", build("Mackie_24x8_Setup_Guide.pdf", "How Each Piece Works", guide.story())))

EXTRA_TOC_PAGES = 1
# ---- contents: each section's headings, located by scanning that section's own pages ----
from pypdf import PdfReader as _R

SUBS = {
    "Studio Build Summary": ["Documents", "The studio at a glance", "Capacity at a glance", "How channels get recorded", "Aux sends on the 24\u20228",
                             "16-track playback and clock (UMC1820 + ADA8200)", "Headphones and monitoring", "Submixers and personal monitor mixes",
                             "Gain staging rules", "Microphones", "Electronic percussion", "Rack additions and deals", "Connecting more gear to the 24\u20228",
                             "Marshall MG250DFX", "Effects and the Tame Impala sound", "Analog tape: Tascam 246 (once repaired)", "Garage PA", "Power",
                             "Shopping status", "Open items"],
    "Studio Setup Map": ["Rack order (top to bottom)", "Console channel and panning map", "Snake color order", "UMC1820 and ADA8200 (Reaper inputs and playback 9-16)",
                         "Aux sends on the 24\u20228", "PV6 submixer, electronic drums, drum machine and DJ", "Mic notes, acoustic guitar and pedalboard",
                         "Tascam 246 analog tape (once repaired)", "Capacity at a glance", "Open connections and planned additions", "Garage PA (STUDIO OUTPUT)",
                         "TSR-12 reverb", "Wiring the back", "Cables"],
    "Studio Connection Diagram": ["Signal flow", "Power, instrument chains and snake colors"],
    "Monitoring: Outputs and Routes": ["Every output the console has", "The MONITOR section, button by button", "The PHONES sections (Phones 1 and Phones 2)",
                                       "Talkback", "Setups for common sessions", "Rules that keep you out of trouble"],
    "Power: Start-Up and Shutdown": ["Where the Furman plugs in", "What the Furman M-8x2 gives you", "Which outlet gets what", "Two things that stay off the Furman's switched outlets",
                                     "Start-up, in order", "Shutdown, in reverse", "Details that matter"],
    "Gain Staging Guide": ["1. Zero everything first", "2. Set each channel (one at a time)", "3. Channel chart", "4. What ends up in the recording",
                           "5. Outboard and other gear", "6. Final checks"],
    "Setting Compression Levels": ["What the knobs do (76-KT)", "Wiring and gain structure", "Step by step", "Starting points",
                                   "If you buy the dbx alternative instead (266XS or 1066)", "Common mistakes"],
    "EQ Settings, Channel by Channel": ["The EQ section on each 24\u20228 channel, top to bottom", "Rules that matter more than any setting",
                                        "Channels 1-6", "Channels 7-12", "Channels 13-18", "Channels 19-24", "Why each channel is set this way"],
    "Mic Placement": ["Rules that cover everything", "Drums", "Amps", "Vocals, horn and acoustic", "The band tracking together: bleed control",
                      "Room-dependent decisions (what your measurements would change)"],
    "Tascam 246: Setup and Recording": ["What's on the 246 (so the rest makes sense)", "Connections", "Levels: the one thing that matters most",
                                        "246 channel settings", "Recording a pass to tape, step by step", "Using all four tracks", "Things that go wrong"],
    "Reaper Setup": ["1. Driver and audio device (once)", "2. Name the inputs and outputs (once)", "3. The track template (matches the console map)",
                     "4. Playback back to the console", "5. Recording settings", "6. MIDI for the e-drums and SamplePad",
                     "7. Mixing in Reaper: the plugins that replace outboard", "Troubleshooting"],
    "FL Studio Setup": ["What's the same as Reaper (don't redo it)", "1. Audio settings (once)", "2. Map the 16 inputs to Mixer inserts (once, then save as template)",
                        "3. Playback back to the console", "4. Recording a take", "5. MIDI for the e-drums and SamplePad",
                        "6. Mixing in FL: the plugins that replace outboard", "Reaper or FL Studio for this studio?", "Troubleshooting"],
    "Pro Tools Setup": ["What's the same as Reaper (don't redo it)", "1. Session and Playback Engine (once)", "2. I/O Setup (once, then export the settings)",
                        "3. The session template", "4. Recording", "5. MIDI for the e-drums and SamplePad", "6. Mixing: the plugins that replace outboard", "Troubleshooting"],
    "GarageBand Setup": ["What's different about GarageBand", "1. Preferences (once)", "2. Make the tracks and set their inputs", "3. The track layout",
                         "4. Recording", "5. Playback back to the console", "6. MIDI and the built-in instruments", "7. Mixing: the plugins that replace outboard",
                         "When to move up", "Troubleshooting"],
    "Panning Guide": ["Part 1: console pan knobs (tracking)", "Part 2: final mix in Reaper"],
    "Alternate Setups": ["How to use this chapter", "Alternate A: all direct outs", "Alternate A channel map", "Rewiring: what moves",
                         "Settings that change", "Recording more than 16 at once", "Main plan vs Alternate A", "How the direct outs behave on the 24\u20228",
                         "Where the computer comes back in", "Monitoring and latency", "The noise test (do this before deciding)", "Switching back",
                         "Alternate B: stereo playback (two outputs)", "Alternate B wiring", "Alternate B settings", "16-track vs stereo playback", "Moving to 16-track playback later",
                         "Alternate Setups: Connection Diagram"],
    "Studio Equipment List": ["Recording and mixing", "Power", "Monitoring", "PA / powered mixers", "Microphones and wireless", "Amplifiers", "Guitars",
                              "Keys, drums and electronics", "Pedalboard"],
    "Studio Gear Needs List": ["Studio essentials", "For the Tame Impala sound", "Monitoring and recording extras", "Only if needed",
                               "Compressor alternatives and gate option (not in the totals)", "Totals", "What's not on the list, and why"],
    "Goal Studio Diagram": ["Where every planned purchase plugs in"],
    "Studio Equipment Values": ["Console, rack and recording", "Amplifiers", "Guitars", "Synths, drums and electronics",
                                "Microphones, wireless and headphones", "Pedalboard", "Powered PA mixers", "Totals"],
    "How Each Piece Works": ["How it all connects", "Recording", "Monitoring", "Microphones", "Effects and processing", "Other gear",
                             "Power-up and power-down", "Quick gain-staging checklist"],
}

def find_page(path, heading, start, after=0):
    """Page (book numbering) where a heading first appears as its own line, searching from page index `after`."""
    pages = _R(path).pages
    for i in range(after, len(pages)):
        norm = lambda s: s.replace("\u2022", "").replace("\u00b7", "").replace("\x7f", "").replace(" ", "").lower()
        for line in (pages[i].extract_text() or "").splitlines():
            if norm(line.strip()) == norm(heading):
                return start + i, i
    return None, after

def build_contents():
    global total, title_page, cover
    entries = []  # (text, page, bold)
    p = 3 + EXTRA_TOC_PAGES
    for t, d, path in files:
        n = len(_R(path).pages)
        entries.append((t, p, True))
        if t in ("Studio Connection Diagram", "Panning Guide", "Goal Studio Diagram"):
            for k, sub_ in enumerate(SUBS[t]):
                entries.append((sub_, p + k, False))
        else:
            cursor = 0
            for sub_ in SUBS.get(t, []):
                pg, cursor = find_page(path, sub_, p, cursor)
                entries.append((sub_, pg if pg else p, False))
        p += n
    total = p - 1
    title_page = coverpage.make("/home/claude/studio/title.pdf")
    cover = "/home/claude/studio/cover.pdf"

    # two pages, two columns each: split at section boundaries
    ts = ParagraphStyle('toc', parent=cell, fontSize=7.1, leading=8.3)
    tsb = ParagraphStyle('tocb', parent=ts, fontName='Helvetica-Bold', textColor=NAVY)
    tsr = ParagraphStyle('tocr', parent=ts, alignment=2)
    tsbr = ParagraphStyle('tocbr', parent=tsb, alignment=2)
    def cellpair(e):
        if e is None:
            return [Paragraph("", ts), Paragraph("", ts)]
        tx, pg, bold = e
        return [Paragraph(tx if bold else "&nbsp;&nbsp;&nbsp;" + tx, tsb if bold else ts), Paragraph(str(pg), tsbr if bold else tsr)]
    def at_boundary(k):
        while k < len(entries) and not entries[k][2]:
            k += 1
        return k
    def two_col_table(chunk):
        # split the chunk into two balanced columns
        bounds = [i for i in range(1, len(chunk) + 1) if not chunk[i - 1][2]]  # any row, but never strand a section title at a column bottom
        mid = len(chunk) / 2
        half = min(bounds, key=lambda i: abs(i - mid))
        Lc, Rc = chunk[:half], chunk[half:]
        data = []
        for i in range(max(len(Lc), len(Rc))):
            data.append(cellpair(Lc[i] if i < len(Lc) else None) + [""] + cellpair(Rc[i] if i < len(Rc) else None))
        t_ = Table(data, colWidths=[2.95 * inch, 0.4 * inch, 0.3 * inch, 2.95 * inch, 0.4 * inch])
        st_ = [('VALIGN', (0, 0), (-1, -1), 'TOP'), ('TOPPADDING', (0, 0), (-1, -1), 0.5), ('BOTTOMPADDING', (0, 0), (-1, -1), 0.5),
               ('LEFTPADDING', (0, 0), (-1, -1), 2), ('RIGHTPADDING', (0, 0), (-1, -1), 2), ('LINEAFTER', (1, 0), (1, -1), 0.4, colors.HexColor('#cccccc'))]
        for i in range(len(data)):
            if i < len(Lc) and Lc[i][2]:
                st_.append(('LINEABOVE', (0, i), (1, i), 0.4, colors.HexColor('#dddddd')))
            if i < len(Rc) and Rc[i][2]:
                st_.append(('LINEABOVE', (3, i), (4, i), 0.4, colors.HexColor('#dddddd')))
        t_.setStyle(TableStyle(st_))
        return t_
    # Fill contents page 1 as full as it can be: test each candidate cut by actually building a one-page PDF.
    def section_cuts():
        return [i for i, e in enumerate(entries) if e[2] and i > 0] + [len(entries)]
    hdr_first = lambda: [Paragraph("TOAD STUDIO: The Studio Book", title), Paragraph(f"Mackie {B} home studio, Champaign-Urbana. Revised October 15, 2026. Page numbers are at the bottom of every page; the Connection Diagram, Panning Guide and Goal Studio Diagram pages are landscape, so rotate them in your viewer if needed.", sub), Spacer(1, 4), Paragraph("Contents", h)]
    hdr_next = lambda: [Paragraph("Contents, continued", h)]
    tail = lambda: []
    def fits_on_one_page(flow):
        tmp = "/home/claude/studio/_toc_probe.pdf"
        d_ = SimpleDocTemplate(tmp, pagesize=letter, leftMargin=0.75 * inch, rightMargin=0.75 * inch, topMargin=0.5 * inch, bottomMargin=0.5 * inch)
        d_.allowSplitting = 0
        try:
            d_.build(flow)
        except Exception:
            return False
        return len(_R(tmp).pages) == 1
    # Greedy: fill each contents page with as many whole sections as fit; the closing note goes on the last page.
    story_, rest, first = [], entries, True
    while rest:
        cuts = [i for i in range(1, len(rest) + 1) if not rest[i - 1][2]]  # any row, never leaving a section title alone at a page bottom
        head = hdr_first if first else hdr_next
        cut = cuts[0]
        for c_ in cuts:
            last = c_ == len(rest)
            if fits_on_one_page(head() + [two_col_table(rest[:c_])] + (tail() if last else [])):
                cut = c_
            else:
                break
        if story_:
            story_.append(PageBreak())
        story_ += head() + [two_col_table(rest[:cut])]
        rest, first = rest[cut:], False
    story_ += tail()
    doc = SimpleDocTemplate(cover, pagesize=letter, leftMargin=0.75 * inch, rightMargin=0.75 * inch, topMargin=0.5 * inch, bottomMargin=0.5 * inch)
    doc.allowSplitting = 0
    doc.build(story_)
    return entries

entries = build_contents()
while len(_R(cover).pages) - 1 != EXTRA_TOC_PAGES:
    EXTRA_TOC_PAGES = len(_R(cover).pages) - 1
    entries = build_contents()
rows = [["Section", "Page"]] + [[tx, str(pg)] for tx, pg, bold in entries if bold]

w = PdfWriter()
for path in [title_page, cover] + [f[2] for f in files]:
    for pg in PdfReader(path).pages:
        w.add_page(pg)
for i, pg in enumerate(w.pages, 1):
    pw, ph = float(pg.mediabox.width), float(pg.mediabox.height)
    buf = io.BytesIO()
    c = rl_canvas.Canvas(buf, pagesize=(pw, ph))
    c.setFont("Helvetica", 8); c.setFillColor(colors.grey)
    c.drawCentredString(pw / 2, 10, f"TOAD STUDIO  |  page {i} of {total}")
    c.save(); buf.seek(0)
    pg.merge_page(PdfReader(buf).pages[0])
w.add_metadata({"/Title": "TOAD STUDIO: The Studio Book"})
with open(OUT + "Studio_Book_Complete.pdf", "wb") as f:
    w.write(f)
print("pages", total, "needs", needs.TOTALS, "values", vtot)
for r in rows[1:]:
    print(r[1], r[0])
