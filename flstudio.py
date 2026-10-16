from common import *


def story():
    st = [Paragraph("FL Studio Setup", title),
          Paragraph("The same studio in FL Studio instead of Reaper. The driver, sample rate, clock and all the wiring are identical to the Reaper page; what's different is how FL takes in audio, which runs through the Mixer rather than tracks. Recording external audio needs FL Studio Producer Edition or higher. Control names follow the FL Studio manual.", sub)]
    st += sec("What's the same as Reaper (don't redo it)", [
        "Behringer's UMC ASIO driver, 48 kHz, 24-bit, the same block size, the ADA8200 clocked to the UMC1820: all exactly as in the Reaper page, sections 1 and the clock notes in the Setup Map.",
        "Inputs 1-8 are the console groups, 9-16 are the ADA8200 (direct outs). Outputs 1-10 are the UMC1820's analog jacks (tape returns 1-8 on outputs 1-8), outputs 11-18 are the ADAT outs (tape returns 9-16).",
        "You still monitor through the console, not the computer. Latency and feedback rules are the same."])
    st += sec("1. Audio settings (once)", [
        "Options > Audio Settings (F10). Device: the Behringer UMC ASIO driver. The manual's own advice: use the manufacturer's ASIO driver; \"FL Studio ASIO\" is a compatibility fallback that adds latency and jitter, and ASIO4ALL is only for combining several devices. One interface means the Behringer driver.",
        "Sample rate 48000. Buffer length: start around 256 samples (about 5 ms); larger if you hear underruns, which FL shows as a counter in the Audio Settings window.",
        "Mixer menu > Disk recording: tick <b>Auto-unarm</b> so armed inserts drop out after a take, and <b>Latency compensation</b> so recorded clips line up with the Playlist.",
        "Options > Project general settings: default recording folder inside a dated project folder on the PC, same habit as Reaper."])
    st += sec("2. Map the 16 inputs to Mixer inserts (once, then save as template)", [
        "Open the Mixer (F9). On Insert 1, right-click the <b>Input</b> menu (top right of the insert, with the Recording Pickup selector in front of it) and choose <b>Auto-map</b>. FL assigns each device input to a successive insert: input 1 to Insert 1, through input 16 to Insert 16. It also disables those inserts' sends to the Master so the live input can't feed back; you see meters but hear nothing, which is correct because you're listening through the console.",
        "Mono vs stereo: the Input menu has a stereo list on top and a mono list below. For every mono source (kick, snare, bass, vocals, trumpet, drum machine) pick the mono entry so it feeds both sides. Use the stereo pairs only for inputs 3/4 (drums), 7/8 (Reface) and 14/15 (SH-201). Auto-map picks stereo pairs, so fix the mono ones by hand afterwards.",
        "Recording Pickup selector on each insert: <b>EXT</b> (external), the manual's recommendation, so the recording is the raw input before any insert effects.",
        "Name and color the inserts to match the console map (right-click the insert name, F2): 1 Kick, 2 Snare, 3-4 Drums, 5 Bass, 6 Guitars, 7-8 Reface / Tape, 9 Lead vocal, 10 Wireless, 11 Trumpet, 12 Vocal 2, 13 Vocal 3, 14-15 SH-201, 16 Drum machine.",
        "Link each insert to a Playlist track so takes land in a predictable place: right-click a Playlist track header > Track mode > Audio track > pick the insert. Do this for all 16, in order.",
        "File > Save as template (or save to Templates folder) as \"Toad Studio tracking\"."])
    out = [["Mixer insert", "Output (insert's OUT menu)", "Console tape return", "Note"],
           ["1-8 (groups)", "UMC outputs 1-8, one per insert", "Tape returns 1-8", "Pair inserts 3/4 and 7/8 as stereo outs 3-4 and 7-8."],
           ["9-16 (ADA8200)", "UMC outputs 11-18, one per insert", "Tape returns 9-16", "FL numbers the ADAT outs 11-18 exactly as Reaper does."],
           ["Master", "UMC outputs 1-2", "Tape returns 1-2", "The whole mix comes back on MIX-B when you only want a stereo return."]]
    st += [Paragraph("3. Playback back to the console", h), tbl(out, [1.3 * inch, 2.1 * inch, 1.4 * inch, 2.7 * inch]),
           Spacer(1, 4), Paragraph("Each insert's output is chosen in its OUT menu, next to the Input menu. By default everything goes to the Master; for 16-track overdubbing give each insert its own hardware output as above and leave the Master on 1-2. Keep the UMC1820's MAIN OUT knob all the way up; MIX-B level on the console is the volume.", note)]
    st += sec("4. Recording a take", [
        "Arm the inserts you're recording: click the <b>disk icon</b> at the bottom of each insert (selecting an input arms it automatically; check it's lit).",
        "Right-click the transport <b>Record</b> button and make sure <b>Audio</b> is ticked in the recording filter. This is the step everyone misses: with Audio unticked, FL records knob moves and notes but no sound.",
        "Left-click Record so it lights orange, then press Play. Recording runs until Stop. In Song mode with Auto-create audio clip on, the takes appear as Audio Clips on the linked Playlist tracks.",
        "Count-in: the one-click recording mic icon in the toolbar gives a 4-beat count-in and records straight into the Playlist; use it for quick takes. For the count-in click through the headphones, turn the metronome on and set it to count-in only.",
        "Levels: the same -12 to -6 dBFS target on the insert meters. Set it at the console trim; the insert fader is playback only.",
        "<b>Monitor external input: Off</b> on every audio insert (right-click the insert's input area). You hear yourself through the console; FL's monitoring would add a delayed copy. If a take comes back slightly early or late against the click, use the Audio input delay compensation control in the Mixer menu."])
    st += sec("5. MIDI for the e-drums and SamplePad", [
        "Options > MIDI Settings: enable the UMC1820 MIDI In (e-drum module) and the SamplePad 4 USB port as inputs. Set each to a different controller type only if FL asks; generic is fine.",
        "Add FPC (FL's drum sampler) or a drum VST on a Channel Rack channel, route it to a free Mixer insert (17 or above), and record the pad hits as a Pattern. One pad can be any drum; move notes in the Piano roll to re-assign them.",
        "FL records MIDI into Patterns by default, so for the pads use Pattern mode or make sure the Notes box is ticked in the recording filter."])
    st += sec("6. Mixing in FL: the plugins that replace outboard", [
        "Fruity Limiter in compressor mode, or Maximus, for bus compression; Fruity Parametric EQ 2 for surgery; Fruity Delay 3 for the aux-2 delay stand-in; Fruity Reeverb 2 for reverb.",
        "The room-mic crush: Fruity Limiter with ratio high, fast attack and release, 10-15 dB of gain reduction, on the room-mic insert, blended under the clean drums.",
        "Export: File > Export > WAV, 24-bit, for masters; MP3 320 for sharing, to a \"Mixes\" folder inside the project folder."])
    st += sec("Reaper or FL Studio for this studio?", [
        "Either works with everything in this book. The console does the tracking work in both cases; the computer is a 16-track tape machine.",
        "Reaper's track-per-input model maps onto the console more directly and its per-track hardware outputs are quicker to set up. FL Studio's strengths are the Channel Rack and Piano roll for the e-drums, SamplePad and drum machine programming.",
        "A reasonable split: track the band in Reaper, program beats and synth parts in FL, and move audio between them as WAV files. Both read the same 24-bit 48 kHz files, so nothing is lost."])
    st += sec("Troubleshooting", [
        "Nothing records: the recording filter's Audio box is unticked, or no insert has its disk icon lit, or the input is set on the insert but it's a stereo entry for a mono mic (you'll get one side only).",
        "FL sees only 2 inputs or none: Audio Settings isn't on the Behringer ASIO driver.",
        "A doubled, delayed sound while playing: Monitor external input is on. Turn it off; you're monitoring through the console.",
        "Takes land on the wrong Playlist track: the insert isn't linked to a Playlist track; set Track mode > Audio track on the track you want.",
        "Clicks on inputs 9-16 only: clock. The ADA8200's SYNC light must read LOCKED (Setup Map).",
        "Everything in the Playlist is a quarter-beat late: Disk recording > Latency compensation is off."])
    return st
