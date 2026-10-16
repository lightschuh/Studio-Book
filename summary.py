from common import *
import needs


def story():
    docs = [["Section", "What it's for"],
            ["Studio Setup Map", "Rack order, 24-channel map with pan settings, four snakes, ADA8200, TSR-12, PV6, Tascam 246, garage PA, wiring, cable list."],
            ["Studio Connection Diagram", "Visual: signal flow (page 1), power and instrument chains with snake colors (page 2). Print and hang by the rack."],
            ["Monitoring: Outputs and Routes", "Every output and what feeds it; the MONITOR and PHONES sections button by button; talkback; setups for each kind of session."],
            ["Power: Start-Up and Shutdown", "What plugs into each Furman outlet, the switch-on order, the shutdown order, and why."],
            ["Gain Staging Guide", "Zeroing the board, setting each of the 24 channels, outboard levels, troubleshooting."],
            ["Setting Compression Levels", "Dialing in the 76-KT on a channel insert, with starting points per source and the dbx alternative settings."],
            ["EQ Settings, Channel by Channel", "What each EQ knob does and what not to do with it; a knob-picture starting point for every channel."],
            ["Mic Placement", "Distance, position and aim for every mic'd source; bleed control for band takes; which decisions depend on room size."],
            ["Tascam 246: Setup and Recording", "The 246's own controls, how it connects, levels for tape, recording passes, bouncing, and four-track use."],
            ["Reaper Setup", "ASIO driver, enabling all 16 inputs and outputs, the track template, playback routing, MIDI, recording and autosave settings."],
            ["FL Studio Setup", "The same studio in FL Studio: Mixer insert inputs and Auto-map, the recording filter, outputs to the tape returns, MIDI."],
            ["Pro Tools Setup", "The same studio in Pro Tools: Playback Engine, I/O Setup paths, session template, recording, MIDI. Needs Artist tier or above."],
            ["GarageBand Setup", "The same studio on a Mac in GarageBand: an 8-input recorder with stereo-only playback; good for overdubs and demos."],
            ["Panning Guide", "Console pan knobs for tracking (24 channels) and starting pan positions for the Reaper mix."],
            ["Alternate Setups", "Other ways to wire the same studio, each with what changes and how to switch back. Alternate A: all direct outs, one source per track, with a noise test. Alternate B: stereo playback on two outputs, mixing in Reaper."],
            ["Studio Equipment List", "Everything you own, October 2026."],
            ["Studio Gear Needs List", "What's still missing, with price ranges, and what was ruled out."],
            ["Goal Studio Diagram", "The prospective map: today's gear plus every planned purchase, wired in."],
            ["Studio Equipment Values", "Rough used-market value of everything, with totals."],
            ["How Each Piece Works", "What each piece of your gear does and how it connects to the 24&bull;8; power order; quick gain checklist."]]
    st = [Paragraph("Studio Build Summary", title),
          Paragraph(f"Everything decided so far for the Mackie {B} studio, in one place. October 2026.", sub),
          Paragraph("Documents", h), tbl(docs, [1.9 * inch, 5.6 * inch])]
    st += sec("The studio at a glance", [
        f"Mackie {B} console (24 channels, 8 groups) on the desk; rolling rack underneath (about 12U): UMC1820, ADA8200, TSR-12, room for the 76-KT and a delay unit, a rack shelf for the computer, Furman M-8x2, Mackie power supply at the bottom. No rack headphone amp: personal mixers at the players' spots cover that. Planned around the desk: a screen on a swing arm right of the console, and the DIY monitors clamped to the back edge.",
        "16 recording inputs in Reaper: groups 1-8 into the UMC1820 (Reaper 1-8) and 8 direct outs into the ADA8200 over ADAT (Reaper 9-16). 16 playback tracks: UMC1820 outputs to tape returns 1-8, ADA8200 outputs to tape returns 9-16. Reaper at 44.1 or 48 kHz.",
        "Four 8-channel snakes, same color order on all: brown, red, yellow, green, blue, gray, white, black. White tape = recording, black = playback 1-8, blue = direct outs, yellow = ADA8200 playback 9-16 (the 6 ft snake).",
        "All channels assigned except ch 22 (held for the drum machine if it has a stereo out)."])
    st += sec("Capacity at a glance", CAP)
    st += sec("How channels get recorded", [
        "<b>Group channels</b> (drums, bass, guitars, Reface CS): press the channel's group button (1-2, 3-4, 5-6 or 7-8) and L/R. Pan picks the odd or even group, so pan settings stay fixed. Toms and rooms share groups 3-4; both guitar amps share group 6.",
        "<b>Direct-out channels</b> (lead vocal, wireless, trumpet, vocals 2-3, SH-201, drum machine): pan doesn't affect the recording. Press L/R only. The direct out is after the EQ, fader and mute, so keep faders near U (unity) and don't mute a channel while it's recording.",
        "<b>Monitor-only channels</b> (PV6 submix of e-drums, SamplePad 4 and DJ; Tascam 246 return): heard in the mix, not recorded through the console. E-drums and the SamplePad record as MIDI.",
        "On every recorded channel, the EQ and fader are part of what Reaper gets. Set them before a take and leave them alone during it.",
        "Lopsided headphones from hard-panned groups: press MONO or use a performer mix on AUX SEND 3/4. Neither changes the recording. Final panning happens in Reaper."])
    st += sec(f"Aux sends on the {B}", [
        "<b>Aux 1 and 2:</b> each has its own knob on every channel. One PRE button covers both. The talkback mic can be sent into them.",
        "<b>Aux 3-6:</b> two knobs per channel. SHIFT makes them aux 3 and 4 (up) or aux 5 and 6 (down), so one channel can feed 3/4 or 5/6, not both. One PRE button covers the pair. SOURCE sends that channel's tape return (Reaper playback on MIX-B) instead of the live channel.",
        "<b>Headphones:</b> the two phones jacks can listen to aux 3/4 or aux 5/6 directly, not aux 1/2.",
        "<b>How this studio uses them:</b> effects on aux 1 and 2 with PRE up (TSR-12 reverb on 1, a delay on 2 later); headphone mixes on aux 3-6 with PRE down.",
        "<b>Setting up the aux 3/4 performer mix, step by step:</b> (1) on each channel the performer needs, SHIFT up and PRE down; (2) aux 3 knob = how loud that channel is in their left ear, aux 4 = right ear, so turn both up equally for a centered sound, or favor one for a little stereo; (3) raise the AUX SEND 3 and 4 masters in the master section to about noon; (4) on the Phones 2 section press AUX SEND 3/4 and bring its level up slowly; (5) keep Phones 1 on MONITOR so you hear the control room mix. Because PRE is down, moving channel faders won't change what the performer hears.",
        "<b>What's left to fill:</b> aux 2 is the only open effects send. Aux 5/6 is a second performer mix or two more mono cues for personal mixers. Aux returns 2, 3 and 4 are open stereo line inputs for a delay or any extra line source (DJ mixer, a phone) when the channels are full."])
    st += sec("16-track playback and clock (UMC1820 + ADA8200)", [
        f"Two optical cables: ADA8200 ADAT out {AR} UMC1820 optical in (recording), and UMC1820 ADAT out {AR} ADA8200 ADAT in (playback). The ADA8200's 8 outputs feed tape returns 9-16 through the 6 ft snake.",
        "Clock with both cables: UMC1820 is the master; set the ADA8200's SYNC to ADAT IN until it shows LOCKED. With only the first cable, set the ADA8200 to its internal clock at Reaper's sample rate and set the UMC1820 to clock from its optical input.",
        "The ADA8200's outputs are XLR: use an XLR (female) to TRS snake, or 8 XLR-female-to-TRS-male adapters on a TRS snake. Worth checking before Todd sends the 6 ft snake.",
        "UMC1820 outputs 1-2 are its MAIN OUT jacks, which follow the front MAIN OUT knob. Turn that knob all the way up and leave it, so playback tracks 1-2 match 3-8.",
        "In Reaper, route tracks 9-16 to hardware outputs 11-18 (the ADAT outs); they play on MIX-B channels 9-16. The Reaper Setup page has the full template."])
    st += sec("Headphones and monitoring", [
        f"The {B} has two headphone outputs, each with its own level and source (MONITOR, MIX-B, AUX 3/4, AUX 5/6, EXTERNAL).",
        "Basic: press MONITOR on both phones sections and L/R MIX in the monitor section. Reaper playback comes back on the tape returns: press MIX-B and raise MIX-B LEVEL. The full button-by-button walkthrough, every output, talkback and per-session setups are on the Monitoring page.",
        "Headphones: used Sony MDR-7506 and Sennheiser HD 280 Pro, both getting new pads.",
        "Headphone amp: decided against, to keep the rack space for a delay unit. Up to 2 people use Phones 1 and 2. For more, small mixers with headphone jacks at each player's spot, fed from aux sends 3-6; they double as personal headphone amps.",
        f"Speakers: CONTROL ROOM out {AR} Peavey 260 stereo power amp {AR} DIY passive monitors (Parts Express kit). Until those are built, all mixing is on headphones."])
    st += sec("Submixers and personal monitor mixes", [
        "<b>Freeing console channels:</b> a small mixer can combine monitor-only sources (like the PV6 does for the e-drums, SamplePad 4 and DJ mixer) into one stereo pair. Don't submix anything you want on its own track; the blend gets locked in.",
        "<b>Musicians' own mixes:</b> feed a small mixer per musician from aux sends 3-6 with PRE down, each send carrying a group of instruments, e.g. aux 3 = drums, aux 4 = bass and guitars, aux 5 = vocals and trumpet, aux 6 = keys. Each player plugs headphones into their mixer and turns up \"more me\". This replaces using AUX 3/4 as a stereo pair for Phones 2.",
        "Because aux 3/4 and 5/6 share knobs, set SHIFT up on the drum, bass and guitar channels (aux 3 or 4) and SHIFT down on the vocal, trumpet and keys channels (aux 5 or 6).",
        "Any small mixer with a headphone jack works. The powered PA mixers aren't a good fit for this; use them for the garage PA and gigs."])
    st += sec("Gain staging rules", [
        f"Set each {B} channel with its fader at U: press SOLO and raise the trim until peaks regularly reach 0 on the L/R meters. Solo on this console is after the fader, so the fader has to be at U first. Aim for Reaper peaks around -12 to -6 dBFS.",
        "<b>Mixer feeds what's recorded or the main mix</b> (PV6 submixer): set gains and master to unity once, then leave them. Small balance tweaks on its faders are fine.",
        "<b>Mixer only feeds someone's ears</b> (personal headphone mixers): musicians can change anything. It can't affect the recording.",
        "Tascam 246: tape meters around 0 VU, a little past for saturation."])
    st += sec("Microphones", [
        "Every owned mic has a spot: kick and snare mics, room mics, SM58-style (3) on toms and guitar amp 2, SM57 on guitar amp 1, SM58 on trumpet, Worker Bee on lead vocal, Peavey on vocal 2, Turner 95D on vocal 3. Bass goes through its DI out.",
        f"No rack mic preamp needed: the {B} has 24 preamps and the ADA8200 adds 8. Next mic to buy, if any: another SM57.",
        "Phantom power is switched in blocks of eight channels (1-8, 9-16, 17-24). The Worker Bee on ch 10 means channels 9-16 all get 48V. That's fine for balanced dynamic mics. Check the wireless receiver's manual, and see the Turner note below.",
        "Turner 95D: made in high- and low-impedance versions with Amphenol MC1M or MC2M connectors; check the OHMS box. High: needs a matching transformer. Low (200 ohms): needs an adapter or rewired cable to XLR. Until its wiring is confirmed, don't plug it into a block with phantom on. Output is low (about 1.25 mV/Pa) and range narrow (100 Hz-10 kHz): a lo-fi character mic, great for a vintage vocal or a crushed mono room mic.",
        "Inline mic booster (Cloudlifter CL-1, Triton FetHead, sE DM1): only if a quiet vocal needs the trim near max and you hear hiss. Dynamic mics only, never condensers.",
        "Acoustic guitar overdubs: Worker Bee on ch 10, aimed at the 12th fret, 8-12 inches away. Keep it off the PV6, which isn't recorded."])
    st += sec("Electronic percussion", [
        "Roland e-drum pad and Alesis SamplePad 4 (5 pads total) go into the PV6 for monitoring and record as MIDI through the UMC1820's MIDI in or USB. One pad can play any sound; build parts a drum at a time."])
    st += sec("Rack additions and deals", [
        "Priority: (1) a compressor; (2) a patchbay; (3) a Pultec-style EQ such as the Klark Teknik EQP-KT, not a graphic EQ; (4) a rack drawer for patch cables.",
        "Compressor decision: the Klark Teknik 76-KT (1176-style) is the primary choice and is in the totals. Alternatives if one doesn't turn up, or for four channels later: two dbx 266XS from Drew's listing ($110 the pair, clean, with gates), or two dbx 1066 from Cory's listing ($150 each, better built, same four channels).",
        "Cory Pollard's listing also has 2 patchbays ($20 each) and 2 Hosa 8-channel TS snakes ($20 each): $80 for the four, worth taking even without the 1066s. Test every patchbay jack and each snake tail before paying.",
        "Klark Teknik DN514+ quad gate, $100 with free shipping: a fair price. It goes on the inserts of kick, snare and both toms and tightens the drums before they're recorded. Reaper can gate for free afterwards, so buy it only if tom ring and bleed are bothering you now. It takes 1U; with the headphone amp dropped, the rack has room for it under the delay unit.",
        "Klark Teknik 76-KT: the one in that listing sold. Still on the needs list as the 1176-style character compressor; if you buy the 1066s it becomes a nice-to-have at around $100-135 used.",
        "Skip from that listing: Warm Audio WA273-EQ ($1,100, a luxury), dbx 1074 quad gate (Reaper can gate later), dbx 231 graphic EQ (PA use only).",
        "Behringer HA8000 headphone amp listed at $50: passed on it; the rack slot goes to a delay unit and personal mixers handle extra headphones.",
        "Power amp: covered by the Peavey 260 (vintage 1970s stereo power amp). It drives passive speakers only; it isn't rack-mount, so it goes on a shelf."])
    st += sec(f"Connecting more gear to the {B}", [
        f"Studio monitors: the biggest gap. Plan: CONTROL ROOM out {AR} Peavey 260 {AR} DIY passive monitors built from a Parts Express kit (C-Note pair about $160). Get the Peavey checked by a tech, match speaker impedance to its rating, use real speaker cable, power it on last. JBL 305P MkII powered monitors remain the plug-and-play backup.",
        "A delay on AUX SEND 2 / AUX RETURN 2 (aux 1 is the TSR-12).",
        "Personal headphone mixers on AUX SENDS 3-6.",
        "Radial ProDI into any mic input: records a clean guitar or bass track alongside the amp mic, so it can be re-amped later; also for an acoustic pickup. Synths, drum machines and the DJ mixer don't need one.",
        "Reference tracks into the 2-TK input to compare mixes against Tame Impala songs."])
    st += sec("Marshall MG250DFX", [
        "The rear jacks are FX send, FX return(s), footswitch and CD input. The jack that didn't work was most likely the FX return: it skips the preamp, so a guitar plugged in there sounds weak or silent, and anything in it cuts off the preamp. A photo of the back panel will confirm.",
        "Use it as a loop: drive and fuzz pedals in front of the amp; delay, reverb, modulation and the 720 looper between FX SEND and FX RETURN."])
    st += sec("Effects and the Tame Impala sound", [
        "TSR-12 on aux send 1 (PRE up), returned on aux return 1, mix 100% wet. Monitor-only; Reaper records dry.",
        "Klark Teknik 76-KT (1176-style FET) on a channel insert via Y cable for squashed drums and vocals. Mackie inserts: tip = send, ring = return.",
        f"Guitar chain: guitar {AR} pedalboard (Big Muff, DBA Exploding Head, Cock Fight Plus, JHS gain, La Grotte) {AR} Diamond Vibrato {AR} MXR Phase 90 {AR} 720 looper {AR} amp. Vibrato needs a 9-18V supply; Phase 90 a 9V adapter or battery.",
        "Kevin Parker notes: SM57-style dynamics on drums and amps, heavy 70s drum compression and saturation, Juno-106 run through guitar pedals (run the SH-201 through the pedalboard into ch 17), Vox AC30, SSL-style bus compressor, Manley Vari-Mu on the master. Reaper's ReaComp can cover the mix bus.",
        "Tascam 246 tape saturation is another route to the 70s drum sound once it's repaired."])
    st += sec("Analog tape: Tascam 246 (once repaired)", [
        f"To tape: {B} MAIN MIX out L/R {AR} two 246 line inputs. From tape: 246 stereo line out {AR} ch 23-24.",
        "To capture tape into Reaper, assign ch 23-24 to groups 7-8 in place of the Reface. Not synced: line takes up by ear or with a click.",
        "Full setup, the 246's own mixer settings, dbx, tape speed, bouncing and punch-ins are on the Tascam 246 page."])
    st += sec("Garage PA", [
        f"STUDIO OUTPUT L/R {AR} one powered mixer (Powerpod 410 or EMX62M) in the garage for playback or a monitor mix. Talkback reaches it through PHONES &amp; STUDIO.",
        "The other powered mixer can take the MAIN MIX outs for live shows. Garage mics would need a long XLR snake back to the console."])
    st += sec("Power", [
        "The Furman plugs straight into a grounded wall outlet (never a power strip). All rack audio gear plugs into its eight switched rear outlets (won on eBay, on its way). Two things stay off it: the Peavey 260, on its own wall outlet so it can be last on and first off, and the computer, so a tripped breaker can't kill a session. Keep the Mackie power supply's umbilical away from the snakes.",
        f"Start-up: levels down {AR} Furman switch (console PSU, UMC1820, ADA8200, outboard all come up) {AR} computer and Reaper {AR} wait 20-30 s {AR} Peavey 260 {AR} bring levels up. Shutdown in reverse: levels down, Peavey off, computer down, Furman off. Full page: Power: Start-Up and Shutdown.",
        "If the window AC causes clicks or hum, power the studio from another circuit."])
    rows = [["Needs list", "Low", "High"]] + [[n, f"${l:,}", f"${hh:,}"] for n, l, hh in needs.TOTALS]
    st += [KeepTogether([Paragraph("Shopping status", h), tbl(rows, [5.0 * inch, 1.1 * inch, 1.1 * inch], last_bold=True),
                         Spacer(1, 3), Paragraph("Details and what each tier includes are in the Studio Gear Needs List.", note)])]
    st += sec("Open items", [
        "Tascam 246 repair (won't play tape).",
        "Run the group-vs-direct-out noise test (Alternate Setups) and decide whether to try Alternate A.",
        "Used MDR-7506 and HD 280 Pro: order pads. Confirm the HD 280 Pro is a 2016 or newer unit before buying the genuine Sennheiser pad kit.",
        "Power supplies for the Diamond Vibrato (9-18V) and Phase 90 (9V).",
        "Identify the 1970s Roland drum machine model (decides whether it needs ch 22 for a stereo out, and narrows its value).",
        "Check the Turner 95D's impedance and wiring before plugging it into the console.",
        "Send photos when back in the studio: Turner OHMS box and connector, back of the console, Marshall back panel, second pedalboard.",
        "Measure the live room and control room (length, width, ceiling height; which walls are hard or soft) so the Mic Placement page's room-dependent items become exact.",
        "Find a used 76-KT (around $100-135). Decide on Cory's patchbays and snakes, and whether the DN514+ gate is worth it now.",
        "Swap the 3 ft snake with Todd for the 6 ft one (the 3 ft doesn't reach); ideally XLR (female) to TRS for the ADA8200 outputs. Until then, play back in stereo (Alternate B).",
        "Third snake, XLR cables, second optical cable, MIDI cable, Tascam and DJ cables (see the Setup Map cable list).",
        "Install the Furman when it arrives: just above the Mackie power supply with one empty space between.",
        "Peavey 260: tech check, then build the monitors."])
    return st
