import re


def get_input():
    cards = []
    for line in open('.cached_input/2023_04').readlines():
        matches = re.search(r':\s*([^\\|]+)\|\s*(.+)', line)
        winners = [int(x) for x in matches.group(1).split()]
        picked = [int(x) for x in matches.group(2).split()]
        cards.append((winners, picked))
    return cards


def part1(cards):
    total = 0
    for (winners, picked) in cards:
        overlaps = len(set(winners) & set(picked))
        if overlaps > 0:
            total += 2**(overlaps-1)
    return total


def part2(cards):
    totals = [1] * len(cards)
    for i, (winners, picked) in enumerate(cards):
        overlaps = len(set(winners) & set(picked))
        for j in range(i+1, min(i+1+overlaps, len(cards))):
            totals[j] += totals[i]
    return sum(totals)


print(part1(get_input()))
print(part2(get_input()))
