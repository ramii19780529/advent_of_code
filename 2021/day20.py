# Day 20: Trench Map
# https://adventofcode.com/2021/day/20


def get_neighbors(position):
  """Return the coordinates of each "pixel" surrounding the pixel
  location that is passed in, starting from the top left, progressing
  left to right, finishing on the bottom right.
  """
  yield from [
    (position[0] + x, position[1] + y)
    for y in (-1, 0, 1)
    for x in (-1, 0, 1)
  ]


def expand(data):
  """Return the expanded image by expanding the area of the image by one
  pixel on each side using the current state of the infinate area.
  """
  expanded_image = data.copy()
  for position in data:
    for check_position in get_neighbors(position):
      if check_position not in expanded_image:
        expanded_image[check_position] = infinity
  return expanded_image


def get_index(data, position):
  """Return the nine-bit number used as an index to look up the correct
  pixel state from the enhancement algorithm. It uses the current state
  of the pixels nine neighbors to set bits on or off.
  """
  index = 0
  for check_position in get_neighbors(position):
    index = (index << 1) + (data.get(check_position, infinity) == "#")
  return index


def enhance_image(data, algorithm):
  """Return the image data "enhanced" by the algorithm."""
  global infinity
  enhanced_image = expand(data)
  for position in enhanced_image:
    enhanced_image[position] = algorithm[get_index(data, position)]
  # Originally, the test data worked, but the puzzle input did not. I
  # found that the issue was with the "infinite" image values. If the
  # algorithm contains "#" in the first position and "." in the last
  # position, all infinite pixels toggle with each enhancement. I added
  # the "infinity" variable to track the current state of the infinite
  # pixels to be used in expand() and get_index().
  infinity = algorithm[-1] if infinity == "#" else algorithm[0]
  return enhanced_image


# Parse the puzzle input file.
with open("2021\\day20.txt") as puzzle_input:
  image_enhancement_algorithm, input_image = puzzle_input.read().split("\n\n")
  input_image = {
    (x, y): pixel
    for y, pixels in enumerate(input_image.splitlines())
    for x, pixel in enumerate(pixels)
  }

# Parts one and two.
infinity = "."
for e in range(50):
  input_image = enhance_image(input_image, image_enhancement_algorithm)
  # Part two was just more loops of part one.
  if e in (1, 49):
    print(sum([pixel == "#" for pixel in input_image.values()]))
