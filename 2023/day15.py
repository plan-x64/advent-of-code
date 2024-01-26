from collections import OrderedDict


def get_input():
    return open('.cached_input/2023_15').read().split(',')


def aoc_hash(string, start):
    updated = start
    for c in string:
        updated += ord(c)
        updated *= 17
        updated = updated % 256
    return updated


def power(boxes):
    total = 0
    for i, b in enumerate(boxes):
        for j, (label, lens) in enumerate(b.items()):
            total += (i+1)*(j+1)*lens
    return total


def part1(instructions):
    return sum(aoc_hash(i, 0) for i in instructions)


def part2(instructions):
    boxes = [OrderedDict() for _ in range(256)]

    for i in instructions:
        if '-' in i:
            label, _ = i.split('-')
            idx = aoc_hash(label, 0)
            if label in boxes[idx]:
                boxes[idx].pop(label)
        else:
            label, lens = i.split('=')
            idx = aoc_hash(label, 0)
            if label in boxes[idx]:
                boxes[idx][label] = int(lens)
            else:
                boxes[idx][label] = int(lens)

    return power(boxes)


print(part1(get_input()))
print(part2(get_input()))
