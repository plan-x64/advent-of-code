def get_input():
    return [*open('.cached_input/2017_09').readline()]


def filtered_stream(stream):
    filtered = []
    idx = 0
    while idx < len(stream):
        c = stream[idx]
        if c == '!':
            idx += 1
        else:
            filtered.append(c)
        idx += 1
    return filtered


def part1(stream):
    idx = 0
    depth = 0
    score = 0
    filtered = filtered_stream(stream)

    while idx < len(filtered):
        c = filtered[idx]
        if c == '<':
            idx = filtered.index('>', idx+1)
        elif c == '{':
            depth += 1
        elif c == '}':
            score += depth
            depth -= 1
        idx += 1
    return score


def part2(stream):
    idx = 0
    score = 0
    filtered = filtered_stream(stream)

    while idx < len(filtered):
        c = filtered[idx]
        if c == '<':
            end_idx = filtered.index('>', idx + 1)
            score += end_idx - idx - 1
            idx = end_idx
        idx += 1
    return score


print(part1(get_input()))
print(part2(get_input()))
