# Day 19: Beacon Scanner
# https://adventofcode.com/2021/day/19


def orientate(point, x, y, z, i, j, k):
  """ Return a tuple of the point orientated
  by the orientation passed in.
  """
  return (point[x] * i, point[y] * j, point[z] * k)


def orientations(beacons):
  """ Return a dict where the key is one of the 24 possible orentations
  and the values are a set of all beacons points orientated to the
  key orientation.
  """
  return {
    orientation: {
      orientate(beacon, *orientation)
      for beacon in beacons
    }
    for orientation in [
      (x, y, z, i, j, k)
      for x, y, z in ((0, 2, 1), (1, 0, 2), (2, 1, 0))
      for i, j, k in ((+1, +1, -1), (+1, -1, +1), (-1, +1, +1), (-1, -1, -1))
    ] + [
      (x, y, z, i, j, k)
      for x, y, z in ((0, 1, 2), (1, 2, 0), (2, 0, 1))
      for i, j, k in ((+1, +1, +1), (+1, -1, -1), (-1, +1, -1), (-1, -1, +1))
    ]
  }


def subtract_points(point_one, point_two):
  """ Return a tuple containing the difference
  between each axis in the two points.
  """
  return (
    point_one[0] - point_two[0],
    point_one[1] - point_two[1],
    point_one[2] - point_two[2]
  )


def add_points(point_one, point_two):
  """ Return a tuple containing the
  sum of each axis in the two points.
  """
  return (
    point_one[0] + point_two[0],
    point_one[1] + point_two[1],
    point_one[2] + point_two[2]
  )


def offsets(beacons):
  """ Return a dict where each key is the original point of each beacon
  and the value is the difference between that point and all other
  points in the beacons list.
  """
  return {
    point_one: {
      subtract_points(point_one, point_two)
      for point_two in beacons
    }
    for point_one in beacons
  }


def overlap(beacons, absolute_beacons):
  """ Return the scanner offset and orientation based on the point of a
  known beacon and the point of a relative beacon sharing at least 12
  offset beacons.
  """
  absolute_beacon_offsets = offsets(absolute_beacons)
  for orientation, beacon_orientations in orientations(beacons).items():
    beacon_offsets = offsets(beacon_orientations)
    for point_one, point_two in [
      (point_one, point_two)
      for point_one in absolute_beacon_offsets
      for point_two in beacon_offsets
    ]:
      if len(
        absolute_beacon_offsets[point_one]
        & beacon_offsets[point_two]
      ) > 11:
        return subtract_points(point_one, point_two), orientation


def manhattan_distance(point_one, point_two):
  """ Return the manhattan distance between two points."""
  return (
    abs(point_one[0] - point_two[0])
    + abs(point_one[1] - point_two[1])
    + abs(point_one[2] - point_two[2])
  )


# Parse the puzzle input file.
with open("2021\\day19.txt") as puzzle_input:
  scanners_relative_beacon_positions = [
    {
      eval(relative_beacon_position)
      for relative_beacon_position in scanner.splitlines()
      if "---" not in relative_beacon_position
    }
    for scanner in puzzle_input.read().split("\n\n")
  ]


# Use the first set of beacons from the first scanner as our starting
# point for absolute (known) beacon positions and add the first scanner
# to the list of absolute (known) scanner positions at 0, 0, 0.
absolute_beacon_positions, *scanners = scanners_relative_beacon_positions
absolute_scannner_positions = {(0, 0, 0)}
while scanners:
  # Grap the beacons of the next scanner.
  relative_beacon_positions = scanners.pop(0)
  result = overlap(
    relative_beacon_positions,
    absolute_beacon_positions
  )
  # If we don't find an overlap, we add the beacons of that scanner
  # back to the list so we can check it again after we find more beacons
  # from other scanners in the list. We are assuming that the puzzle
  # input will always contain scanners that overlap at least 12 beacons.
  # If we do find an overlap, union the beacons to the set of known
  # beacon locations, calculating the absolute location by adding the
  # coordinates of the orientated points with the scanner offset, then
  # add the scanner offset to the set of absolute scanner locations.
  if result is None:
    scanners.append(relative_beacon_positions)
  else:
    scanner_offset, orientation = result
    absolute_beacon_positions |= {
      add_points(orientate(point, *orientation), scanner_offset)
      for point in relative_beacon_positions
    }
    absolute_scannner_positions.add(scanner_offset)

# Part 1.
print(len(absolute_beacon_positions))

# Part 2.
largest_distance = 0
for point_one, point_two in [
  (point_one, point_two)
  for point_one in absolute_scannner_positions
  for point_two in absolute_scannner_positions
]:
  distance = manhattan_distance(point_one, point_two)
  if distance > largest_distance:
    largest_distance = distance
print(largest_distance)
