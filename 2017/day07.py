from collections import deque


def get_input():
    nodes = {}
    lines = open('.cached_input/2017_07').read().splitlines()
    for line in lines:
        parts = line.split()
        node_name, node_weight = parts[0], int(parts[1][1:-1])

        if len(parts) > 2:
            children = [child.replace(',', '') for child in parts[3:]]
        else:
            children = []

        nodes[node_name] = (node_weight, children)
    return nodes


def find_root(nodes):
    parents = set([name for name, (_, children) in nodes.items() if children != []])
    children = set([child for (_, children) in nodes.values() for child in children if children != []])
    return list(parents - children)[0]


def part1(nodes):
    return find_root(nodes)


def reverse_topo_sort(start, nodes):
    order = []
    start_nodes = []
    q = [start]
    while q:
        name = q.pop()
        order.append(name)
        _, children = nodes[name]
        if children:
            q.extend(children)
        else:
            start_nodes.append(name)
    return reversed(order), start_nodes


def part2(nodes):
    order, start_nodes = reverse_topo_sort(find_root(nodes), nodes)
    weights = {start: nodes[start][0] for start in start_nodes}
    queue = deque(order)

    while queue:
        name = queue.popleft()
        weight, children = nodes[name]
        child_weights = [weights[child] for child in children]
        
        if child_weights and max(child_weights) != min(child_weights):
            desired = max(child_weights, key=child_weights.count)
            invalid_child = [child for child in children if weights[child] != desired][0]
            _, invalid_children = nodes[invalid_child]
            return desired - sum([weights[child] for child in invalid_children])
        else:
            weights[name] = weight + sum(child_weights)


print(part1(get_input()))
print(part2(get_input()))
