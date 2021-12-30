# Day 15: Chiton
# https://adventofcode.com/2021/day/15


from heapq import heappop, heappush


def get_lowest_risk(grid):
  # This function returns the lowest risk out of all
  # paths in the grid using a Dijkstra-like algorithm.

  # Add the starting position (top left) as our first node.
  # Since we are not moving into that position, the risk is zero.
  next_node = []
  heappush(next_node, (0, (0, 0)))

  # Set the destination (bottom left).
  destination = (len(grid[0]) - 1, len(grid) - 1)
  visited = set()

  # Loop until we hit the destination.
  while True:
    risk, (x, y) = heappop(next_node)
    if (x, y) in visited:
      continue
    if (x, y) == destination:
      return risk
    visited.add((x, y))
    if x > 0:
      heappush(next_node, (risk + grid[y][x - 1], (x - 1, y)))
    if x + 1 < len(grid[y]):
      heappush(next_node, (risk + grid[y][x + 1], (x + 1, y)))
    if y > 0:
      heappush(next_node, (risk + grid[y - 1][x], (x, y - 1)))
    if y + 1 < len(grid):
      heappush(next_node, (risk + grid[y + 1][x], (x, y + 1)))


# Parse the puzzle input file.
with open("2021\\day15.txt") as puzzle_input:
  chiton_risk_map = [
    [*map(int, row)]
    for row in puzzle_input.read().splitlines()
  ]

# Part one.
print(get_lowest_risk(chiton_risk_map))

# Part two.
chiton_risk_full_map = []
for y in range(5):
  for i, row in enumerate(chiton_risk_map):
    chiton_risk_full_map.append([])
    for x in range(5):
      for risk in row:
        new_risk = (risk + x + y - 1) % 9 + 1
        chiton_risk_full_map[i + (y * len(chiton_risk_map[i]))].append(new_risk)
print(get_lowest_risk(chiton_risk_full_map))
