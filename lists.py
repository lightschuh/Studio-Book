from common import *

D_ = "&mdash;"


def equipment():
    secs = [
        ("Recording and mixing", [
            ("Mackie", "24&bull;8", "8-bus analog console, with meter bridge and 220W power supply"),
            ("Behringer", "U-Phoria UMC1820", "Audio interface"),
            ("Behringer", "Ultragain Digital ADA8200", "8-channel mic preamp / ADAT expander"),
            ("Peavey", "PV6", "Mixer (monitor submixer: e-drums, SamplePad 4, DJ)"),
            ("Tascam", "246 Portastudio", "4-track cassette recorder (in repair)"),
            ("DigiTech", "TSR-12", "Rack effects processor"),
            ("Monoprice", "8-channel TRS snake (2), 20 ft", "Snake cables"),
            (D_, "8-channel snake, 3 ft", "Snake cable (swapping for 6 ft)"),
            (D_, "Rolling rack", "Equipment rack under the desk"),
            ("Cockos", "Reaper", "DAW (desktop PC)")]),
        ("Power", [("Furman", "Merit Series M-8x2", "Rackmount power conditioner (won on eBay, on its way)")]),
        ("Monitoring", [
            ("Peavey", "260 Stereo Booster Amplifier", "Vintage stereo power amp (for the DIY monitors)"),
            ("Sony", "MDR-7506", "Closed-back headphones (used)"),
            ("Sennheiser", "HD 280 Pro", "Closed-back headphones (used)")]),
        ("PA / powered mixers", [("Phonic", "Powerpod 410", "Powered mixer / PA"), ("Yamaha", "EMX62M", "Powered mixer")]),
        ("Microphones and wireless", [
            ("Neat", "Worker Bee", "Condenser microphone"),
            ("Shure", "SM57", "Dynamic microphone"), ("Shure", "SM58", "Dynamic microphone"),
            (D_, "SM58-style (3)", "Dynamic microphones"), ("Peavey", D_, "Dynamic microphone (came with PA)"),
            ("Turner", "95D", "Vintage dynamic microphone"),
            (D_, D_, "Snare, kick, and room mics"),
            ("Audio-Technica", "ATW-R3210", "UHF diversity wireless receiver"),
            ("Audio-Technica", "ATW-T3201", "Body-pack transmitter"),
            ("Behringer", "PS400 Micro Power", "Phantom power supply (not needed with the 24&bull;8)")]),
        ("Amplifiers", [("Magnatone", "M10 Custom", "Tube guitar amp"), ("Marshall", "MG250DFX", "2x12 guitar combo amp"),
                        ("Orange", D_, "Guitar amp"), ("Fender", D_, "Bass amp")]),
        ("Guitars", [("Silvertone", "ET-230 style (1960s)", "Electric guitar"), ("Schecter", D_ + " (7-string, white)", "Electric guitar"), (D_, D_, "Acoustic guitar")]),
        ("Keys, drums and electronics", [
            ("Yamaha", "Reface CS", "Synthesizer"), ("Roland", "SH-201", "Synthesizer"),
            ("Roland", D_ + " (1970s)", "Drum machine"), ("Roland", D_, "Electronic drum module + 1 pad"),
            ("Alesis", "SamplePad 4", "Percussion pad"), (D_, D_, "DJ setup"),
            (D_, D_, 'Drum kit: kick, 14" snare, 13" rack tom, 16" floor tom'),
            ("Overtone Labs", "Tune-bot", "Drum tuner")]),
        ("Pedalboard", [("Electro-Harmonix", "720", "Stereo looper"), ("Electro-Harmonix", "Big Muff", "Fuzz"),
                        ("Electro-Harmonix", "Cock Fight Plus", "Talking wah / fuzz"), ("Death By Audio", "Exploding Head", "Pedal"),
                        (D_, "La Grotte", "Pedal"), ("JHS", D_, "Gain pedal")]),
    ]
    st = [Paragraph("Studio Equipment List", title), Paragraph("Everything you own. Updated October 2026.", sub)]
    for name, rows in secs:
        t = tbl([["Make", "Model", "Type"]] + [list(r) for r in rows], [1.6 * inch, 2.2 * inch, 3.7 * inch], bold_first=False)
        st.append(KeepTogether([Paragraph(name, h), t]))
    st += [Spacer(1, 6), Paragraph("Not listed yet: the second pedalboard on the amp cart, and the makes and models marked with a dash. Send those and they'll be filled in.", note)]
    return st


def values():
    cats = [
        ("Console, rack and recording", [
            (f"Mackie {B} with meter bridge and 220W power supply", 600, 1200, "A refurbished 24x8x2 + power supply bundle was listed at $1,199.99 by a vintage dealer; private sales run lower."),
            ("Behringer UMC1820", 150, 200, ""), ("Behringer ADA8200", 150, 200, ""), ("DigiTech TSR-12", 50, 100, ""),
            ("Furman M-8x2", 60, 90, "Won on eBay."), ("Peavey PV6", 40, 80, ""),
            ("Tascam 246 Portastudio (not playing tape)", 75, 150, "Worth noticeably more once repaired."),
            ("Snakes: 2 x 20 ft TRS, 1 x 3 ft", 70, 100, ""), ("Rolling rack", 50, 100, "")]),
        ("Amplifiers", [
            ("Magnatone M10 Custom", 600, 1100, "Equipboard average about $740; a 1965 M10A in excellent working condition was listed at $1,349.99."),
            ("Marshall MG250DFX (2x12 combo)", 200, 300, "Solid-state stereo combo."),
            ("Fender bass amp and Orange guitar amp", 250, 900, "Models unknown; the biggest swing in this category."),
            ("Peavey 260 Stereo Booster Amplifier (1970s)", 75, 175, "Rough estimate; untested vintage power amp.")]),
        ("Guitars", [
            ("Silvertone ET-230 style (1960s, likely Teisco-made)", 300, 800, "Teisco built guitars for Sears' Silvertone line; the ET-230 is the 1960s Teisco \"sharkfin\" design. Originality and condition drive the price."),
            ("Schecter 7-string (white)", 200, 350, "Exact model unknown."),
            ("Acoustic guitar", 100, 400, "Brand and model unknown.")]),
        ("Synths, drums and electronics", [
            ("Yamaha Reface CS", 250, 330, ""),
            ("Roland SH-201", 350, 500, "Equipboard average about $395; a used one from Japan listed on eBay at $494."),
            ("1970s Roland drum machine", 300, 2000, "Model unknown. A CR-78 is the high end."),
            ("Roland e-drum module + 1 pad", 50, 150, ""), ("Alesis SamplePad 4", 80, 120, ""),
            ("DJ setup", 200, 800, "Brands and models unknown."),
            ('Drum kit (kick, 14" snare, 13" and 16" toms)', 200, 500, ""), ("Overtone Labs Tune-bot", 50, 80, "")]),
        ("Microphones, wireless and headphones", [
            ("Neat Worker Bee", 80, 120, ""), ("Audio-Technica ATW-R3210 + ATW-T3201", 150, 250, ""),
            ("Shure SM57", 60, 75, ""), ("Shure SM58", 60, 75, ""), ("SM58-style mics (3)", 30, 60, ""),
            ("Peavey mic", 15, 30, ""), ("Turner 95D (vintage)", 50, 150, ""), ("Kick, snare and room mics", 50, 150, "Models unknown."),
            ("Behringer PS400", 15, 25, ""), ("Sony MDR-7506 + Sennheiser HD 280 Pro (used)", 80, 100, "Priced at $40 each; both need pads.")]),
        ("Pedalboard", [
            ("Electro-Harmonix 720 looper", 100, 140, ""), ("Electro-Harmonix Big Muff", 50, 80, ""),
            ("Electro-Harmonix Cock Fight Plus", 100, 140, ""), ("Death By Audio Exploding Head", 120, 200, ""),
            ("La Grotte", 100, 200, ""), ("JHS gain pedal", 100, 180, "")]),
        ("Powered PA mixers", [("Phonic Powerpod 410", 100, 200, ""), ("Yamaha EMX62M", 100, 180, "")])]
    st = [Paragraph("Studio Equipment Values", title),
          Paragraph("Rough used-market estimates, October 2026. Low = quick private sale or rough condition; High = good condition, patient sale. The computer and the second pedalboard aren't included.", sub)]
    tots = []
    for name, rows in cats:
        t, (l, hh) = money_tbl(rows, ["Item", "Low", "High", "Notes"], [2.3 * inch, 0.65 * inch, 0.65 * inch, 3.9 * inch], [1, 2])
        tots.append((name, l, hh))
        st.append(KeepTogether([Paragraph(name, h), t]))
    L = sum(x[1] for x in tots); Hh = sum(x[2] for x in tots)
    tt = plain_tbl([["Category", "Low", "High"]] + [[n, f"${l:,}", f"${hh:,}"] for n, l, hh in tots] + [["Total", f"${L:,}", f"${Hh:,}"]], [3.6 * inch, 1.1 * inch, 1.1 * inch])
    st += [KeepTogether([Paragraph("Totals", h), tt, Spacer(1, 8),
                         Paragraph("Most likely value: around the middle of the range. The widest swings come from the drum machine model, the Fender and Orange amp models, the Silvertone, the DJ setup and the acoustic guitar. Replacing everything new would cost much more, probably $12,000-20,000+.", note), Spacer(1, 4),
                         Paragraph("For insurance: photograph each piece and record serial numbers. Researched prices (Mackie, Magnatone, SH-201) and the Silvertone/Teisco background come from dealer listings, eBay and Equipboard; all other figures are rough estimates, and prices change often.", note)])]
    return st, (L, Hh)
