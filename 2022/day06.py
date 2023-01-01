import collections
import datautils
import itertools


def _sliding_window(iterable, n):
    it = iter(iterable)
    window = collections.deque(itertools.islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)


def find_first_marker(stream, matches):
    for idx, line in enumerate(_sliding_window(stream, matches)):
        if len(set(line)) == matches:
            return idx+matches


if __name__ == "__main__":
    url = "https://adventofcode.com/2022/day/6/input"
    data = datautils.read_input_data(url)

    print("({},  {})".format(find_first_marker(data, 4), find_first_marker(data, 14)))
