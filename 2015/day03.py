# Day 3: Perfectly Spherical Houses in a Vacuum
# https://adventofcode.com/2015/day/3


def get_house(directions, santas):
    # Returns the number of houses visited by one or more Santas
    # following the directions provided by the drunk elves.
    x, y = [0, 0], [0, 0]
    houses = set([(0, 0)])
    for santa, direction in enumerate(directions):
        if direction == "^":
            y[santa % santas] -= 1
        if direction == "v":
            y[santa % santas] += 1
        if direction == "<":
            x[santa % santas] -= 1
        if direction == ">":
            x[santa % santas] += 1
        yx = (y[santa % santas], x[santa % santas])
        houses.add(yx)
    return len(houses)


# Parse the puzzle input file.
with open("advent_of_code\\2015\\day03.txt") as puzzle_input:
    directions = puzzle_input.read().strip()

# Part one.
print(get_house(directions, 1))

# Part two.
print(get_house(directions, 2))
