from common import *


def story():
    st = [Paragraph("Setting Compression Levels", title),
          Paragraph(f"How to dial in the Klark Teknik 76-KT on a {B} channel insert, plus settings for the dbx alternatives. The goal: the compressor does what you want, and the recording stays at the same level as before.", sub)]
    st += sec("What the knobs do (76-KT)", [
        "<b>Input:</b> how hard the signal hits the compressor. On an 1176-style unit there is no threshold knob; turning Input up is what makes it compress more.",
        "<b>Output:</b> brings the level back up after compression. This is the knob that keeps the recording at the same volume as bypass.",
        "<b>Attack:</b> how fast it grabs a loud note, about 20 to 800 microseconds. Clockwise is faster. Fast = grabs the drum hit itself; slower = lets the hit through and clamps what follows, which keeps punch.",
        "<b>Release:</b> how long it holds on after the note drops, about 80 to 700 milliseconds. Clockwise is faster. Fast release sounds pumping and aggressive; slow sounds smoother.",
        "<b>Ratio buttons:</b> 4:1 moderate, 8:1 severe, 12:1 mild limiting, 20:1 hard limiting. Pressing all four at once (\"all buttons in\") gives the crushed, exploding sound on drums and room mics.",
        "<b>Meter:</b> shows gain reduction (GR), the amount in dB being turned down. Set the meter switch to GR for all of the steps below. The +4/+8 positions show output level instead."])
    st += sec("Wiring and gain structure", [
        f"Channel insert jack {AR} insert Y cable: TRS end into the insert, tip (send) to the 76-KT input, ring (return) from the 76-KT output. The compressor sits after the channel trim and before the EQ and fader, so it's recorded.",
        "The 76-KT's XLR jacks are balanced, +4 dBu. The Mackie inserts are unbalanced, -2 dBu, a little lower. That's fine: use a TRS-to-dual-XLR insert cable, or the 76-KT's 1/4\" jacks if your unit has them. Expect to run the 76-KT Input a bit higher than you would from a +4 source.",
        f"Set the channel trim first, exactly as in the Gain Staging Guide, with the compressor bypassed. The compressor must never be used to fix a bad trim setting."])
    steps = [["Step", "What to do", "What you're listening or looking for"],
             ["1", "Bypass the 76-KT (or pull the insert). Play the part at full volume and note where the channel meters and Reaper peak.", "This is the level you'll match at the end."],
             ["2", "Un-bypass. Output at about 12 o'clock, Input low, Attack and Release at 12 o'clock, ratio 4:1, meter on GR.", "The meter needle should sit at 0 with the part playing: no compression yet."],
             ["3", "Turn Input up slowly while the part plays.", "The needle starts dipping left on loud notes. Stop when it dips to the amount in the table below."],
             ["4", "Set Attack. Start at 12 o'clock, turn it slower (counter-clockwise) if the drum or pluck loses its snap.", "Transients still cut through; the needle moves right after the hit, not on it."],
             ["5", "Set Release. Turn it faster (clockwise) until the needle gets back to 0 between notes, then back off a touch.", "The needle breathes with the music and never gets stuck down. Fast on drums, slower on vocals and bass."],
             ["6", "Flip bypass in and out while adjusting Output.", "Both sound equally loud. The console meters and Reaper peak where they did in step 1."],
             ["7", "Check the whole band playing together, and check Reaper for clipping.", "If the recording is now too hot, lower Output, not the trim."]]
    st += [Paragraph("Step by step", h), tbl(steps, [0.45 * inch, 3.6 * inch, 3.45 * inch])]
    starts = [["Source", "Ratio", "Attack", "Release", "Gain reduction", "Notes"],
              ["Lead vocal", "4:1", "Medium (12 o'clock)", "Medium", "3-6 dB on loud lines", "Fast enough to catch peaks, slow enough that quiet words don't jump up. 8:1 for a shouted take."],
              ["Bass (DI or amp)", "4:1", "Slow (9-10 o'clock)", "Medium-slow", "3-5 dB", "Slow attack keeps the pluck; the compressor evens out note-to-note volume."],
              ["Room mic (Turner or ch 5/6)", "All buttons in", "Fast (3 o'clock)", "Fast (3-4 o'clock)", "10-20 dB, pinned", "The Tame Impala crush. Blend this under the close drum mics in Reaper."],
              ["Kick or snare (close mic)", "4:1 or 8:1", "Slow (9 o'clock)", "Fast", "3-6 dB", "Slow attack lets the hit through; fast release pumps. Too fast an attack makes drums sound dull."],
              ["Drum pair (groups 3-4, if a 2-channel unit)", "4:1", "Medium-slow", "Fast", "4-8 dB", "Link the two channels so the stereo image doesn't wander."],
              ["Acoustic guitar", "4:1", "Medium", "Medium", "2-4 dB", "Light touch; too much flattens the strumming."],
              ["Synths through pedals", "4:1 or 8:1", "Fast", "Medium", "3-8 dB", "Tames the spiky peaks from fuzz pedals before the trim."]]
    st += [Paragraph("Starting points", h), tbl(starts, [1.35 * inch, 0.75 * inch, 1.0 * inch, 0.9 * inch, 1.0 * inch, 2.5 * inch]),
           Spacer(1, 4), Paragraph("Knob positions are rough: the 76-KT's attack and release scales run backwards from most compressors (clockwise = faster), so go by the meter and your ears.", note)]
    st += sec("If you buy the dbx alternative instead (266XS or 1066)", [
        "These have a Threshold knob, so Input stays fixed: leave the console insert level alone and turn Threshold down until the gain-reduction meter shows the amount in the table above.",
        "Ratio knob: 4:1 for vocals, bass and acoustic; 8:1 or higher for drums. OverEasy (soft knee) on for vocals and bass; off (hard knee) for drums.",
        "Attack and Release: the Auto mode is a fine default for vocals and bass; switch to manual for drums and set them as in the table.",
        "Output gain: match bypass exactly as in step 6. The gate section: threshold all the way down (off) unless you're using it to cut tom ring; then raise it just until the ring stops between hits.",
        "Stereo link for the drum pair: press Stereo Couple and use channel 1's controls for both."])
    st += sec("Common mistakes", [
        "Needle pinned left all the time: Input is too high or release too slow. The part will sound squashed and small. Back Input off until the needle returns to 0 between phrases (unless you're going for the room-mic crush on purpose).",
        "Drums sound dull: attack is too fast. Slow it down until the stick hit comes back.",
        "Everything got louder when you un-bypassed: Output is too high. That's not a better sound, it's just louder. Match bypass before judging.",
        "Hiss or noise rises between notes: too much gain reduction with a fast release is pumping the noise floor up. Reduce Input, or add the gate (DN514+) on that channel.",
        "Mix bus: don't put the 76-KT on the main L/R inserts. Reaper's ReaComp or a bus-compressor plugin does that job at mixdown, where you can undo it.",
        "Hardware compression is printed to the recording. When unsure, use less; you can always add more in Reaper, but you can't take it off."])
    return st
