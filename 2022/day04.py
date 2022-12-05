# Day 4: Camp Cleanup
# https://adventofcode.com/2022/day/4

overlap = [0, 0]
with open("advent_of_code\\2022\\day04.txt") as puzzle_input:
    sections = [
        [*map(int, sections.replace("-", ",").split(","))]
        for sections in puzzle_input.read().splitlines()
    ]
    for a, b, c, d in sections:
        if (a >= c and b <= d) or (a <= c and b >= d):
            overlap[0] += 1
            overlap[1] += 1
        elif (c <= a <= d) or (c <= b <= d):
            overlap[1] += 1

print(overlap)
