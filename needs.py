from common import *

HEAD = ["Item", "Suggested model", "Qty", "Low", "High", "Notes"]
WID = [1.25 * inch, 1.55 * inch, 0.5 * inch, 0.55 * inch, 0.55 * inch, 3.1 * inch]

studio = [
    ("Ear pads: Sony MDR-7506", "Genuine Sony or aftermarket (Brainwavz, Wicked Cushions, GEVO)", "1 pair", 12, 22, "Aftermarket around $12 to $17; genuine Sony about $16 to $22."),
    ("Ear pads: Sennheiser HD 280 Pro", "Genuine Sennheiser pad kit or aftermarket", "1 set", 10, 25, "Aftermarket pairs around $10 to $15. Genuine kit (ear + headband pads) about $24, fits 2016 and newer units."),
    ("XLR cables", "15-20 ft for drums, amps and trumpet; 25 ft for vocals and room mics", "Up to 15", 90, 150, "Estimate for budget cables. The channel map uses 14 mic lines plus 1 spare; subtract any you already own."),
    ("Optical (TOSLINK) cable", "Any standard TOSLINK cable, 3-6 ft", "1", 8, 15, "Estimate. UMC1820 ADAT out to ADA8200 ADAT in, for 16-track playback and clock. Add one more if you don't have the ADA8200-to-UMC1820 cable yet."),
    ("Third 8-channel TRS snake", "Monoprice (to match yours) or Hosa CSS-801 / CSS-803", "1", 43, 56, "Direct outs from ch 10-11, 14-18 and 21 to the ADA8200 (all 8 tails). Eight single TRS cables also work. The two Hosa snakes in Cory's listing ($20 each) could cover this."),
]
sound = [
    ("FET compressor", "Klark Teknik 76-KT", "1", 135, 209, "$209 new; around $135 used. 1176-style, for squashed drums and vocals. Two dbx 1066s from Cory's listing ($150 each) are the alternative."),
    ("Insert (Y) cables", "TRS to dual TS insert cable", "2", 20, 40, "Estimate. One connects the 76-KT to a channel insert on the 24&bull;8; the second is a spare. Four channels of compression would need 4; add 4 more for the gate."),
    ("Vibrato pedal", "Diamond Vibrato (reissue)", "1", 249, 279, "About $249 to $279 new. The pedal Parker used on most Lonerism guitars. Needs a 9-18V supply; check whether one is included."),
    ("Phaser pedal", "MXR Phase 90", "1", 100, 100, "$99.99 new; often cheaper used. Needs a 9V adapter or battery."),
]
extras = [
    ("DIY passive monitor kit (pair)", "Parts Express C-Note MT kit, or the Hitmaker MT studio monitor kit", "1 pair", 160, 250, "C-Note pair with knock-down cabinets about $159.98; drivers, crossovers and cabinets included. Upper figure is an estimate for the Hitmaker. Check the impedance against the Peavey 260's rating."),
    ("Peavey 260 tech check", "Local amp tech", "1", 60, 150, "Rough estimate: clean controls, check capacitors, fit a grounded 3-prong plug if it has a 2-prong."),
    ("Line cables to the Peavey 260", '1/4" TRS (console) to 1/4" TS (amp)', "2", 15, 30, "Estimate. CONTROL ROOM out L/R to Peavey channels A and B."),
    ("Speaker cable", "Real speaker cable, length to suit", "2", 15, 30, "Estimate. Peavey outputs to the DIY monitors. Never instrument cables."),
    ("DI box", "Radial ProDI", "1", 80, 129, "About $80 used, around $129 new. Passive, with a -15dB pad and ground lift. Clean guitar/bass track for re-amping; acoustic with a pickup."),
    ("Rack shelf for the computer", "2U vented rack shelf (on order)", "1", 20, 40, "Estimate. Holds the PC in the rack above the Furman. A lip or strap so it can't slide when the rack rolls."),
    ("Monitor swing arm", "Desk-clamp monitor arm, VESA", "1", 25, 60, "Estimate. Clamps to the desk right of the console; keeps the screen off the console surface."),
    ("Speaker clamp mounts", "Pair of desk-edge clamp speaker brackets, or a DIY wood bracket", "1 pair", 20, 60, "Estimate. Mount the DIY monitors on the back edge of the desk, tweeters at ear height."),
    ("Reference cable", "3.5mm to dual RCA", "1", 5, 12, "Estimate. Phone or computer into the 2-TK input to A/B against reference tracks."),
]
options = [
    ("Alternative B: two dbx 266XS", "Drew's Facebook listing", "1 pair", 110, 110, "Four channels of clean compression plus a gate on each, for less than one 1066. Covers the drum pair (linked), lead vocal and bass. Doesn't give the 1176 crunch; the 76-KT or ReaComp still does that. Test every channel and gain-reduction meter."),
    ("Alternative C: two dbx 1066", "Cory's Facebook listing", "1 pair", 300, 300, "Same four channels, better built. Only worth it over the 266XS pair if the price comes down."),
    ("Quad noise gate", "Klark Teknik DN514+ (Facebook, $100, free shipping)", "1", 100, 100, "Fair price. Four channels on the inserts of kick, snare and both toms; cuts ring and cymbal bleed before it's recorded. Reaper can gate for free afterwards, so this is a convenience, not a must. Needs 4 insert Y cables."),
]
maybe = [
    ("Delay / second effects unit", "Used rack delay or multi-effects, e.g. TC Electronic D-Two, Boss RV/DD rack units, or a second TSR-12", "1", 60, 200, "Estimate. Aux send 2 to its input, outputs to aux return 2. Takes the rack slot the headphone amp would have used."),
    ("Personal headphone mixers", "Small 4-channel mixers with a headphone jack (Behringer Xenyx 502 class), one per extra player", "1-3", 30, 60, "Estimate, each. Fed from aux sends 3-6; each one doubles as that player's headphone amp. Replaces a rack headphone amp."),
    ("XLR-female to TRS-male adapters", "Any brand", "8", 15, 30, "Estimate. Only if the 6 ft snake from Todd is TRS on both ends (ADA8200 outputs are XLR)."),
]

_t = {}
for _k, _rows in (("studio", studio), ("sound", sound), ("extras", extras), ("maybe", maybe), ("options", options)):
    _t[_k] = (sum(r[3] for r in _rows), sum(r[4] for r in _rows))
L1, H1 = _t["studio"]; L2, H2 = _t["sound"]; L4, H4 = _t["extras"]; L3, H3 = _t["maybe"]
TOTALS = [
    ("Studio essentials", L1, H1),
    ("Essentials + Tame Impala sound", L1 + L2, H1 + H2),
    ("Essentials + Tame Impala + monitoring extras", L1 + L2 + L4, H1 + H2 + H4),
    ("Everything, including only-if-needed items", L1 + L2 + L3 + L4, H1 + H2 + H3 + H4),
]


def story():
    s = [Paragraph("Studio Gear Needs List", title),
         Paragraph("Checked against your Studio Equipment List (October 2026): only what's still missing. Low = budget, used, or lowest common price; High = new or bundle price. Tax and shipping not included.", sub)]
    t1, _ = money_tbl(studio, HEAD, WID, [3, 4]); t2, _ = money_tbl(sound, HEAD, WID, [3, 4])
    t4, _ = money_tbl(extras, HEAD, WID, [3, 4]); t3, _ = money_tbl(maybe, HEAD, WID, [3, 4]); t5, _ = money_tbl(options, HEAD, WID, [3, 4])
    s += [Paragraph("Studio essentials", h), t1, Paragraph("For the Tame Impala sound", h), t2,
          KeepTogether([Paragraph("Monitoring and recording extras", h), t4, Spacer(1, 3),
                        Paragraph("<b>Budget DI alternative:</b> Behringer DI400P, about $30 new. Pick one DI or the other; totals use the Radial ProDI.", note)]),
          KeepTogether([Paragraph("Only if needed", h), t3]),
          KeepTogether([Paragraph("Compressor alternatives and gate option (not in the totals)", h),
                        Paragraph("Decision: the 76-KT is the primary compressor and is in the totals above. These are the alternatives seen on Facebook Marketplace, kept here in case a 76-KT doesn't turn up or you want four channels later. Prices are the listed asking prices.", cell), Spacer(1, 4), t5])]
    tot = plain_tbl([["Estimated total", "Low", "High"]] + [[n, f"${l:,}", f"${hh:,}"] for n, l, hh in TOTALS], [3.4 * inch, 1.1 * inch, 1.1 * inch])
    dropped = [["Not on the list", "Why"],
               ["Audio interface", "You have the Behringer UMC1820, plus the ADA8200 for 8 more inputs."],
               ["Second 8-channel snake", "You have two 20 ft snakes: one for recording, one for playback."],
               ["Furman M-8x2 power conditioner", "Won on eBay; on its way."],
               ["Rack", "You have the rolling rack under the desk."],
               ["Power amp (Crown)", "Not needed: the Peavey 260 stereo power amp drives the DIY passive monitors."],
               ["Powered monitors (JBL 305P MkII)", "Replaced by the Peavey 260 + DIY passive monitors. Still the plug-and-play backup: $169 each new, about $80-124 used."],
               ["Graphic EQ (dbx 231)", "For correcting PA speakers and rooms, not studio recording; console EQ and ReaEQ cover it. Maybe for the garage PA."],
               ["Mic preamp", "Not needed: the 24&bull;8 has 24 preamps, plus 8 on the ADA8200."],
               ["More microphones, SM57s", "Every mic position is covered (SM57, SM58, 3 SM58-style, Peavey, Turner 95D, Worker Bee, drum and room mics). Another SM57 is the first add if you want one."],
               ["AT2020 condenser", "You have the Neat Worker Bee."],
               ["Lexicon MX200 reverb", "Your DigiTech TSR-12 covers reverb and delay on an aux send."],
               ["dbx 166XS compressor", "Replaced by the 76-KT, which suits the drum sound better. Reaper's free ReaComp covers the mix bus."],
               ["Mic stands", "Add stands only if you're short."],
               ["Patchbay and patch cables", "Nice to have, not needed to get started. Two are in Cory's listing at $20 each."],
               ["Headphones", "A used Sony MDR-7506 and Sennheiser HD 280 Pro at $40 each. Only replacement pads are listed."],
               ["Rack headphone amp (HA8000)", "Dropped to keep the rack slot for a delay unit. Personal mixers at the players' spots do the job and don't need rack space."],
               ["Fuzz Face, pedal power supply", "The Big Muff on your pedalboard covers fuzz. The Diamond Vibrato and Phase 90 still need their own supplies."]]
    dt = tbl(dropped, [2.2 * inch, 5.3 * inch])
    s += [KeepTogether([Paragraph("Totals", h), tot, Spacer(1, 4),
                        Paragraph("The Goal Studio Diagram on the next page shows where every item above plugs in once it's bought.", note)]),
          Paragraph("What's not on the list, and why", h), dt, Spacer(1, 8),
          Paragraph("Notes: Prices come from major retailers and used-market listings and change often. Items marked \"Estimate\" were not priced from a specific listing. The Tascam 246 repair isn't included. The Behringer PS400 isn't needed with the 24&bull;8, which has built-in phantom power.", note)]
    return s
