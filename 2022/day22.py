import datautils
import re


def parse_input(data):
    lines = data.splitlines()

    start_pos = complex(lines[0].index('.'), 0)
    board = {(x+y*1j): c for y, line in enumerate(lines[:-2]) for x, c in enumerate(line) if c in '.#'}
    instructions = re.findall(r'\d+|[LR]', lines[-1])
    return start_pos, board, instructions


def wrap_2d(position, direction, board):
    wrap_pos = position

    match int(direction.real), int(direction.imag):
        case (1, 0): wrap_pos = complex(0, position.imag)
        case (-1, 0): wrap_pos = complex(205, position.imag)
        case (0, 1): wrap_pos = complex(position.real, 0)
        case (0, -1): wrap_pos = complex(position.real, 205)

    while wrap_pos not in board:
        wrap_pos += direction

    return wrap_pos, direction


def wrap_3d(pos, direction, _):
    match (pos.real // 50, pos.imag // 50), (int(direction.real), int(direction.imag)):
        case (1, 0), (-1, 0): return complex(0, 149 - pos.imag), complex(1, 0)
        case (1, 0), (0, -1): return complex(0, 150 + pos.real - 50), complex(1, 0)
        case (2, 0), (1, 0): return complex(99, 149 - pos.imag), complex(-1, 0)
        case (2, 0), (0, -1): return complex(pos.real - 100, 199), complex(0, -1)
        case (2, 0), (0, 1): return complex(99, 50 + pos.real - 100), complex(-1, 0)
        case (1, 1), (-1, 0): return complex(pos.imag - 50, 100), complex(0, 1)
        case (1, 1), (1, 0): return complex(pos.imag - 50 + 100, 49), complex(0, -1)
        case (0, 2), (0, -1): return complex(50, 50 + pos.real), complex(1, 0)
        case (0, 2), (-1, 0): return complex(50, 149 - pos.imag), complex(1, 0)
        case (1, 2), (1, 0): return complex(149, 149 - pos.imag), complex(-1, 0)
        case (1, 2), (0, 1): return complex(49, 150 + pos.real - 50), complex(-1, 0)
        case (0, 3), (-1, 0): return complex(pos.imag - 150 + 50, 0), complex(0, 1)
        case(0, 3), (1, 0): return complex(pos.imag - 150 + 50, 149), complex(0, -1)
        case(0, 3), (0, 1): return complex(50 + pos.real, 0), complex(0, 1)


def traverse(start, board, instructions, wrap_func):
    pos = start
    direction = complex(1, 0)

    travelled = [(pos, direction)]
    for instruction in instructions:
        recent = []
        if instruction == 'L':
            direction *= -1j
            recent.append((pos, direction))
        elif instruction == 'R':
            direction *= 1j
            recent.append((pos, direction))
        else:
            for _ in range(int(instruction)):
                next_pos = pos + direction
                next_direction = direction
                if next_pos not in board:
                    next_pos, next_direction = wrap_func(pos, direction, board)

                if board[next_pos] == '#':
                    break
                else:
                    pos = next_pos
                    direction = next_direction
                    recent.append((pos, direction))
        travelled.extend(recent)

    return pos, direction, travelled


def password(pos, direction):
    x, y = int(pos.real), int(pos.imag)
    return (1000 * (y + 1)) + (4 * (x + 1)) + int([1 + 0j, 0 + 1j, -1 + 0j, 0 - 1j].index(direction))


def part1(start, board, instructions):
    end, direction, _ = traverse(start, board, instructions, wrap_2d)
    return password(end, direction)


def part2(start, board, instructions):
    end, direction, _ = traverse(start, board, instructions, wrap_3d)
    return password(end, direction)


if __name__ == "__main__":
    url = "https://adventofcode.com/2022/day/22/input"
    input_data = datautils.read_input_data(url)
    parsed = parse_input(input_data)
    print("({},  {})".format(part1(*parsed), part2(*parsed)))
