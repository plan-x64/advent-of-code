from functools import reduce
from operator import xor


def knot_hash(knot, lengths, times):
    knot = [i for i in range(len(knot))]
    idx = 0
    skip_size = 0
    for _ in range(times):
        for length in lengths:
            affected = [(idx + i) % len(knot) for i in range(length)]
            swaps = list(zip(affected, affected[::-1]))[:(length // 2)]
            for j, k in swaps:
                knot[j], knot[k] = knot[k], knot[j]
            idx = (idx + length + skip_size) % len(knot)
            skip_size += 1
    return knot


def part1(size):
    lengths = list(map(int, open('.cached_input/2017_10').read().replace(',', ' ').split()))
    knot = knot_hash([i for i in range(size)], lengths, 1)
    return knot[0]*knot[1]


def part2(size):
    lengths = list(map(ord, [*open('.cached_input/2017_10').read()])) + [17, 31, 73, 47, 23]
    knot = knot_hash([i for i in range(size)], lengths, 64)
    dense = [reduce(xor, knot[offset*16:(offset+1)*16]) for offset in range(16)]
    hex_str = ''.join(['{:02x}' .format(block) for block in dense])
    return hex_str


print(part1(256))
print(part2(256))
