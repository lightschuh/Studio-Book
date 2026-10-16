from common import *


def story():
    rack = [["Position", "Unit", "Status", "Why it goes here"],
            ["1 (top)", "Behringer UMC1820", "In the rack", "Used most: gain knobs, front inputs 1-2, meters. Closest to the desk."],
            ["2", "Behringer ADA8200", "In the rack", "Direct-out channels record here (Reaper inputs 9-16); its outputs play Reaper tracks 9-16 to tape returns 9-16. Short optical cables to the UMC1820."],
            ["3", "DigiTech TSR-12", "In the rack", "Reverb/delay on aux send 1."],
            ["4", "Compressor: Klark Teknik 76-KT or dbx 1066", "Not bought yet", "Adjusted often while tracking."],
            ["5", "Delay / second effects unit", "Future", "On aux send 2 / aux return 2. Headphones for 3+ people are handled by personal mixers at the players' spots, not a rack headphone amp."],
            ["6", "Rack shelf with the computer", "Shelf on order", "A 2U vented shelf. The PC's own fan pulls air through the gap, which also keeps power-supply heat off the gear above. Leave the front of the shelf clear."],
            ["7", "Furman M-8x2", "On its way", "Everything plugs in here; one switch handles power."],
            ["8 (bottom)", f"Mackie {B} power supply", "In the rack", "Heaviest, runs warm, can put hum into nearby audio gear. Farthest from the UMC1820 and TSR-12."]]
    chan = [["Ch", "Source", "Cable", "Pan", "Records to (Reaper input)"]] + [[c[0], c[1], c[2], c[3], c[5]] for c in CH]
    direct_to = {ch: i + 1 for i, ch in enumerate(DIRECT_CH)}
    snake = [["#", "Color", "Recording (white tape)", "Playback 1-8 (black tape)", "Direct outs (blue tape)", "Playback 9-16 (yellow tape)"]]
    for i, col in enumerate(SNAKE_COLORS, 1):
        snake.append([str(i), col, f"Group out {i} {AR} UMC1820 in {i}" + (" (front)" if i <= 2 else ""),
                      f"UMC1820 out {i} {AR} tape return {i}" + (" (MAIN OUT)" if i <= 2 else ""),
                      f"Ch {DIRECT_CH[i-1]} direct out {AR} ADA8200 in {i}", f"ADA8200 out {i} {AR} tape return {i+8}"])
    cables = [["Cable", "Qty", "Use"],
              ["8-channel TRS snake, 20 ft", "2 owned + 1 needed", "Recording, playback 1-8, and direct outs to the ADA8200 (all 8 tails used). Eight single TRS cables also work for the third."],
              ["8-channel snake, 6 ft", "1 (swapping the 3 ft)", f"ADA8200 outputs {AR} tape returns 9-16. XLR (female) to TRS, or a TRS snake plus 8 XLR-to-TRS adapters. Not needed for stereo playback (Alternate Setups, Alternate B)."],
              ["XLR mic cable", "14 + 1 spare", "15-20 ft for drums, amps and trumpet; 25 ft for vocals and room mics."],
              ['1/4" TS line cable', "14", "Reface CS to ch 12-13 (2). SH-201 to ch 17-18 (2). E-drum module to PV6 (2). SamplePad 4 to PV6 (2). PV6 main out to ch 19-20 (2). Drum machine to ch 21 (1). TSR-12: aux send 1 to input, L/R outs to aux return 1 (3, short)."],
              ["Optical (TOSLINK) cable", "2", f"ADA8200 ADAT out {AR} UMC1820 optical in; UMC1820 ADAT out {AR} ADA8200 ADAT in."],
              ["MIDI cable (5-pin DIN)", "1", f"E-drum module MIDI out {AR} UMC1820 MIDI in."],
              ["Insert Y cable", "1 per compressor channel", "1 for the 76-KT (TRS to dual 1/4&quot;; TRS to dual XLR if using its XLR jacks). Two dbx 1066s would need 4."],
              ["Monitor line cables", "2", f'CONTROL ROOM out L/R {AR} Peavey 260 inputs. 1/4" TRS to 1/4" TS.'],
              ["Speaker cable", "2 runs", f"Peavey 260 outputs {AR} DIY monitors. Also needed between any guitar amp head and its cabinet. Never use an instrument cable for either."],
              ["Tascam 246 cables", "2 + 2", f'MAIN MIX out L/R {AR} 246 line inputs (2 x 1/4"). 246 line out L/R {AR} ch 23-24 (2 x RCA-to-1/4" if its outs are RCA).'],
              ["DJ mixer cables", "2", f'DJ mixer master or booth out {AR} PV6 inputs. Ends to match both mixers (often RCA-to-1/4").'],
              ["Instrument cables", "2 long, 1 medium, patch cables", f"Guitar {AR} pedalboard {AR} Diamond Vibrato {AR} Phase 90 {AR} amp; bass {AR} bass amp."],
              ["Reference cable", "1", f"3.5mm to dual RCA: phone or computer {AR} 2-TK input."],
              ["Long balanced cables", "2 (optional)", f"STUDIO OUTPUT L/R {AR} garage PA. Length to suit the run; ends to match the PA's inputs."]]
    st = [Paragraph("Studio Setup Map", title),
          Paragraph(f"Rack order, channel map, four snakes, effects routing and cables for the Mackie {B} studio. October 2026.", sub),
          Paragraph("Rack order (top to bottom)", h), tbl(rack, [0.8 * inch, 1.75 * inch, 1.0 * inch, 3.95 * inch]),
          Spacer(1, 4), Paragraph("The Peavey 260 power amp isn't rack-mount: it sits on a shelf near the rack with air around it.", note),
          Paragraph("Console channel and panning map", h),
          Paragraph("Groups 1-8 feed UMC1820 inputs 1-8 (Reaper 1-8). Direct outs feed ADA8200 inputs 1-8 (Reaper 9-16). Channel 22 is open.", cell), Spacer(1, 4),
          tbl(chan, [0.4 * inch, 2.0 * inch, 0.8 * inch, 0.8 * inch, 3.5 * inch]), Spacer(1, 4),
          Paragraph("<b>Group channels</b> (1-9, 12-13): press the group button for that pair (1-2, 3-4, 5-6 or 7-8) plus L/R to hear it. Pan picks the group, so keep these settings fixed. If they sound lopsided in the headphones, press MONO or use the AUX SEND 3/4 performer mix; neither changes the recording. "
                    "<b>Direct-out channels</b> (10-11, 14-18, 21): pan doesn't affect what's recorded, so set it for the headphones. Press L/R only, no group buttons. The direct out is after the EQ, fader and mute: keep faders near U (unity) and don't mute while recording. "
                    "<b>Monitor-only channels</b> (19-20 and 23-24): press L/R only; they aren't recorded through the console. "
                    "<b>Other layouts:</b> an all-direct-outs version of this map (every channel 1-16 on its own track, no groups) is in the Alternate Setups chapter, with how to switch.", note), Spacer(1, 3),
          Paragraph("<b>Mics:</b> every mic you own has a spot. Kick and snare mics on 1-2, room mics on 5-6, bass through its DI out. If the Turner moves to a mono room \"crush\" mic, vocal 3 needs another mic; an SM57 is the best add. "
                    "<b>Phantom power</b> is switched in blocks of eight channels (1-8, 9-16, 17-24): the Worker Bee on ch 10 puts 48V on the mic inputs of 9-16.", note)]
    st += [KeepTogether([Paragraph("Snake color order", h),
                         Paragraph("Same order on both ends of all four snakes. UMC1820 inputs 1-2 are on the front panel; inputs 3-8 are on the back.", cell), Spacer(1, 4),
                         tbl(snake, [0.3 * inch, 0.55 * inch, 1.6 * inch, 1.7 * inch, 1.65 * inch, 1.7 * inch]), Spacer(1, 4),
                         Paragraph("Check each color one at a time: brown into group out 1, confirm signal on input 1 in Reaper, then continue through black. "
                                   "UMC1820 outputs 1-2 are its MAIN OUT jacks, which follow the front MAIN OUT knob: turn that knob all the way up and leave it so playback tracks 1-2 match 3-8.", note)])]
    st += sec("UMC1820 and ADA8200 (Reaper inputs and playback 9-16)", [
        f"Recording: optical cable from the ADA8200's ADAT out to the UMC1820's optical in. Its line inputs 1-8 (on the front) take {B} direct outs from channels 10, 11, 14-18 and 21 through the third snake (blue tape).",
        f"16-track playback: second optical cable from the UMC1820's ADAT out to the ADA8200's ADAT in. The ADA8200's 8 outputs (XLR, on the back) feed tape returns 9-16 through the 6 ft snake (yellow tape). In Reaper, route tracks 9-16 to the 8 ADAT outputs; they play back on MIX-B channels 9-16.",
        "The ADA8200's outputs are XLR: use an XLR (female) to TRS snake, or 8 XLR-female-to-TRS-male adapters on the rack end of a TRS snake.",
        "Clock, with both optical cables connected: the UMC1820 is the master; set the ADA8200's SYNC switch to ADAT IN until it shows LOCKED.",
        "Clock, with only the ADA8200-to-UMC1820 cable: set the ADA8200 to its internal clock at the same sample rate as Reaper, and set the UMC1820's clock source to its optical input. Clicks and pops on inputs 9-16 mean the clock isn't set right.",
        "Keep Reaper at 44.1 or 48 kHz. At 88.2/96 kHz, ADAT carries only 4 channels."])
    st += sec(f"Aux sends on the {B}", [
        "Aux 1 and 2 have their own knobs on every channel and share one PRE button. Talkback can be sent into them.",
        "Aux 3-6 share two knobs: SHIFT up = aux 3 and 4, SHIFT down = aux 5 and 6, so one channel feeds 3/4 or 5/6, not both. One PRE button covers the pair. SOURCE sends the channel's tape return (MIX-B) instead of the live channel.",
        "The phones jacks can listen to aux 3/4 or 5/6, not 1/2. So: effects on aux 1 and 2 (PRE up), headphone mixes on aux 3-6 (PRE down).",
        "Aux 3/4 performer mix: on each channel the performer needs, SHIFT up, PRE down, aux 3 = left ear, aux 4 = right ear (equal for centered). AUX SEND 3 and 4 masters to about noon. On Phones 2 press AUX SEND 3/4 and raise its level. Phones 1 stays on MONITOR for you.",
        "Still open: aux 2 (second effect), aux 5/6 (a second performer mix or two mono cues), aux returns 2-4 (stereo line inputs for a delay or any extra source)."])
    st += sec("PV6 submixer, electronic drums, drum machine and DJ", [
        "Peavey PV6 as a monitor submixer: e-drum module, SamplePad 4 and DJ mixer into the PV6; PV6 main out into ch 19-20, panned L/R, L/R button only. Set the balance between them on the PV6 and the overall level on the console.",
        f"Keep the PV6's channel gains and master at unity (normal) settings to avoid adding hiss. Only monitor-only sources go through it; anything you want on its own track goes straight into the {B}.",
        "E-drums: record the pad as MIDI. Module MIDI out to the UMC1820's MIDI in, then record a MIDI track in Reaper. One pad can play any sound, so build parts one drum at a time and replace sounds later.",
        "Alesis SamplePad 4: main output into the PV6 with the e-drums. Record it as MIDI through its USB port to the computer. The UMC1820 has one MIDI in, which the e-drum module uses.",
        "1970s Roland drum machine: output to ch 21, recorded through its direct out on ADA8200 in 8 (Reaper 16). Use ch 22 if it has a stereo out.",
        "DJ sets: record on the DJ mixer's record out, or temporarily repatch the SH-201's ADA8200 inputs 6-7."])
    st += sec("Mic notes, acoustic guitar and pedalboard", [
        "Turner 95D: check the OHMS box on the label. High impedance: it needs an inline Hi-Z to low-Z matching transformer before the console's XLR input. Low (200 ohms): it needs an adapter or rewired cable from its Amphenol connector to XLR. Until that's sorted, keep it off channels 9-16 while the Worker Bee's phantom power is on. Great as a lo-fi vocal mic or a mono room mic crushed through a compressor.",
        "Acoustic guitar (overdubs): Worker Bee on ch 10, aimed at the 12th fret about 8-12 inches away. Ch 10 records through its direct out. Keep it off the PV6, which isn't recorded.",
        f"Pedalboard (720 looper, La Grotte, DBA Exploding Head, Big Muff, Cock Fight Plus, JHS gain): guitar {AR} drive and fuzz pedals {AR} Diamond Vibrato {AR} Phase 90 {AR} 720 looper {AR} amp. The Big Muff covers the fuzz role.",
        f"Marshall MG250DFX FX loop: drive and fuzz pedals go in front of the amp's front input; delay, reverb, modulation and the 720 looper can go in the loop instead (FX SEND {AR} pedals {AR} FX RETURN). The FX RETURN feeds the power amp directly: a guitar plugged straight in there sounds weak or silent, and anything in the return cuts off the preamp.",
        f"Synths through pedals, Kevin Parker style: SH-201 L out {AR} pedalboard {AR} ch 17. Keep the synth's volume low going in; synths run much hotter than guitars."])
    st += sec("Tascam 246 analog tape (once repaired)", [
        f"To tape: the {B}'s MAIN MIX out L/R feeds two 246 line inputs. Whatever is in the L/R mix (a Reaper playback, a stem, or a live take) goes to the cassette tracks you arm on the 246.",
        "From tape: the 246's stereo line out feeds ch 23-24. Balance its 4 tracks on the 246's own mixer; set overall level on the console. Keep ch 23-24 out of the L/R mix while recording to tape, or the tape output feeds back into its own input.",
        f"Levels: the {B} runs hotter than the 246. Start with the 246's input trims low and raise them until tape meters peak around 0 VU; push slightly past for more tape saturation.",
        "Capturing tape into Reaper: assign ch 23-24 to groups 7-8 (temporarily in place of the Reface CS) and record Reaper inputs 7-8. The cassette isn't synced to Reaper, so line takes up by ear or with a click at the start.",
        "Good uses: run drums or a full mix through tape for 70s-style saturation, or record 4-track ideas on the 246 by itself (its own mic inputs) and dump them in later."])
    st += sec("Capacity at a glance", CAP)
    st += sec("Open connections and planned additions", [
        f"Monitors: CONTROL ROOM outputs L/R {AR} Peavey 260 inputs (channel A = left, B = right; TRS-to-TS cables) {AR} speaker cable {AR} DIY passive monitors (Parts Express kit).",
        "Peavey 260 first use: tech check first. Speaker impedance at or above the amp's rated minimum (back panel). Level knobs low, CONTROL ROOM level low, then bring both up while watching the VU meters. Power it on last and off first.",
        f"AUX SEND 2 {AR} a delay (second effects unit, or a pedal with the send kept low) {AR} AUX RETURN 2.",
        f"Channel inserts {AR} compressor (76-KT, or a pair of dbx 266XS / 1066) with insert Y cables: drum pair, lead vocal, bass.",
        f"Channel inserts 1-4 {AR} Klark Teknik DN514+ quad gate (option) with 4 insert Y cables: kick, snare, rack tom, floor tom. Set thresholds with the drummer at full volume; use the LF/HF key filters so cymbals don't open the tom gates.",
        f"AUX SENDS 3-6 {AR} small personal headphone mixers, one per musician (aux 3 drums, 4 bass and guitars, 5 vocals and trumpet, 6 keys), or AUX SEND 3/4 {AR} an 8-channel headphone amp.",
        "Any mic input: Radial ProDI for a clean guitar or bass track for re-amping, or an acoustic pickup.",
        "2-TK input: phone or computer (3.5mm to RCA) for reference tracks; press 2-TK in the monitor section.",
        "Patchbay in the rack for inserts and repatching (groups 7-8 swaps, ADA8200 borrowing).",
        "Garage alternative: the Peavey 260 can also drive passive PA speakers from STUDIO OUTPUT, freeing both powered mixers for gigs."])
    st += sec("Garage PA (STUDIO OUTPUT)", [
        f"Feed one powered mixer (Phonic Powerpod 410 or Yamaha EMX62M) from the {B}'s STUDIO OUTPUT L/R. Choose its source in the MONITOR section and set level with the STUDIO knob.",
        f"Use it for playback or a monitor mix in the garage. TALKBACK {AR} PHONES &amp; STUDIO lets you talk to whoever is out there.",
        "For live shows, the other powered mixer can take the MAIN MIX outputs instead.",
        "Garage mics would need their own long XLR snake back to the console; not included here."])
    st += sec("TSR-12 reverb", [
        f"Wiring: {B} AUX SEND 1 {AR} TSR-12 left input; TSR-12 L/R outputs {AR} AUX RETURN 1 L/R.",
        "TSR-12: mix 100% wet; set input level so the meter peaks just under overload.",
        "Per channel: aux 1 to about noon, PRE up (not pressed). Master AUX SEND 1 to about noon; raise AUX RETURN 1 and assign it to L/R.",
        f"Don't press TALKBACK {AR} AUX SEND 1 while tracking. Reverb is monitor-only; Reaper records dry."])
    st += sec("Wiring the back", [
        "Power cords down one rear rail, audio cables down the other. Snakes through the wire basket.",
        "Keep the power supply's umbilical away from the snakes and the coiled snake slack; cross only at a right angle.",
        "Plug the power supply, UMC1820, ADA8200 and outboard gear into the Furman.",
        "The computer lives on a rack shelf below the headphone-amp space, so the USB run to the UMC1820 is short. Its power cord goes to the wall, not the Furman.",
        "If the window AC shares the wall circuit and causes clicks or hum, power the studio from another circuit."])
    st += [Paragraph("Cables", h), tbl(cables, [1.9 * inch, 1.5 * inch, 4.1 * inch])]
    return st
