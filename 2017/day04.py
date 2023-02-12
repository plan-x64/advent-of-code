def get_input():
    return open('.cached_input/2017_04').read().splitlines()


def part1(pwds):
    return sum([1 for pwd in pwds if len(pwd.split()) == len(set(pwd.split()))])


def part2(pwds):
    count = 0
    for pwd in pwds:
        sorted_set = set([''.join(sorted(s)) for s in pwd.split()])
        if len(pwd.split()) == len(sorted_set):
            count += 1
    return count


print(part1(get_input()))
print(part2(get_input()))
