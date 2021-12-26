# Day 1: Sonar Sweep
# https://adventofcode.com/2021/day/1


def sonar_sweep_increases(data, window = 1):
  # Using zip on the data, offset by the window, works because the only
  # difference between the sum of two adjacent sliding windows is the
  # first number in the first window and the last number in the next.
  return sum([
    floor_depth[0] < floor_depth[1]
    for floor_depth in zip(data, data[window:])
  ])


# Parse the puzzle input file.
with open("2021\day01.txt") as puzzle_input:
  sonar_sweep_report = [
    int(sea_floor_depth)
    for sea_floor_depth in puzzle_input.read().splitlines()
  ]

# Part one.
print(sonar_sweep_increases(sonar_sweep_report))

# Part two.
print(sonar_sweep_increases(sonar_sweep_report, 3))
