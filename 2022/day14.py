import itertools

import datautils


def parse_input(data):
    rocks = set()
    lines = [[tuple(map(int, coord.split(','))) for coord in line.split(' -> ')] for line in data.splitlines()]
    for line in lines:
        for ((x1, y1), (x2, y2)) in itertools.pairwise(line):
            if x2 != x1:
                rocks.update([(x, y1) for x in (range(x1, x2+1) if x2 > x1 else range(x2, x1+1))])
            else:
                rocks.update([(x1, y) for y in (range(y1, y2+1) if y2 > y1 else range(y2, y1+1))])
    return rocks


def pt1(rocks):
    start = (500, 0)
    bottom = max([y for (_, y) in rocks])
    sand = set()
    obstacles = set(rocks)
    while True:
        result = drop(start, lambda p: p in obstacles, bottom)
        if result is not None:
            sand.add(result)
            obstacles.add(result)
        else:
            break

    # graph(rocks, sand)
    return len(sand)


def pt2(rocks):
    start = (500, 0)
    bottom = max([y for (_, y) in rocks]) + 2
    sand = set()
    obstacles = set(rocks)
    while (500, 0) not in sand:
        result = drop(start, lambda p: pt2_collision(p, obstacles, bottom), bottom)
        if result is not None:
            sand.add(result)
            obstacles.add(result)
        else:
            break

    # graph(rocks, sand)
    return len(sand)


def pt2_collision(pos, obstacles, bottom):
    (x, y) = pos
    return (pos in obstacles) or (y == bottom)


def drop(pos, collision, bottom):
    (x, y) = pos

    if y > bottom:
        return None

    if not collision((x, y+1)):
        return drop((x, y+1), collision, bottom)
    elif not collision((x-1, y+1)):
        return drop((x-1, y+1), collision, bottom)
    elif not collision((x+1, y+1)):
        return drop((x+1, y+1), collision, bottom)
    else:
        return x, y


def graph(rocks, sand):
    obstacles = rocks.union(sand)
    min_x = min([x for (x, _) in obstacles])
    min_y = min([y for (_, y) in obstacles])
    max_x = max([x for (x, _) in obstacles])
    max_y = max([y for (_, y) in obstacles])

    lines = []
    for y in range(min_y, max_y+1):
        line = []
        for x in range(min_x, max_x+1):
            if (x, y) in rocks:
                line.append('x')
            elif (x, y) in sand:
                line.append('o')
            else:
                line.append('.')
        lines.append(line)

    print('\n')
    print('\n'.join([''.join(line) for line in lines]))


if __name__ == "__main__":
    url = "https://adventofcode.com/2022/day/14/input"
    input_data = datautils.read_input_data(url)

    print("({},  {})".format(pt1(parse_input(input_data)), pt2(parse_input(input_data))))
