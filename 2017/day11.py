from functools import reduce
from itertools import accumulate
import numpy as np
from operator import add


def get_input():
    increments = {
        'nw': np.array([-1, 0, +1]),
        'n': np.array([0, -1, +1]),
        'ne': np.array([+1, -1, 0]),
        'sw': np.array([-1, +1, 0]),
        's': np.array([0, +1, -1]),
        'se': np.array([+1, 0, -1])
    }
    directions = open('.cached_input/2017_11').read().split(',')
    return list(map(lambda x: increments[x], directions))


def distance(pos):
    return sum(np.absolute(pos)) // 2


def part1(steps):
    return distance(reduce(add, steps))


def part2(steps):
    return max(map(distance, accumulate(steps)))


print(part1(get_input()))
print(part2(get_input()))
