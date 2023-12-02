from functools import reduce


def get_input():
    draws = []
    for line in open('.cached_input/2023_02').readlines():
        (_, draw) = line.split(':')
        draws.append([parse_cubes(cubes) for cubes in draw.strip().split(';')])
    return draws


def parse_cubes(cubes):
    parsed_cubes = []
    for cube in cubes.strip().split(','):
        (num, color) = cube.strip().split(' ')
        parsed_cubes.append((int(num), color))
    return parsed_cubes


def part1(games):
    maxs = {'red': 12, 'green': 13, 'blue': 14}

    total = 0
    for i, game in enumerate(games):
        if not any([num > maxs[color] for draw in game for (num, color) in draw]):
            total += i + 1
    return total


def part2(games):
    powers = []
    for i, game in enumerate(games):
        maxs = {'red': 0, 'green': 0, 'blue': 0}
        cubes = [(color, num) for draw in game for (num, color) in draw]
        for (color, num) in cubes:
            if maxs[color] < num:
                maxs[color] = num

        powers.append(reduce(lambda x, y: x*y, maxs.values()))
    return sum(powers)


print(part1(get_input()))
print(part2(get_input()))
