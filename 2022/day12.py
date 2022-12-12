# Day 12: Hill Climbing Algorithm
# https://adventofcode.com/2022/day/12

from heapq import heappop, heappush


def shortest_path(grid, start, ends, direction):
    # This function returns the shortest path in
    # the grid using a Dijkstra-like algorithm.
    next_node = []
    visited = set()
    heappush(next_node, (0, start))
    # Loop until we hit an end.
    while True:
        steps, (x, y) = heappop(next_node)
        if (x, y) in visited:
            continue
        if (x, y) in ends:
            return steps
        visited.add((x, y))
        height = ord(grid[y][x])
        for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
            if 0 <= ny < len(grid):
                if 0 <= nx < len(grid[ny]):
                    if (ord(grid[ny][nx]) - height) * direction <= 1:
                        heappush(next_node, (steps + 1, (nx, ny)))


# Parse the puzzle input file.
with open("advent_of_code\\2022\\day12.txt") as puzzle_input:
    height_map = [list(row) for row in puzzle_input.read().splitlines()]
    # Set the start and end positions.
    # Part 1, S is the start and E is the end.
    # Part 2, E is the start and any position that contains an "a" is the end.
    starts = [None, None]
    ends = [set(), set()]
    for y, line in enumerate(height_map):
        for x, height in enumerate(line):
            if height == "S":
                height_map[y][x] = "a"
                starts[0] = (x, y)
            if height == "E":
                height_map[y][x] = "z"
                starts[1] = (x, y)
                ends[0].add((x, y))
            if height_map[y][x] == "a":
                ends[1].add((x, y))

# Part one.
print(shortest_path(height_map, starts[0], ends[0], 1))

# Part two.
print(shortest_path(height_map, starts[1], ends[1], -1))
