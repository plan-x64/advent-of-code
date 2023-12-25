from itertools import pairwise


def get_input():
    lines = [line.strip('\n') for line in open('.cached_input/2023_09').readlines()]
    return [list(map(int, line.split())) for line in lines]


def fwd_predict(reading):
    diffs = [b-a for a, b in pairwise(reading)]
    if all(map(lambda x: x == 0, diffs)):
        return reading[0]
    else:
        return reading[-1] + fwd_predict(diffs)


def part1(readings):
    return sum([fwd_predict(reading) for reading in readings])


def back_predict(reading):
    diffs = [b - a for a, b in pairwise(reading)]
    if all(map(lambda x: x == 0, diffs)):
        return reading[0]
    else:
        return reading[0] - back_predict(diffs)


def part2(readings):
    return sum([back_predict(reading) for reading in readings])


print(part1(get_input()))
print(part2(get_input()))
