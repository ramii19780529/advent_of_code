# Day 2: Rock Paper Scissors
# https://adventofcode.com/2022/day/2

# Parse the puzzle input file.
with open("advent_of_code\\2022\\day02.txt") as puzzle_input:
    esg = [[ord(r[0]) - 64, ord(r[2]) - 87] for r in puzzle_input.readlines()]
    print(sum((p2 + 1 - p1) % 3 * 3 + p2 for p1, p2 in esg))
    print(sum((p2 + p1) % 3 + 1 + (p2 - 1) * 3 for p1, p2 in esg))
