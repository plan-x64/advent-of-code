import datautils
import re


def _parse_line(line):
    matches = re.search("([0-9]{1,2})-([0-9]{1,2}),([0-9]{1,2})-([0-9]{1,2})", line)
    first = set(range(int(matches.group(1)), int(matches.group(2)) + 1))
    second = set(range(int(matches.group(3)), int(matches.group(4)) + 1))
    return first, second


def full_overlap(first, second):
    return first.issubset(second) or second.issubset(first)


def partial_overlap(first, second):
    return len(first.intersection(second)) > 0


if __name__ == "__main__":
    url = "https://adventofcode.com/2022/day/4/input"
    lines = datautils.read_input_data(url).splitlines()

    full_overlaps = sum([full_overlap(*_parse_line(line)) for line in lines])
    partial_overlaps = sum([partial_overlap(*_parse_line(line)) for line in lines])

    print("({},  {})".format(full_overlaps, partial_overlaps))
