from common import *


def story():
    ch = [["Ch", "Source", "Input", "48V", "Starting trim", "Fader", "Notes"],
          ["1", "Kick (kick mic)", "Mic", "If cond.", "Low", "U", "Very loud source. Group 1."],
          ["2", "Snare (snare mic)", "Mic", "If cond.", "Low", "U", "Check rimshots; they peak hardest. Group 2."],
          ["3", "Rack tom (SM58-style)", "Mic", "No", "Low-med", "U", "Hit hard to set level. Groups 3-4."],
          ["4", "Floor tom (SM58-style)", "Mic", "No", "Low-med", "U", "Groups 3-4."],
          ["5", "Room L", "Mic", "If cond.", "Med-high", "U", "Set L and R to the same trim. Groups 3-4."],
          ["6", "Room R", "Mic", "If cond.", "Med-high", "U", "Match ch 5. Groups 3-4."],
          ["7", "Bass amp DI out (or mic)", "Mic or line", "No", "Low-med", "U", "If the DI out is line level, use the line input. Group 5."],
          ["8", "Magnatone (SM57)", "Mic", "No", "Low-med", "U", "Depends on amp volume; set the amp first. Group 6."],
          ["9", "Marshall MG250DFX or Orange (SM58-style)", "Mic", "No", "Low-med", "U", "Shares group 6 with ch 8. Set each trim first, then balance the two on their faders and leave them."],
          ["10", "Lead vocal (Worker Bee)", "Mic", "Yes", "Med", "U", f"Set with the loudest line of the song. Direct out {AR} ADA8200 in 1."],
          ["11", "Wireless (ATW-R3210)", "Mic", "No", "Med", "U", f"Set the receiver's output level first. Direct out {AR} ADA8200 in 2."],
          ["12-13", "Reface CS L/R", "Line", "No", "Low", "U", "Synth volume about 3/4. Groups 7-8."],
          ["14", "Trumpet (SM58)", "Mic", "No", "Low", "U", f"Very loud; player 1-2 ft back. Direct out {AR} ADA8200 in 3."],
          ["15", "Vocal 2 (Peavey)", "Mic", "No", "Med-high", "U", f"Direct out {AR} ADA8200 in 4."],
          ["16", "Vocal 3 (Turner 95D)", "Mic", "No (see note)", "High", "U", f"Low-output vintage mic; check impedance first. Direct out {AR} ADA8200 in 5."],
          ["17-18", "Roland SH-201 L/R", "Line", "No", "Low", "U", f"Through the pedalboard, check levels again. Direct outs {AR} ADA8200 in 6-7."],
          ["19-20", "PV6 main out (e-drums, SamplePad 4, DJ)", "Line", "No", "Low", "To taste", "PV6 at unity. Monitor only."],
          ["21", "1970s Roland drum machine", "Line", "No", "Low-med", "U", f"Vintage outputs can be quieter. Direct out {AR} ADA8200 in 8."],
          ["22", "Open", "&mdash;", "&mdash;", "&mdash;", "&mdash;", ""],
          ["23-24", "Tascam 246 line out L/R", "Line", "No", "Med", "To taste", "Consumer-level outputs; trim up a little more than other line sources."]]
    st = [Paragraph("Gain Staging Guide", title),
          Paragraph(f"Channel-by-channel levels for the Mackie {B} studio, October 2026. Goal: clean, strong signals with room to spare, peaking around -12 to -6 dBFS in Reaper.", sub)]
    st += sec("1. Zero everything first", [
        "Trims all the way down, aux sends down, EQ switched out, phones and control room levels down.",
        "Group masters 1-8 and the main L/R fader at U (unity).",
        "UMC1820 inputs 1-8: LINE, not INST; gain knobs at minimum; pads off (switch a pad in only if an input still clips). ADA8200: gain knobs at minimum. The console does the amplifying; these just pass it along.",
        "Reaper track faders at 0 dB."])
    st += sec("2. Set each channel (one at a time)", [
        "Put the channel's fader at U and make sure it isn't muted. Solo on this console is taken after the fader, so the fader has to be at U for the reading to mean anything.",
        "Have the player perform the loudest part of the song, not a quiet warm-up.",
        "Press the channel's SOLO and watch the L/R meters. A hard-panned channel shows on one meter only.",
        "Raise the trim until peaks regularly reach 0 on the meters. An occasional +2 or +3 is fine; steady red is not.",
        "Release SOLO. Leave the fader at U; on group channels, the group master stays at U too.",
        "Check Reaper: peaks around -12 to -6 dBFS. Too hot or too quiet? Change the trim, not the fader."])
    st += [Paragraph("3. Channel chart", h),
           Paragraph("Starting trims are where to begin, not final settings; your ears and meters decide. U = unity (0) on the fader.", cell), Spacer(1, 4),
           tbl(ch, [0.55 * inch, 1.55 * inch, 0.6 * inch, 0.65 * inch, 0.7 * inch, 0.5 * inch, 2.95 * inch]), Spacer(1, 4),
           Paragraph("<b>48V (phantom power)</b> is switched in blocks of eight channels: 1-8, 9-16 and 17-24, with the switch at the top of each block. "
                     "\"If cond.\" means only if that mic is a condenser. The Worker Bee on ch 10 needs it, so the mic inputs on 9-16 all get 48V. "
                     "That's safe for balanced dynamic mics (SM58, Peavey). Check the wireless receiver's manual before leaving it on a powered block. "
                     "Keep the Turner 95D off a powered block until it's on a matching transformer or proper low-impedance XLR wiring. "
                     "Turn the block's faders down before switching phantom, and don't plug or unplug mics with it on.", note)]
    st += sec("4. What ends up in the recording", [
        "Group channels: trim, EQ, fader, pan and the group master all shape what Reaper gets.",
        "Direct-out channels: trim, EQ, fader and mute. Pan and the L/R button don't matter to the recording.",
        "So set EQ and faders before the take and leave them. Use the phones level, MIX-B and aux sends to change what people hear."])
    st += sec("5. Outboard and other gear", [
        "<b>Compressor (76-KT or dbx):</b> see the Setting Compression Levels page. Short version: trim first with the compressor bypassed, then Input (or Threshold) for 3-6 dB of gain reduction, then Output until bypass and un-bypass sound equally loud.",
        "<b>TSR-12:</b> aux 1 master at about noon; TSR-12 input so its meter peaks just under overload; mix 100% wet; AUX RETURN 1 to taste.",
        "<b>PV6 submixer:</b> its channel gains and master at unity; set each source's own volume moderately high; balance the sources on the PV6.",
        "<b>Tascam 246:</b> input trims low to start, then tape meters around 0 VU; a little past for saturation.",
        "<b>Reaper playback:</b> MIX-B level and tape-return levels set so playback sits naturally under the live mix. UMC1820 MAIN OUT knob all the way up, since it sets the level of playback tracks 1-2.",
        "<b>Headphones:</b> phones level low before anyone puts headphones on; build mixes with aux sends 3-6.",
        "<b>Garage PA:</b> STUDIO level low, PA inputs at unity, then raise STUDIO level.",
        "<b>Peavey 260 + DIY monitors:</b> CONTROL ROOM level and Peavey level knobs low; play a mix, raise CONTROL ROOM to a normal setting, then raise the Peavey until it's loud enough. VU meters should stay below the red."])
    st += sec("6. Final checks", [
        "Re-check with the whole band playing: everyone plays louder together.",
        "Hiss on a quiet singer: move the mic closer before adding gain. If the trim is near max and hiss remains, consider an inline booster (Cloudlifter-style) for that mic.",
        "Distortion with meters fine: check the source itself (amp, synth, DJ mixer, PV6) for clipping.",
        "Clicks and pops only on Reaper inputs 9-16: check the ADA8200's clock setting (see the Setup Map).",
        "Write down final trim positions (masking tape on the console) so sessions are repeatable."])
    return st
