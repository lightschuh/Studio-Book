from common import *


def story():
    st = [Paragraph("Reaper Setup", title),
          Paragraph(f"Getting Reaper on the PC to see all 16 inputs and 16 outputs through the UMC1820, with a track template that matches the console channel map, playback going back to the tape returns, MIDI for the pads, and recording settings that leave headroom.", sub)]
    st += sec("1. Driver and audio device (once)", [
        "Install Behringer's UMC driver for Windows from Behringer's site before plugging the UMC1820 in. Use the ASIO driver, not Windows' built-in WASAPI or DirectSound: ASIO is the only mode that exposes all 18 inputs and 20 outputs and gives low latency.",
        "In Reaper: Options > Preferences > Audio > Device. Audio system: <b>ASIO</b>. ASIO driver: <b>UMC ASIO Driver</b> (the name on your system may say BEHRINGER UMC). Enable inputs: first <b>1</b>, last <b>16</b>. Enable outputs: first <b>1</b>, last <b>18</b>.",
        "Sample rate: <b>48000</b> (or 44100). Never 88.2 or 96 kHz: ADAT drops to 4 channels and inputs 13-16 vanish. Set the same rate on the ADA8200's switch. Block size: start at <b>256</b>; go to 128 if headphone latency bothers performers, 512 if you hear clicks.",
        "Click ASIO Configuration to open the UMC control panel and confirm the sample rate and clock there too. The UMC1820's inputs 9-16 are the ADAT input (the ADA8200); 17-18 are S/PDIF, which you aren't using.",
        "Preferences > Project > Media: recording format <b>WAV, 24-bit</b>. 24-bit is what gives you room to record at -12 dBFS without losing anything."])
    st += sec("2. Name the inputs and outputs (once)", [
        "Preferences > Audio > Device > Input channel name aliasing: name them so the track-input menu reads like the console map. Inputs 1-8 are the groups; 9-16 are the ADA8200.",
        "Suggested names: 1 Kick (grp1), 2 Snare (grp2), 3 Drums L (grp3), 4 Drums R (grp4), 5 Bass (grp5), 6 Guitars (grp6), 7 Reface L / Tape L (grp7), 8 Reface R / Tape R (grp8), 9 Lead vocal (ADA1), 10 Wireless (ADA2), 11 Trumpet (ADA3), 12 Vocal 2 (ADA4), 13 Vocal 3 (ADA5), 14 SH-201 L (ADA6), 15 SH-201 R (ADA7), 16 Drum machine (ADA8).",
        "Output aliasing: 1-2 Tape ret 1-2 (UMC main), 3-8 Tape ret 3-8, 9-10 unused (UMC 9-10), 11-18 Tape ret 9-16 (ADAT to the ADA8200). Reaper numbers the UMC1820's outputs 1-10 as the analog jacks and 11-18 as ADAT; the console's tape returns 9-16 are therefore Reaper outputs 11-18."])
    tracks = [["Reaper track", "Input", "Record arm default", "Output (playback)", "Console channel it plays back on"],
              ["1 Kick", "Mono 1", "Armed in the drum template", "Out 1", "Tape return 1"],
              ["2 Snare", "Mono 2", "Armed", "Out 2", "Tape return 2"],
              ["3-4 Drums (toms + rooms)", "Stereo 3/4", "Armed", "Outs 3/4", "Tape returns 3-4"],
              ["5 Bass", "Mono 5", "Armed", "Out 5", "Tape return 5"],
              ["6 Guitars", "Mono 6", "Armed", "Out 6", "Tape return 6"],
              ["7-8 Reface CS (or Tascam capture)", "Stereo 7/8", "Off until used", "Outs 7/8", "Tape returns 7-8"],
              ["9 Lead vocal", "Mono 9", "Armed", "Out 11", "Tape return 9"],
              ["10 Wireless", "Mono 10", "Off until used", "Out 12", "Tape return 10"],
              ["11 Trumpet", "Mono 11", "Off until used", "Out 13", "Tape return 11"],
              ["12 Vocal 2", "Mono 12", "Off until used", "Out 14", "Tape return 12"],
              ["13 Vocal 3", "Mono 13", "Off until used", "Out 15", "Tape return 13"],
              ["14-15 SH-201", "Stereo 14/15", "Off until used", "Outs 16/17", "Tape returns 14-15"],
              ["16 Drum machine", "Mono 16", "Off until used", "Out 18", "Tape return 16"],
              ["17 E-drums (MIDI)", "MIDI: UMC1820 MIDI in, all channels", "Armed when the pad is in use", "Out 18 (shares the drum machine's return) or the main 1/2", "Tape return 16, or 1-2"],
              ["18 SamplePad (MIDI)", "MIDI: SamplePad USB, all channels", "Off until used", "Main 1/2", "Tape returns 1-2"],
              ["MASTER", "", "", "Outs 1/2", "Tape returns 1-2 (MIX-B)"]]
    st += [Paragraph("3. The track template (matches the console map)", h), tbl(tracks, [1.6 * inch, 1.35 * inch, 1.2 * inch, 1.5 * inch, 1.85 * inch]),
           Spacer(1, 4), Paragraph("Build this once, then File > Project templates > Save project as template, named \"Toad Studio tracking\". Every new session starts from it. Set each track's input with the small IN button on the track panel, and its output in the track's Routing window: untick \"Master send\" and add a hardware output to the out listed above. The MASTER goes to outs 1/2 so a quick mix comes back on tape returns 1-2 when you press MIX-B.", note)]
    st += sec("4. Playback back to the console", [
        "Two ways to hear Reaper, pick per session. <b>Per-track playback:</b> every track to its own hardware out as in the table, so each Reaper track comes back on its own console tape return and you mix on the console's MIX-B section (or flip the channel to TAPE). That's the 16-track overdub setup.",
        "<b>Mix playback:</b> tracks send to the master only, master to outs 1/2, and the whole mix comes back on tape returns 1-2. Simpler for writing and for mixing in Reaper; press MIX-B on the console and you hear it.",
        "The UMC1820's front MAIN OUT knob sets outs 1-2 only. Keep it all the way up; the console's MIX-B level is your volume.",
        "Don't route a track to the same hardware out as the input it's recording from while the console channel is in the L/R mix: that's a feedback loop through the console. The per-track plan avoids it because recording comes from group/direct outs and playback goes to tape returns, which are separate paths."])
    st += sec("5. Recording settings", [
        "Preferences > Audio > Recording: <b>input monitoring off</b> on all audio tracks (the track panel's monitor button). You're hearing yourself through the console, with zero latency; Reaper's monitoring would add a delayed copy. Turn Reaper monitoring on only for the MIDI tracks, which need it to hear the virtual drums.",
        "Record mode (Options > Record mode): <b>Normal</b> for tracking. Use <b>Time selection auto punch</b> for punch-ins; it starts and stops recording at the selection edges.",
        "Levels: the whole book aims for peaks around -12 to -6 dBFS on the Reaper meters. At 24-bit that's plenty. If a track's meter is touching the top, fix it at the console trim, not with Reaper's input gain (there isn't one; the fader is playback only).",
        "Pre-roll and count-in: Preferences > Audio > Recording > \"Count-in before recording\": 2 bars, and the metronome on during count-in only. The count-in through the headphone mix is also the click you'll use to line up Tascam passes.",
        "Project settings (Alt+Enter): BPM and time signature per song; <b>Timebase for items: Time</b>, so a later tempo change doesn't stretch recorded audio.",
        "Autosave: Preferences > Project > \"Save project every 5 minutes\" and \"when recording stops\". Record files into a dated project folder on the PC, not a USB drive."])
    st += sec("6. MIDI for the e-drums and SamplePad", [
        "Preferences > Audio > MIDI Devices: enable <b>UMC1820 MIDI In</b> (the e-drum module) and the <b>SamplePad 4</b> USB MIDI port as inputs. Enable UMC1820 MIDI Out only if you want Reaper to drive the module's sounds.",
        "On the MIDI tracks, insert <b>ReaSamplOmatic5000</b> or a drum instrument plugin (the free MT Power Drum Kit works well for the one-pad-at-a-time method) and arm with monitoring on. Record the pad hits as MIDI notes, then move or re-pitch notes to any drum sound afterwards.",
        "To record the module's own sounds as audio instead, that's the PV6 path on console channels 19-20, which is monitor-only by design. Use the MIDI path for anything you want to keep."])
    st += sec("7. Mixing in Reaper: the plugins that replace outboard", [
        "<b>ReaComp</b> on the drum bus and master does the clean bus compression the dbx units would. <b>ReaEQ</b> for anything beyond the console's broad strokes. <b>ReaDelay</b> and <b>ReaVerb</b> stand in for the aux-2 delay until you buy one.",
        "For the Tame Impala crush in the box: a free 1176-style plugin on the room-mic track, or ReaComp with ratio 20:1, fast attack, fast release, pushed 10-15 dB, blended under the clean drums. Not as good as the real 76-KT, but close for demos.",
        "Render (File > Render): WAV 24-bit for masters, MP3 320 for sharing. Render to a \"Mixes\" folder inside the project folder with the date in the filename."])
    st += sec("Troubleshooting", [
        "Reaper shows only 8 inputs: audio system isn't ASIO, or last input is set to 8. Both are in Preferences > Audio > Device.",
        "Inputs 9-16 are silent or clicky: the ADA8200 and UMC1820 aren't on the same clock, or the sample rates differ. See the Setup Map's clock notes; the ADA8200's SYNC light must read LOCKED.",
        "Doubled, slightly delayed sound in headphones while recording: Reaper's input monitoring is on. Turn it off on the audio tracks.",
        "Playback is heard only on tape returns 1-2: the tracks are sending to the master instead of their own hardware outs. Check each track's Routing window.",
        "Crackles when the screen is busy: raise the block size one step, and set Windows' power plan to High performance. USB hubs cause this too; the UMC1820 should be on its own port on the PC.",
        "Reaper can't find the files after a session: the project was saved to a different folder than the media. Use File > Save project as with \"Copy all media into project directory\" ticked once, and the template's folder setting after that."])
    return st
