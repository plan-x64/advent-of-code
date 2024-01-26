def get_input():
    puzzles = open('.cached_input/2023_13').read().strip().split('\n\n')
    return [p.split('\n') for p in puzzles]

def score(puzzle, target):
    for i in range(1, len(puzzle)):
        delta = sum(c1 != c2 for r1, r2 in zip(puzzle[i - 1::-1], puzzle[i::]) for c1, c2 in zip(r1, r2))
        if delta == target:
            return i

    return None

def calculate(puzzles, target):
    horizontal = []
    vertical = []

    for p in puzzles:
        y_score = score(p, target)
        if y_score is not None:
            horizontal.append(y_score)
        else:
            vertical.append(score(list(zip(*p)), target))

    return (100 * sum(horizontal)) + sum(vertical)

print(calculate(get_input(), 0))
print(calculate(get_input(), 1))
