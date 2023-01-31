import datautils
from operator import add, sub, floordiv, mul


def parse_input(data):
    nodes = dict()
    for line in data.splitlines():
        name, operation = line.split(':', 1)
        if operation.strip().isnumeric():
            nodes[name] = ('const', int(operation.strip()))
        else:
            arg1, op, arg2 = operation.split()
            nodes[name] = (op, (arg1, arg2))
    return nodes


def to_expr(node, nodes):
    operation, args = nodes[node]
    if operation == 'const':
        return args
    else:
        arg1, arg2 = args
        return operation, (to_expr(arg1, nodes), to_expr(arg2, nodes))


def _evaluate(expr):
    operations = {'+': add, '-': sub, '*': mul, '/': floordiv}
    operation, args = expr
    operands = tuple(map(lambda x: x if isinstance(x, int) else _evaluate(x), args))
    return operations[operation](*operands)


def part1(nodes):
    return _evaluate(to_expr('root', nodes))


def _find_path(expr, path):
    if isinstance(expr, int):
        return None  # leaf that is a const
    elif isinstance(expr, str):
        return path  # we found the unbound variable

    _, (left, right) = expr

    l_path = _find_path(left, path + ['L'])
    if l_path is not None:
        return l_path

    r_path = _find_path(right, path + ['R'])
    if r_path is not None:
        return r_path

    return None


def _solve(expr):
    path = _find_path(expr, [])
    reverse_left = {
        '+': lambda x, y: ('-', (x, y)),
        '-': lambda x, y: ('+', (x, y)),
        '*': lambda x, y: ('/', (x, y)),
        '/': lambda x, y: ('*', (x, y))
    }

    reverse_right = {
        '+': lambda x, y: ('-', (x, y)),
        '-': lambda x, y: ('-', (y, x)),
        '*': lambda x, y: ('/', (x, y)),
        '/': lambda x, y: ('/', (y, x))
    }

    _, (left, right) = expr
    total = _evaluate(left) if path[0] == 'R' else _evaluate(right)
    current_expr = left if path[0] == 'L' else right

    for direction in path[1:]:
        op, (left, right) = current_expr

        if direction == 'L':
            new_expr = reverse_left[op](total, right if isinstance(right, int) else _evaluate(right))
            total = _evaluate(new_expr)
            current_expr = left
        else:
            new_expr = reverse_right[op](total, left if isinstance(left, int) else _evaluate(left))
            total = _evaluate(new_expr)
            current_expr = right

    return total


def part2(nodes):
    nodes['humn'] = ('const', 'x')
    return _solve(to_expr('root', nodes))


if __name__ == "__main__":
    url = "https://adventofcode.com/2022/day/21/input"
    input_data = datautils.read_input_data(url)
    parsed = parse_input(input_data)
    print("({},  {})".format(part1(parsed), part2(parsed)))
