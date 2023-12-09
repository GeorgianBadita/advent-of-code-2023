from enum import IntEnum


class HandType(IntEnum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7


card_values = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "J": 10,
    "T": 9,
    "9": 8,
    "8": 7,
    "7": 6,
    "6": 5,
    "5": 4,
    "4": 3,
    "3": 2,
    "2": 1,
}


class Hand:
    def __init__(self, hand):
        self.hand = hand
        self.type = self.__get_type(hand)

    def __get_type(self, hand):
        fc = {}
        for card in hand:
            fc[card] = fc.get(card, 0) + 1

        max_occ = max(fc.values())

        # we have high card
        if max_occ == 1:
            return HandType.HIGH_CARD

        # we have one pair
        if max_occ == 2 and len(fc) == 4:
            return HandType.ONE_PAIR

        # we have two pairs
        if max_occ == 2 and len(fc) == 3:
            return HandType.TWO_PAIR

        # we have three of a kind
        if max_occ == 3 and len(fc) == 3:
            return HandType.THREE_OF_A_KIND

        # we have full house
        if max_occ == 3 and len(fc) == 2:
            return HandType.FULL_HOUSE

        # we have four of a kind
        if max_occ == 4 and len(fc) == 2:
            return HandType.FOUR_OF_A_KIND

        # we have five of a kind
        return HandType.FIVE_OF_A_KIND

    def __lt__(self, ot):
        if self.type < ot.type:
            return True

        if self.type > ot.type:
            return False

        for idx in range(len(self.hand)):
            if card_values[self.hand[idx]] < card_values[ot.hand[idx]]:
                return True

            if card_values[self.hand[idx]] > card_values[ot.hand[idx]]:
                return False

        return False

    def __eq__(self, ot):
        return self.hand == ot.hand

    # Just in case I am using it for sets or something
    def __hash__(self):
        return hash(repr(self))


def read_file(path):
    hands = []
    with open(path, "r") as f:
        lines = f.readlines()
        for line in lines:
            hand, bid = line.split(" ")
            hands.append((Hand(hand), int(bid.strip())))

    return hands


def solve(poker_hands):
    poker_hands = sorted(poker_hands, key=lambda x: x[0])
    res = 0
    for idx, poker_hand in enumerate(poker_hands):
        _, bid = poker_hand
        res += (idx + 1) * bid

    return res


file_path = "./in-day7.txt"

poker_hands = read_file(file_path)

print(solve(poker_hands))
