from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch

OUT = "/mnt/user-data/outputs/"
NAVY = colors.HexColor('#1f3a5f')
LIGHT = colors.HexColor('#e8eef5')
GRID = colors.HexColor('#bbbbbb')
ZEBRA = colors.HexColor('#f6f6f6')
B = "24&bull;8"
AR = "&rarr;"

ss = getSampleStyleSheet()
title = ParagraphStyle('t', parent=ss['Title'], fontSize=18, spaceAfter=4)
sub = ParagraphStyle('s', parent=ss['Normal'], fontSize=9.5, textColor=colors.HexColor('#555555'), spaceAfter=10)
h = ParagraphStyle('h', parent=ss['Heading2'], fontSize=13, spaceBefore=10, spaceAfter=6, textColor=NAVY)
h3 = ParagraphStyle('h3', parent=ss['Heading3'], fontSize=10.5, spaceBefore=8, spaceAfter=3, textColor=NAVY)
cell = ParagraphStyle('c', parent=ss['Normal'], fontSize=8.5, leading=10.5)
cellb = ParagraphStyle('cb', parent=cell, fontName='Helvetica-Bold')
hdr = ParagraphStyle('hd', parent=cell, fontName='Helvetica-Bold', textColor=colors.white)
note = ParagraphStyle('n', parent=ss['Normal'], fontSize=8.5, leading=11, textColor=colors.HexColor('#444444'))


def bul(s):
    return Paragraph("&bull;&nbsp;&nbsp;" + s, cell)


def sec(t, items):
    return [KeepTogether([Paragraph(t, h)] + [bul(i) for i in items])]


def tbl(rows, widths, bold_first=True, last_bold=False):
    data = [[Paragraph(c, hdr) for c in rows[0]]]
    for r in rows[1:]:
        data.append([Paragraph(c, cellb if (j == 0 and bold_first) else cell) for j, c in enumerate(r)])
    t = Table(data, colWidths=widths, repeatRows=1)
    st = [('BACKGROUND', (0, 0), (-1, 0), NAVY), ('GRID', (0, 0), (-1, -1), 0.4, GRID),
          ('VALIGN', (0, 0), (-1, -1), 'TOP'), ('TOPPADDING', (0, 0), (-1, -1), 4), ('BOTTOMPADDING', (0, 0), (-1, -1), 4)]
    for i in range(2, len(data), 2):
        st.append(('BACKGROUND', (0, i), (-1, i), ZEBRA))
    if last_bold:
        st.append(('BACKGROUND', (0, -1), (-1, -1), LIGHT))
    t.setStyle(TableStyle(st))
    return t


def money_tbl(rows, head, widths, money_cols):
    """rows: tuples; money_cols: indexes holding ints. Adds a Subtotal row. Returns table, sums."""
    data = [[Paragraph(x, hdr) for x in head]]
    sums = {i: 0 for i in money_cols}
    for r in rows:
        line = []
        for j, v in enumerate(r):
            if j in money_cols:
                sums[j] += v
                line.append(Paragraph(f"${v:,}", cell))
            else:
                line.append(Paragraph(v, cellb if j == 0 else cell))
        data.append(line)
    tot = [Paragraph("Subtotal", cellb)] + [""] * (len(head) - 1)
    for j in money_cols:
        tot[j] = Paragraph(f"${sums[j]:,}", cellb)
    data.append(tot)
    t = Table(data, colWidths=widths, repeatRows=1)
    st = [('BACKGROUND', (0, 0), (-1, 0), NAVY), ('VALIGN', (0, 0), (-1, -1), 'TOP'),
          ('GRID', (0, 0), (-1, -1), 0.4, GRID), ('BACKGROUND', (0, -1), (-1, -1), LIGHT),
          ('TOPPADDING', (0, 0), (-1, -1), 4), ('BOTTOMPADDING', (0, 0), (-1, -1), 4)]
    for i in range(2, len(data) - 1, 2):
        st.append(('BACKGROUND', (0, i), (-1, i), ZEBRA))
    t.setStyle(TableStyle(st))
    return t, [sums[j] for j in money_cols]


def plain_tbl(rows, widths, shade_last=True):
    data = [[Paragraph(c, cellb if (i == 0 or (shade_last and i == len(rows) - 1)) else cell) for c in r] for i, r in enumerate(rows)]
    t = Table(data, colWidths=widths)
    st = [('GRID', (0, 0), (-1, -1), 0.4, GRID), ('BACKGROUND', (0, 0), (-1, 0), LIGHT)]
    if shade_last:
        st.append(('BACKGROUND', (0, -1), (-1, -1), LIGHT))
    t.setStyle(TableStyle(st))
    return t


def build(name, doc_title, story, margins=0.5):
    doc = SimpleDocTemplate(OUT + name, pagesize=letter, leftMargin=margins * inch, rightMargin=margins * inch,
                            topMargin=0.55 * inch, bottomMargin=0.6 * inch, title=doc_title)
    doc.build(story)
    return OUT + name


# ---------------- shared studio data (single source of truth) ----------------
# ch, source, cable, pan label, pan value (-1..1 or None), records-to, kind (group/direct/monitor/open)
CH = [
    ("1", "Kick", "XLR", "Hard L", -1, "Group 1 (Reaper 1)", "group"),
    ("2", "Snare", "XLR", "Hard R", 1, "Group 2 (Reaper 2)", "group"),
    ("3", "Rack tom (SM58-style)", "XLR", "10 o'clock", -0.4, "Groups 3-4 (Reaper 3-4)", "group"),
    ("4", "Floor tom (SM58-style)", "XLR", "2 o'clock", 0.4, "Groups 3-4 (Reaper 3-4)", "group"),
    ("5", "Room L", "XLR", "Hard L", -1, "Groups 3-4 (Reaper 3-4)", "group"),
    ("6", "Room R", "XLR", "Hard R", 1, "Groups 3-4 (Reaper 3-4)", "group"),
    ("7", "Bass amp (DI out or mic)", "XLR", "Hard L", -1, "Group 5 (Reaper 5)", "group"),
    ("8", "Magnatone (SM57)", "XLR", "Hard R", 1, "Group 6 (Reaper 6)", "group"),
    ("9", "Marshall or Orange (SM58-style)", "XLR", "Hard R", 1, "Group 6 (Reaper 6)", "group"),
    ("10", "Lead vocal (Worker Bee)", "XLR", "Center", 0, "Direct out " + AR + " ADA8200 in 1 (Reaper 9)", "direct"),
    ("11", "ATW-R3210 wireless", "XLR", "Center", 0, "Direct out " + AR + " ADA8200 in 2 (Reaper 10)", "direct"),
    ("12", "Reface CS L", '1/4" TS', "Hard L", -1, "Group 7 (Reaper 7)", "group"),
    ("13", "Reface CS R", '1/4" TS', "Hard R", 1, "Group 8 (Reaper 8)", "group"),
    ("14", "Trumpet (SM58)", "XLR", "1 o'clock", 0.2, "Direct out " + AR + " ADA8200 in 3 (Reaper 11)", "direct"),
    ("15", "Vocal 2 (Peavey)", "XLR", "10 o'clock", -0.4, "Direct out " + AR + " ADA8200 in 4 (Reaper 12)", "direct"),
    ("16", "Vocal 3 (Turner 95D)", "XLR", "2 o'clock", 0.4, "Direct out " + AR + " ADA8200 in 5 (Reaper 13)", "direct"),
    ("17", "Roland SH-201 L", '1/4" TS', "9 o'clock", -0.6, "Direct out " + AR + " ADA8200 in 6 (Reaper 14)", "direct"),
    ("18", "Roland SH-201 R", '1/4" TS', "3 o'clock", 0.6, "Direct out " + AR + " ADA8200 in 7 (Reaper 15)", "direct"),
    ("19", "Peavey PV6 main out L", '1/4"', "Hard L", -1, "Monitor only (e-drums, SamplePad 4, DJ)", "monitor"),
    ("20", "Peavey PV6 main out R", '1/4"', "Hard R", 1, "Monitor only (e-drums, SamplePad 4, DJ)", "monitor"),
    ("21", "1970s Roland drum machine", '1/4" TS', "Center", 0, "Direct out " + AR + " ADA8200 in 8 (Reaper 16)", "direct"),
    ("22", "Open (drum machine R if stereo)", "&mdash;", "&mdash;", None, "&mdash;", "open"),
    ("23", "Tascam 246 line out L", 'RCA to 1/4"', "Hard L", -1, "Monitor; assign to groups 7-8 to capture into Reaper", "monitor"),
    ("24", "Tascam 246 line out R", 'RCA to 1/4"', "Hard R", 1, "Monitor; assign to groups 7-8 to capture into Reaper", "monitor"),
]
SNAKE_COLORS = ["Brown", "Red", "Yellow", "Green", "Blue", "Gray", "White", "Black"]
DIRECT_CH = ["10", "11", "14", "15", "16", "17", "18", "21"]

# Needs-list money (kept here so the summary and the needs list can't drift apart)
CAP = [
    "<b>Console channels:</b> 23 of 24 used. Ch 22 is open, held for the drum machine if it has a stereo out; free for anything if it's mono.",
    "<b>Recording inputs:</b> 16 of 16 used. Groups 1-8 " + AR + " UMC1820 (Reaper 1-8); direct outs " + AR + " ADA8200 (Reaper 9-16). Anything new can be heard, but recording it means borrowing a group or direct-out path (like the Tascam on groups 7-8).",
    "<b>Playback:</b> 16 tracks. UMC1820 outputs 1-8 " + AR + " tape returns 1-8; ADA8200 outputs " + AR + " tape returns 9-16.",
    "<b>Still open for signals:</b> aux send 2 and AUX RETURN 2 (second effects unit); 2-TK and EXTERNAL inputs (monitor only: reference tracks, a phone); spare PV6 inputs (monitor-only sources); any mic input via the Radial ProDI once that channel's source is swapped.",
    "<b>If you outgrow 16 inputs:</b> the UMC1820's one ADAT input is taken by the ADA8200, so more recording channels means a bigger interface or a second one. Before that, submix monitor-only sources on the PV6.",
]
