from collections import defaultdict
import datautils
import itertools


def parse_input(data):
    fs = defaultdict(int)
    stack = ['/']
    for line in map(str.split, data.splitlines()):
        if line[1] == 'cd':
            if line[2] == '/':
                stack = ['/']
            elif line[2] == '..':
                stack.pop()
            else:
                stack.append(line[2] + '/')
        elif line[1] == 'ls':
            continue
        elif line[0] == 'dir':
            fs[''.join(stack) + line[1] + '/'] += 0
        else:
            for idx in range(len(stack)):
                fs[''.join(stack[:idx+1])] += int(line[0])

    return sorted(fs.values())


if __name__ == "__main__":
    url = "https://adventofcode.com/2022/day/7/input"
    input_data = datautils.read_input_data(url)
    sizes = parse_input(input_data)

    pt1 = sum(itertools.takewhile(lambda x: x < 100000, sizes))
    pt2 = next(itertools.dropwhile(lambda x: x < (sizes[-1] - 40000000), sizes))
    print("({},  {})".format(pt1, pt2))