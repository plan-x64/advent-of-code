def get_input():
    return list(map(int, open('.cached_input/2019_02').read().split(',')))


def calculate(memory, noun, verb):
    memory[1], memory[2] = noun, verb
    ip = 0
    while memory[ip] != 99:
        opcode, op1, op2, result = memory[ip:ip + 4]
        if opcode == 1:
            memory[result] = memory[op1] + memory[op2]
        elif opcode == 2:
            memory[result] = memory[op1] * memory[op2]
        ip += 4
    return memory[0]


def part1(memory):
    return calculate(memory, 12, 2)


def part2(memory):
    goal = 19690720

    import itertools
    for noun, verb in itertools.permutations(range(100), 2):
        current = memory.copy()
        result = calculate(current, noun, verb)
        if result == goal:
            return (100 * noun) + verb


print(part1(get_input()))
print(part2(get_input()))
