def get_input():
    return [[c for c in line.strip()] for line in open('.cached_input/2023_14').readlines()]


def tilt_north(platform):
    move_count = 0
    for y in range(1, len(platform)):
        for x in range(len(platform[0])):
            if platform[y][x] == 'O' and platform[y - 1][x] == '.':
                platform[y][x] = '.'
                platform[y - 1][x] = 'O'
                move_count += 1
    return platform, move_count


def rotate(platform):
    rotated = [[None for _ in range(len(platform))] for _ in range(len(platform[0]))]
    for i in range(len(platform)):
        for j in range(len(platform[i])):
            rotated[j][len(platform) - 1 - i] = platform[i][j]
    return rotated


def full_tilt(platform):
    for i in range(len(platform)):
        platform, moves = tilt_north(platform)
        if moves == 0:
            break
    return platform


def cycle(platform):
    platform = full_tilt(platform)  # north
    platform = rotate(platform)
    platform = full_tilt(platform)  # west
    platform = rotate(platform)
    platform = full_tilt(platform)  # south
    platform = rotate(platform)
    platform = full_tilt(platform)  # east
    return rotate(platform)


def load(platform):
    total = 0
    for i, elems in enumerate(platform):
        total += sum(e == 'O' for e in elems) * (len(platform) - i)
    return total


def part1(platform):
    platform = full_tilt(platform)
    return load(platform)


def part2(platform):
    cache = {}
    step = 0
    goal = 1000000000
    while step < goal:
        platform = cycle(platform)
        step += 1

        key = tuple(tuple(p) for p in platform)
        if key in cache:
            start, period = cache[key], step - cache[key]
            increment = period * ((goal-step) // period)
            step += increment
        else:
            cache[key] = step

    return load(platform)


print(part1(get_input()))
print(part2(get_input()))
