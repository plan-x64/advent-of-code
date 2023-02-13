def get_input():
    pipes = dict()
    for line in open('.cached_input/2017_12').read().splitlines():
        node, neighbors = line.split(' <-> ')
        pipes[int(node)] = list(map(int, neighbors.replace(',', '').split()))
    return pipes


def traverse(start, pipes):
    q = [start]
    visited = set()

    while q:
        node = q.pop()
        visited.add(node)
        q.extend([connection for connection in pipes[node] if connection not in visited])

    return visited


def part1(pipes):
    return len(traverse(0, pipes))


def part2(pipes):
    not_seen = set([k for k in pipes.keys()])
    groups = 0

    while not_seen:
        not_seen -= traverse(next(iter(not_seen)), pipes)
        groups += 1

    return groups


print(part1(get_input()))
print(part2(get_input()))
