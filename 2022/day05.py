from collections import deque
import datautils


def _parse_input(data):
    (state, moves) = data.split('\n\n')
    return _parse_state(state), _parse_moves(moves)


def _parse_state(state):
    lines = state.splitlines()
    crate_count = len(lines[-1].split())

    # Pad missing values
    empty = [None] * crate_count
    parsed = []
    for chars in lines[:-1]:
        columns = chars[1::4]
        parsed.append([char if char != ' ' else None for char in columns] + empty[len(columns):])

    # Build stacks
    crates = [deque() for _ in range(0, crate_count)]
    for idx, value in enumerate(zip(*parsed)):
        crates[idx].extendleft(filter(lambda char: char is not None, value))

    return crates


def _parse_moves(moves):
    tokens = [move.split() for move in moves.splitlines()]
    return [tuple(map(int, token[1::2])) for token in tokens]


def top_items(state):
    nonempty = filter(lambda x: len(x) > 0, state)
    return ''.join(map(deque.pop, nonempty))


def operate_pt1(state, moves):
    for (number, source, destination) in moves:
        for _ in range(number):
            state[destination-1].append(state[source-1].pop())

    return state


def operate_pt2(state, moves):
    for (number, source, destination) in moves:
        popped = [state[source-1].pop() for _ in range(number)]
        state[destination-1].extend(reversed(popped))

    return state


if __name__ == "__main__":
    url = "https://adventofcode.com/2022/day/5/input"

    (cs, ops) = _parse_input(datautils.read_input_data(url))

    final_state_pt1 = operate_pt1([crate.copy() for crate in cs], ops)
    final_state_pt2 = operate_pt2([crate.copy() for crate in cs], ops)
    print("({},  {})".format(top_items(final_state_pt1), top_items(final_state_pt2)))
