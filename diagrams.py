from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from reportlab.lib.utils import simpleSplit
import math
from common import OUT, CH

W, H = landscape(letter)
NAVY = colors.HexColor('#1f3a5f'); LT = colors.HexColor('#e8eef5'); GR = colors.HexColor('#444444')
BLUE = colors.HexColor('#1f5fd6'); GOLD = colors.HexColor('#c99a06'); GREY = colors.HexColor('#999999')
RED = colors.HexColor('#aa3333')


class D:
    def __init__(self, c):
        self.c = c

    def box(self, x, y, w, h, title, lines=(), fill=LT, tsize=10, top=False):
        c = self.c
        c.setFillColor(fill); c.setStrokeColor(NAVY); c.setLineWidth(1)
        c.roundRect(x, y, w, h, 5, fill=1, stroke=1)
        c.setFillColor(NAVY); c.setFont("Helvetica-Bold", tsize)
        ty = (y + h / 2 - tsize * 0.35) if (not lines and not top) else (y + h - tsize - 4)
        c.drawCentredString(x + w / 2, ty, title)
        c.setFillColor(GR); c.setFont("Helvetica", 7.5)
        for i, l in enumerate(lines):
            c.drawCentredString(x + w / 2, y + h - tsize - 16 - i * 10, l)

    def head(self, x1, y1, x2, y2, col):
        a = math.atan2(y2 - y1, x2 - x1); L = 7
        p = self.c.beginPath(); p.moveTo(x2, y2)
        p.lineTo(x2 - L * math.cos(a - 0.4), y2 - L * math.sin(a - 0.4))
        p.lineTo(x2 - L * math.cos(a + 0.4), y2 - L * math.sin(a + 0.4)); p.close()
        self.c.setFillColor(col); self.c.drawPath(p, fill=1, stroke=0)

    def arrow(self, pts, col=GR, width=1.2, dash=None):
        c = self.c
        c.setStrokeColor(col); c.setLineWidth(width)
        c.setDash(*dash) if dash else c.setDash()
        p = c.beginPath(); p.moveTo(*pts[0])
        for q in pts[1:]:
            p.lineTo(*q)
        c.drawPath(p, stroke=1, fill=0); c.setDash()
        self.head(*pts[-2], *pts[-1], col)

    def label(self, x, y, txt, size=7, col=GR, bold=False, center=True, right=False):
        c = self.c
        c.setFillColor(col); c.setFont("Helvetica-Bold" if bold else "Helvetica", size)
        if right:
            c.drawRightString(x, y, txt)
        elif center:
            c.drawCentredString(x, y, txt)
        else:
            c.drawString(x, y, txt)

    def titleblock(self, t, s):
        c = self.c
        c.setFillColor(NAVY); c.setFont("Helvetica-Bold", 18); c.drawCentredString(W / 2, H - 40, t)
        c.setFillColor(colors.grey); c.setFont("Helvetica", 9); c.drawCentredString(W / 2, H - 55, s)


def signal_flow(c):
    d = D(c)
    d.titleblock("Studio Connection Diagram: Signal Flow", "Mackie 24•8 studio, October 2026. Follow the arrows from sources to the console, rack and Reaper.")
    src = [("Drums", ["6 XLR: kick, snare, toms, rooms"], 512, "Ch 1-6"),
           ("Bass amp", ["DI out or mic (XLR)"], 465, "Ch 7"),
           ("Guitar amps", ["Magnatone + Marshall/Orange"], 418, "Ch 8-9"),
           ("Vocals", ["Lead, wireless, vocals 2-3"], 371, "Ch 10-11, 15-16"),
           ("Trumpet", ["XLR"], 324, "Ch 14"),
           ("Synths", ["Reface CS + Roland SH-201"], 277, "Ch 12-13, 17-18"),
           ("PV6 submixer", ["E-drums, SamplePad 4, DJ (monitor)"], 230, "Ch 19-20"),
           ("1970s drum machine", ['1/4" out'], 183, "Ch 21")]
    CX, CW, CY0, CY1 = 225, 200, 160, 535
    d.box(CX, CY0, CW, CY1 - CY0, "Mackie 24•8 console", fill=colors.white, tsize=12, top=True)
    for t, ls, y, cl in src:
        d.box(25, y - 20, 150, 40, t, ls, tsize=9)
        d.arrow([(175, y), (CX, y)])
        d.label(CX + 8, y - 3, cl, 8, NAVY, True, False)
    for t, y in [("Group outs 1-8", 490), ("Tape returns 1-8 (MIX-B)", 455), ("Direct outs 10-11, 14-18, 21", 365),
                 ("Tape returns 9-16 (MIX-B)", 340), ("Aux send 1", 285), ("Aux return 1 L/R", 262),
                 ("Control room out L/R", 200), ("Studio out L/R", 175)]:
        d.label(CX + CW - 8, y - 3, t, 8, NAVY, True, right=True)
    d.label(CX + CW / 2, 440, "Group channels: pan picks the group.", 7)
    d.label(CX + CW / 2, 430, "Direct-out and monitor-only: pan freely.", 7)
    RX, RW = 590, 175
    d.box(RX, 435, RW, 85, "Behringer UMC1820", ["Inputs 1-8 (1-2 on front panel)", "Outs 1-8 (1-2 = MAIN OUT, knob full up)", "ADAT in + out  /  MIDI in"])
    d.box(RX, 335, RW, 70, "Behringer ADA8200", ["Line ins 1-8 = Reaper inputs 9-16", "XLR outs 1-8 = Reaper tracks 9-16"])
    d.box(RX, 245, RW, 60, "DigiTech TSR-12", ["Input L  /  Outputs L-R", "Mix 100% wet"])
    d.box(RX, 150, RW, 60, "Computer: Reaper", ["44.1 or 48 kHz; on a rack shelf", "short USB run to the UMC1820"])
    d.label(RX + RW / 2, 527, "RACK", 8, NAVY, True)
    d.arrow([(CX + CW, 490), (RX, 490)], NAVY, 2.5)
    d.label(507, 505, "Recording snake (white tape)", 7, NAVY, True); d.label(507, 496, "Group outs 1-8 to inputs 1-8", 7)
    d.arrow([(RX, 455), (CX + CW, 455)], colors.black, 2.5)
    d.label(507, 441, "Playback snake (black tape)", 7, colors.black, True); d.label(507, 432, "Outs 1-8 to tape returns 1-8", 7)
    d.arrow([(CX + CW, 365), (RX, 365)], BLUE, 2.5)
    d.label(507, 380, "Direct-out snake (blue tape)", 7, BLUE, True); d.label(507, 371, "Ch 10-11, 14-18, 21 to ADA8200 ins 1-8", 7)
    d.arrow([(RX, 342), (CX + CW, 342)], GOLD, 2.5)
    d.label(507, 329, "ADA8200 playback snake (yellow tape)", 7, GOLD, True); d.label(507, 320, "ADA outs 1-8 to tape returns 9-16", 7)
    d.arrow([(CX + CW, 285), (RX, 285)]); d.label(507, 290, '1/4" cable', 7)
    d.arrow([(RX, 262), (CX + CW, 262)]); d.label(507, 250, '2 x 1/4" cables (L/R)', 7)
    d.arrow([(RX + RW / 2 - 20, 405), (RX + RW / 2 - 20, 435)], NAVY, 1.5)
    d.arrow([(RX + RW / 2 + 20, 435), (RX + RW / 2 + 20, 405)], NAVY, 1.5)
    d.label(RX + RW / 2 + 55, 417, "Optical x2", 7, NAVY, True)
    d.arrow([(RX + RW, 470), (780, 470), (780, 180), (RX + RW, 180)], NAVY, 1.5)
    c.saveState(); c.translate(774, 325); c.rotate(90); d.label(0, 0, "USB", 7, NAVY, True); c.restoreState()
    # monitors
    d.arrow([(CX + CW, 200), (490, 200), (490, 142), (715, 142), (715, 130)])
    d.box(660, 75, 110, 55, "Peavey 260", ["Power amp on a shelf", "Speaker cable > DIY monitors"], tsize=9)
    # garage
    d.arrow([(CX + CW, 175), (480, 175), (480, 110), (500, 110)], GR, 1.2, (4, 3))
    d.box(500, 85, 150, 50, "Garage PA (optional)", ["Powerpod 410 or EMX62M", "Talkback: PHONES & STUDIO"], tsize=9)
    # headphones
    d.arrow([(305, CY0), (305, 115)]); d.arrow([(405, CY0), (405, 115)])
    d.box(255, 70, 108, 45, "Phones 1", ["Sony MDR-7506"], tsize=9)
    d.box(372, 70, 108, 45, "Phones 2", ["Sennheiser HD 280 Pro"], tsize=9)
    d.label(367, 58, "Source: MONITOR, or AUX SEND 3/4 for a performer mix", 7)
    # Tascam
    d.box(25, 75, 150, 55, "Tascam 246", ["4-track cassette", "(once repaired)"], tsize=9)
    d.arrow([(235, CY0), (235, 92), (175, 92)])
    d.label(240, 132, "Main mix out L/R", 7, center=False)
    d.arrow([(175, 118), (205, 118), (205, 170), (CX, 170)])
    d.label(CX + 8, 167, "Ch 23-24 (tape)", 8, NAVY, True, False)
    # legend
    y = 44
    for i, (col, t) in enumerate([(NAVY, "Recording snake"), (colors.black, "Playback snake"), (BLUE, "Direct-out snake"), (GOLD, "ADA playback snake")]):
        c.setStrokeColor(col); c.setLineWidth(2.5); c.line(360 + i * 102, y, 385 + i * 102, y); d.label(390 + i * 102, y - 3, t, 7, center=False)
    c.setStrokeColor(GR); c.setLineWidth(1.2); c.line(360, y - 14, 385, y - 14); d.label(390, y - 17, "Single cable", 7, center=False)
    c.setDash(4, 3); c.line(462, y - 14, 487, y - 14); c.setDash(); d.label(492, y - 17, "Optional", 7, center=False)


def power_page(c):
    d = D(c)
    d.titleblock("Studio Connection Diagram: Power, Instruments and Snake Colors", "Everything plugs into the Furman. Instruments run through pedals before the amp mic.")
    d.label(40, 520, "POWER", 10, NAVY, True, False)
    d.box(40, 380, 110, 50, "Wall outlet", ["Own circuit if the", "window AC causes hum"])
    d.box(200, 380, 120, 50, "Furman M-8x2", ["Rack, above the", "Mackie power supply"])
    d.arrow([(150, 405), (200, 405)])
    tg = [("Mackie power supply", ["Furman outlet 1"], 505), ("Behringer UMC1820", ["outlet 2"], 460), ("Behringer ADA8200", ["outlet 3"], 415), ("DigiTech TSR-12", ["outlet 4"], 370),
          ("Compressor / delay unit", ["outlets 5-6, when added"], 325)]
    c.setStrokeColor(GR); c.setLineWidth(1.2); c.line(320, 405, 360, 405); c.line(360, 325, 360, 505)
    d.box(400, 268, 150, 34, "Peavey 260 (monitors)", ["wall outlet, own switch, on last"], tsize=9)
    d.box(400, 230, 150, 34, "Computer (rack shelf)", ["wall outlet; shut down normally"], tsize=9)
    d.arrow([(95, 380), (95, 285), (400, 285)], GR, 1.2, (4, 3)); d.arrow([(95, 285), (95, 247), (400, 247)], GR, 1.2, (4, 3))
    d.label(100, 330, "straight from the wall", 6.5, GR, False, False)
    for t, ls, y in tg:
        d.arrow([(360, y), (400, y)])
        d.box(400, y - 18, 150, 36, t, ls, tsize=9)
    d.arrow([(550, 505), (610, 505)], NAVY, 2)
    d.label(580, 511, "Umbilical", 7, NAVY, True)
    d.box(610, 487, 150, 36, "Mackie 24•8 console")
    d.label(685, 474, "Keep the umbilical away from the snakes.", 7)
    c.setFillColor(LT); c.roundRect(610, 268, 150, 190, 5, fill=1, stroke=0)
    d.label(620, 442, "Power-up order", 9, NAVY, True, False)
    for i, s in enumerate(["1. All levels down", "2. Furman (rack comes up together)", "3. Computer, Reaper", "4. Wait 20-30 seconds", "5. Peavey 260, own switch", "6. Levels up"]):
        d.label(620, 424 - i * 14, s, 8, GR, False, False)
    d.label(620, 330, "Power down in reverse order.", 8, NAVY, True, False)
    d.label(620, 316, "Phones and control room levels", 8, GR, False, False)
    d.label(620, 304, "down before switching anything.", 8, GR, False, False)
    d.label(40, 212, "INSTRUMENT CHAINS", 10, NAVY, True, False)
    chain = ["Guitar", "Pedalboard", "Vibrato + Phase 90", "720 looper", "Guitar amp", "SM57 / SM58-style", "Console ch 8-9"]
    x = 40
    for i, t in enumerate(chain):
        d.box(x, 165, 88, 35, t, tsize=8)
        if i < len(chain) - 1:
            d.arrow([(x + 88, 182), (x + 104, 182)])
        x += 104
    chain2 = ["Bass", "Bass amp", "DI out or mic", "Console ch 7"]
    x = 40
    for i, t in enumerate(chain2):
        d.box(x, 115, 88, 35, t, tsize=8)
        if i < len(chain2) - 1:
            d.arrow([(x + 88, 132), (x + 104, 132)])
        x += 104
    d.label(470, 141, "SH-201 L out > pedalboard > ch 17 (synth volume low).", 7.5, NAVY, True, False)
    d.label(470, 129, "Marshall: time-based pedals can go in its FX loop instead.", 7.5, GR, False, False)
    d.label(470, 117, "Amp head + separate cab? Speaker cable only.", 7.5, RED, True, False)
    d.label(40, 86, "SNAKE COLOR ORDER (both ends, all four snakes)", 10, NAVY, True, False)
    cols = [("Brown", '#7b4a2a'), ("Red", '#d32f2f'), ("Yellow", '#f4d03f'), ("Green", '#2e9e5b'),
            ("Blue", '#1f5fd6'), ("Gray", '#9e9e9e'), ("White", '#ffffff'), ("Black", '#111111')]
    for i, (n, hx) in enumerate(cols):
        cx = 60 + i * 88
        c.setFillColor(colors.HexColor(hx)); c.setStrokeColor(GR); c.setLineWidth(1)
        c.circle(cx, 58, 12, fill=1, stroke=1)
        c.setFillColor(colors.black if n in ("Yellow", "White") else colors.white)
        c.setFont("Helvetica-Bold", 10); c.drawCentredString(cx, 54, str(i + 1))
        d.label(cx + 32, 54, n, 8, GR, False)
    d.label(40, 32, "Tape near each end: white = recording, black = playback 1-8, blue = direct outs, yellow = ADA8200 playback 9-16.", 7.5, GR, False, False)


def console_pan(c):
    d = D(c)
    d.titleblock("Panning Guide, Part 1: Console Pan Knobs (Tracking)", "Dot = 24•8 pan knob position. Group channels: pan picks the group, keep it fixed. Direct-out channels: pan only changes the headphones.")
    x0, x1 = 300, 560; top = 520; rh = 19
    d.label(x0, top + 24, "L", 9, NAVY, True); d.label((x0 + x1) / 2, top + 24, "C", 9, NAVY, True); d.label(x1, top + 24, "R", 9, NAVY, True)
    d.label(50, top + 24, "Ch", 8, NAVY, True, False); d.label(80, top + 24, "Source", 8, NAVY, True, False); d.label(600, top + 24, "Records to", 8, NAVY, True, False)
    short = {"group": lambda s: s.split(" (")[0], "direct": lambda s: "Direct out > ADA8200 in " + s.split("in ")[1].split(" ")[0],
             "monitor": lambda s: "Monitor only" if "Monitor only" in s else "Monitor; groups 7-8 to capture", "open": lambda s: ""}
    for i, (ch, nm, cab, panl, p, dest, kind) in enumerate(CH):
        y = top - i * rh
        if i % 2 == 0:
            c.setFillColor(colors.HexColor('#f6f6f6')); c.rect(40, y - 6, 712, rh, fill=1, stroke=0)
        d.label(50, y, ch, 8, NAVY, True, False); d.label(80, y, nm.replace("&mdash;", "-"), 8, GR, False, False)
        c.setStrokeColor(colors.HexColor('#bbbbbb')); c.setLineWidth(1); c.line(x0, y + 3, x1, y + 3)
        for t in (x0, (x0 + x1) / 2, x1):
            c.line(t, y - 1, t, y + 7)
        col = {"group": NAVY, "direct": BLUE, "monitor": GREY, "open": GREY}[kind]
        if p is not None:
            c.setFillColor(col); c.circle(x0 + (p + 1) / 2 * (x1 - x0), y + 3, 5, fill=1, stroke=0)
        d.label(600, y, short[kind](dest), 8, col, kind == "group", False)
    y = top - len(CH) * rh - 6
    c.setFillColor(NAVY); c.circle(60, y, 5, fill=1, stroke=0); d.label(72, y - 3, "Group channel: keep this pan setting", 8, GR, False, False)
    c.setFillColor(BLUE); c.circle(270, y, 5, fill=1, stroke=0); d.label(282, y - 3, "Direct-out: pan for headphones; L/R only", 8, GR, False, False)
    c.setFillColor(GREY); c.circle(500, y, 5, fill=1, stroke=0); d.label(512, y - 3, "Monitor only: not recorded through the console", 8, GR, False, False)
    d.label(W / 2, y - 20, "Lopsided headphones? Press MONO or use the AUX SEND 3/4 performer mix. Neither changes the recording. Set final panning in Reaper.", 8, NAVY, True)


def reaper_pan(c):
    d = D(c)
    d.titleblock("Panning Guide, Part 2: Final Mix in Reaper", "Suggested starting points for mixdown. Console pan doesn't carry over; set these on Reaper's tracks.")
    MIX = [("1", "Kick", 0, 0, "Center: anchors the low end."), ("2", "Snare", 0, 0, "Center (or just off, to taste)."),
           ("3-4", "Toms + rooms (stereo)", None, 1.0, "Stereo track at full width. Rack tom ends up left of center, floor tom right, matching the console pans."),
           ("5", "Bass", 0, 0, "Center: low end stays mono."),
           ("6", "Guitars (Magnatone + Marshall/Orange)", -0.35, 0, "Slightly left; for wide guitars, double-track and pan the second take right."),
           ("7-8", "Reface CS (stereo)", None, 0.7, "Stereo track at about 70% width so it doesn't crowd the guitars."),
           ("9", "Lead vocal", 0, 0, "Center, always."), ("10", "Wireless", 0, 0, "Center if it's a lead part; off-center if it's an instrument."),
           ("11", "Trumpet", 0.35, 0, "Right, opposite the guitar track."), ("12", "Vocal 2", -0.45, 0, "Harmony left."),
           ("13", "Vocal 3", 0.45, 0, "Harmony right, mirroring vocal 2."),
           ("14-15", "Roland SH-201 (stereo)", None, 1.0, "Stereo pair: hard L/R for a wide pad, or narrow it if it fights the Reface."),
           ("16", "1970s drum machine", 0, 0, "Center, or slightly off if it's a percussion layer.")]
    x0, x1 = 300, 560; top = 505; rh = 27
    d.label(x0, top + 24, "L", 9, NAVY, True); d.label((x0 + x1) / 2, top + 24, "C", 9, NAVY, True); d.label(x1, top + 24, "R", 9, NAVY, True)
    d.label(50, top + 24, "Reaper", 8, NAVY, True, False); d.label(95, top + 24, "Track", 8, NAVY, True, False); d.label(590, top + 24, "Why", 8, NAVY, True, False)
    for i, (tr, nm, p, w, why) in enumerate(MIX):
        y = top - i * rh
        if i % 2 == 0:
            c.setFillColor(colors.HexColor('#f6f6f6')); c.rect(40, y - 12, 712, rh, fill=1, stroke=0)
        d.label(50, y, tr, 8, NAVY, True, False); d.label(95, y, nm, 8, GR, False, False)
        c.setStrokeColor(colors.HexColor('#bbbbbb')); c.setLineWidth(1); c.line(x0, y + 3, x1, y + 3)
        for t in (x0, (x0 + x1) / 2, x1):
            c.line(t, y - 1, t, y + 7)
        if p is None:
            c.setStrokeColor(GOLD); c.setLineWidth(4)
            c.line(x0 + (1 - w) / 2 * (x1 - x0), y + 3, x0 + (1 + w) / 2 * (x1 - x0), y + 3)
        else:
            c.setFillColor(NAVY); c.circle(x0 + (p + 1) / 2 * (x1 - x0), y + 3, 5, fill=1, stroke=0)
        c.setFillColor(GR); c.setFont("Helvetica", 7.2)
        for k, ln in enumerate(simpleSplit(why, "Helvetica", 7.2, 160)):
            c.drawString(590, y + 5 - k * 8.5, ln)
    y = top - len(MIX) * rh - 4
    c.setFillColor(NAVY); c.circle(60, y, 5, fill=1, stroke=0); d.label(72, y - 3, "Mono track: pan position", 8, GR, False, False)
    c.setStrokeColor(GOLD); c.setLineWidth(4); c.line(230, y, 255, y); d.label(262, y - 3, "Stereo track: width", 8, GR, False, False)
    for i, t in enumerate(["Rules of thumb: kick, snare, bass and lead vocal stay centered. Balance the sides: what goes left, something similar goes right.",
                           "Check the mix in mono (Reaper master mono button or the console's MONO): nothing important should disappear.",
                           "Headphones exaggerate width; once the monitors are built, re-check panning on them."]):
        d.label(W / 2, y - 20 - i * 12, t, 7.8, NAVY if i == 0 else GR, i == 0)


def make(name, doc_title, pages):
    c = canvas.Canvas(OUT + name, pagesize=(W, H)); c.setTitle(doc_title)
    for fn in pages:
        fn(c); c.showPage()
    c.save()
    return OUT + name


def goal_studio(c):
    """Prospective map: today's gear plus everything on the needs list, wired in."""
    d = D(c)
    d.titleblock("Goal Studio: Everything on the Needs List Connected", "Where each planned purchase plugs in. Orange dashed = on the needs list. Navy solid = already in the studio.")
    PLAN = colors.HexColor('#b35c00')

    def pbox(x, y, w, h, title, lines=(), tsize=9):
        c.setFillColor(colors.HexColor('#fff4e8')); c.setStrokeColor(PLAN); c.setLineWidth(1); c.setDash(4, 3)
        c.roundRect(x, y, w, h, 5, fill=1, stroke=1); c.setDash()
        c.setFillColor(PLAN); c.setFont("Helvetica-Bold", tsize)
        c.drawCentredString(x + w / 2, y + h - tsize - 4, title)
        c.setFillColor(GR); c.setFont("Helvetica", 7.2)
        for i, l in enumerate(lines):
            c.drawCentredString(x + w / 2, y + h - tsize - 15 - i * 9.5, l)

    def parrow(pts):
        d.arrow(pts, PLAN, 1.2, (4, 3))

    # console in the middle; one label per port, each at the y of the line that uses it
    CX, CW, CY0, CY1 = 310, 170, 110, 530
    d.box(CX, CY0, CW, CY1 - CY0, "Mackie 24\u20228 console", fill=colors.white, tsize=12, top=True)
    LEFT = [("Mic inputs", 492), ("Line inputs", 455), ("Phones 1 / 2", 300), ("2-TK in", 260), ("Aux sends 3-6", 215)]
    RIGHT = [("Channel inserts", 476), ("Group outs 1-8", 430), ("Direct outs", 405), ("Tape returns 1-16", 370),
             ("Aux 1 send / return", 325), ("Aux 2 send / return", 285), ("Control room out", 160)]
    for t, y in LEFT:
        d.label(CX + 8, y - 3, t, 7.5, NAVY, True, False)
    for t, y in RIGHT:
        d.label(CX + CW - 8, y - 3, t, 7.5, NAVY, True, right=True)

    # ---- left column ----
    LX, LW = 30, 165
    d.box(LX, 470, LW, 48, "Mics, amps, synths, PV6", ["Everything you record or hear today", "(channel list in the Setup Map)"], tsize=9)
    d.arrow([(LX + LW, 494), (CX, 494)]); d.label(252, 499, "XLR x15 (planned)", 6.5, PLAN)
    pbox(LX, 400, LW, 50, "Guitar pedals (planned)", ["Diamond Vibrato + MXR Phase 90", "after the pedalboard, then the amp mic"])
    parrow([(LX + LW, 425), (240, 425), (240, 480), (CX, 480)])
    pbox(LX, 335, LW, 50, "Radial ProDI (planned)", ["Guitar or bass > DI > a mic input", "thru jack carries on to the amp"])
    parrow([(LX + LW, 360), (255, 360), (255, 457), (CX, 457)])
    pbox(LX, 275, LW, 48, "Headphone pads (planned)", ["MDR-7506 + HD 280 Pro", "into Phones 1 and 2"])
    parrow([(CX, 300), (LX + LW, 300)])
    pbox(LX, 215, LW, 48, "Reference cable (planned)", ["Phone or computer, 3.5mm to RCA", "into the 2-TK input; press 2-TK"])
    parrow([(LX + LW, 260), (CX, 260)])
    pbox(LX, 150, LW, 50, "Personal mixers (planned)", ["one per extra player,", "fed from aux sends 3-6"])
    parrow([(CX, 215), (270, 215), (270, 175), (LX + LW, 175)])

    # ---- right column ----
    RX, RW = 600, 170
    pbox(RX, 452, RW, 46, "Klark Teknik 76-KT (planned)", ["alt: 2 x dbx 266XS or 1066", "inserts: drums, vocal, bass"])
    parrow([(CX + CW, 478), (RX, 478)]); parrow([(RX, 470), (CX + CW, 470)])
    pbox(RX, 500, RW, 32, "Quad gate (option)", ["DN514+ on inserts of ch 1-4"], tsize=8.5)
    parrow([(CX + CW, 490), (RX, 516)])
    d.box(RX, 365, RW, 68, "UMC1820 + ADA8200", ["Reaper inputs 1-16, playback 1-16", "2nd optical cable (planned)", "3rd snake + 6 ft snake (planned)"], tsize=9)
    d.arrow([(CX + CW, 430), (RX, 420)], NAVY, 2.2)
    parrow([(CX + CW, 405), (RX, 400)])
    d.arrow([(RX, 383), (CX + CW, 370)], colors.black, 2.2)
    d.label(540, 440, "Recording snake", 6.5, NAVY); d.label(540, 393, "Third snake (planned)", 6.5, PLAN)
    d.label(540, 362, "Playback 1-8; 9-16 planned", 6.5, GR)
    d.box(RX, 300, RW, 45, "DigiTech TSR-12", ["Reverb on aux 1 / return 1"], tsize=9)
    d.arrow([(CX + CW, 328), (RX, 328)]); d.arrow([(RX, 320), (CX + CW, 320)])
    pbox(RX, 240, RW, 48, "Delay unit (future)", ["Aux 2 / return 2", "second effects unit or a pedal"])
    parrow([(CX + CW, 288), (RX, 270)]); parrow([(RX, 262), (CX + CW, 280)])
    pbox(RX, 170, RW, 52, "Patchbay (planned)", ["Inserts, compressor ins/outs,", "groups 7-8 swaps. 2 in Cory's listing"])
    d.label(RX + RW / 2, 160, "in the rack, between the console and the gear above", 6.5, PLAN)
    d.box(RX, 95, RW, 50, "Furman M-8x2 (on its way)", ["Console power supply, rack gear", "and the Peavey all plug in here"], tsize=9)

    # ---- bottom: monitoring ----
    pbox(CX, 30, 90, 55, "Peavey 260", ["tech check (planned)", "TRS-to-TS in"], tsize=8.5)
    parrow([(CX + CW, 160), (555, 160), (555, 57), (CX + 90, 57)])
    d.label(520, 100, "control room out", 6.5, PLAN)
    pbox(170, 30, 125, 55, "DIY monitors (planned)", ["Parts Express C-Note", "or Hitmaker kit"], tsize=8.5)
    parrow([(CX, 57), (295, 57)]); d.label(302, 65, "speaker cable", 6, PLAN)

    # legend
    y = 14
    c.setStrokeColor(NAVY); c.setLineWidth(1); c.setDash(); c.roundRect(600, y - 4, 14, 10, 2, fill=0, stroke=1)
    d.label(619, y - 2, "Owned", 7, center=False)
    c.setStrokeColor(PLAN); c.setDash(4, 3); c.roundRect(665, y - 4, 14, 10, 2, fill=0, stroke=1); c.setDash()
    d.label(684, y - 2, "On the needs list / planned", 7, center=False)


def alt_diagram(c):
    d = D(c)
    d.titleblock("Alternate Setups: Connection Diagram",
                 "Alternate A recording (all direct outs) with Alternate B playback (two outputs). Dashed lines are only for 16-track playback.")
    src = [("Ch 1-8", ["Kick, snare, toms, room L/R,", "bass, Magnatone"], 470),
           ("Ch 9-16", ["Marshall/Orange, lead vocal, wireless,", "Reface L/R, trumpet, vocals 2-3"], 395),
           ("Ch 17-24", ["SH-201, PV6, drum machine, Tascam:", "monitor only in Alternate A"], 320)]
    CX, CW, CY0, CY1 = 225, 210, 150, 530
    d.box(CX, CY0, CW, CY1 - CY0, "Mackie 24•8 console", fill=colors.white, tsize=12, top=True)
    for t, ls, y in src:
        d.box(20, y - 25, 170, 50, t, ls, tsize=9)
        d.arrow([(190, y), (CX, y)])
    for t, y in [("Direct outs 1-8", 470), ("Direct outs 9-16", 395), ("Tape returns 1-2 (MIX-B)", 330),
                 ("Tape returns 3-16", 290), ("Control room out L/R", 200)]:
        d.label(CX + CW - 8, y - 3, t, 8, NAVY, True, right=True)
    for i, t in enumerate(["Ch 1-16: L/R assign only, faders at U", "Groups not used: faders down, L-R up",
                           "Pans set the headphones only", "Press MIX-B to hear Reaper"]):
        d.label(CX + 10, 255 - i * 11, t, 7, center=False)
    RX, RW = 590, 175
    d.box(RX, 430, RW, 85, "Behringer UMC1820", ["Inputs 1-8 = Reaper 1-8", "Outs 1-2 = MAIN OUT (knob full up)", "Outs 3-8: 16-track playback only"])
    d.box(RX, 310, RW, 75, "Behringer ADA8200", ["Line ins 1-8 = Reaper 9-16", "Gain knobs at minimum", "XLR outs: 16-track playback only"])
    d.box(RX, 165, RW, 70, "Computer: Reaper", ["Track N = input N = channel N", "All tracks to master; master to outs 1/2"])
    d.label(RX + RW / 2, 522, "RACK", 8, NAVY, True)
    # recording
    d.arrow([(CX + CW, 470), (RX, 470)], NAVY, 2.5)
    d.label(512, 485, "Recording snake (white tape)", 7, NAVY, True); d.label(512, 476, "Direct outs 1-8 to inputs 1-8", 7)
    d.arrow([(CX + CW, 395), (530, 395), (530, 355), (RX, 355)], BLUE, 2.5)
    d.label(500, 409, "Direct-out snake (blue tape)", 7, BLUE, True); d.label(500, 400, "Direct outs 9-16 to ADA8200 ins 1-8", 7)
    # optical
    d.arrow([(RX + RW / 2 - 25, 385), (RX + RW / 2 - 25, 430)], NAVY, 1.5)
    d.label(RX + RW / 2 - 30, 405, "Optical (recording)", 7, NAVY, True, right=True)
    d.arrow([(RX + RW / 2 + 25, 430), (RX + RW / 2 + 25, 385)], NAVY, 1.5, (4, 3))
    d.label(RX + RW / 2 + 30, 405, "Optical (playback)", 7, NAVY, True, center=False)
    # usb
    d.arrow([(RX + RW, 470), (780, 470), (780, 200), (RX + RW, 200)], NAVY, 1.5)
    c.saveState(); c.translate(774, 335); c.rotate(90); d.label(0, 0, "USB", 7, NAVY, True); c.restoreState()
    # playback
    d.arrow([(RX, 445), (560, 445), (560, 330), (CX + CW, 330)], colors.black, 2.5)
    d.label(442, 321, "Playback snake (black tape)", 7, colors.black, True, False); d.label(442, 312, "Brown + red tails only:", 7, center=False); d.label(442, 303, "outs 1-2 to tape returns 1-2", 7, center=False)
    d.arrow([(RX, 438), (570, 438), (570, 295), (CX + CW, 295)], colors.black, 1.5, (4, 3))
    d.arrow([(RX, 320), (580, 320), (580, 285), (CX + CW, 285)], GOLD, 1.5, (4, 3))
    d.label(498, 274, "16-track only: outs 3-8 to returns 3-8,", 7, GR); d.label(498, 265, "ADA outs to returns 9-16 (6 ft snake)", 7, GR)
    # monitoring
    d.arrow([(CX + CW, 200), (480, 200), (480, 120)])
    d.box(420, 70, 160, 50, "Speakers", ["Powered (e.g. Edifier), or", "Peavey 260 + DIY monitors"], tsize=9)
    d.arrow([(275, CY0), (275, 120)]); d.arrow([(385, CY0), (385, 120)])
    d.box(225, 70, 100, 50, "Phones 1", ["MONITOR, or", "MIX-B + AUX 3&4"], tsize=9)
    d.box(335, 70, 75, 50, "Phones 2", ["Performer:", "AUX SEND 3&4"], tsize=9)
    d.box(20, 70, 190, 50, "Backing track in a performer mix", ["Ch 1-2: press SOURCE on aux 3/4,", "raise those two aux knobs"], tsize=8)
    # legend
    y = 44
    for i, (col, t) in enumerate([(NAVY, "Recording snake"), (BLUE, "Direct-out snake"), (colors.black, "Playback snake"), (GOLD, "ADA playback snake")]):
        c.setStrokeColor(col); c.setLineWidth(2.5); c.line(250 + i * 115, y, 275 + i * 115, y); d.label(280 + i * 115, y - 3, t, 7, center=False)
    c.setStrokeColor(GR); c.setLineWidth(1.2); c.line(250, y - 14, 275, y - 14); d.label(280, y - 17, "Single cable", 7, center=False)
    c.setDash(4, 3); c.line(365, y - 14, 390, y - 14); c.setDash(); d.label(395, y - 17, "Only for 16-track playback (not used in Alternate B)", 7, center=False)
