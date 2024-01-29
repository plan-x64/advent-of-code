from heapq import heappop, heappush


def get_input():
    nums = [[int(n) for n in line.strip()] for line in open('.cached_input/2023_17').readlines()]

    graph = {}
    for i, row in enumerate(nums):
        for k, num in enumerate(row):
            graph[i + k*1j] = num
    return graph, complex(len(nums)-1, len(nums[0])-1)


def traverse(graph, dest, min_step, max_step):
    prioq = [(0, 0, 0+0j, 1+0j), (0, 0, 0+0j, 0-1j)]
    visited = set()
    order = 0

    while prioq:
        cost, _, pos, direction = heappop(prioq)

        if pos == dest:
            return cost

        if (pos, direction) in visited:
            continue
        else:
            visited.add((pos, direction))

        for d in direction * 1j, direction * -1j:
            for step in range(min_step, max_step+1):
                if pos+d*step in graph:
                    c = sum(graph[pos+d*i] for i in range(1, step+1))
                    order = order + 1
                    heappush(prioq, (cost + c, order, (pos+d*step), d))


print(traverse(*get_input(), min_step=1, max_step=3))
print(traverse(*get_input(), min_step=4, max_step=10))
