from collections import defaultdict
import datautils
import heapq


def parse_input(data):
    grid = []
    start = None
    end = None
    lowest = []
    for y, line in enumerate(data.splitlines()):
        row = []
        for x, char in enumerate(line):
            if char == 'S':
                row.append(ord('a'))
                start = (x, y)
            elif char == 'E':
                row.append(ord('z'))
                end = (x, y)
            elif char == 'a':
                lowest.append((x, y))
                row.append(ord(char))
            else:
                row.append(ord(char))
        grid.append(row)
    return grid, start, end, lowest


def neighbors(grid, pos):
    x, y = pos
    moves = []
    if x - 1 >= 0:
        moves.append((x - 1, y))
    if x + 1 < len(grid[y]):
        moves.append((x + 1, y))
    if y - 1 >= 0:
        moves.append((x, y - 1))
    if y + 1 < len(grid):
        moves.append((x, y + 1))
    return list(filter(lambda m: elevation(grid, m)-elevation(grid, pos) <= 1,  moves))


def elevation(grid, pos):
    (x, y) = pos
    return grid[y][x]


def find_path(grid, start):
    ptq = [(0, start)]
    heapq.heapify(ptq)

    prev_min_path = {}
    costs = defaultdict(lambda: 999)
    costs[start] = 0

    visited = set()

    while ptq:
        (cost, pos) = heapq.heappop(ptq)

        if pos in visited:
            continue  # already computed this value

        for (x, y) in neighbors(grid, pos):
            if (x, y) in visited:
                continue

            new_cost = cost + 1
            if new_cost < costs[(x, y)]:
                costs[(x, y)] = new_cost
                prev_min_path[(x, y)] = pos

            heapq.heappush(ptq, (costs[(x, y)], (x, y)))
        visited.add(pos)

    return costs


def pt1(data):
    grid, start, end, _ = parse_input(data)
    costs = find_path(grid, start)
    return costs[end]


def pt2(data):
    grid, start, end, lowest = parse_input(data)

    """
    Due to the rules with going up and down, the graph is directed so to find all shortest paths
    from the end we need to invert the heights and then traverse starting at the end node. The
    benefit of doing this is that we only need to perform a singular calculation of the graph rather
    than O(num of 'a''s) searches
    """
    inverted_grid = [[ord('z') - val for val in row] for row in grid]

    costs = find_path(inverted_grid, end)
    return min(costs[low] for low in lowest)


if __name__ == "__main__":
    url = "https://adventofcode.com/2022/day/12/input"
    input_data = datautils.read_input_data(url)

    print("({},  {})".format(pt1(input_data), pt2(input_data)))
