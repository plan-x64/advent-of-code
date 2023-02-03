from collections import defaultdict, deque
import datautils


def parse_input(data):
    return [(x+10000, y+10000) for y, line in enumerate(data.splitlines()) for x, c in enumerate(line) if c == '#']


_initial_order = [
    ('N', ['N', 'NE', 'NW']),
    ('S', ['S', 'SE', 'SW']),
    ('W', ['W', 'NW', 'SW']),
    ('E', ['E', 'NE', 'SE'])
]


_moves = {
    'NE': lambda x, y: (x+1, y-1),
    'N': lambda x, y: (x, y-1),
    'NW': lambda x, y: (x-1, y-1),
    'S': lambda x, y: (x, y+1),
    'SE': lambda x, y: (x+1, y+1),
    'SW': lambda x, y: (x-1, y+1),
    'W': lambda x, y: (x-1, y),
    'E': lambda x, y: (x+1, y)
}


def determine_move(pos, positions, order):
    if all([f(*pos) not in positions for f in _moves.values()]):
        return None

    for move_direction, directions in order:
        if all([_moves[direction](*pos) not in positions for direction in directions]):
            return _moves[move_direction](*pos)


def min_grid(positions):
    xs = [x for x, _ in positions]
    ys = [y for _, y in positions]
    x_min, x_max = min(xs), max(xs)
    y_min, y_max = min(ys), max(ys)
    grid = [['.'] * (x_max - x_min + 1) for _ in range(y_max - y_min + 1)]

    for x, y in positions:
        x_rel, y_rel = (x - x_min), (y - y_min)
        grid[y_rel][x_rel] = '#'
    return grid


def step(positions, order):
    # first half of round
    all_updated = set()
    no_move = set()
    proposed = defaultdict(list)
    for pos in positions:
        determined = determine_move(pos, positions, order)
        if determined is not None:
            proposed[determined].append(pos)
        else:
            no_move.add(pos)

    # second half of round
    for pos_new, positions_old in proposed.items():
        if len(positions_old) == 1:
            all_updated.add(pos_new)
        else:
            all_updated.update(positions_old)
    all_updated.update(no_move)

    return all_updated


def part1(elves):
    positions = set(elves)
    order = deque(_initial_order)

    for _ in range(10):
        positions = step(positions, order)
        order.rotate(-1)

    return len([c for line in min_grid(positions) for c in line if c == '.'])


def part2(elves):
    positions = set(elves)
    order = deque(_initial_order)

    for i in range(1000):
        updated_positions = step(positions, order)

        if updated_positions == positions:
            return i+1
        else:
            positions = updated_positions

        order.rotate(-1)


if __name__ == "__main__":
    url = "https://adventofcode.com/2022/day/23/input"
    input_data = datautils.read_input_data(url)
    parsed = parse_input(input_data)
    print("({},  {})".format(part1(parsed), part2(parsed)))
