# Day 11: Dumbo Octopus
# https://adventofcode.com/2021/day/11


def get_neighbors(x1, y1):
  # Return every point around point x1, y1.
  for x2 in (-1, 0, 1):
    for y2 in (-1, 0, 1):
      if not x2 == y2 == 0:
        yield (x1 + x2, y1 + y2)


def get_flashes(octopus):
  # This recursive function increases the energy of all neighboring
  # octopi and if they flash due to the increase, increase their
  # neighbors, etc. Return the total number of flashes.
  global octopi
  if octopus not in octopi: return 0
  if octopi[octopus][1]: return 0
  octopi[octopus][0] += 1
  if octopi[octopus][0] < 10: return 0
  octopi[octopus] = [0, True]
  return 1 + sum(list(map(get_flashes, get_neighbors(*octopus))))


# Parse the puzzle input file.
with open("2021\\day11.txt") as puzzle_input:
  # The boolean in the list is used to track if
  # the octopus has already flashed in the step.
  octopi = {
    (x, y):[int(energy), False]
    for y, line in enumerate(puzzle_input)
    for x, energy in enumerate(line.strip())
  }

# Parts one and two.
flashes = 0
steps = 0
while any(data[0] > 0 for data in octopi.values()):
  steps += 1
  flashers = []
  for octopus, data in octopi.items():
    octopi[octopus] = [data[0] + 1, False]
    if data[0] == 9: flashers.append(octopus)
  step_flashes = sum(list(map(get_flashes, flashers)))
  if step_flashes == len(octopi): print(steps)
  flashes += step_flashes
  if steps == 100: print(flashes)
