def get_input():
    return open('.cached_input/2023_01').read().splitlines()


def first_num(line, replacements):
    for i in range(len(line)):
        for num, item in replacements:
            if line[i:].startswith(item):
                return num


def calibrate(line, replacements):
    return (first_num(line, replacements) * 10) + first_num(line[::-1], [(k, v[::-1]) for (k, v) in replacements])


def part1(data):
    replacements = list(enumerate('0123456789'))
    return sum([calibrate(line, replacements) for line in data])


def part2(data):
    replacements = (list(enumerate('0123456789')) +
                    list(enumerate(['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'])))
    return sum([calibrate(line, replacements) for line in data])


print(part1(get_input()))
print(part2(get_input()))
