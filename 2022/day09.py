import datautils
import itertools


def parse_input(data):
    for line in data.splitlines():
        (direction, amount) = line.split()
        for move in itertools.repeat((direction, 1), int(amount)):
            yield move


def simulate(iterable, knots):
    rope = [(0, 0)] + [(0, 0)] * knots

    visited = set()
    visited.add(rope[-1])

    for operation in iterable:
        (direction, amount) = operation
        head = rope[0]
        if direction == 'U':
            rope[0] = (head[0], head[1]+1)
        elif direction == 'D':
            rope[0] = (head[0], head[1]-1)
        elif direction == 'L':
            rope[0] = (head[0]-1, head[1])
        elif direction == 'R':
            rope[0] = (head[0]+1, head[1])

        rope = list(itertools.accumulate(rope[1:], move_knot, initial=rope[0]))
        visited.add(rope[-1])
    return len(visited)


def move_knot(head, tail):
    hx, hy = head
    tx, ty = tail

    x_dist = abs(hx - tx)
    y_dist = abs(hy - ty)
    pseudo_distance = x_dist**2 + y_dist**2  # (euclidean distance)^2

    while (y_dist > 1) or (x_dist > 1):
        if pseudo_distance > 4:  # (euclidean distance)^2 > 4 means that we need to move diagonal
            tx += 1 if hx > tx else -1
            ty += 1 if hy > ty else -1
        elif (x_dist > 1) and (y_dist <= 1):
            tx += 1 if hx > tx else -1
        elif (x_dist <= 1) and (y_dist > 1):
            ty += 1 if hy > ty else -1
        x_dist = abs(hx - tx)
        y_dist = abs(hy - ty)

    return tx, ty


if __name__ == "__main__":
    url = "https://adventofcode.com/2022/day/9/input"
    input_data = datautils.read_input_data(url)

    print("({},  {})".format(simulate(parse_input(input_data), 1), simulate(parse_input(input_data), 9)))
