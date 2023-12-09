import math

def get_input(combinator):
    lines = open('.cached_input/2023_06').readlines()
    return list(zip(*[combinator(line) for line in lines]))

def split_races(line):
    return list(map(int, line.split(':')[1].split()))

def single_race(line):
    return [int(''.join(line.split(':')[1].split(' ')))]

def count_ways(records):
    return [list(filter(lambda n: n > dist, [hold*(time-hold) for hold in range(time)])) for (time, dist) in records]

print(math.prod(map(len, count_ways(get_input(split_races)))))
print(math.prod(map(len, count_ways(get_input(single_race)))))
