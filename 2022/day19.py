import datautils
import numpy as np
import re


def parse_input(data):
    blueprints = {}
    for line in data.splitlines():
        i, a, b, c, d, e, f = map(int, re.findall(r'\d+', line))
        # each blueprint contains (what bot is made, what the cost of said bot is)
        blueprints[i] = ((np.array([1, 0, 0, 0]), np.array([a, 0, 0, 0])),  # ore
                         (np.array([0, 1, 0, 0]), np.array([b, 0, 0, 0])),  # clay
                         (np.array([0, 0, 1, 0]), np.array([c, d, 0, 0])),  # obsidian
                         (np.array([0, 0, 0, 1]), np.array([e, 0, f, 0])),  # geode
                         (np.array([0, 0, 0, 0]), np.array([0, 0, 0, 0])))  # add no new bot (default)
    return blueprints


def truncate(states):
    def key(state):
        return tuple(np.flip(state[0])+np.flip(state[1])) + tuple(np.flip(state[1]))
    return sorted({key(states): states for states in states}.values(), key=key)[-1000:]


def find_max(blueprint, t):
    states = [(np.array([1, 0, 0, 0]), np.array([0, 0, 0, 0]))]
    for curr_t in range(0, t):
        added = []
        for bots, resources in states:
            for make, cost in blueprint:
                if all(cost <= resources):
                    added.append((bots + make, resources + bots - cost))
        states = truncate(added)
    return max(resources[3] for (_, resources) in states)


def part1(blueprints):
    return np.sum([num * find_max(blueprint, 24) for num, blueprint in blueprints.items()])


def part2(blueprints):
    return np.prod([find_max(blueprint, 32) for blueprint in list(blueprints.values())[0:3]])


if __name__ == "__main__":
    url = "https://adventofcode.com/2022/day/19/input"
    input_data = datautils.read_input_data(url)
    parsed = parse_input(input_data)
    print("({},  {})".format(part1(parsed), part2(parsed)))
