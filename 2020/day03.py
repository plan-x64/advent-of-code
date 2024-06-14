def get_input():
    grid = [[c for c in line.strip('\n')] for line in open('.cached_input/2020_03').readlines()]
    trees = set()
    for i, row in enumerate(grid):
        for j, item in enumerate(row):
            if item == '#':
                trees.add((i, j))

    return (len(grid), len(grid[0])), trees


def move(dx, dy):
    x, y = (0, 0)

    while True:
        x, y = x+dx, y+dy
        yield y, x


def traverse(change, size, trees):
    depth, length = size
    dx, dy = change

    from itertools import takewhile
    positions = list(takewhile(lambda p: p[0] < depth, move(dx, dy)))
    return sum([(row, col % length) in trees for row, col in positions])


def part1(size, trees):
    return traverse((3, 1), size, trees)


def part2(size, trees):
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    import math
    return math.prod(traverse(slope, size, trees) for slope in slopes)


print(part1(*get_input()))
print(part2(*get_input()))
