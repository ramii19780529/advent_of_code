# Day 6: Lanternfish
# https://adventofcode.com/2021/day/6


def get_spawn(fish, days):
  # Since the age of each fish is tracked by the index, we can simply
  # shift the entire list to the left, adding the fish that spawned from
  # index zero to index six, and adding their babies to index eight.
  for day in range(days):
    # I had to fiddle with the numbers for a bit to get the indexes
    # correct since the list shift has to happen before we add the
    # spawning fish and babies back to the list.
    fish = [*fish[1:7], fish[0] + fish[7], fish[8], fish[0]]
  return sum(fish)


# Parse the puzzle input file.
with open("2021\\day06.txt") as puzzle_input:
  lanternfish = [0, 0, 0, 0, 0, 0, 0, 0, 0]
  age_of_each_fish = tuple(map(int, puzzle_input.read().split(",")))
  # In the lanternfish list, each index represents the number of days
  # until the fish spawns. So give a list of ages for each fish, we
  # use the age as the index into the list, and just add the fish to
  # the correct age in the list.
  for age in age_of_each_fish:
    lanternfish[age] += 1

# Part one.
print(get_spawn(lanternfish, 80))

# Part two.
print(get_spawn(lanternfish, 256))
