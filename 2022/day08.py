# Day 8: Treetop Tree House
# https://adventofcode.com/2022/day/8

from math import prod

# Parse the puzzle input file.
with open("advent_of_code\\2022\\day08.txt") as puzzle_input:
    treemap = [[*map(int, line)] for line in puzzle_input.read().splitlines()]
    visible = 0
    scenic = 0
    for y, row in enumerate(treemap):
        for x, height in enumerate(row):
            # Part 1
            if y == 0 or y == len(treemap) - 1:
                visible += 1
            elif x == 0 or x == len(row) - 1:
                visible += 1
            elif max(row[:x]) < height:
                visible += 1
            elif max(row[x + 1 :]) < height:
                visible += 1
            elif max(tree[x] for tree in treemap[:y]) < height:
                visible += 1
            elif max(tree[x] for tree in treemap[y + 1 :]) < height:
                visible += 1
            # Part 2
            views = [0, 0, 0, 0]
            for i in row[x + 1 :]:
                views[0] += 1
                if i >= height:
                    break
            for i in row[x - 1 :: -1]:
                views[1] += 1
                if i >= height:
                    break
            for i in [row[x] for row in treemap[y + 1 :]]:
                views[2] += 1
                if i >= height:
                    break
            for i in [row[x] for row in treemap[y - 1 :: -1]]:
                views[3] += 1
                if i >= height:
                    break
            if prod(views) > scenic:
                scenic = prod(views)

print([visible, scenic])
