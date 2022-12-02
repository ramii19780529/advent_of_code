# Day 2: I Was Told There Would Be No Math
# https://adventofcode.com/2015/day/2


# Parse the puzzle input file.
with open("2015\\day02.txt") as puzzle_input:
    presents_dimensions = [
        sorted(map(int, present_dimensions.split("x")))
        for present_dimensions in puzzle_input.read().splitlines()
    ]

# Parts one and two.
wrapping_paper = 0
ribbon = 0
for (
    x,
    y,
    z,
) in presents_dimensions:
    present_surface = (2 * x * y, 2 * y * z, 2 * z * x)
    wrapping_paper += sum(present_surface) + min(present_surface) // 2
    ribbon += (x + x + y + y) + (x * y * z)
print(wrapping_paper)
print(ribbon)
