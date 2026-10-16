from common import *
from reportlab.platypus import Flowable
import math
GR = colors.HexColor("#444444")

# Per-channel EQ settings. Knob values are dB for gain knobs and Hz/kHz for sweeps.
# (ch, name, locut, hi_db, himid_freq_label, himid_db, bw, lomid_freq_label, lomid_db, lo_db, why)
# bw: 'wide' | 'med' | 'narrow'  (HI MID bandwidth knob)
EQ = [
    ("1", "Kick", False, 0, "4k", +3, "med", "400", -4, +3, "Low shelf adds thump; 400 Hz cut removes the cardboard \"box\"; 4 kHz gives the beater click so it cuts through. Keep LO CUT off."),
    ("2", "Snare", False, +2, "5k", +2, "med", "250", -2, 0, "A little top for crack. If it rings, sweep LO MID until the ring is loudest, then cut 3-4 dB there."),
    ("3", "Rack tom", True, 0, "5k", +2, "med", "500", -3, +2, "LO CUT on: nothing useful below 75 Hz on a 13\" tom. Cut the boxy 500 Hz, add stick attack at 5 kHz."),
    ("4", "Floor tom", False, 0, "4k", +2, "med", "400", -3, +2, "Same idea as the rack tom. LO CUT off so the low thump stays. Both toms share groups 3-4, so keep them similar."),
    ("5", "Room L", True, +2, "3k", -2, "wide", "300", -3, 0, "Rooms are about air and smack. Cut the mud at 300 Hz, soften 3 kHz if the cymbals are harsh, LO CUT on (the kick mic already has the lows)."),
    ("6", "Room R", True, +2, "3k", -2, "wide", "300", -3, 0, "Match channel 5 exactly, or the stereo picture shifts."),
    ("7", "Bass (DI or amp)", False, 0, "800", +2, "med", "80", 0, +2, "Gentle: a touch of low shelf for weight, a little 800 Hz so it's audible on small speakers. No LO CUT ever on bass."),
    ("8", "Magnatone (SM57)", True, 0, "3k", 0, "med", "200", -2, 0, "SM57 on a tube amp needs almost nothing. LO CUT on to drop the rumble a close mic picks up. Cut a little 200 Hz if it's muddy."),
    ("9", "Marshall/Orange (SM58-style)", True, +1, "4k", +2, "med", "300", -2, 0, "SM58-style mics are a little darker than an SM57 on an amp: a small lift at 4 kHz and the HI shelf brings back the bite."),
    ("10", "Lead vocal (Worker Bee)", True, +2, "3k", +2, "med", "250", -3, 0, "Condenser: LO CUT on for plosives and rumble, cut the 250 Hz chestiness, a little 3 kHz presence, HI shelf for air. Cut less than you think."),
    ("11", "Wireless (ATW-R3210)", True, 0, "2.5k", +2, "med", "250", -2, 0, "Depends on what's plugged into the body pack. Start flat and add presence only if it sounds dull."),
    ("12", "Reface CS L", False, 0, "1k", 0, "med", "150", 0, 0, "Flat. Synths come out already shaped. EQ IN off until something is actually wrong."),
    ("13", "Reface CS R", False, 0, "1k", 0, "med", "150", 0, 0, "Match channel 12."),
    ("14", "Trumpet (SM58)", True, -1, "3k", -3, "narrow", "300", 0, 0, "Trumpet is naturally bright and loud. Cut 3 kHz a little so it doesn't pierce; LO CUT on. Distance from the mic does more than EQ."),
    ("15", "Vocal 2 (Peavey)", True, +1, "3k", +2, "med", "250", -2, 0, "Dynamic mic: a bit more presence than the Worker Bee needs, plus LO CUT."),
    ("16", "Vocal 3 (Turner 95D)", True, +3, "4k", +3, "med", "400", -3, 0, "Vintage mic with a narrow 100 Hz-10 kHz range. Boost the top to open it up, or leave it dark on purpose for the lo-fi vocal sound."),
    ("17", "SH-201 L", False, 0, "1k", 0, "med", "150", 0, 0, "Flat; EQ on the synth or the pedals instead. Through fuzz pedals, cut 3-5 kHz a little if it's harsh."),
    ("18", "SH-201 R", False, 0, "1k", 0, "med", "150", 0, 0, "Match channel 17."),
    ("19", "PV6 submix L", False, 0, "1k", 0, "med", "150", 0, 0, "Monitor only. Flat; adjust on the PV6."),
    ("20", "PV6 submix R", False, 0, "1k", 0, "med", "150", 0, 0, "Monitor only. Flat."),
    ("21", "1970s drum machine", False, +2, "3k", +1, "med", "200", 0, +2, "Old drum machines are dull and thin: a little low shelf and top brings them to life. Keep LO CUT off."),
    ("22", "Open", False, 0, "1k", 0, "med", "150", 0, 0, ""),
    ("23", "Tascam 246 L", False, +1, "3k", 0, "med", "150", 0, 0, "Tape loses a little top; a 1 dB HI shelf brings it back. Otherwise flat, so you hear what the tape did."),
    ("24", "Tascam 246 R", False, +1, "3k", 0, "med", "150", 0, 0, "Match channel 23."),
]


class Strip(Flowable):
    """One channel strip, drawn like the board: buttons, then HI, HI MID (freq, width, gain), LO MID (freq, gain), LO."""
    W, H = 1.2 * inch, 3.75 * inch

    def __init__(self, row):
        super().__init__(); self.row = row; self.width = self.W; self.height = self.H

    def knob(self, c, x, y, r, frac, label, value, moved=None):
        if moved is None:
            moved = abs(frac) > 0.01
        c.setStrokeColor(colors.HexColor('#777777')); c.setLineWidth(0.8); c.setFillColor(colors.HexColor('#f0f0f0'))
        c.circle(x, y, r, fill=1, stroke=1)
        for f, col in ((-1, GRID), (0, NAVY), (1, GRID)):
            a = math.radians(90 - 150 * f)
            c.setStrokeColor(col); c.setLineWidth(0.8)
            c.line(x + (r + 1.5) * math.cos(a), y + (r + 1.5) * math.sin(a), x + (r + 4) * math.cos(a), y + (r + 4) * math.sin(a))
        a = math.radians(90 - 150 * frac)
        c.setStrokeColor(colors.HexColor('#b35c00') if moved else NAVY); c.setLineWidth(2.2)
        c.line(x, y, x + r * 0.85 * math.cos(a), y + r * 0.85 * math.sin(a))
        c.setFillColor(colors.HexColor('#b35c00') if moved else NAVY); c.setFont("Helvetica-Bold", 7)
        c.drawCentredString(x, y + r + 6.5, value)
        c.setFillColor(GR); c.setFont("Helvetica", 5.6); c.drawCentredString(x, y - r - 8, label)

    def button(self, c, x, y, w, h, label, on):
        c.setStrokeColor(colors.HexColor('#777777')); c.setLineWidth(0.8)
        c.setFillColor(colors.HexColor('#b35c00') if on else colors.white)
        c.rect(x, y, w, h, fill=1, stroke=1)
        c.setFillColor(colors.white if on else GR); c.setFont("Helvetica-Bold", 6)
        c.drawCentredString(x + w / 2, y + h / 2 - 2.2, label + (" ON" if on else " off"))

    def draw(self):
        c = self.canv; ch, name, locut, hi, hmf, hm, bw, lmf, lm, lo, why = self.row
        cx = self.W / 2
        c.setFillColor(NAVY); c.setFont("Helvetica-Bold", 8.5); c.drawCentredString(cx, self.H - 11, f"Ch {ch}")
        c.setFillColor(GR); c.setFont("Helvetica", 6.2)
        c.drawCentredString(cx, self.H - 21, name if len(name) <= 24 else name[:23] + ".")
        flat = all(v == 0 for v in (hi, hm, lm, lo))
        self.button(c, cx - 36, self.H - 36, 34, 10, "LO CUT", locut)
        self.button(c, cx + 2, self.H - 36, 34, 10, "EQ IN", not flat)
        def g(v): return max(-1, min(1, v / 15.0))
        def db(v): return f"{v:+d} dB" if v else "0 (flat)"
        R = 11
        y = self.H - 66
        self.knob(c, cx, y, R, g(hi), "HI: 12 kHz shelf", db(hi))
        y -= 48
        fr = {"500": -1, "800": -0.85, "1k": -0.7, "2.5k": -0.2, "3k": -0.1, "4k": 0.1, "5k": 0.25}.get(hmf, 0)
        self.knob(c, cx - 22, y, 8.5, fr, "HI MID freq", hmf if hmf.endswith("k") else hmf + " Hz", moved=True)
        self.knob(c, cx + 22, y, 8.5, {"wide": -0.8, "med": 0, "narrow": 0.8}[bw], "bandwidth", bw, moved=(bw != "med"))
        y -= 44
        self.knob(c, cx, y, R, g(hm), "HI MID gain", db(hm))
        y -= 48
        lfr = {"80": -0.9, "150": -0.6, "200": -0.45, "250": -0.35, "300": -0.25, "400": -0.1, "500": 0}.get(lmf, 0)
        self.knob(c, cx - 22, y, 8.5, lfr, "LO MID freq", lmf + " Hz", moved=True)
        self.knob(c, cx + 22, y, 8.5, g(lm), "LO MID gain", db(lm))
        y -= 46
        self.knob(c, cx, y, R, g(lo), "LO: 80 Hz shelf", db(lo))


def strips_table(rows):
    per = 6
    cells = [[Strip(r) for r in rows[i:i + per]] for i in range(0, len(rows), per)]
    t = Table(cells, colWidths=[Strip.W] * per, rowHeights=[Strip.H] * len(cells))
    t.setStyle(TableStyle([('GRID', (0, 0), (-1, -1), 0.3, GRID), ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                           ('LEFTPADDING', (0, 0), (-1, -1), 0), ('RIGHTPADDING', (0, 0), (-1, -1), 0),
                           ('TOPPADDING', (0, 0), (-1, -1), 0), ('BOTTOMPADDING', (0, 0), (-1, -1), 0)]))
    return t


def story():
    st = [Paragraph("EQ Settings, Channel by Channel", title),
          Paragraph(f"Starting points for the {B}'s channel EQ, drawn the way the knobs look on the board. Orange = moved from flat. These are places to begin while tracking, not rules; your mics, room and ears decide.", sub)]
    st += sec(f"The EQ section on each {B} channel, top to bottom", [
        "<b>LO CUT button:</b> a high-pass filter at 75 Hz, 18 dB per octave. Removes rumble, floor thumps, plosive pops and mic-stand noise below 75 Hz. It works even when EQ IN is off. <b>Use it on</b> vocals, toms, guitar amps, trumpet and room mics. <b>Never on</b> kick, bass, synths with low notes, or the drum machine: it takes the bottom off them.",
        "<b>HI knob:</b> a 12 kHz shelf, ±15 dB. Everything above about 12 kHz goes up or down together. <b>For:</b> air and sparkle on vocals, cymbals and acoustic guitar. <b>Don't:</b> boost it on dynamic mics that are already hissy, or on a trumpet; a 15 dB range is there for repair, 1-3 dB is a normal move.",
        "<b>HI MID knobs:</b> three of them. FREQ sweeps the center from 500 Hz to 18 kHz; BANDWIDTH sets how wide the band is, from 3 octaves (wide, gentle) to 1/12 octave (a surgical notch); the gain knob is ±15 dB. This is the presence band: 2-5 kHz is where a vocal or guitar cuts through, and also where things get harsh. <b>Don't:</b> boost a narrow band; narrow settings are for cutting problems (a ring, a whistle). Boosts should be wide.",
        "<b>LO MID knobs:</b> FREQ sweeps 45 Hz to 3 kHz and the gain is ±15 dB; the width is fixed at 2 octaves (broad). This is the mud band: 200-500 Hz is where drums get boxy and vocals get chesty. Most useful EQ moves on this console are small cuts here. <b>Don't:</b> boost it on more than one or two sources, or the mix turns to soup.",
        "<b>LO knob:</b> an 80 Hz shelf, ±15 dB. Weight and thump. <b>For:</b> kick, floor tom, bass. <b>Don't:</b> boost it on anything that isn't a bass instrument; low end piles up fast, and the cheap fix is LO CUT on everything that doesn't need lows.",
        "<b>EQ IN button:</b> switches the four EQ bands in or out (LO CUT stays active). Leave it out on any channel set flat, and use it to A/B your EQ: if \"in\" doesn't sound clearly better, set the knobs back to 0."])
    st += sec("Rules that matter more than any setting", [
        "Set trim and the compressor first, then EQ. The EQ is before the fader and the group outs and direct outs, so whatever you do here is recorded. Reaper's ReaEQ can do the fine work later with undo; the console EQ is for broad shaping and fixing real problems.",
        "Cut before you boost. A 3 dB cut at 300 Hz does what a 3 dB boost at 3 kHz does, with less noise and less chance of clipping.",
        "Find a problem by sweeping: boost the mid gain, turn the FREQ knob slowly until the ugly part jumps out, then turn the gain down to a cut at that spot.",
        "EQ moves of 1-3 dB are normal. If you need more than 6 dB, move the mic instead: an inch at the amp grille or a few inches on a vocal changes more than any knob.",
        "Which mic is on the channel matters. A condenser (Worker Bee) has more top and more low rumble: LO CUT on, go easy on HI. Dynamic mics (SM57, SM58, the knockoffs, Peavey) are a bit darker: small presence lifts are fine. The Turner 95D has almost no top or bottom to begin with. Line sources (synths, PV6, Tascam) usually want no EQ at all.",
        "Stereo pairs (rooms 5-6, Reface 12-13, SH-201 17-18, Tascam 23-24) get identical settings, or the image shifts.",
        "Listen in context. Solo makes everything sound like it needs more of everything. Decide with the band playing."])
    legend = Paragraph("Each strip reads top to bottom like the board: LO CUT and EQ IN buttons, HI shelf, HI MID (frequency, bandwidth, gain), LO MID (frequency, gain), LO shelf. Orange = set away from flat. Pointer straight up = 0 dB or the middle of the sweep.", note)
    st += [PageBreak(), Paragraph("Channels 1-6", h), legend, Spacer(1, 4), strips_table(EQ[0:6]), Spacer(1, 8),
           Paragraph("Channels 7-12", h), strips_table(EQ[6:12]),
           PageBreak(), Paragraph("Channels 13-18", h), strips_table(EQ[12:18]), Spacer(1, 8),
           Paragraph("Channels 19-24", h), strips_table(EQ[18:24]), PageBreak()]
    whyrows = [["Ch", "Source", "Why these settings"]] + [[r[0], r[1], r[10]] for r in EQ if r[10]]
    st += [Paragraph("Why each channel is set this way", h), tbl(whyrows, [0.4 * inch, 1.7 * inch, 5.4 * inch])]
    return st
