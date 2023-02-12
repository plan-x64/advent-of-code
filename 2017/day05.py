def get_input():
    return list(map(int, open('.cached_input/2017_05').read().splitlines()))


def jump(jmps, inc_func):
    idx = 0
    counter = 0
    while idx < len(jmps):
        old, idx = idx, idx + jmps[idx]
        jmps[old] = inc_func(jmps[old])
        counter += 1
    return counter


def part1(jmps):
    return jump(jmps, lambda x: x + 1)


def part2(jmps):
    return jump(jmps, lambda x: x + (1 if x < 3 else -1))


print(part1(get_input()))
print(part2(get_input()))
