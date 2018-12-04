"""
--- Day 2: Inventory Management System ---

You stop falling through time, catch your breath, and check the screen on
the device. "Destination reached. Current Year: 1518. Current Location:
North Pole Utility Closet 83N10." You made it! Now, to find those
anomalies.

Outside the utility closet, you hear footsteps and a voice. "...I'm not
sure either. But now that so many people have chimneys, maybe he could
sneak in that way?" Another voice responds, "Actually, we've been working
on a new kind of suit that would let him fit through tight spaces like
that. But, I heard that a few days ago, they lost the prototype fabric,
the design plans, everything! Nobody on the team can even seem to
remember important details of the project!"

"Wouldn't they have had enough fabric to fill several boxes in the
warehouse? They'd be stored together, so the box IDs should be similar.
Too bad it would take forever to search the warehouse for two similar box
IDs..." They walk too far away to hear any more.

Late at night, you sneak to the warehouse - who knows what kinds of
paradoxes you could cause if you were discovered - and use your fancy
wrist device to quickly scan every box and produce a list of the likely
candidates (your puzzle input).

To make sure you didn't miss any, you scan the likely candidate boxes
again, counting the number that have an ID containing exactly two of any
letter and then separately counting those with exactly three of any
letter. You can multiply those two counts together to get a rudimentary
checksum and compare it to what your device predicts.

For example, if you see the following box IDs:

abcdef contains no letters that appear exactly two or three times.
bababc contains two a and three b, so it counts for both.
abbcde contains two b, but no letter appears exactly three times.
abcccd contains three c, but no letter appears exactly two times.
aabcdd contains two a and two d, but it only counts once.
abcdee contains two e.
ababab contains three a and three b, but it only counts once.

Of these box IDs, four of them contain a letter which appears exactly
twice, and three of them contain a letter which appears exactly three
times. Multiplying these together produces a checksum of 4 * 3 = 12.

What is the checksum for your list of box IDs?

--- Part Two ---

Confident that your list of box IDs is complete, you're ready to find the
boxes full of prototype fabric.

The boxes will have IDs which differ by exactly one character at the same
position in both strings. For example, given the following box IDs:

abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz

The IDs abcde and axcye are close, but they differ by two characters (the
second and fourth). However, the IDs fghij and fguij differ by exactly
one character, the third (h and u). Those must be the correct boxes.

What letters are common between the two correct box IDs? (In the example
above, this is found by removing the differing character from either ID,
producing fgij.)
"""

from collections import Counter
from src.utils import read_file


def compute_checksum(ids):
    ids_containing_a_letter_twice = [i for i in ids if id_contains_letter_n_times(i, 2)]
    ids_containing_a_letter_thrice = [i for i in ids if id_contains_letter_n_times(i, 3)]
    return len(ids_containing_a_letter_twice) * len(ids_containing_a_letter_thrice)


def id_contains_letter_n_times(x, n):
    return n in Counter(x).values()


"""
Day 2 Step 2
The list of box ids is trasformed in a number_of_ids * lenght(id) matrix.
Then, given that the offending ids differs by one characted in the same
position, one column at a time is removed. When the resulting list contains
two identical "truncated" ids the "offending" character position is found.
"""


def find_adjacent_boxes_id(ids):
    id_lenght = len(ids[0])

    for char_to_remove_idx in range(id_lenght):
        cleaned_ids = [remove_char_at(i, char_to_remove_idx) for i in ids]
        id_counter = Counter(cleaned_ids)
        if 2 in id_counter.values():
            adjacent_boxes_id, _ = id_counter.most_common(1)[0]
            return adjacent_boxes_id


def remove_char_at(s, char_to_remove):
    return s[:char_to_remove] + s[char_to_remove + 1 :]


if __name__ == "__main__":
    warehouse_ids = read_file("02_IMS.txt")
    checksum = compute_checksum(warehouse_ids)
    print(f"Checksum: {checksum}")

    adjacent_boxes_id = find_adjacent_boxes_id(warehouse_ids)
    print(f"Adjacent boxes ID: {adjacent_boxes_id}")
