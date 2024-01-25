from collections import Counter


def get_input():
    hands = []
    for line in open('.cached_input/2023_07').readlines():
        (hand, bid) = line.strip('\n').split(' ')
        hands.append((hand, int(bid)))
    return hands


def strength_joker(hand):
    substituted = [strength(hand.replace('J', replace)) for replace in '23456789TQKA']
    best, fake_hand = max(substituted, key=lambda bh: bh[0])

    hand = hand.replace('T', chr(ord('9') + 1))
    hand = hand.replace('J', chr(ord('2') - 1))
    hand = hand.replace('Q', chr(ord('9') + 3))
    hand = hand.replace('K', chr(ord('9') + 4))
    hand = hand.replace('A', chr(ord('9') + 5))
    return best, hand


def strength(hand):
    hand = hand.replace('T', chr(ord('9') + 1))
    hand = hand.replace('J', chr(ord('9') + 2))
    hand = hand.replace('Q', chr(ord('9') + 3))
    hand = hand.replace('K', chr(ord('9') + 4))
    hand = hand.replace('A', chr(ord('9') + 5))
    counter = sorted(Counter(hand).values())

    if counter == [5]:
        return 10, hand
    elif counter == [1, 4]:
        return 9, hand
    elif counter == [2, 3]:
        return 8, hand
    elif counter == [1, 1, 3]:
        return 7, hand
    elif counter == [1, 2, 2]:
        return 6, hand
    elif counter == [1, 1, 1, 2]:
        return 5, hand
    elif counter == [1, 1, 1, 1, 1]:
        return 4, hand


def part1(hands):
    hands = sorted(hands, key=lambda hb: strength(hb[0]))
    return sum((i+1)*bid for i, (_, bid) in enumerate(hands))


def part2(hands):
    hands = sorted(hands, key=lambda hb: strength_joker(hb[0]))
    return sum((i + 1) * bid for i, (_, bid) in enumerate(hands))


print(part1(get_input()))
print(part2(get_input()))
