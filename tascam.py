from common import *


def story():
    st = [Paragraph("Tascam 246: Setup and Recording", title),
          Paragraph(f"How the 246 Portastudio connects to the {B}, how its own mixer is set, and the settings for recording to tape, bouncing, and getting four tracks back out. Everything here is for after the repair; it doesn't play tape yet. Control names follow the 246's panel.", sub)]
    st += sec("What's on the 246 (so the rest makes sense)", [
        "<b>Six input channels.</b> Channels 1-4 have a selector for MIC/LINE, OFF or REMIX (tape playback of that track). Channels 5-6 select MIC/LINE, OFF or LINE B (a pair of phono inputs on the back). Each channel has a trim with an overload LED, a two-band sweepable EQ (HI 1-8 kHz, LO 62 Hz-1.5 kHz, inner knob = cut/boost, outer = frequency), two post-fader effect sends, pan, and a fader. All inputs are unbalanced 1/4\".",
        "<b>Assign buttons per channel: L/1, R/2, 3, 4.</b> A channel goes to tape track 1 or 2 through L/1 and R/2 with the pan (left = 1, right = 2), and to tracks 3 and 4 directly. At mixdown, L/1 and R/2 are the stereo left and right program busses.",
        "<b>Four RECORD FUNCTION buttons</b> arm the tracks; the LED flashes when armed and stays lit while recording. <b>Four big VU meters</b> show the tape tracks; two smaller ones show the stereo mix, the monitor mix or the effect sends depending on the meter select button.",
        "<b>Monitor section:</b> a level and pan for each of the four tape tracks (this is its own little cue mixer), a MONO button, PHONES level, and a CUE / PGM button. In PGM you hear the mix going to tape; in CUE you hear the tape tracks through the monitor section. The INSERT button is for punch-ins.",
        "<b>Back panel:</b> four TAPE OUT phonos (one per track, straight off the tape), stereo program outs, monitor outs, two effect send outs, LINE B inputs, six channel insert jacks, and two dbx noise-reduction slide switches (all tracks, or track 4 alone).",
        "<b>Under the cassette door:</b> the tape speed switch, 1-7/8 or 3-3/4 ips. Use 3-3/4 ips for everything you record here; it's cleaner and brighter. 1-7/8 exists only to play tapes made on slower machines. The pitch control (±12%) has its own on/off switch; leave it off unless you're doing it on purpose."])
    conn = [["Direction", f"From", "To", "Cable", "Notes"],
            ["Console to tape", f"{B} MAIN MIX OUT L and R", "246 channels 5 and 6, selector on MIC/LINE (or LINE B phonos on the back)", '1/4" TRS to 1/4" TS, 2', f"The {B}'s main outs are +4 dBu balanced; the 246 inputs are -10 dBV unbalanced. Expect to keep the console's main fader lower than usual and the 246 trims low."],
            ["Tape back to console", "246 TAPE OUT 1-4 (phono), or the stereo program outs for a mixed pair", f"{B} ch 23-24 line inputs", 'RCA to 1/4" TS, 2 (or 4 if you want all four tracks on their own console channels)', "Ch 23-24 are the book's plan. For four separate tape tracks into the console at once, borrow ch 21-22 as well."],
            ["Into Reaper", f"{B} ch 23-24 assigned to groups 7-8", "UMC1820 inputs 7-8 (Reaper 7-8)", "Already wired", "Temporarily in place of the Reface CS. Record 23-24 in Reaper, then put the Reface back on 7-8."],
            ["Power", "246 integral mains lead", "Furman rear outlet 7 (the spare)", "", "Low draw. It can share the Furman switch with the rack."]]
    st += [Paragraph("Connections", h), tbl(conn, [0.95 * inch, 1.5 * inch, 1.65 * inch, 1.3 * inch, 2.1 * inch])]
    st += sec("Levels: the one thing that matters most", [
        f"Set the {B} side first, as in the Gain Staging Guide: whatever you're sending to tape should be peaking near 0 on the console's L/R meters with the main fader at U.",
        "Then turn the 246's channel 5/6 trims up from zero until the big VU meters for the armed tracks peak around 0 VU on the loudest parts. The overload LED next to the trim must not flash. Cassette has very little headroom above 0 VU; +3 is the ceiling, and with dbx engaged even that starts to crunch.",
        "For the saturation sound you're after, run the meters into the red on drums and bass by a VU or two, then listen back. The crunch you hear is the tape, and it's permanent. Back off if cymbals turn to mush.",
        "Leave the 246's channel faders at the 0 mark for the tape-in path; use the trims for level, the same rule as on the console.",
        f"If the tape comes back too quiet into the {B}, raise the trims on ch 23-24, not the 246's program faders."])
    eq = [["246 channel", "Used for", "Trim", "EQ HI (1-8 kHz)", "EQ LO (62-1.5k)", "Effect 1 / 2", "Pan", "Assign"],
          ["5", f"{B} main mix L", "To 0 VU", "Flat", "Flat", "Off", "Hard L", "L/1 (and 3 for a drum pass)"],
          ["6", f"{B} main mix R", "Match ch 5", "Flat", "Flat", "Off", "Hard R", "R/2 (and 4 for a drum pass)"],
          ["1-4 on REMIX", "Playback of tracks 1-4 at mixdown or bounce", "To taste", "Up to +3 dB at 5-6 kHz to put back the top tape loses", "Cut 2-3 dB around 250 Hz if muddy", "Off (the TSR-12 is on the console)", "Spread L/R to taste", "L/1 and R/2 = the stereo outs"],
          ["1-4 on MIC/LINE", "Recording straight into the 246 (4-track ideas away from the console)", "To 0 VU", "Flat to start", "Flat", "Off", "Per assign rule", "1 track each"]]
    st += [KeepTogether([Paragraph("246 channel settings", h), tbl(eq, [0.75 * inch, 1.35 * inch, 0.6 * inch, 1.2 * inch, 1.05 * inch, 0.95 * inch, 0.7 * inch, 0.9 * inch]),
           Spacer(1, 3), Paragraph(f"The rule for EQ on the 246: none on the way in. The console's EQ already shaped the sound, and anything you add here is baked into the tape. Use its EQ only on the way back out, and lightly. The console's ch 23-24 EQ (HI shelf +1 dB) is the planned place for that.", note)])]
    rec = [["Step", "Do this", "Watch for"],
           ["1", "Tape speed to 3-3/4 ips. dbx switch to the position for all four tracks (on). Pitch off. Clean tape, wound a few seconds past the leader.", "The dbx LED. Decide dbx on or off before recording and never change it between recording and playback: a tape recorded with dbx on and played with it off sounds pumped and dull, and the reverse is hissy."],
           ["2", f"Press RECORD FUNCTION on the track(s) you're recording. Set the 246 to PGM so you hear what's going to tape.", "The armed LEDs flash."],
           ["3", f"On the {B}: keep ch 23-24 OUT of the L/R mix (their L/R buttons up). Otherwise the tape output feeds back into its own input.", "If you hear a building howl or echo, this is why."],
           ["4", "Set levels as above: console to 0, then 246 trims to 0 VU on the armed tracks.", "Overload LEDs stay off."],
           ["5", "Press RECORD and PLAY together. Record the pass. Stop. Zero return.", "The counter: note where the take starts."],
           ["6", "Playback check: 246 to CUE, raise that track's level in the monitor section, and listen on the 246's own headphone jack, or set ch 23-24 into L/R on the console and listen there.", "Compare to the dry Reaper track. The difference is what tape did."],
           ["7", f"Capture into Reaper: assign ch 23-24 to groups 7-8, arm Reaper inputs 7-8, press play on the 246. Line the take up by ear or with the click at the start.", "There is no sync between the 246 and Reaper. Record a short click or count-in at the head of every tape pass so lining up is easy."]]
    st += [Paragraph("Recording a pass to tape, step by step", h), tbl(rec, [0.4 * inch, 4.2 * inch, 2.9 * inch])]
    st += sec("Using all four tracks", [
        "<b>Two stereo passes.</b> Pass one: console mix to tracks 1-2 (ch 5 to L/1, ch 6 to R/2). Pass two: a different mix or the same mix with heavier saturation to tracks 3-4 (ch 5 and 6 assigned to 3 and 4). Play all four back and blend them in the monitor section or on the console.",
        "<b>Drums-only crush.</b> Send only the drum groups to the console's L/R (mute everything else, or use the group masters), tape them to 3-4 with the meters hot, then capture that pair into Reaper as a parallel \"tape drums\" track to blend under the clean ones. This is the closest thing to the Tame Impala drum sound you can do without a reel-to-reel.",
        "<b>Bouncing inside the 246.</b> Put channels 1-3 on REMIX, assign them all to track 4, arm 4, record. Tracks 1-3 are now mixed onto 4 and can be re-used. Each bounce adds hiss and loses some top, so bounce once, not twice, and record the loudest sources last.",
        "<b>Four-track songwriting away from the console.</b> Channels 1-4 on MIC/LINE, one source per track, a mic straight into a 1/4\" input. The 246 is a complete little studio on its own; dump the four TAPE OUTs into the console later.",
        "<b>Punch-ins.</b> Set the 246 to CUE with INSERT on, play up to the spot, press RECORD at the punch point; the monitor switches from tape to input at that moment. The optional footswitch jack does the same hands-free."])
    st += sec("Things that go wrong", [
        "Playback sounds dull and pumpy, or bright and hissy: dbx mismatch between record and play. Match the switch and try again.",
        "Howling or a slap echo when ch 23-24 are up: feedback loop. Take 23-24 out of L/R while recording to tape.",
        "Wow and flutter (pitch wobble): a worn belt or pinch roller, which is probably part of the repair. Also check that the pitch control is switched off.",
        "One channel of the pair is quiet: a trim mismatch between 246 ch 5 and 6, or the console's main L/R fader isn't the stereo pair you think (it is on the 8•Bus; check the sub-master assignment).",
        "The tape dropouts on track 4: the dbx switch for track 4 is separate for a reason. Try it off for that track if you're recording a sync tone or a click there.",
        "Head cleaning: cotton swab and isopropyl on the heads, capstan and pinch roller every few hours of use. Dirty heads lose high end before anything else."])
    return st
