# Day 18: Snailfish
# https://adventofcode.com/2021/day/18


def flatten(number, level = 0):
  # Flatten a snailfish number into a list of lists containing the
  # depth and value of each regular number in the order they appear.
  if type(number) == int: return [[level, number]]
  return flatten(number[0], level + 1) + flatten(number[1], level + 1)


def explode(number):
  # Explode the first snailfish pair that needs to be exploded.
  for i, n in enumerate(number):
    if n[0] == 5:
      left = number.pop(i)[1]
      right = number.pop(i)[1]
      number.insert(i, [4, 0])
      if i - 1 >= 0: number[i - 1][1] += left
      if i + 1 < len(number): number[i + 1][1] += right
      return number, True
  return number, False


def split(number):
  # Split the first snailfish regular number that needs to be split.
  for i, n in enumerate(number):
    if n[1] > 9:
      number.pop(i)
      number.insert(i, [n[0] + 1, int(n[1] / 2 + 0.5)])
      number.insert(i, [n[0] + 1, int(n[1] / 2)])
      return number, True
  return number, False


def reduce(number):
  # Reduce the number by exploding and
  # splitting until neither can be done.
  while True:
    number, has_exploded = explode(number)
    if has_exploded: continue
    number, has_split = split(number)
    if has_split: continue
    break
  return number


def add(number_a, number_b):
  # Join two flattened numbers and increase the depth
  # of each by one, then reduce the entire number.
  number = []
  for n in number_a + number_b:
    number.append([n[0] + 1, n[1]])
  return reduce(number)


def magnitude(number):
  # Calculate the "magnitude" of a flattened number.
  for level in [4, 3, 2, 1]:
    for i in range(len(number)):
      if i >= len(number): break
      # The highest level numbers are always pairs.
      if number[i][0] == level:
        a = number.pop(i)[1] * 3
        b = number.pop(i)[1] * 2
        number.insert(i, [level - 1, a + b])
  return number[0][1]


# Parse the puzzle input file.
with open("2021\\day18.txt") as puzzle_input:
  snailfish_numbers = [
    flatten(eval(line))
    for line in puzzle_input
  ]

# Part one.
total = snailfish_numbers[0]
for snailfish_number in snailfish_numbers[1:]:
  total = add(total, snailfish_number)
print(magnitude(total))

# Part two.
max_magnitude = 0
for a in snailfish_numbers:
  for b in snailfish_numbers:
    if a == b: continue
    total = magnitude(add(a, b))
    if total > max_magnitude: max_magnitude = total
print(max_magnitude)
