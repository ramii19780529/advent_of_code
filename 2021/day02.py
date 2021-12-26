# Day 2: Dive!
# https://adventofcode.com/2021/day/2


def simulate_course(data, use_aim = False):
  # Just increment the correct variable based on
  # the input in the file, then return the results. 
  horizontal_position, depth, aim = 0, 0, 0
  for command, units in data:
    if command == "forward":
       horizontal_position += int(units)
       depth += aim * int(units)
    elif command == "down": aim += int(units)
    elif command == "up": aim -= int(units)
  # When not using aim (part 1) the aim is actually the depth.
  return horizontal_position * (depth if use_aim else aim)


# Parse the puzzle input file.
with open("2021\\day02.txt") as puzzle_input:
  planned_course = [
      command.split() for command in puzzle_input.read().splitlines()
  ]

# Part one.
print(simulate_course(planned_course))

# Part two.
print(simulate_course(planned_course, True))
