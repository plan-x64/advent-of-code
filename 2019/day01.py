def get_input():
    return map(int, open('.cached_input/2019_01').read().split('\n'))


def decrement(mass):
    reduced = (mass // 3) - 2
    while reduced > 0:
        yield reduced
        reduced = (reduced // 3) - 2


def part1(masses):
    return sum([(mass // 3) - 2 for mass in masses])


def part2(masses):
    return sum([sum(m for m in decrement(mass)) for mass in masses])


print(part1(get_input()))
print(part2(get_input()))
