from common import *


def story():
    st = [Paragraph("Monitoring: Every Output and Where It Goes", title),
          Paragraph(f"The {B}'s monitor section explained button by button, every output the console has and what feeds it, and ready-made setups for the sessions you'll actually run. Button names are from the Mackie 8&bull;Bus manual.", sub)]
    outs = [["Output (rear panel)", "What's on it", "Where it goes in this studio", "Level control"],
            ["CNTRL RM OUT L/R", "Whatever source buttons are pressed in the MONITOR section, summed if MONO is in", f"Peavey 260 {AR} DIY monitors (the room speakers)", "CNTRL RM knob. Talkback drops it 20 dB."],
            ["STUDIO OUT L/R", "The same monitor-section selection as the control room", "Garage PA (powered mixer) when wanted", "STUDIO knob. Talkback does NOT drop it."],
            ["PHONES 1", "Its own five source buttons (below)", "Your headphones (MDR-7506)", "PHONES 1 level"],
            ["PHONES 2", "Its own five source buttons", "Performer headphones (HD 280 Pro)", "PHONES 2 level"],
            ["MAIN MIX OUT L/R", "The L/R mix: everything assigned L/R, at the main fader", "Tascam 246 inputs (for tape). Not used for speakers.", "Main L/R fader"],
            ["MIX-B OUT L/R", "The MIX-B bus: Reaper playback from the tape returns", "Spare. Could feed a playback-only cue later.", "MIX-B LEVEL"],
            ["AUX SEND 1-6", "Per-channel aux knobs, at each aux master", "1: TSR-12. 2: open. 3/4 and 5/6: performer mixes (also selectable on the phones)", "Aux masters"],
            ["GROUP OUTS 1-8, DIRECT OUTS", "Recording feeds", "UMC1820 and ADA8200 (see the Setup Map)", "Group masters; channel faders"]]
    st += [Paragraph("Every output the console has", h), tbl(outs, [1.3 * inch, 2.0 * inch, 2.5 * inch, 1.7 * inch])]
    st += sec("The MONITOR section, button by button", [
        "<b>Source buttons: L/R MIX, MIX-B, 2-TK (tape), EXTERNAL.</b> They pick what the control room and studio outputs carry, and you can press any combination; the sources add together. L/R MIX = the live mix at the main fader. MIX-B = Reaper playback coming back on the tape returns. 2-TK = the 2-TRACK INPUT jacks (your reference cable from a phone or computer). EXTERNAL = the EXTERNAL INPUT jacks (a spare stereo line in).",
        "<b>MONO.</b> Sums left and right for the speakers and the L/R meters. Press it to check that nothing disappears in mono, or to make hard-panned group channels sit in the middle of your headphones while tracking.",
        "<b>CNTRL RM level.</b> The room speaker volume, through the Peavey. Fully clockwise is unity; normal listening is well below that. Has no effect on headphones or on the recording.",
        "<b>STUDIO level.</b> Volume of the STUDIO OUT, which carries the same selection as the control room. In this studio that's the garage PA feed; leave it down when the garage isn't in use.",
        "<b>MIX-B section: MIX-B LEVEL and ASSIGN TO L/R MIX.</b> MIX-B LEVEL sets how loud Reaper playback is on the MIX-B bus. ASSIGN TO L/R MIX folds the playback into the main mix, which you'd use to hear a Reaper track while recording to tape, and should otherwise leave out so playback doesn't end up in a tape bounce by accident."])
    st += sec("The PHONES sections (Phones 1 and Phones 2)", [
        "Each has its own level knob, its own SOLO button, and five source buttons: <b>MONITOR, MIX-B, AUX SEND 3&amp;4, AUX SEND 5&amp;6, EXTERNAL.</b> You can press more than one.",
        "<b>MONITOR</b> = the same thing the control room speakers are getting, taken after the source buttons. The CNTRL RM knob and MONO do not touch the phones, so you can turn the room down to nothing and still hear everything in headphones.",
        "<b>MIX-B</b> = Reaper playback only. <b>AUX SEND 3&amp;4</b> and <b>5&amp;6</b> = the performer mixes built on those aux knobs (aux 3 left ear, aux 4 right). <b>EXTERNAL</b> = the EXTERNAL INPUT jacks, a private cue that appears on no channel.",
        "<b>Solo and headphones.</b> The solo bus only reaches a phones output whose MONITOR button is pressed. If Phones 2 is on AUX SEND 3&amp;4, pressing SOLO lights the Rude Solo light but the performer hears no change, which is exactly what you want: you can solo-check a channel without disturbing them. Solo is after the fader on this console; the SOLO level knob at its center detent makes a soloed channel match its unsoloed level."])
    st += sec("Talkback", [
        "The talkback mic is built into the console, just above the main L/R fader. Four momentary buttons send it to <b>AUX SEND 1, AUX SEND 2, TAPE SUBGRPS</b> (the L/R mix and all eight groups) and <b>PHONES/STUDIO</b>.",
        "To talk to a performer on Phones 2: hold PHONES/STUDIO. To talk to the garage: the same button, since it also feeds the STUDIO OUT.",
        "While talkback is held, the control room output drops 20 dB so the speakers don't feed back into the mic. The studio output is not dropped. Keep the garage PA modest if someone's talking back from out there.",
        "Never hold AUX SEND 1 or 2 or TAPE SUBGRPS during a take: AUX 1 would put your voice into the reverb, and TAPE SUBGRPS would put it into the recording.",
        "The talkback level knob starts at its center detent."])
    setups = [["Session", "MONITOR section", "Phones 1 (you)", "Phones 2 (performer)", "Notes"],
              ["Tracking a performer, you at the desk", "L/R MIX in. MIX-B in if they're playing to a Reaper track. MONO out.", "MONITOR", "AUX SEND 3&4, built from aux 3/4 (PRE down) on the channels they need, plus MIX-B if they need the playback", "Room speakers low or off while mics are open, so they don't bleed into the mics. Talk with PHONES/STUDIO."],
              ["Tracking yourself", "L/R MIX in, MIX-B in", "MONITOR, and MONO pressed in the monitor section if the hard-panned groups sound lopsided", "Unused or same as Phones 1", "MONO changes only what you hear, never the recording."],
              ["Full band, everyone in headphones", "L/R MIX and MIX-B in", "MONITOR", "AUX SEND 3&4 for the second person; everyone else on a personal mixer fed from aux 3-6", "Each aux pair is one stereo mix. The personal mixers are the headphone amps for players 3 and up."],
              ["Mixing in Reaper", "MIX-B in only. Everything else out.", "MONITOR, or nothing: use the speakers", "Off", "You're listening to Reaper's output on the tape returns. The console's channel faders are out of the path. Check in mono with MONO."],
              ["Reference track A/B", "Toggle between MIX-B (your mix) and 2-TK (the reference). Press only one at a time.", "MONITOR", "Off", "Match the two levels by ear with MIX-B LEVEL and the phone's volume before judging anything."],
              ["Recording to the Tascam 246", "L/R MIX in. Keep ch 23-24 out of L/R.", "MONITOR", "Off", "The 246 gets MAIN MIX OUT at the main fader. To hear the tape back afterwards, assign ch 23-24 to L/R and listen on L/R MIX; MIX-B has nothing to do with the tape."],
              ["Playback in the garage", "Same selection as the room; STUDIO knob up", "MONITOR", "Off", "STUDIO OUT mirrors the control room selection. Talkback reaches it undimmed."]]
    st += [Paragraph("Setups for common sessions", h), tbl(setups, [1.25 * inch, 1.6 * inch, 1.2 * inch, 1.7 * inch, 1.75 * inch])]
    st += sec("Rules that keep you out of trouble", [
        "Only the MONITOR section and the two PHONES sections decide what people hear. Nothing in them changes what Reaper records, so experiment freely.",
        "Open mics plus loud room speakers equals bleed and feedback. While tracking, monitor on headphones and keep CNTRL RM low; the Peavey's own knobs are the last line of defense.",
        "Press one of L/R MIX or MIX-B at a time when you need to know which is which. With both in, a Reaper track and the live mix add together, which is right for overdubs but confusing for troubleshooting.",
        "If you hear nothing in the room: check in this order: CNTRL RM knob, a source button pressed, Peavey level knobs, Peavey power. If you hear nothing in Phones 2: its level, a source button, and whether the aux 3/4 masters are up.",
        "If the performer hears your solo-checking, Phones 2 is on MONITOR. Switch it to AUX SEND 3&amp;4.",
        "If talkback feeds back: you're holding it with CNTRL RM too loud for a 20 dB dip, or the garage PA is loud enough to reach the mic. Turn the room down first."])
    return st
