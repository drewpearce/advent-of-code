from helpers.aoc import get_input


class Hand(object):
    def __init__(self, cards, bid, wild=None):
        self.cards = cards
        self.bid = int(bid)
        self.type = self.determine_type(wild=wild)

    def determine_type(self, wild=None):
        counts = {}

        for c in self.cards:
            if c in counts:
                counts[c] += 1
            else:
                counts[c] = 1

        if wild and wild in counts:
            return self.determine_type_w_wild(counts, wild)

        if 5 in counts.values():
            # 5 of a Kind
            return 6
        elif 4 in counts.values():
            # 4 of a Kind
            return 5
        elif 3 in counts.values() and 2 in counts.values():
            # Full House
            return 4
        elif 3 in counts.values():
            # 3 of a Kind
            return 3
        elif 2 in counts.values() and list(counts.values()).count(2) == 2:
            # 2 Pair
            return 2
        elif 2 in counts.values():
            # 1 Pair
            return 1
        else:
            return 0

    def determine_type_w_wild(self, counts, wild):
        wild_count = counts.pop(wild)

        if (
            wild_count == 5
            or any([c + wild_count == 5 for c in counts.values()])
        ):
            return 6
        elif (
            wild_count == 4
            or any([c + wild_count == 4 for c in counts.values()])
        ):
            return 5
        elif (
            (wild_count == 3 and 2 in counts.values())
            or (wild_count == 2 and 3 in counts.values())
            or (
                wild_count == 1
                and 2 in counts.values()
                and list(counts.values()).count(2) == 2
            )
        ):
            return 4
        elif (
            wild_count == 3
            or wild_count == 2
            or (wild_count == 1 and 2 in counts.values())
        ):
            return 3
        elif wild_count == 2 and 2 in counts.values():
            return 2
        else:
            return 1


def part_1(_in):
    cards = '23456789TJQKA'
    hands = [
        Hand(*line.split(' '))
        for line in _in.splitlines()
    ]
    hands = sorted(
        hands,
        key=lambda h: (h.type, tuple(cards.index(c) for c in h.cards)),
    )

    return sum([h.bid * (i + 1) for i, h in enumerate(hands)])


def part_2(_in):
    cards = 'J23456789TQKA'
    hands = [
        Hand(*line.split(' '), wild='J')
        for line in _in.splitlines()
    ]
    hands = sorted(
        hands,
        key=lambda h: (h.type, tuple(cards.index(c) for c in h.cards)),
    )

    return sum([h.bid * (i + 1) for i, h in enumerate(hands)])


def main():
    _in = get_input(2023, 7)
#     _in = """32T3K 765
# T55J5 684
# KK677 28
# KTJJT 220
# QQQJA 483
# """
    print(part_1(_in))
    print(part_2(_in))


if __name__ == '__main__':
    main()
