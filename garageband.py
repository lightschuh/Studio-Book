from common import *


def story():
    st = [Paragraph("GarageBand Setup", title),
          Paragraph("The same studio in GarageBand. Two things to know first: GarageBand runs on Mac and iPad only, so this page applies if a Mac joins the studio alongside the Windows PC; and GarageBand is built for small sessions, so it works for overdubs and demos but can't do the full 16-input band tracking the other pages describe. Control names follow Apple's GarageBand User Guide.", sub)]
    st += sec("What's different about GarageBand", [
        "<b>Simultaneous recording is limited.</b> Apple's guide says you can record to more than one audio track at a time but doesn't publish a cap; in practice GarageBand users report a ceiling of around 8 armed tracks. Treat it as an 8-input recorder: the console's groups 1-8 into the UMC1820, with the ADA8200's 8 extra inputs for overdubs one at a time. Logic Pro, GarageBand's big brother, removes the limit and opens GarageBand projects directly.",
        "<b>No ASIO.</b> On a Mac the UMC1820 and ADA8200 are class-compliant: no driver to install. The Mac's Core Audio sees the UMC1820 with all 18 inputs and 20 outputs.",
        "<b>Outputs are stereo only.</b> GarageBand sends everything to one stereo output pair. There is no per-track hardware output, so there is no 16-track playback to the tape returns. Playback comes back on tape returns 1-2 and you press MIX-B on the console. For per-track returns you need Logic, Reaper (which also runs on Mac), or Pro Tools.",
        "<b>Projects are fixed at 44.1 kHz</b> in GarageBand's settings (Preferences > Audio/MIDI > Sample rate offers 44.1 or 48 in recent versions; older versions are 44.1 only). Whichever you choose, set the UMC1820 and ADA8200 to match."])
    st += sec("1. Preferences (once)", [
        "GarageBand > Settings (Preferences) > Audio/MIDI. Output Device: <b>UMC1820</b>. Input Device: <b>UMC1820</b>. Sample rate 48 kHz if offered, otherwise 44.1 kHz, and set the ADA8200's switch and the UMC1820 to the same.",
        "In the same pane, set the buffer (I/O Buffer Size) to Medium or Small for tracking. GarageBand hides latency controls behind these presets.",
        "Audio MIDI Setup (in Applications > Utilities): confirm the UMC1820 shows 18 ins and 20 outs and the right sample rate. This app is where the Mac's clock and rate are set; GarageBand follows it.",
        "Settings > Advanced: tick <b>Show advanced tools</b>. Without it, Record Enable buttons and per-track input selection don't appear."])
    st += sec("2. Make the tracks and set their inputs", [
        "Track > New Track > Audio (mic icon), <b>Input: Input 1</b> for a mono source or <b>Input 1 + 2</b> for a stereo pair. Repeat per source; GarageBand asks for the input as you create each track, which is the quickest way to map the console channels.",
        "To change an input later: select the track, open the Smart Controls (B), and use the <b>Input</b> menu in the recording settings area, or double-click the track header for the track's inspector.",
        "Show the Record Enable buttons: Track > <b>Configure Track Header</b> (or Option-T), tick <b>Record Enable</b>. Apple's guide: the Record Enable button must be visible on each track you want to record to.",
        "Name and color the tracks to match the console map, and save the project as a template by keeping a blank copy called \"Toad Studio tracking\" (GarageBand has no template feature; File > Save As and duplicate it per session)."])
    tracks = [["GarageBand track", "Input (UMC1820)", "Console source", "Armable at once?"],
              ["Kick", "Input 1", "Group 1", "Yes"], ["Snare", "Input 2", "Group 2", "Yes"],
              ["Drums (stereo)", "Input 3 + 4", "Groups 3-4", "Yes"], ["Bass", "Input 5", "Group 5", "Yes"],
              ["Guitars", "Input 6", "Group 6", "Yes"], ["Reface / Tape (stereo)", "Input 7 + 8", "Groups 7-8", "Yes (this is the 8-input live set)"],
              ["Lead vocal", "Input 9", "ADA8200 1 (ch 10 direct out)", "As an overdub, or swap into the live set"],
              ["Wireless", "Input 10", "ADA8200 2", "Overdub"], ["Trumpet", "Input 11", "ADA8200 3", "Overdub"],
              ["Vocal 2", "Input 12", "ADA8200 4", "Overdub"], ["Vocal 3", "Input 13", "ADA8200 5", "Overdub"],
              ["SH-201 (stereo)", "Input 14 + 15", "ADA8200 6-7", "Overdub"], ["Drum machine", "Input 16", "ADA8200 8", "Overdub"],
              ["E-drums (Software Instrument)", "MIDI: UMC1820 MIDI In", "Pad", "Yes"], ["SamplePad (Software Instrument)", "MIDI: SamplePad USB", "Pad", "Yes"]]
    st += [Paragraph("3. The track layout", h), tbl(tracks, [1.7 * inch, 1.3 * inch, 1.9 * inch, 2.6 * inch]),
           Spacer(1, 4), Paragraph("For a live band take, arm the first eight (the group inputs) and record the drums, bass, guitars and keys together; the lead vocal goes down in the same pass only if you move it onto a group (assign ch 10 to group 7 or 8 instead of the Reface for that song). Everything on the ADA8200 inputs is then overdubbed one or two at a time, which is how most GarageBand records get made anyway.", note)]
    st += sec("4. Recording", [
        "Arm the tracks (Record Enable buttons). Apple's guide notes that record-enabling a track also lets you monitor the input in GarageBand; turn each armed track's <b>monitoring</b> off (the small speaker icon next to Record Enable, or in Smart Controls) because you're hearing yourself through the console and would otherwise get a delayed double.",
        "Set the metronome and count-in (the metronome and count-in buttons in the control bar; count-in length in Settings > Metronome). The count-in is also your click for lining up Tascam passes.",
        "Press Record (R), play, press Stop. Multiple takes on one track go into a take folder; click the take number to choose.",
        "Levels: the same -12 to -6 dBFS target on the track meters, set at the console trim. GarageBand's track volume is playback only; its recording level control (in Smart Controls) stays at 0 because the UMC1820's gain is at minimum and the console is doing the work.",
        "Punch-ins: Record > Autopunch (or the Autopunch button in the control bar) and drag the red punch range in the ruler."])
    st += sec("5. Playback back to the console", [
        "GarageBand's stereo output goes to UMC1820 outputs 1-2, which are tape returns 1-2. Press MIX-B on the console and raise MIX-B LEVEL. That's it; there is no per-track return.",
        "For a performer to hear a backing track and themselves, the console does the blend: MIX-B (GarageBand) plus the live channel on the aux 3/4 performer mix or on MONITOR.",
        "The UMC1820's front MAIN OUT knob sets outputs 1-2. Keep it all the way up."])
    st += sec("6. MIDI and the built-in instruments", [
        "The UMC1820's MIDI in and the SamplePad's USB port appear automatically in GarageBand once the Mac sees them. Create a Software Instrument track, pick a Drum Kit, and play the pad; GarageBand records the MIDI. Drummer tracks and Apple's drum kits are a real strength here for the one-pad-at-a-time method."])
    st += sec("7. Mixing: the plugins that replace outboard", [
        "Compressor and Channel EQ on every track (GarageBand's are Logic's, trimmed down). Delay and Reverb on the two master effect sends stand in for the TSR-12 and the aux-2 delay.",
        "For the room-mic crush: Compressor set to the Vintage FET model, ratio high, fast attack and release, pushed hard, on the room-mic track under the clean drums.",
        "Share > Export Song to Disk: WAV 24-bit for masters, AAC or MP3 for sharing."])
    st += sec("When to move up", [
        "You'll feel GarageBand's limits the first time the whole band wants to record together with vocals, or the first time you want each track back on its own console channel. Logic Pro is the natural step: same files, same look, no track limits, per-track outputs, and it opens every GarageBand project you've made. Reaper also runs on the Mac and would let the PC and Mac share one workflow."])
    st += sec("Troubleshooting", [
        "Only inputs 1-2 appear: Input Device isn't the UMC1820, or Show advanced tools is off.",
        "Tracks can't all be armed: you've hit the simultaneous-record ceiling. Record in two passes, or move to Logic or Reaper.",
        "Doubled, delayed sound: track monitoring is on. Turn it off; the console is your monitor.",
        "Clicks on inputs 9-16: sample rate mismatch between the project, the UMC1820 and the ADA8200. Set all three the same in Audio MIDI Setup and on the ADA8200.",
        "The project plays back at the wrong pitch after changing the rate: GarageBand resampled. Keep one rate per project from the start."])
    return st
