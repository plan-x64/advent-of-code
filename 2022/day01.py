import datautils


def sum_generator(data):
    current_sum = 0
    for line in data.split('\n'):
        if line == '':
            total = current_sum
            current_sum = 0
            yield total
        else:
            current_sum = current_sum + int(line)


if __name__ == "__main__":
    url = "https://adventofcode.com/2022/day/1/input"
    input_data = datautils.read_input_data(url)

    sorted_sums = sorted([x for x in sum_generator(input_data)])

    print("({},  {})".format(sorted_sums[-1], sum(sorted_sums[-3:])))
