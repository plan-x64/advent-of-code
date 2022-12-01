import adventutils
from collections import Counter
import itertools
import sys

def parse_input(input):
    return ([char for char in input[0]], dict(pair.split(' -> ') for pair in input[2:]))

def diff(starting_polymer, rules, steps):
    pairs = Counter(itertools.pairwise(starting_polymer))

    for _ in range(steps):
        updated_pairs = Counter()
        for (p1, p2) in pairs.keys():
            if p1+p2 in rules: 
                updated_pairs[(p1, rules[p1+p2])] += pairs[(p1, p2)]
                updated_pairs[(rules[p1+p2], p2)] += pairs[(p1, p2)]
                updated_pairs[(p1, p2)] -= pairs[(p1, p2)]

        pairs.update(updated_pairs)

    firsts = Counter()
    seconds = Counter()
    for ((p1, p2), count) in pairs.items():
        if count > 0:
            firsts[p1] += count
            seconds[p2] += count
    first_counts = firsts.most_common()
    second_counts = seconds.most_common()
    return max(first_counts[0][1], second_counts[0][1]) - min(first_counts[-1][1], second_counts[-1][1])

def main():
    sessionId = sys.argv[1]
    url = "https://adventofcode.com/2021/day/14/input"
    input = adventutils.gather_input_data(url, sessionId)

    (starting_polymer, rules) = parse_input(input)
    print("Part1: {}".format(diff(starting_polymer, rules, 10)))
    print("Part2: {}".format(diff(starting_polymer, rules, 40)))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Need to pass 'python day14.py sessionId' (Arguments={}, Length={})".format(str(sys.argv), len(sys.argv)))
    else:  
        main()