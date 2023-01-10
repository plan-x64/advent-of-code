import datautils
from functools import reduce
from operator import add, mul


def parse_input(data):
    monkeys = []
    for text in data:
        lines = text.splitlines()
        monkeys.append(parse_monkey(lines))
    return monkeys


def parse_monkey(lines):
    items = parse_items(lines[1])
    operation = parse_operation(lines[2])
    outcome = parse_test(lines[3:])
    return items, operation, outcome


def parse_items(line):
    return [int(val) for val in line[18:].split(',')]


def parse_divisor(line):
    return int(line[21:].split()[0])


def parse_gcd(data):
    return reduce(mul, [parse_divisor(text.splitlines()[3]) for text in data], 1)


def parse_operation(line):
    (operand, value) = tuple(line[23:].split(' '))
    operator = mul if operand == '*' else add
    if value == "old":
        return lambda x, w: w(operator(x, x))
    else:
        return lambda x, w: w(operator(x, int(value)))


def parse_test(lines):
    divisor = parse_divisor(lines[0])
    true = int(lines[1][29:].split()[0])
    false = int(lines[2][30:].split()[0])
    return lambda x: true if (x % divisor == 0) else false


def execute(monkeys, counter, worry):
    for idx, (items, operation, outcome) in enumerate(monkeys):
        for _ in range(len(items)):
            counter[idx] += 1
            item = operation(items.pop(0), worry)
            next_monkey = outcome(item)
            monkeys[next_monkey][0].append(item)
    return monkeys, counter


def simulate(monkeys, steps, worry):
    counter = [0] * len(monkeys)
    for _ in range(steps):
        monkeys, counter = execute(monkeys, counter, worry)
    return counter


if __name__ == "__main__":
    url = "https://adventofcode.com/2022/day/11/input"
    input_data = datautils.read_input_data(url).split('\n\n')
    gcd = parse_gcd(input_data)

    pt1 = mul(*sorted(simulate(parse_input(input_data), 20, lambda x: x // 3))[-2:])
    pt2 = mul(*sorted(simulate(parse_input(input_data), 10000, lambda x: x % gcd))[-2:])

    print("({},  {})".format(pt1, pt2))
