import datautils
import itertools


def parse_input(data):
    network = {}
    flows = {}
    for line in data.splitlines():
        (valve_text, tunnels_text) = tuple(line.split(';'))
        valve = valve_text[6:8]
        flow_rate = int(valve_text[23:])
        connections = tunnels_text.replace(',', ' ').split()[4:]
        network[valve] = connections
        if flow_rate > 0:
            flows[valve] = flow_rate
    return network, flows


def min_paths(network):
    valves = network.keys()
    costs = {}
    for (v1, v2) in itertools.product(valves, valves):
        if v1 == v2:
            costs[(v1, v2)] = 0
        elif v2 in network[v1]:
            costs[(v1, v2)] = 1
        else:
            costs[(v1, v2)] = 9999

    for intermediate in valves:
        for start in valves:
            for end in valves:
                costs[(start, end)] = min(costs[(start, end)], costs[(start, intermediate)] + costs[(intermediate, end)])

    return costs


def calculate(flows, costs, initial_state):
    stack = [initial_state]
    maxes = []

    while stack:
        valve, accum, open_valves, remaining = stack.pop()
        maxes.append((accum, set(open_valves)))
        for next_valve, flow in flows.items():
            time_left = remaining - costs[(valve, next_valve)] - 1
            if time_left <= 0 or next_valve in open_valves:
                continue
            else:
                stack.append((next_valve, accum + flow * time_left, open_valves + [next_valve], time_left))

    return maxes


def pt1(network, flows):
    costs = min_paths(network)
    maxes = calculate(flows, costs, ('AA', 0, [], 30))
    return max(accum for (accum, _) in maxes)


def pt2(network, flows):
    costs = min_paths(network)
    maxes = calculate(flows, costs, ('AA', 0, [], 26))
    return max(accum1 + accum2 for (accum1, open1) in maxes for (accum2, open2) in maxes if open1.isdisjoint(open2))


if __name__ == "__main__":
    url = "https://adventofcode.com/2022/day/16/input"
    input_data = datautils.read_input_data(url)

    print("({},  {})".format(pt1(*parse_input(input_data)), pt2(*parse_input(input_data))))
