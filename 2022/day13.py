import datautils
import functools
import itertools
import json
from math import prod


def parse_input(data):
    pairs = []
    for packets in data.split('\n\n'):
        p1, p2 = tuple(packets.split('\n'))
        pairs.append((json.loads(p1), json.loads(p2)))
    return pairs


def compare(p1, p2):
    if p1 is None:
        return -1
    elif p2 is None:
        return 1

    if isinstance(p1, list) or isinstance(p2, list):
        p1s = p1 if isinstance(p1, list) else [p1]
        p2s = p2 if isinstance(p2, list) else [p2]
        for e1, e2 in itertools.zip_longest(p1s, p2s, fillvalue=None):
            result = compare(e1, e2)
            if result == 0:
                continue
            else:
                return result
        return 0
    elif p1 == p2:
        return 0
    else:
        return -1 if p1 < p2 else 1


def pt1(packets):
    messages = {idx+1: compare(p1, p2) for idx, (p1, p2) in enumerate(packets)}
    return sum([k for k, v in messages.items() if v == -1])


def pt2(packets):
    dividers = [[[2]], [[6]]]
    messages = [item for pair in packets for item in pair] + dividers
    ordered = sorted(messages, key=functools.cmp_to_key(compare))
    return prod([(idx+1) for (idx, val) in enumerate(ordered) if val in dividers])


if __name__ == "__main__":
    url = "https://adventofcode.com/2022/day/13/input"
    input_data = datautils.read_input_data(url)
    print("({},  {})".format(pt1(parse_input(input_data)), pt2(parse_input(input_data))))
