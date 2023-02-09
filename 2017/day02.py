from itertools import permutations


def get_input():
    lines = open('.cached_input/2017_02').read().splitlines()
    return [[int(c) for c in line.split()] for line in lines]


def part1(spreadsheet):
    return sum([max(row) - min(row) for row in spreadsheet])


def part2(spreadsheet):
    sum = 0
    for row in spreadsheet:
        for numerator, divisor in permutations(row, 2):
            if numerator % divisor == 0:
                sum += numerator // divisor
    return sum


print(part1(get_input()))
print(part2(get_input()))
