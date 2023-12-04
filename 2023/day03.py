from collections import defaultdict
from itertools import product
import re
import math


def get_input():
    return [line.strip('\n') for line in open('.cached_input/2023_03').readlines()]


def parse_nums(schematic):
    nums = []
    for i, line in enumerate(schematic):
        for match in re.finditer(r'(\d+)', line):
            nums.append((int(match.group()), (i, match.span())))
    return nums, len(schematic)


def parse_symbols(schematic, regex):
    symbols = set()
    for i, line in enumerate(schematic):
        for match in re.finditer(regex, line):
            symbols.add((i, match.start()))
    return symbols


def surrounding(coords, size):
    (y, (start, end)) = coords
    xs = range(max(start-1, 0), min(end+1, size))
    ys = range(max(y-1, 0), min(y+2, size))
    return set(product(ys, xs))


def part1(schematic):
    (nums, size) = parse_nums(schematic)
    symbols = parse_symbols(schematic, r'[^\d|\\.]')
    return sum([num for (num, coords) in nums if not surrounding(coords, size).isdisjoint(symbols)])


def part2(schematic):
    (nums, size) = parse_nums(schematic)
    symbols = parse_symbols(schematic, r'(\*)')

    gears = defaultdict(list)
    for (num, coords) in nums:
        overlaps = surrounding(coords, size) & symbols
        if len(overlaps) > 0:
            for overlap in overlaps:
                gears[overlap].append(num)

    return sum([math.prod(parts) for parts in gears.values() if len(parts) == 2])


print(part1(get_input()))
print(part2(get_input()))
