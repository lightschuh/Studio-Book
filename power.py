from common import *


def story():
    st = [Paragraph("Power: Furman Outlets, Start-Up and Shutdown", title),
          Paragraph(f"Where everything plugs in, the order to switch it on and off, and why. The Mackie manual's only power rule is that the {B} is powered only by its own Mackie 8&bull;Bus power supply; the sequence below is standard studio practice, not a Mackie requirement.", sub)]
    st += sec("Where the Furman plugs in", [
        "<b>Straight into a grounded wall outlet.</b> Not into a power strip, surge protector or UPS. Stacking surge protectors is against most electrical codes and UL listings, can make the surge protection work worse rather than better, and puts the whole rack's load through the weakest strip's wiring and switch.",
        "Check the outlet first with a plug-in outlet tester (a few dollars at a hardware store): it should show correct wiring and a good ground. The Furman's surge protection and filtering both dump to ground; on an ungrounded or miswired outlet they do little, and that's also a common cause of hum.",
        "If the wall outlet is too far from the rack, use a <b>heavy-duty extension cord</b>, 12 or 14 gauge, three-prong, rated 15 A, as short as will reach. That's acceptable where a power strip isn't. Avoid thin household cords.",
        "Use an outlet on a different circuit from the window AC if you can (find out by flipping breakers and seeing what goes dark). The AC's compressor kicking on is the most likely source of clicks in this room.",
        "The Peavey 260 and the computer, which stay off the Furman, go to the wall too, on the same circuit as the Furman so everything shares one ground. Plugging those two into an ordinary surge strip is fine, since that strip isn't stacked on anything."])
    st += sec("What the Furman M-8x2 gives you", [
        "Nine outlets: eight switched outlets on the rear panel and one convenience outlet on the front. Fifteen-amp rating with its own circuit breaker, surge and spike protection, and RFI/EMI noise filtering. A Protection OK light on the front tells you the surge protection is still alive; if it goes dark, the Furman has taken a hit and should be replaced.",
        "The front switch turns the eight rear outlets on and off together. Everything plugged into the back comes up at once, so the Furman is step one of the start-up and the last thing off.",
        "Load check: the whole rack draws well under 15 A. The Mackie power supply is the biggest item at around 2 A; the UMC1820, ADA8200, TSR-12 and a compressor are a fraction of an amp each. The Peavey 260 power amp is the one thing to keep off the Furman's switched outlets (see below)."])
    outlets = [["Rear outlet", "Plug in", "Why here"],
               ["1", f"Mackie {B} power supply", "Biggest draw, and the console must be up before anything that listens to it."],
               ["2", "Behringer UMC1820", "Computer interface. Fine on a switched outlet; the computer wakes it over USB."],
               ["3", "Behringer ADA8200", "Comes up with the UMC1820 so the ADAT clock locks right away."],
               ["4", "DigiTech TSR-12", "Outboard effects."],
               ["5", "Compressor (76-KT) when it arrives", "Outboard dynamics."],
               ["6", "Delay / second effects unit, when added", "Outboard effects."],
               ["7", "Spare", "Patchbays need no power. Keep this free."],
               ["8", "Spare", "Keep one free. Never daisy-chain a second power strip off the Furman."],
               ["Front", "Phone or laptop charger, soldering iron, a work light", "Convenience only. Nothing in the audio path."],
               ["Not on the Furman", "Peavey 260 power amp; the computer", "See the next section."]]
    st += [Paragraph("Which outlet gets what", h), tbl(outlets, [1.0 * inch, 2.4 * inch, 4.1 * inch]),
           Spacer(1, 4), Paragraph("Label each plug at the Furman end with masking tape (\"MACKIE PSU\", \"UMC\", and so on) so a tripped breaker or a swap doesn't turn into a guessing game.", note)]
    st += sec("Two things that stay off the Furman's switched outlets", [
        "<b>Peavey 260 power amp.</b> A power amp must come on last and go off first, so it can't be on the same switch as everything else: if it powered up with the rack, the turn-on thumps of the console and interface would go straight to the speakers. Plug it into a wall outlet on the same circuit (or a separate surge strip), and use its own power switch as the final step each way.",
        "<b>The computer.</b> It sits on a shelf in the rack but does not plug into the Furman: cutting its power with the Furman switch is the same as pulling the plug mid-session. Give it its own outlet and shut it down normally. If the Furman trips, the computer stays up and Reaper's autosave is intact.",
        "Everything else audio belongs on the Furman: the point of a conditioner is that one filtered, surge-protected feed covers the whole signal chain, which also helps against ground-loop hum."])
    up = [["Step", "Switch on", "Before you do"],
          ["1", "All levels down: CNTRL RM, STUDIO, both PHONES, Peavey 260 input knobs. Main L/R fader down.", "Nothing can thump through speakers or headphones that have no level."],
          ["2", "Furman front switch. The eight rear outlets come up: Mackie power supply, UMC1820, ADA8200, TSR-12, compressor, delay unit.", "Check the Protection OK light. The console's power LED and the power supply fan should come on."],
          ["3", "Computer, then open Reaper.", "The UMC1820 should show up as the audio device; the ADA8200 SYNC light should read LOCKED."],
          ["4", "Wait about 20-30 seconds.", "Lets the console's circuits settle and any relays click before the amp is live."],
          ["5", "Peavey 260 power switch (its own switch, at the wall).", "Its level knobs are still down from step 1."],
          ["6", "Bring up CNTRL RM to a normal setting, then the Peavey's level knobs, then phones levels.", "Now the room and headphones are live. Raise the main L/R fader last, with music playing, so you hear it come in."]]
    st += [Paragraph("Start-up, in order", h), tbl(up, [0.45 * inch, 3.8 * inch, 3.25 * inch])]
    down = [["Step", "Switch off", "Why"],
            ["1", "Save the Reaper project. Main L/R fader down, CNTRL RM, STUDIO and PHONES levels down, Peavey level knobs down.", "Protects the session and the speakers from whatever happens next."],
            ["2", "Peavey 260 power switch off.", "Amp off first, so no later click reaches the speakers."],
            ["3", "Close Reaper and shut the computer down from its menu.", "The interface will drop off the USB cleanly."],
            ["4", "Furman front switch off. The console, interface, ADA8200 and outboard all go down together.", "Fine for all of this gear; none of it has a disk or a session to lose."],
            ["5", "Leave the Furman plugged into the wall.", "Its surge protection only works while it's connected. Unplug it only for storms or when you're away for a long time."]]
    st += [Paragraph("Shutdown, in reverse", h), tbl(down, [0.45 * inch, 3.8 * inch, 3.25 * inch])]
    st += sec("Details that matter", [
        f"The {B} has no power switch of its own; it's on when the power supply is on. The power supply's umbilical plugs into DC POWER IN on the console: connect it with everything off, and never plug or unplug it live.",
        "Mackie's one hard rule: power the console only from the Mackie 8&bull;Bus power supply. No substitutes.",
        "Phantom power: switch the 48V blocks on after start-up with the block's faders down, and off before shutdown. Never plug or unplug a mic on a powered block.",
        "The power supply runs warm and its fan needs air: keep the empty rack space between it and the Furman, and never block the front vents (the kitten's spot is fine; a blanket is not).",
        "If the Furman's breaker trips: everything on the rear outlets goes dark at once, but the Peavey and computer stay up. Turn the Peavey's levels down, press the breaker back in, and start again from step 2. If it trips twice, something is drawing too much or has a fault; stop and find it.",
        "Storms: the Furman absorbs surges, but nothing stops a direct lightning hit. Unplug the Furman and the Peavey from the wall when a bad storm is coming.",
        "If you ever add a power sequencer (Furman's M-8S model does this), it automates steps 2-5 with one button: conditioner, then outboard, then amps, a few seconds apart, and in reverse on shutdown. Not needed now."])
    return st
