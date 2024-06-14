def get_input():
    return [int(line.strip('\n')) for line in open('.cached_input/2020_01').readlines()]


def part1(expenses):
    recorded = set(expenses)

    want = 2020
    for expense in expenses:
        other = want - expense
        if other in recorded:
            return other * expense

def part2(expenses):
    from itertools import product
    recorded = {n1+n2: (n1, n2) for n1, n2 in product(expenses, repeat=2)}

    want = 2020
    for expense in expenses:
        other = want - expense
        if other in recorded:
            n1, n2 = recorded[other]
            return n1 * n2 * expense

print(part1(get_input()))
print(part2(get_input()))