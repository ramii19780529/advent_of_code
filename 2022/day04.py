# Day 4: Camp Cleanup
# https://adventofcode.com/2022/day/4

overlap = [0, 0]
with open("advent_of_code\\2022\\day04.txt") as puzzle_input:
    sections = [
        [*map(int, sections.replace("-", ",").split(","))]
        for sections in puzzle_input.read().splitlines()
    ]
    for s in sections:
        if s[0] >= s[2] and s[1] <= s[3]:
            overlap[0] += 1
            overlap[1] += 1
        elif s[0] <= s[2] and s[1] >= s[3]:
            overlap[0] += 1
            overlap[1] += 1
        elif s[0] >= s[2] and s[0] <= s[3]:
            overlap[1] += 1
        elif s[1] >= s[2] and s[1] <= s[3]:
            overlap[1] += 1

print(overlap)
