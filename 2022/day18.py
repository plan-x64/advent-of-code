import datautils


def _surrounding(coord):
    (x, y, z) = coord
    return {(x - 1, y, z), (x + 1, y, z), (x, y - 1, z), (x, y + 1, z), (x, y, z - 1), (x, y, z + 1)}


def _flood_fill(coords):
    max_bound = max([i for coord in coords for i in [*coord]])+1  # visit 1 cube past the cube furthest from origin
    stack = [(-1, -1, -1)]  # start at a cube guaranteed not to be in the input
    visited = set()
    while stack:
        coord = stack.pop()
        stack.extend([side for side in (_surrounding(coord) - coords - visited) if _in_bounds(side, max_bound)])
        visited.add(coord)
    return visited


def _in_bounds(coord, maximum):
    return all(-1 <= i <= maximum for i in coord)


def part1(coords):
    return sum((s not in coords) for coord in coords for s in _surrounding(coord))


def part2(coords):
    outside = _flood_fill(coords)
    return sum(s in outside for coord in coords for s in _surrounding(coord))


def parse_input(data):
    return set([tuple(map(int, (line.split(',')))) for line in data.splitlines()])


if __name__ == "__main__":
    url = "https://adventofcode.com/2022/day/18/input"
    input_data = datautils.read_input_data(url)
    parsed = parse_input(input_data)

    print("({},  {})".format(part1(parsed), part2(parsed)))
