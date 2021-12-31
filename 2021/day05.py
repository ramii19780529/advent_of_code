# Day 5: Hydrothermal Venture
# https://adventofcode.com/2021/day/5


def get_points(x1, y1, x2, y2, diagonals):
  # Return all points between the two points, inclusive.
  # Part one only calls for checking rows and columns.
  # For part two, I added support for diagonals.
  if x1 == x2:
    yield from ((x1, y) for y in range(min(y1, y2), max(y1, y2) + 1))
  elif y1 == y2:
    yield from ((x, y1) for x in range(min(x1, x2), max(x1, x2) + 1))
  elif diagonals:
    yield (x1, y1)
    while not (x1 == x2 and y1 == y2):
      if not x1 == x2: x1 += [-1, 1][x1 < x2]
      if not y1 == y2: y1 += [-1, 1][y1 < y2]
      yield (x1, y1)


# Parse the puzzle input file.
with open("2021\\day05.txt") as puzzle_input:
  vent_lines = tuple(
    tuple(
      tuple(map(int, points.split(",")))
      for points in line.split("->")
    )
    for line in puzzle_input.read().splitlines()
  )

# Part one.
vent_points = {}
for point1, point2 in vent_lines:
  for point in get_points(*point1, *point2, False):
    vent_points[point] = vent_points.get(point, 0) + 1
print(sum(overlap > 1 for overlap in vent_points.values()))

# Part two.
vent_points = {}
for point1, point2 in vent_lines:
  for point in get_points(*point1, *point2, True):
    vent_points[point] = vent_points.get(point, 0) + 1
print(sum(overlap > 1 for overlap in vent_points.values()))
