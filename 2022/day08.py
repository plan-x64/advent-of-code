import datautils
from math import prod


def parse_input(data):
    return [[int(char) for char in line] for line in data.splitlines()]


def count_visible(grid):
    transpose = list(zip(*grid))
    peaks = set()

    for y, row in enumerate(grid):
        peaks.update([(x, y) for x in visible(row)])
        peaks.update([(len(row)-1-x, y) for x in visible(list(reversed(row)))])

    for x, column in enumerate(transpose):
        peaks.update([(x, y) for y in visible(column)])
        peaks.update([(x, len(column) - 1 - y) for y in visible(list(reversed(column)))])

    return len(peaks)


def max_score(grid):
    transpose = list(zip(*grid))
    maximum = 0
    for i in range(1, len(grid)-1):
        for j in range(1, len(grid)-1):
            left = sight_line(grid[i][j], grid[i][(j-1)::-1])
            right = sight_line(grid[i][j], grid[i][(j+1):])
            up = sight_line(transpose[j][i], transpose[j][(i-1)::-1])
            down = sight_line(transpose[j][i], transpose[j][(i+1):])

            maximum = max(maximum, prod([left, right, up, down]))
    return maximum


def sight_line(height, line):

    count = 0
    for val in line:
        count += 1
        if val >= height:
            break

    return count


def visible(trees):
    maxes = [0]

    for i in range(len(trees)):
        if trees[i] > trees[maxes[-1]]:
            maxes.append(i)

    return maxes


if __name__ == "__main__":
    url = "https://adventofcode.com/2022/day/8/input"
    parsed = parse_input(datautils.read_input_data(url))
    print("({},  {})".format(count_visible(parsed), max_score(parsed)))
