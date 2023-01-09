import datautils


def execute(instructions):
    state = [1]  # initialize 0th cycle (or "state before cycle 1")

    for instruction in instructions:
        if instruction == 'noop':
            state.append(state[-1])
        else:
            inc = int(instruction.split()[1])
            state.append(state[-1])
            state.append(state[-1] + inc)

    return state


def part1(state):
    return sum([val * (20 + 40 * idx) for idx, val in enumerate(state[19:220:40])])


def part2(state):
    return [draw_row(state, 40*row_idx) for row_idx in range(6)]


def draw_part2(screen):
    return '\n'.join([''.join(row) for row in screen])


def draw_row(state, cycle_offset):
    draw_pos = 0
    row = []
    for char_idx in range(40):
        sprite_mid = state[cycle_offset + char_idx]

        if draw_pos in [sprite_mid - 1, sprite_mid, sprite_mid + 1]:
            row.append('#')
        else:
            row.append('.')

        draw_pos += 1
    return row


if __name__ == "__main__":
    url = "https://adventofcode.com/2022/day/10/input"
    input_data = datautils.read_input_data(url)
    output = execute(input_data.splitlines())

    print('Part1: {}'.format(part1(output)))
    print('Part2:\n{}'.format(draw_part2(part2(output))))
