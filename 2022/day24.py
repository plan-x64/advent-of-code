import datautils


def parse_input(data):
    blizzards = set()
    walls = set()
    for y, line in enumerate(data.splitlines()):
        for x, char in enumerate(line):
            if char == '#':
                walls.add((x-1, y-1))
            elif char == '^':
                blizzards.add((x-1, y-1, 0, -1))
            elif char == 'v':
                blizzards.add((x-1, y-1, 0, 1))
            elif char == '>':
                blizzards.add((x-1, y-1, 1, 0))
            elif char == '<':
                blizzards.add((x-1, y-1, -1, 0))

    max_x = max(x for (x, _) in walls)
    max_y = max(y for (_, y) in walls)

    # Add walls above and below the start/end, respectively
    walls.add((0, -2))
    walls.add((max_x-1, max_y+1))

    start, end = (0, -1), (max_x-1, max_y)
    return start, end, walls, blizzards, max_x, max_y


def shortest(start, goals, ws, bs, max_x, max_y):
    positions = {start}
    time = 1

    while goals:
        time += 1
        blizzards = {((bx + time * dx) % max_x, (by + time * dy) % max_y) for bx, by, dx, dy in bs}
        possible = {(x + dx, y + dy) for dx, dy in {(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)} for x, y in positions}
        positions = possible - blizzards - ws

        if goals[0] in positions:
            positions = {goals.pop(0)}

    return time


def part1(start, end, ws, bs, max_x, max_y):
    return shortest(start, [end], ws, bs, max_x, max_y)


def part2(start, end, ws, bs, max_x, max_y):
    return shortest(start, [end, start, end], ws, bs, max_x, max_y)


if __name__ == "__main__":
    url = "https://adventofcode.com/2022/day/24/input"
    input_data = datautils.read_input_data(url)
    parsed = parse_input(input_data)
    print("({},  {})".format(part1(*parsed), part2(*parsed)))
