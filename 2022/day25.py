import datautils


def parse_input(data):
    return [snafu_to_decimal(line) for line in data.splitlines()]


def snafu_to_decimal(snafu):
    num = 0
    for i, c in enumerate(reversed(snafu)):
        if c.isdigit():
            num += int(c) * (5 ** i)
        elif c == '-':
            num += -1 * (5 ** i)
        elif c == '=':
            num += -2 * (5 ** i)
    return num


def decimal_to_snafu(num):
    quinary = []
    current = num
    while current != 0:
        quinary.append(current % 5)
        current = current // 5

    snafu = quinary.copy() + [0]  # append 0 for carry operations
    for i in range(len(quinary)):
        if snafu[i] == 3:
            snafu[i] = '='
            snafu[i+1] += 1
        elif snafu[i] == 4:
            snafu[i] = '-'
            snafu[i+1] += 1
        elif snafu[i] == 5:
            snafu[i] = 0
            snafu[i+1] += 1

    return ''.join(reversed([str(c) for c in snafu])).lstrip('0')


if __name__ == "__main__":
    url = "https://adventofcode.com/2022/day/25/input"
    input_data = datautils.read_input_data(url)
    parsed = parse_input(input_data)
    print("({},  {})".format(decimal_to_snafu(sum(parsed)), None))
