# Day 1: Not Quite Lisp
# https://adventofcode.com/2015/day/1


# Parse the puzzle input file.
with open("2015\\day01.txt") as puzzle_input:
    directions = puzzle_input.read().strip()

# Parts one and two.
floor = 0
basement = None
for i, direction in enumerate(directions):
    if not basement and floor < 0:
        basement = i
    if direction == "(":
        floor += 1
    if direction == ")":
        floor -= 1
print(floor)
print(basement)
