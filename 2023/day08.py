from itertools import cycle
import math
import re


def get_input():
    data = [line.strip('\n') for line in open('.cached_input/2023_08').readlines()]
    instructions = [c for c in data[0]]

    graph = dict()
    for line in data[2:]:
        node, left, right = re.findall(r'[A-Z]{3}', line)
        graph[node] = (left, right)

    return instructions, graph


def traverse(instructions, graph, start, end_cond):
    node = start
    count = 0

    for instruction in cycle(instructions):
        count += 1
        left, right = graph[node]
        if instruction == 'L':
            node = left
        else:
            node = right

        if end_cond(node):
            return count


def part1(instructions, graph):
    return traverse(instructions, graph, 'AAA', lambda c: c == 'ZZZ')


def part2(instructions, graph):
    current_nodes = set([k for k in graph.keys() if k.endswith('A')])
    results = [traverse(instructions, graph, node, lambda c: c.endswith('Z')) for node in current_nodes]
    return math.lcm(*results)


print(part1(*get_input()))
print(part2(*get_input()))

