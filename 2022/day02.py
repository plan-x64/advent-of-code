import datautils
from enum import IntEnum


class Hand(IntEnum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class Outcome(IntEnum):
    LOSS = 0
    DRAW = 3
    WIN = 6


opponent_symbols = {
    'A': Hand.ROCK,
    'B': Hand.PAPER,
    'C': Hand.SCISSORS,
}

outcome_symbols_part1 = {
    'X': Hand.ROCK,
    'Y': Hand.PAPER,
    'Z': Hand.SCISSORS
}


outcome_symbols_part2 = {
    'X': Outcome.LOSS,
    'Y': Outcome.DRAW,
    'Z': Outcome.WIN
}


def part1_score(opponent: Hand, mine: Hand) -> int:
    difference = abs(opponent - mine)

    if difference == 0:
        return Outcome.DRAW+mine
    elif difference == 1 and opponent > mine:
        return Outcome.LOSS+mine
    elif difference == 1 and mine > opponent:
        return Outcome.WIN+mine
    elif difference > 1 and opponent > mine:
        return Outcome.WIN+mine
    else:
        return Outcome.LOSS+mine


def part2_score(opponent: Hand, outcome: Outcome) -> int:
    if outcome == Outcome.LOSS:
        return outcome + Hand(((opponent - 2) % 3) + 1)
    elif outcome == Outcome.DRAW:
        return outcome + opponent
    else:
        return outcome + Hand((opponent % 3) + 1)


def _parse_line(line, outcome_symbols):
    (opponent_symbol, my_symbol) = tuple(line.split())
    return opponent_symbols[opponent_symbol], outcome_symbols[my_symbol]


if __name__ == "__main__":
    url = "https://adventofcode.com/2022/day/2/input"
    input_data = datautils.read_input_data(url)
    expected_total_part1 = sum([part1_score(*_parse_line(x, outcome_symbols_part1)) for x in input_data.splitlines()])
    expected_total_part2 = sum([part2_score(*_parse_line(x, outcome_symbols_part2)) for x in input_data.splitlines()])

    print("({},  {})".format(expected_total_part1, expected_total_part2))
