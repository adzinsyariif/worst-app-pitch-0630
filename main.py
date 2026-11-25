"""Worst app pitch entry: candidate drafting and selection.

Candidates considered (each is a single sentence):

a) BlinkCounter counts how many times you blink each day and alerts you
   if you blink too much.
b) FridgeDoor photographs your open fridge every 10 seconds and texts
   you "still cold" until you close it, for people who stare into
   fridges hoping new food appears.
c) PetRock AI gives your pet rock a voice, mood tracking, and push
   notifications so it can tell you when it feels ignored, for owners
   who want a pet that judges them silently.
d) SockMatch is a dating app exclusively for single socks whose
   partners vanished in the wash, matching them by fabric and trauma
   so they can grieve together.

Evaluation against the judge criteria, in order:

1. Specific app + useless function in one sentence:
   a names a counter and its alert, b names a fridge camera and its
   texts, c names a rock companion and its notifications, d names a
   dating service and its matching. All four pass this bar.

2. Funny uselessness (absurd logic / deadpan confidence / mismatch
   with a problem nobody has):
   a is weak here because blink tracking could pass as wellness.
   b is stronger: the fridge will not gain food by being watched.
   c is strong: a rock cannot feel ignored, yet the pitch treats its
   feelings as a product requirement. d is strongest: single socks
   have no dating problem, and pairing them by shared loss treats
   laundry as bereavement with complete seriousness.

3. Sounds like a real pitch (product name, what it does, who for):
   a gives a name and a function but no audience. b gives a name, a
   function, and an implied audience of fridge-starers. c gives a
   name, features, and an audience of rock owners. d gives a name,
   a familiar category (dating app), an exclusive audience (single
   socks), and a matching method, which reads most like a founder
   describing a market.

4. One clean sentence, no padding, no second idea:
   a is clean but thin. b carries an extra timing detail that pads
   the joke. c stacks three features before landing the point. d
   keeps one idea (match the socks) and spends its length on the
   matching logic alone.

5. Vivid specific picture, not a generic apps joke:
   a leaves only a counter. b leaves a fridge door and a phone
   buzzing. c leaves a phone buzzing with a complaint from a rock.
   d leaves two unmatched socks being introduced to each other,
   which is the most specific and memorable image of the four.

Conclusion: candidate d wins on criteria 2, 3, and 5 while tying on
1 and 4, so d is adopted as the final pitch. Revision 1 wrote
candidate a as the first draft; revision 2 below replaces it with d.
"""

from pathlib import Path

# Revision 2 (final): candidate d. It beats revision 1 because the
# blink counter could pass as wellness (weak on criterion 2), names
# no audience (weak on 3), and leaves only a generic counter in mind
# (weak on 5), while SockMatch pairs a problem nobody has with a
# familiar dating-app pitch and a specific picture of two socks
# being matched by fabric and trauma, all in one clean sentence.
PITCH = (
    "SockMatch is a dating app exclusively for single socks whose "
    "partners vanished in the wash, matching them by fabric and "
    "trauma so they can grieve together."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(PITCH, encoding="utf-8")


if __name__ == "__main__":
    main()
