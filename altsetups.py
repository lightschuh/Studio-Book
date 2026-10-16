from common import *


def story():
    st = [Paragraph("Alternate Setups", title),
          Paragraph(f"Other ways to wire the same studio. The Setup Map is the main plan and stays as it is; everything in this chapter is an option to try, with what changes, what it costs you, and how to switch back. New variations get added here as Alternate B, C and so on.", sub)]
    st += sec("How to use this chapter", [
        "Each alternate lists only what's <b>different</b> from the main plan. Anything not mentioned (rack, power, playback to the tape returns, clock, aux sends, monitoring outputs) stays exactly as the rest of the book describes.",
        "Every alternate here can be tried and undone in an afternoon by moving snake tails at the back of the console. Nothing needs buying. Alternates can be combined: for example, Alternate A's recording with Alternate B's playback, which is what the connection diagram at the end of this chapter shows."])

    # ---------------- Alternate A ----------------
    st += [Paragraph("Alternate A: all direct outs", h),
           Paragraph(f"Recording skips the eight groups. Each of channels 1-16 sends its own direct out to its own Reaper input, so channel 1 = Reaper track 1 through channel 16 = Reaper track 16, and each track plays back on the same channel's tape return. This is a standard way to track on an in-line console like the {B}: every source gets its own track, and the balance between them is decided in the mix instead of at tracking.", cell), Spacer(1, 4)]

    amap = [["Ch", "Source", "Records to", "Pan (headphones only)"],
            ["1", "Kick", "Direct out " + AR + " UMC1820 in 1 (Reaper 1)", "Center"],
            ["2", "Snare", "Direct out " + AR + " UMC1820 in 2 (Reaper 2)", "Center or slightly R"],
            ["3", "Rack tom", "Direct out " + AR + " UMC1820 in 3 (Reaper 3)", "10 o'clock"],
            ["4", "Floor tom", "Direct out " + AR + " UMC1820 in 4 (Reaper 4)", "2 o'clock"],
            ["5", "Room L", "Direct out " + AR + " UMC1820 in 5 (Reaper 5)", "Hard L"],
            ["6", "Room R", "Direct out " + AR + " UMC1820 in 6 (Reaper 6)", "Hard R"],
            ["7", "Bass (DI out or mic)", "Direct out " + AR + " UMC1820 in 7 (Reaper 7)", "Center"],
            ["8", "Magnatone (SM57)", "Direct out " + AR + " UMC1820 in 8 (Reaper 8)", "10 o'clock"],
            ["9", "Marshall or Orange", "Direct out " + AR + " ADA8200 in 1 (Reaper 9)", "2 o'clock"],
            ["10", "Lead vocal (Worker Bee)", "Direct out " + AR + " ADA8200 in 2 (Reaper 10)", "Center"],
            ["11", "ATW-R3210 wireless", "Direct out " + AR + " ADA8200 in 3 (Reaper 11)", "Center"],
            ["12-13", "Reface CS L/R", "Direct outs " + AR + " ADA8200 in 4-5 (Reaper 12-13)", "Hard L / hard R"],
            ["14", "Trumpet (SM58)", "Direct out " + AR + " ADA8200 in 6 (Reaper 14)", "1 o'clock"],
            ["15", "Vocal 2 (Peavey)", "Direct out " + AR + " ADA8200 in 7 (Reaper 15)", "10 o'clock"],
            ["16", "Vocal 3 (Turner 95D)", "Direct out " + AR + " ADA8200 in 8 (Reaper 16)", "2 o'clock"],
            ["17-18, 21", "SH-201 L/R, drum machine", "<b>Not recorded</b> in this layout (monitor only). See \"Recording more than 16\".", "As in the main map"],
            ["19-20, 23-24", "PV6, Tascam 246", "Monitor only, same as the main plan", "As in the main map"]]
    st += [KeepTogether([Paragraph("Alternate A channel map", h),
                         Paragraph("The sources stay on the same channels as the main map; only what the snakes plug into changes. Pans now affect only what you hear, so they can be set naturally (kick and bass centered) instead of hard left/right to pick a group.", cell), Spacer(1, 4),
                         tbl(amap, [0.75 * inch, 1.75 * inch, 3.3 * inch, 1.7 * inch])])]

    st += sec("Rewiring: what moves", [
        "<b>White-tape snake (recording 1-8):</b> unplug its console end from GROUP OUTS 1-8 and plug the same tails, in the same color order, into the DIRECT OUTS of channels 1-8. The UMC1820 end doesn't move.",
        "<b>Blue-tape snake (direct outs to the ADA8200):</b> move its console tails from the direct outs of channels 10, 11, 14, 15, 16, 17, 18, 21 to the direct outs of channels <b>9-16</b>, in color order (brown = ch 9 through black = ch 16). The ADA8200 end doesn't move.",
        "<b>Playback does not move.</b> The black-tape and yellow-tape snakes stay on tape returns 1-16. Reaper track N now plays back on channel N's own tape return, which is how this console was designed to be used.",
        "Label the console ends with a second strip of tape (\"ALT A\") so nobody has to guess which layout is plugged in."])
    st += sec("Settings that change", [
        "<b>Channel assign buttons:</b> on channels 1-16 press <b>L/R only</b>, no group buttons. The groups are no longer in the recording path; leave group faders down and the group L-R assign buttons up.",
        "<b>Channel faders 1-16 at U (unity), and leave them there while recording.</b> On the 24&bull;8 the direct out is taken after the EQ, the fader and the mute. Moving a fader changes the recorded level; muting a channel mutes its track. Set the level with the trim knob only, to -12 to -6 dBFS on Reaper's meters.",
        "<b>EQ is printed.</b> Whatever the channel EQ and LO CUT are doing goes onto the track. Keep it to corrective moves (LO CUT on vocals, a small cut where something's boomy) and save the real shaping for Reaper.",
        "<b>Inserts still work.</b> The 76-KT on a channel insert is recorded, because the insert sits ahead of the direct out in the channel.",
        "<b>Monitoring:</b> the hard-panned group issue goes away. With natural pans the control room and MONITOR headphones sound balanced without pressing MONO. Aux 3/4 performer mixes work the same as now.",
        "<b>Reaper:</b> save a second track template, \"Toad Studio tracking (direct)\", with tracks named in the order of the channel map above (track N = input N = console channel N). Outputs don't change.",
        "<b>UMC1820 and ADA8200:</b> same as now: gain knobs at minimum, UMC inputs 1-2 on LINE, not INST."])
    st += sec("Recording more than 16 at once", [
        "This layout records 16 sources, one per track. The main plan squeezes 20 sources into 16 tracks by blending some on the groups. If a session needs the SH-201 or the drum machine, swap a blue snake tail for that session: for example move the tail from ch 15's direct out to ch 17's and from ch 16's to ch 18's, and the SH-201 records instead of vocals 2 and 3.",
        "Or run a hybrid for that session: put the white snake's last tails back on GROUP OUTS 7-8, assign the SH-201 (ch 17-18) to groups 7-8, and give up the bass and Magnatone tracks (or move them to group pairs too). Hybrids work but are easy to get confused by; write down which tails are where."])

    rows = [["", "Main plan (groups + direct outs)", "Alternate A (all direct outs)"],
            ["Sources recorded at once", "20 sources onto 16 tracks", "16 sources, one per track"],
            ["Drums", "Toms and room mics blended onto one stereo pair (groups 3-4); balance fixed at tracking", "Every drum mic on its own track; balance decided in the mix"],
            ["Two guitar amps", "Blended onto group 6", "Separate tracks (8 and 9)"],
            ["Noise", "Groups add the bus summing stage", "Skips the bus; possibly quieter (test it, below)"],
            ["Recording level set by", "Trim, channel fader and group fader", "Trim only (faders fixed at U)"],
            ["Headphone pans", "Group channels hard L/R; MONO often needed", "Natural pans; no MONO needed"],
            ["Setup effort", "As in the Setup Map", "Simpler: L/R assign only on every channel"],
            ["Best for", "Big band takes with everything going", "Up to 16 sources when you want to mix later"]]
    st += [KeepTogether([Paragraph("Main plan vs Alternate A", h), tbl(rows, [1.5 * inch, 3.0 * inch, 3.0 * inch])])]

    st += sec("How the direct outs behave on the 24&bull;8", [
        "<b>After the EQ, fader and mute.</b> A direct out on this console is not a raw mic feed. Whatever the channel's EQ, fader and mute are doing is what gets recorded, so faders stay at U and nobody touches mutes during a take.",
        "<b>Unbalanced</b> (1/4\" TS). Fine at line level over the 20 ft snakes. Keep the snakes away from power cords; an unbalanced line picks up hum more easily than a balanced one.",
        "<b>Independent of the groups and the L/R mix.</b> The direct out works whether or not the channel is assigned anywhere, so the L/R assign is only for hearing the channel.",
        "<b>Noise.</b> Skipping the groups removes the bus summing stage from the recording path. Groups pick up a little hiss from every channel assigned to them, so a direct out can be quieter. How much depends on the console; the noise test below measures it."])
    st += sec("Where the computer comes back in", [
        "<b>Playback goes to the tape returns, never to channel inputs.</b> The 24&bull;8 is an in-line console: every channel has a second path (Mix-B) fed by its own tape return. UMC1820 outputs 1-8 feed tape returns 1-8 and the ADA8200's outputs feed tape returns 9-16, exactly as in the main plan. That gives 16 playback tracks while all 24 channel inputs stay free for sources. Plugging playback into channel inputs (for example channels 17-24) would give only 8 playback tracks and take away the channels that hold the SH-201, PV6, drum machine and Tascam.",
        "In this layout the returns line up one to one: channel N records track N, and channel N's tape return plays track N back. Press MIX-B in the monitor section and raise MIX-B LEVEL to hear playback.",
        "<b>The groups don't reach the main mix unless asked.</b> A group feeds the L/R mix only when its L-R assign button in the master section is pressed. In this layout leave all eight up."])
    st += sec("Monitoring and latency", [
        "<b>Headphones</b> plug into the console's PHONES jacks (Monitoring chapter). <b>Speakers</b> connect to CONTROL ROOM OUTPUTS L/R. Powered bookshelf speakers such as Edifiers need only a cable from 1/4\" TRS to their input (RCA or 3.5 mm on most models); turn CNTRL RM down before connecting them.",
        "<b>Zero latency for the performer.</b> The console sends each live mic straight to the headphones and speakers; the computer is not in that path.",
        "<b>Backing tracks and earlier takes come from the computer.</b> They play from Reaper through the tape returns, and new overdubs record into Reaper. Reaper shifts each recorded take back by the interface's latency so it lines up. This works as long as Reaper's input monitoring is off on the audio tracks (Reaper Setup, section 5)."])
    st += sec("The noise test (do this before deciding)", [
        "Set up one mic, say the kick mic on ch 1, with the trim at its normal recording setting.",
        "Main-plan path: ch 1 assigned to group 1, group fader at U, recording on Reaper track 1. Record 15 seconds of silence (nobody playing, the mic connected).",
        "Alternate path: move the white snake's brown tail from GROUP OUT 1 to ch 1's DIRECT OUT, ch 1 assigned to L/R only, fader at U. Record another 15 seconds of silence on the same track.",
        "In Reaper, solo each clip, turn up the master and listen on headphones, and compare their peak readings (or run each through a plugin meter). A difference of 3 dB or more is real; less than that and the groups weren't the problem, and hiss is more likely coming from trim set too high or a noisy source.",
        "If the groups do turn out noisier, also try pressing in only the group buttons you need (unassign every unused channel from the groups) in the main plan. That alone lowers bus noise."])
    st += sec("Switching back", [
        "Move the white snake back to GROUP OUTS 1-8 and the blue snake back to the direct outs of 10, 11, 14-18 and 21, re-press the group assign buttons from the Setup Map, and load the main Reaper template. Everything else in the book applies again unchanged."])

    # ---------------- Alternate B ----------------
    st += [Paragraph("Alternate B: stereo playback (two outputs)", h),
           Paragraph("Reaper plays the whole mix back to the console on two outputs instead of sixteen. The console still records all 16 inputs and still handles every live source and headphone mix; the mixing of recorded tracks happens in Reaper. Use it until the 6 ft playback snake is in place, or for good if you prefer to mix in the computer. It works with either the main plan or Alternate A.", cell), Spacer(1, 4)]
    st += sec("Alternate B wiring", [
        "UMC1820 outputs 1-2 (the MAIN OUT jacks) to <b>tape returns 1-2</b>, on the brown and red tails of the black-tape snake, which are already connected in the main plan. Nothing else is needed.",
        "Not used for playback: UMC1820 outputs 3-8, the ADA8200's outputs and the yellow-tape snake. The second optical cable (UMC1820 to ADA8200) is optional; with only one optical cable, set the ADA8200 to its internal clock and the UMC1820 to clock from optical (Setup Map).",
        "The UMC1820's front MAIN OUT knob controls outputs 1-2: keep it all the way up and use MIX-B LEVEL on the console as the playback volume."])
    st += sec("Alternate B settings", [
        "<b>Reaper:</b> every track's output goes to the master only; master to outputs 1/2. This is the \"Mix playback\" mode in Reaper Setup, section 4.",
        "<b>Console:</b> press MIX-B in the monitor section and raise MIX-B LEVEL to hear the playback in the control room and on MONITOR headphones.",
        "<b>Performer headphone mixes:</b> on channels 1 and 2, press SOURCE on the aux 3/4 section so those two aux knobs send the tape return (the Reaper mix) instead of the live channel. Raise them to put the backing track in the aux 3/4 mix. Channels 1 and 2 still record their live mics normally; SOURCE changes only what the aux hears. Or set the phones source to MIX-B plus AUX SEND 3&amp;4.",
        "<b>Overdubs:</b> the same as always. The live source goes through the console to the headphones with no latency, the backing track comes from Reaper, and Reaper's input monitoring stays off on audio tracks."])
    rows_b = [["", "16-track playback (main plan)", "Stereo playback (Alternate B)"],
              ["Cables", "Black and yellow snakes, 2 optical cables", "Two tails of the black snake"],
              ["Where recorded tracks are mixed", "On the console: each track on its own tape return, with MIX-B level, EQ and aux sends", "In Reaper, with plugins (Reaper Setup, section 7)"],
              ["TSR-12 and outboard on recorded tracks", "Per track, from the console", "On the whole mix only, or use Reaper plugins"],
              ["Backing track in headphones", "Any mix of tracks, set per track", "The Reaper mix as one stereo feed"],
              ["Best for", "Mixing on the console, analog summing, outboard on playback", "Writing, overdubs and mixing in the computer; fewer cables"]]
    st += [KeepTogether([Paragraph("16-track vs stereo playback", h), tbl(rows_b, [1.7 * inch, 2.9 * inch, 2.9 * inch])])]
    st += sec("Moving to 16-track playback later", [
        "Connect UMC1820 outputs 3-8 to tape returns 3-8 (the rest of the black snake), the second optical cable, and the ADA8200's outputs to tape returns 9-16 on the 6 ft snake. In Reaper, send each track to its own output as in the main template. Stereo playback still works at any time by sending tracks to the master only."])
    return st
