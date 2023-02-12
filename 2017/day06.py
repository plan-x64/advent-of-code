def get_input():
    return list(map(int, open('.cached_input/2017_06').read().split()))


def distribute(mem):
    max_value = max(mem)
    offset = mem.index(max_value)
    mem[offset] = 0
    offset += 1
    for i in range(max_value):
        mem[(i + offset) % len(mem)] += 1
    return mem


def detect_loop(mem):
    observed = set()
    observed.add(tuple(mem))
    cycle = 0

    while True:
        cycle += 1
        mem = distribute(mem)
        if tuple(mem) in observed:
            return cycle, mem
        else:
            observed.add(tuple(mem))


def part1(mem):
    cycle, _ = detect_loop(mem)
    return cycle


def part2(mem):
    _, mem = detect_loop(mem)
    cycle, _ = detect_loop(mem)
    return cycle


print(part1(get_input()))
print(part2(get_input()))
