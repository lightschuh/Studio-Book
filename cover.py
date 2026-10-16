"""TOAD STUDIO title page: a front-view line illustration of the desk, console, rack and planned additions."""
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from common import OUT

W, H = letter
NAVY = colors.HexColor('#1f3a5f'); INK = colors.HexColor('#2b2b2b'); PLAN = colors.HexColor('#b35c00')
WOOD = colors.HexColor('#8b5a2b'); WOOD2 = colors.HexColor('#6e4522'); STEEL = colors.HexColor('#3a3a3a')
PANEL = colors.HexColor('#5b5f66'); PANEL2 = colors.HexColor('#2e3136'); PAPER = colors.HexColor('#f7f4ee')
WALL = colors.HexColor('#dfe3e8'); CARPET = colors.HexColor('#cfc6b8'); LIGHT = colors.HexColor('#e8eef5')


def rr(c, x, y, w, h, fill, stroke=INK, r=3, lw=0.8, dash=None):
    c.setFillColor(fill); c.setStrokeColor(stroke); c.setLineWidth(lw)
    c.setDash(*dash) if dash else c.setDash()
    c.roundRect(x, y, w, h, r, fill=1, stroke=1); c.setDash()


def label(c, x, y, t, size=7, col=INK, bold=False, center=True):
    c.setFillColor(col); c.setFont("Helvetica-Bold" if bold else "Helvetica", size)
    (c.drawCentredString if center else c.drawString)(x, y, t)


def rack_unit(c, x, y, w, h, name, sub="", planned=False, knobs=8):
    rr(c, x, y, w, h, PANEL2 if not planned else PAPER, PLAN if planned else INK, 2, 0.8, (3, 2) if planned else None)
    col = PLAN if planned else colors.white
    label(c, x + w / 2, y + h - 9, name, 6.5, col, True)
    if sub:
        label(c, x + w / 2, y + 3, sub, 5, PLAN if planned else colors.HexColor('#bbbbbb'))
    # little knobs/jacks row
    c.setFillColor(PLAN if planned else colors.HexColor('#9aa0a8'))
    for i in range(knobs):
        kx = x + 14 + i * ((w - 28) / max(1, knobs - 1))
        c.circle(kx, y + h / 2 - 1, 1.6, fill=1, stroke=0)


def speaker(c, x, y, w, h, planned=True):
    rr(c, x, y, w, h, PAPER if planned else PANEL2, PLAN if planned else INK, 3, 0.9, (3, 2) if planned else None)
    c.setStrokeColor(PLAN if planned else colors.HexColor('#bbbbbb')); c.setLineWidth(0.8); c.setFillColor(colors.white if planned else PANEL)
    c.circle(x + w / 2, y + h * 0.38, w * 0.3, fill=1, stroke=1)
    c.circle(x + w / 2, y + h * 0.78, w * 0.12, fill=1, stroke=1)


def console(c, x, y, w, h):
    # body
    rr(c, x, y, w, h, PANEL, INK, 4, 1)
    # meter bridge
    rr(c, x + 6, y + h - 2, w - 12, 16, PANEL2, INK, 2, 0.8)
    c.setFillColor(colors.HexColor('#e9e4cf'))
    for i in range(2):
        c.roundRect(x + w - 60 + i * 24, y + h + 2, 18, 9, 1, fill=1, stroke=0)
    c.setStrokeColor(colors.HexColor('#888'))
    for i in range(24):
        c.line(x + 14 + i * ((w - 90) / 23), y + h, x + 14 + i * ((w - 90) / 23), y + h + 11)
    # 24 channel strips: knobs + fader
    strip_w = (w - 70) / 24
    for i in range(24):
        sx = x + 8 + i * strip_w + strip_w / 2
        c.setFillColor(colors.HexColor('#b9bec6'))
        for k in range(6):
            c.circle(sx, y + h - 14 - k * 9, 1.7, fill=1, stroke=0)
        c.setStrokeColor(colors.HexColor('#2a2a2a')); c.setLineWidth(0.8)
        c.line(sx, y + 8, sx, y + 34)
        c.setFillColor(colors.HexColor('#eeeeee')); c.rect(sx - 2.2, y + 14 + (i % 3) * 4, 4.4, 5, fill=1, stroke=0)
    # master section
    rr(c, x + w - 60, y + 6, 54, h - 14, PANEL2, INK, 2, 0.6)
    c.setFillColor(colors.HexColor('#b9bec6'))
    for r_ in range(4):
        for k in range(4):
            c.circle(x + w - 52 + k * 12.5, y + h - 20 - r_ * 10, 1.7, fill=1, stroke=0)
    c.setFillColor(colors.HexColor('#eeeeee'))
    for k in range(9):
        c.rect(x + w - 54 + k * 5.5, y + 12, 3.5, 5, fill=1, stroke=0)
    label(c, x + w / 2, y - 9, "Mackie 24•8", 7, INK, True)


def draw_cover(c):
    # background: wall and carpet
    c.setFillColor(WALL); c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(CARPET); c.rect(0, 0, W, 215, fill=1, stroke=0)
    c.setStrokeColor(colors.HexColor('#c2b9aa')); c.setLineWidth(0.5); c.line(0, 215, W, 215)

    # title
    c.setFillColor(NAVY); c.setFont("Helvetica-Bold", 44); c.drawCentredString(W / 2, H - 92, "TOAD STUDIO")
    c.setStrokeColor(NAVY); c.setLineWidth(1.2); c.line(W / 2 - 150, H - 104, W / 2 + 150, H - 104)
    c.setFillColor(colors.HexColor('#555555')); c.setFont("Helvetica", 11)
    c.drawCentredString(W / 2, H - 122, "The Studio Book")
    c.setFont("Helvetica", 9)
    c.drawCentredString(W / 2, H - 137, "Mackie 24•8 home studio, Champaign-Urbana  •  October 2026")

    # window AC, picture, lamp (room cues from the photo)
    rr(c, 420, 520, 120, 70, colors.HexColor('#cfd4da'), colors.HexColor('#9aa0a6'), 2, 0.6)
    rr(c, 430, 540, 100, 42, colors.HexColor('#4a4a4a'), colors.HexColor('#333'), 2, 0.6)
    c.setStrokeColor(colors.HexColor('#777')); c.setLineWidth(0.5)
    for i in range(5):
        c.line(435 + i * 20, 544, 435 + i * 20, 578)
    rr(c, 150, 520, 80, 64, colors.HexColor('#e9dcc3'), colors.HexColor('#8a6b3a'), 1, 1.5)
    label(c, 190, 548, "art", 7, colors.HexColor('#8a6b3a'))
    c.setStrokeColor(INK); c.setLineWidth(1.4); c.line(95, 215, 95, 540)
    c.setFillColor(colors.HexColor('#fff9e8')); c.setStrokeColor(colors.HexColor('#aaa')); c.setLineWidth(0.6)
    c.ellipse(70, 536, 120, 556, fill=1, stroke=1)
    c.setFillColor(INK); c.circle(95, 215, 9, fill=1, stroke=0)

    # desk
    DX, DY, DW = 110, 395, 500
    rr(c, DX, DY, DW, 16, WOOD, WOOD2, 2, 1)
    c.setStrokeColor(WOOD2); c.setLineWidth(1.5)
    for lx in (DX + 60, DX + DW - 60):
        c.line(lx, DY, lx, 215)
    c.setFillColor(colors.HexColor('#1f6fd1')); c.rect(DX + 40, DY, 10, 16, fill=1, stroke=0)  # blue tape, as in the photo

    # console on the desk
    console(c, DX + 50, DY + 16, 330, 62)

    # speakers clamped to the back edge of the desk (planned)
    for sx in (DX + 2, DX + DW - 50):
        c.setStrokeColor(PLAN); c.setLineWidth(1.2); c.setDash(3, 2)
        c.rect(sx + 16, DY + 8, 16, 16, fill=0, stroke=1)
        c.line(sx + 24, DY + 24, sx + 24, DY + 44)
        c.setDash()
        speaker(c, sx, DY + 44, 48, 70)
        label(c, sx + 24, DY + 126, "DIY monitor", 6, PLAN, True)
        label(c, sx + 24, DY + 118, "clamped to back edge", 5, PLAN)

    # computer screen on a swing arm, clamped to the desk right of the console
    ax = DX + 395
    c.setStrokeColor(PLAN); c.setLineWidth(1.6); c.setDash(3, 2)
    c.rect(ax - 7, DY + 10, 14, 14, fill=0, stroke=1)       # desk clamp
    c.line(ax, DY + 24, ax, DY + 64)                          # post
    c.line(ax, DY + 64, ax + 10, DY + 92)                     # arm
    c.setDash()
    rr(c, ax - 24, DY + 90, 60, 40, PAPER, PLAN, 2, 1, (3, 2))
    c.setFillColor(colors.HexColor('#dfe8f5')); c.rect(ax - 20, DY + 94, 52, 32, fill=1, stroke=0)
    label(c, ax + 6, DY + 107, "Reaper", 7, PLAN, True)
    label(c, ax + 6, DY + 138, "screen on swing arm", 6, PLAN)

    # rack under the desk
    RX, RY, RW = DX + 175, 224, 150
    c.setStrokeColor(STEEL); c.setLineWidth(3)
    c.line(RX, RY, RX, DY - 2); c.line(RX + RW, RY, RX + RW, DY - 2)
    c.setFillColor(STEEL)
    for wx in (RX + 6, RX + RW - 6):
        c.circle(wx, RY - 3, 4, fill=1, stroke=0)
    ux, uw = RX + 6, RW - 12
    y = DY - 22
    rack_unit(c, ux, y, uw, 17, "Behringer UMC1820", knobs=8); y -= 19
    rack_unit(c, ux, y, uw, 17, "Behringer ADA8200", knobs=8); y -= 19
    rack_unit(c, ux, y, uw, 17, "DigiTech TSR-12", knobs=5); y -= 19
    rack_unit(c, ux, y, uw, 17, "Klark Teknik 76-KT", "planned", True, 4); y -= 19
    rack_unit(c, ux, y, uw, 17, "Delay unit", "future", True, 5); y -= 33
    # rack shelf with the computer on it (shelf on order)
    c.setStrokeColor(PLAN); c.setLineWidth(1.2); c.setDash(3, 2)
    c.setFillColor(PAPER); c.rect(ux, y, uw, 5, fill=1, stroke=1); c.setDash()
    rr(c, ux + 28, y + 5, uw - 56, 26, PANEL2, INK, 2, 0.8)
    label(c, ux + uw / 2, y + 15, "PC", 7, colors.white, True)
    label(c, ux + uw / 2, y - 7, "rack shelf (on order)", 5.5, PLAN)
    y -= 24
    rack_unit(c, ux, y, uw, 17, "Furman M-8x2", "on its way", True, 1); y -= 21
    rack_unit(c, ux, y, uw, 18, "Mackie power supply", knobs=0)
    c.setStrokeColor(colors.HexColor('#999')); c.setLineWidth(0.5)
    for i in range(10):
        c.line(ux + 10 + i * 12, y + 4, ux + 10 + i * 12, y + 10)

    # Peavey 260 on a shelf, right of the rack
    rr(c, RX + RW + 30, 290, 100, 6, WOOD, WOOD2, 1, 0.8)
    c.setStrokeColor(WOOD2); c.setLineWidth(1.2)
    for lx in (RX + RW + 34, RX + RW + 126):
        c.line(lx, 215, lx, 290)
    rr(c, RX + RW + 36, 296, 88, 30, PANEL2, INK, 2, 0.8)
    c.setFillColor(colors.HexColor('#e9e4cf'))
    c.rect(RX + RW + 54, 304, 14, 9, fill=1, stroke=0); c.rect(RX + RW + 92, 304, 14, 9, fill=1, stroke=0)
    label(c, RX + RW + 80, 318, "Peavey 260", 6, colors.white, True)
    label(c, RX + RW + 80, 282, "power amp, own switch", 5, INK)

    # guitar case leaning on the right wall, as in the photo
    c.setFillColor(colors.HexColor('#6b4a2e')); c.setStrokeColor(INK); c.setLineWidth(0.8)
    p = c.beginPath(); p.moveTo(585, 215); p.lineTo(606, 215); p.lineTo(598, 390); p.lineTo(586, 390); p.close()
    c.drawPath(p, fill=1, stroke=1)

    # legend
    y0 = 150
    rr(c, 60, y0 - 70, W - 120, 100, colors.white, colors.HexColor('#cccccc'), 4, 0.6)
    label(c, 72, y0 + 14, "What's drawn", 8, NAVY, True, False)
    c.setStrokeColor(INK); c.setLineWidth(1); c.setDash(); c.rect(72, y0 - 2, 12, 8, fill=0, stroke=1)
    label(c, 90, y0, "In the studio now: Mackie 24•8 with meter bridge, UMC1820, ADA8200, TSR-12, Mackie power supply, the PC.", 7, INK, False, False)
    c.setStrokeColor(PLAN); c.setDash(3, 2); c.rect(72, y0 - 18, 12, 8, fill=0, stroke=1); c.setDash()
    label(c, 90, y0 - 16, "Planned: 76-KT, a delay unit, a rack shelf for the PC, Furman M-8x2, Peavey 260 on a side shelf, DIY monitors clamped to", 7, PLAN, False, False)
    label(c, 90, y0 - 27, "the back edge of the desk, and a computer screen on a swing arm clamped to the right of the console.", 7, PLAN, False, False)
    label(c, 90, y0 - 44, "Monitor placement: tweeters at ear height, each speaker the same distance from your head as they are from each other.", 7, INK, False, False)
    label(c, 90, y0 - 55, "Keep the swing arm on the opposite side from the Peavey's power cord so the screen cable never crosses the snakes.", 7, INK, False, False)

    c.setFillColor(colors.HexColor('#777')); c.setFont("Helvetica", 7)
    c.drawCentredString(W / 2, 28, "Josh Leitschuh  •  Contents on the next page")


def make(path):
    c = canvas.Canvas(path, pagesize=letter); c.setTitle("TOAD STUDIO")
    draw_cover(c); c.showPage(); c.save()
    return path
