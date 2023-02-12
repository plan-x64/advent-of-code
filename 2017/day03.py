from collections import defaultdict
from itertools import cycle
from math import sqrt, floor


def pattern(num):
    repeats = [i+1 for i in range(floor(sqrt(5/4 * num))) for _ in (0, 1)]
    directions = cycle([1+0j, 1j, -1+0j, -1j])
    return [direction for amount, direction in zip(repeats, directions) for _ in range(amount)][:num-1]


def part1(num):
    position = complex(0, 0)
    for inc in pattern(num):
        position += inc

    return abs(int(position.real)) + abs(int(position.imag))


def adjacent(position):
    return [position + complex(i, j) for i in range(-1, 2) for j in range(-1, 2) if complex(i, j) != 0+0j]


def part2(num):
    values = defaultdict(int)
    values[complex(0, 0)] = 1

    position = complex(0, 0)
    for i, inc in enumerate(pattern(num)):
        position += inc
        value = sum([values[pos] for pos in adjacent(position)])
        if value > num:
            return value
        else:
            values[position] = values[position] + value


print(part1(277678))
print(part2(277678))
