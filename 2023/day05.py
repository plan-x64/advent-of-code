def get_input():
    sections = open('.cached_input/2023_05').read().split('\n\n')
    starting = [int(num) for num in sections[0][7:].split(' ')]

    transforms = []
    for section in sections[1:]:
        transform = [tuple(map(int, line.split(' '))) for line in section.split('\n')[1:]]
        transforms.append(transform)

    return starting, transforms


def convert(transform, i):
    for (dst, src, length) in transform:
        if (src <= i) and (src+length > i):
            return dst + (i-src)
    return i


def part1(starting, transforms):
    transformed = []
    for seed in starting:
        current = seed
        for transform in transforms:
            current = convert(transform, current)
        transformed.append(current)

    return min(transformed)


def part2(starting, transforms):
    starts = [i for (start, length) in zip(starting[0::2], starting[1::2]) for i in range(start, start + length)]
    transformed = []
    for seed in starts:
        current = seed
        for transform in transforms:
            current = convert(transform, current)
        transformed.append(current)

    return min(transformed)


print(part1(*get_input()))
print(part2(*get_input()))