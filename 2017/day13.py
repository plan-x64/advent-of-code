import re


def get_input():
    firewall = dict()
    for line in open('.cached_input/2017_13').read().splitlines():
        layer, depth = re.findall(r'(\d+)', line)
        firewall[int(layer)] = int(depth)
    return firewall


def scanner_pos(depth, time):
    positions = list(range(depth)) + list(range(depth-2, 0, -1))
    return positions[time % len(positions)]


def simulate(firewall, offset):
    layer = 0
    caught = []
    for time in range(max(firewall.keys()) + 1):
        if layer in firewall and scanner_pos(firewall[layer], time+offset) == 0:
            caught.append(layer)
        layer += 1
    return sum(map(lambda c: c * firewall[c], caught)), caught


def part1(firewall):
    return sum([layer * firewall[layer] for layer in firewall if scanner_pos(firewall[layer], layer) == 0])


def part2(firewall):
    return [t for t in range(5000000) if not any(scanner_pos(firewall[layer], layer + t) == 0 for layer in firewall)][0]


print(part1(get_input()))
print(part2(get_input()))
