import datautils


def _calculate_value(char):
    if char.isupper():
        return ord(char) - 38
    else:
        return ord(char) - 96


def find_common(iterable):
    duplicates = set.intersection(*[set(val) for val in iterable])
    return sum([_calculate_value(char) for char in duplicates])


if __name__ == "__main__":
    url = "https://adventofcode.com/2022/day/3/input"
    lines = [[*line] for line in datautils.read_input_data(url).splitlines()]

    p1 = sum([find_common([chars[0:len(chars)//2], chars[len(chars)//2:]]) for chars in lines])
    p2 = sum([find_common(lines[idx:(idx + 3)]) for idx in range(0, len(lines), 3)])
    print("({},  {})".format(p1, p2))
