# Day 9: Smoke Basin
# https://adventofcode.com/2021/day/9


def get_basin_size(heightmap, y, x, height, memo = set()):
  # A recursive function seems to be a good approach to follow each
  # direction from the point passed in to total the size of the basin.
  if 0 < y >= len(heightmap) or 0 < x >= len(heightmap[y]): return 0
  if (y, x) in memo: return 0
  if heightmap[y][x] == 9 or height > heightmap[y][x]: return 0
  memo.add((y, x))
  return 1 + (
      get_basin_size(heightmap, y + 1, x, heightmap[y][x], memo)
    + get_basin_size(heightmap, y - 1, x, heightmap[y][x], memo)
    + get_basin_size(heightmap, y, x + 1, heightmap[y][x], memo)
    + get_basin_size(heightmap, y, x - 1, heightmap[y][x], memo)
  )


# Parse the puzzle input file.
with open("2021\\day09.txt") as puzzle_input:
  heightmap = [
    [int(height) for height in line.strip()]
    for line in puzzle_input.read().splitlines()
  ]

# Check each height in the heightmap and if it is a low point, add it to
# the risk, plus one, to satisfy the part one requirement, then get the
# size of the low point's basin used to satisfy part two.
risk = 0
basin_sizes = []
for y, row in enumerate(heightmap):
  for x, height in enumerate(row):
    if not (
         (y > 0 and height >= heightmap[y - 1][x])
      or (y < (len(heightmap) - 1) and height >= heightmap[y + 1][x])
      or (x > 0 and height >= heightmap[y][x - 1])
      or (x < (len(row) - 1) and height >= heightmap[y][x + 1])
    ):
      risk += height + 1
      basin_sizes.append(get_basin_size(heightmap, y, x, height))

# Part one.
print(risk)

# Part two.
size = 1
for basin_size in sorted(basin_sizes)[-3:]:
  size *= basin_size
print(size)
