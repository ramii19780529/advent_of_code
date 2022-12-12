# Day 12: Hill Climbing Algorithm
# https://adventofcode.com/2022/day/12

from heapq import heappop, heappush
import copy


def diff(a, b, part):
    # Get the difference between two numbers.
    if part == 1:
        return a - b
    if part == 2:
        return b - a


def shortest_path(grid, part):
    # This function returns the shortest path in
    # the grid using a Dijkstra-like algorithm.

    # Set the start and destination positions.
    # Part 1, S is the start and E is the destination.
    # Part 2, E is the start and any position that contains an "a" is the destination.
    next_node = []
    destination = set()
    visited = set()
    for y, line in enumerate(grid):
        for x, height in enumerate(line):
            if height == "S":
                grid[y][x] = "a"
                if part == 1:
                    heappush(next_node, (0, (x, y)))
                if part == 2:
                    destination.add((x, y))
            if height == "E":
                grid[y][x] = "z"
                if part == 1:
                    destination.add((x, y))
                if part == 2:
                    heappush(next_node, (0, (x, y)))
            if part == 2 and height == "a":
                destination.add((x, y))

    # Loop until we hit a destination.
    while True:
        steps, (x, y) = heappop(next_node)
        if (x, y) in visited:
            continue
        if (x, y) in destination:
            return steps
        visited.add((x, y))
        height = ord(grid[y][x])
        if x > 0 and diff(ord(grid[y][x - 1]), height, part) <= 1:
            heappush(next_node, (steps + 1, (x - 1, y)))
        if x + 1 < len(grid[y]) and diff(ord(grid[y][x + 1]), height, part) <= 1:
            heappush(next_node, (steps + 1, (x + 1, y)))
        if y > 0 and diff(ord(grid[y - 1][x]), height, part) <= 1:
            heappush(next_node, (steps + 1, (x, y - 1)))
        if y + 1 < len(grid) and diff(ord(grid[y + 1][x]), height, part) <= 1:
            heappush(next_node, (steps + 1, (x, y + 1)))


# Parse the puzzle input file.
with open("advent_of_code\\2022\\day12.txt") as puzzle_input:
    height_map = [list(row) for row in puzzle_input.read().splitlines()]

# Part one.
print(shortest_path(copy.deepcopy(height_map), 1))

# Part two.
print(shortest_path(copy.deepcopy(height_map), 2))
