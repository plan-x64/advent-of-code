def get_input():
    data = open('.cached_input/2020_04').read().split('\n\n')
    passports = [datum.replace('\n', ' ').split(' ') for datum in data]
    parsed = [list(map(lambda s: s.split(':'), passport)) for passport in passports]
    return [{k: v for k, v in passport} for passport in parsed]


valid_attrs = {
    'byr': lambda x: 1920 <= int(x) <= 2002,
    'iyr': lambda x: 2010 <= int(x) <= 2020,
    'eyr': lambda x: 2020 <= int(x) <= 2030,
    'hgt',
    'hcl',
    'ecl',
    'pid'
}


def part1(passports):
    return sum(valid_attrs.issubset(set(passport.keys())) for passport in passports)


def part2(passports):
    possibly_valid = [passport for passport in passports if valid_attrs.issubset(set(passport.keys()))]


print(part1(get_input()))
