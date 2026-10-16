from common import *


def story():
    st = [Paragraph("Pro Tools Setup", title),
          Paragraph("The same studio in Pro Tools. Driver, sample rate, clock and wiring are identical to the Reaper page. Pro Tools adds one step the others don't have, the I/O Setup window, where every input and output has to exist as a named path before a track can use it. Control names follow Avid's current Pro Tools.", sub)]
    st += sec("What's the same as Reaper (don't redo it)", [
        "Behringer's UMC ASIO driver on Windows, 48 kHz, 24-bit, the ADA8200 clocked to the UMC1820: all as in the Reaper page and the Setup Map's clock notes.",
        "Inputs 1-8 are the console groups, 9-16 are the ADA8200. Outputs 1-10 are the UMC1820's analog jacks (tape returns 1-8 on 1-8), outputs 11-18 are the ADAT outs (tape returns 9-16).",
        "You monitor through the console, not the computer.",
        "Tier check before you start: Pro Tools Intro is limited to 8 audio tracks total, so it can't run this 16-input studio. Pro Tools Artist (16 simultaneous record inputs) is the minimum; Studio removes the limits. Check the current Avid tier table, since these numbers change."])
    st += sec("1. Session and Playback Engine (once)", [
        "Dashboard > Create: name it, <b>WAV, 24-bit, 48 kHz</b>, I/O Settings: Last Used. Pro Tools fixes the sample rate per session, so pick 48 kHz here and never change the UMC1820 or ADA8200 afterwards.",
        "Setup > Playback Engine. Playback Engine: the <b>Behringer UMC ASIO</b> driver (Windows lists ASIO drivers here). H/W Buffer Size: <b>256</b> for tracking; raise to 1024 when mixing with lots of plugins. Voices: leave at the default. Holding N while Pro Tools starts opens this window if the wrong device is stuck.",
        "Setup > Session (Ctrl+2): Clock Source should be <b>Internal</b> on the UMC1820 side. The ADA8200 follows it over ADAT (SYNC switch to ADAT IN, LOCKED light on)."])
    st += sec("2. I/O Setup (once, then export the settings)", [
        "Setup > I/O (Ctrl+Shift+I). This is the step that trips people up: Pro Tools only offers a track the paths defined here.",
        "<b>Input tab:</b> click <b>Default</b> to let Pro Tools create a path per physical input, then rename them to the console map. Make inputs 3-4, 7-8 and 14-15 stereo paths and leave the rest mono. Click a name to rename: Kick, Snare, Drums (3-4), Bass, Guitars, Reface/Tape (7-8), Lead vocal (ADA1), Wireless (ADA2), Trumpet (ADA3), Vocal 2 (ADA4), Vocal 3 (ADA5), SH-201 (ADA6-7), Drum machine (ADA8).",
        "<b>Output tab:</b> Default, then rename. Outputs 1-2 are the UMC1820's main jacks (tape returns 1-2); make them a stereo path called \"Main / Tape 1-2\". Outputs 3-8 mono paths \"Tape 3\" through \"Tape 8\" (or stereo pairs for 3-4 and 7-8). Outputs 11-18 are the ADAT outs: name them \"Tape 9\" through \"Tape 16\". Outputs 9-10 are the UMC1820's unused analog pair; leave them.",
        "<b>Bus tab:</b> leave the defaults. Set the <b>Monitor Path</b> (bottom of the Output tab) to Main / Tape 1-2.",
        "Click <b>Export Settings</b> and save as \"Toad Studio.pio\" so a new session can Import Settings instead of redoing this."])
    tracks = [["Track", "Input path", "Output path", "Console tape return"],
              ["Kick (mono)", "Kick (in 1)", "Tape 1", "1"], ["Snare (mono)", "Snare (in 2)", "Tape 2", "2"],
              ["Drums (stereo)", "Drums (in 3-4)", "Tape 3-4", "3-4"], ["Bass (mono)", "Bass (in 5)", "Tape 5", "5"],
              ["Guitars (mono)", "Guitars (in 6)", "Tape 6", "6"], ["Reface / Tape capture (stereo)", "Reface/Tape (in 7-8)", "Tape 7-8", "7-8"],
              ["Lead vocal (mono)", "Lead vocal (in 9)", "Tape 9 (out 11)", "9"], ["Wireless (mono)", "Wireless (in 10)", "Tape 10 (out 12)", "10"],
              ["Trumpet (mono)", "Trumpet (in 11)", "Tape 11 (out 13)", "11"], ["Vocal 2 (mono)", "Vocal 2 (in 12)", "Tape 12 (out 14)", "12"],
              ["Vocal 3 (mono)", "Vocal 3 (in 13)", "Tape 13 (out 15)", "13"], ["SH-201 (stereo)", "SH-201 (in 14-15)", "Tape 14-15 (outs 16-17)", "14-15"],
              ["Drum machine (mono)", "Drum machine (in 16)", "Tape 16 (out 18)", "16"],
              ["E-drums (Instrument track)", "MIDI: UMC1820 MIDI In, all", "Main / Tape 1-2", "1-2"], ["SamplePad (Instrument track)", "MIDI: SamplePad USB, all", "Main / Tape 1-2", "1-2"],
              ["Master Fader", "", "Main / Tape 1-2", "1-2 (MIX-B)"]]
    st += [Paragraph("3. The session template", h), tbl(tracks, [2.0 * inch, 1.9 * inch, 1.9 * inch, 1.7 * inch]),
           Spacer(1, 4), Paragraph("Track > New (Ctrl+Shift+N): make the mono and stereo audio tracks in one go, timebase Samples. Set each track's Input and Output selectors in the Mix window's I/O section (the two buttons above the fader). Then File > Save as Template, named \"Toad Studio tracking\", so Dashboard offers it under Templates. With each track on its own output, every Pro Tools track comes back on its own console tape return; switch all outputs to Main / Tape 1-2 when you only want a stereo return on MIX-B.", note)]
    st += sec("4. Recording", [
        "Record-enable tracks with the <b>R</b> button on each track (Alt-click arms every track). It blinks red when armed and stays solid once the transport is record-armed.",
        "Monitoring: you listen through the console, so Pro Tools shouldn't also feed you the live input. Leave <b>Options > Auto Input Monitoring</b> on (its default) and <b>Input Only Monitoring</b> off, and keep the console's tape-return channels for the tracks you're recording out of the L/R mix during the take. Bring them back in for playback. If you ever do monitor through Pro Tools, <b>Options > Low Latency Monitoring</b> bypasses plugins on armed tracks to keep the delay small.",
        "Transport: record button, then Play (or Ctrl+Space). For punch-ins, Options > <b>QuickPunch</b>, which lets you punch in and out on the fly with Ctrl+Space while rolling.",
        "Count-off: Setup > Click/Countoff Options: 2 bars, countoff only during record. Add a click track with Track > Create Click Track; its output can go to Main / Tape 1-2 so it reaches the headphones through MIX-B, and is also the click you'll use to line up Tascam passes.",
        "Levels: the same -12 to -6 dBFS target on the track meters. Pro Tools track meters are post-fader by default; Setup > Preferences > Metering lets you switch them to pre-fader, which is more useful while tracking.",
        "Setup > Preferences > Operation: Auto Backup on, every 5 minutes, keep 10. Sessions and audio into a dated session folder on the PC."])
    st += sec("5. MIDI for the e-drums and SamplePad", [
        "Setup > MIDI > Input Devices: tick the UMC1820 MIDI In and the SamplePad 4. Create two Instrument tracks, set each one's MIDI input to its device (all channels), and insert a drum instrument (Pro Tools ships with Boom and Xpand!2; a free third-party kit works too). Record-enable and record the pad hits as MIDI; re-assign notes to any drum afterwards in the MIDI Editor."])
    st += sec("6. Mixing: the plugins that replace outboard", [
        "Dyn3 Compressor/Limiter on the drum bus and master; EQ3 7-Band for surgery; Mod Delay III for the aux-2 delay stand-in; D-Verb for reverb. All ship with Pro Tools.",
        "The room-mic crush: BF-76 (Avid's included 1176 model) on the room-mic track, all four ratio buttons in, input pushed hard, blended under the clean drums. This is the closest in-the-box match to the 76-KT you're buying.",
        "Bounce: File > Bounce Mix, WAV 24-bit for masters, MP3 for sharing, to a \"Mixes\" folder in the session folder."])
    st += sec("Troubleshooting", [
        "A track's input menu only shows a few inputs: I/O Setup hasn't been defaulted or the paths aren't active. Setup > I/O > Input tab > Default.",
        "No sound from inputs 9-16 or clicks on them: clock. Session Setup clock on Internal, ADA8200 SYNC on ADAT IN and LOCKED.",
        "Audio outputs aren't selectable above 2: Playback Engine is on the wrong device, or the Output tab needs Default.",
        "Doubled, delayed sound while recording: Pro Tools' monitoring is reaching the console through the tape returns while the live channel is also in the mix. Take the tape-return channels out of L/R while tracking.",
        "\"Session sample rate doesn't match\": the UMC1820 is at a different rate than the session. Match it in the UMC control panel and the ADA8200 switch, then reopen the session.",
        "Pro Tools won't open the session's audio: it was moved without the Audio Files folder. Always move the whole session folder."])
    return st
