import datautils


def parse_input(data):
    return [int(line) for line in data.splitlines()]


def mix(encrypted, times=1):
    initial_to_current = list(range(len(encrypted)))

    for _ in range(times):
        for idx, val in enumerate(encrypted):
            if val == 0:
                continue  # there is no move so nothing to do

            idx_old = initial_to_current.index(idx)
            idx_new = (idx_old + val) % (len(encrypted) - 1)
            if idx_new == 0:
                idx_new = len(encrypted) - 1

            initial_to_current.pop(idx_old)
            initial_to_current.insert(idx_new, idx)

    decrypted = [encrypted[i] for i in initial_to_current]
    zero_idx = decrypted.index(0)
    return sum([decrypted[(zero_idx + (i * 1000)) % len(encrypted)] for i in range(1, 4)])


if __name__ == "__main__":
    url = "https://adventofcode.com/2022/day/20/input"
    input_data = datautils.read_input_data(url)
    parsed = parse_input(input_data)

    print("({},  {})".format(mix(parsed), mix([val * 811589153 for val in parsed], 10)))
