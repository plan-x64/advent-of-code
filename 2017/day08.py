from collections import defaultdict
from operator import le, lt, gt, ge, eq, ne
import re


def get_input():
    pattern = re.compile(r'([a-z]+) (inc|dec) (-?\d+) if ([a-z]+) ([!><=]+) (-?\d+)')
    instructions = []
    for line in open('.cached_input/2017_08').read().splitlines():
        reg, op, value, if_reg, if_cond, if_value = re.search(pattern, line).groups()
        instructions.append(((reg, op, int(value)), (if_reg, if_cond, int(if_value))))
    return instructions


def execute(instructions):
    global_max = 0
    ops = {'>': gt, '<': lt, '>=': ge, '<=': le, '==': eq, '!=': ne}
    registers = defaultdict(int)

    for (reg, op, value), (if_reg, if_cond, if_value) in instructions:
        if ops[if_cond](registers[if_reg], if_value):
            registers[reg] += value if op == 'inc' else -value
            global_max = max(global_max, registers[reg])

    largest_key = max(registers, key=lambda k: registers[k])
    return registers[largest_key], global_max


def part1(instructions):
    end_max, _ = execute(instructions)
    return end_max


def part2(instructions):
    _, global_max = execute(instructions)
    return global_max


print(part1(get_input()))
print(part2(get_input()))
