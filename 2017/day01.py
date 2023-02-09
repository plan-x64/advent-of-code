def get_input():
    return [int(d) for d in open('.cached_input/2017_01').read()]


def part1(captcha):
    total = 0
    for i in range(len(captcha)):
        if captcha[i] == captcha[(i+1) % len(captcha)]:
            total += captcha[i]
    return total


def part2(captcha):
    total = 0
    for i in range(len(captcha)):
        if captcha[i] == captcha[(i+len(captcha)//2) % len(captcha)]:
            total += captcha[i]
    return total


print(part1(get_input()))
print(part2(get_input()))
