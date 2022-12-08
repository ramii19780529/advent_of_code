# Day 8: Treetop Tree House
# https://adventofcode.com/2022/day/8

from math import prod

# Parse the puzzle input file.
with open("advent_of_code\\2022\\day08.txt") as puzzle_input:
    treemap = [[*map(int, line)] for line in puzzle_input.read().splitlines()]
    visible = 0
    scenic = 0
    for y, _ in enumerate(treemap):
        for x, height in enumerate(treemap[y]):
            # Part 1
            if y == 0 or y == len(treemap) - 1:
                visible += 1
            elif x == 0 or x == len(treemap[y]) - 1:
                visible += 1
            elif max(treemap[y][:x]) < height:
                visible += 1
            elif max(treemap[y][x + 1 :]) < height:
                visible += 1
            elif max(tree[x] for tree in treemap[:y]) < height:
                visible += 1
            elif max(tree[x] for tree in treemap[y + 1 :]) < height:
                visible += 1
            # Part 2
            views = [0, 0, 0, 0]
            for i in range(x + 1, len(treemap[y])):
                views[0] += 1
                if treemap[y][i] >= height:
                    break
            for i in range(x - 1, -1, -1):
                if i >= 0:
                    views[1] += 1
                    if treemap[y][i] >= height:
                        break
            for i in range(y + 1, len(treemap)):
                views[2] += 1
                if treemap[i][x] >= height:
                    break
            for i in range(y - 1, -1, -1):
                if i >= 0:
                    views[3] += 1
                    if treemap[i][x] >= height:
                        break
            if prod(views) > scenic:
                scenic = prod(views)

print([visible, scenic])
