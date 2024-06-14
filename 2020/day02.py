import re

def get_input():
    passwords = open('.cached_input/2020_02').readlines()
    return [re.findall(r'(\d+)-(\d+) ([a-z]): ([a-z]+)', password)[0] for password in passwords]


def part1(passwords):
    valid = 0

    for minimum, maximum, letter, password in passwords:
        actual = password.count(letter)
        if int(minimum) <= actual <= int(maximum):
            valid += 1

    return valid


def part2(passwords):
    valid = 0

    for i, j, letter, password in passwords:
        if (password[int(i)-1] == letter) ^ (password[(int(j))-1] == letter):
            valid += 1

    return valid


print(part1(get_input()))
print(part2(get_input()))