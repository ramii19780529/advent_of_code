# Day 7: The Treachery of Whales
# https://adventofcode.com/2021/day/7


def triangle(n):
    # Calculate the triangle of a number.
    # This is the sum of every number from 1 to n.
    return n * (n + 1) // 2


def get_fuel(positions, part):
    # So I decided to use brute force on this one since it finishes in a
    # reasonable about of time. Simply iterate through all positions from
    # the minimum to the maximum distances as target positions, sum the
    # total fuel used by each crab to reach the target and keep the lowest
    # calculated amount fuel.
    fuel = 0
    for target in range(min(positions), max(positions) + 1):
        if part == 1:
            test_fuel = sum(abs(n - target) for n in positions)
        elif part == 2:
            test_fuel = sum(triangle(abs(n - target)) for n in positions)
        if fuel == 0 or fuel > test_fuel:
            fuel = test_fuel
    return fuel


# Parse the puzzle input file.
with open("2021\\day07.txt") as puzzle_input:
    crab_position = eval(puzzle_input.read())

# Part one.
print(get_fuel(crab_position, 1))

# Part two.
print(get_fuel(crab_position, 2))
