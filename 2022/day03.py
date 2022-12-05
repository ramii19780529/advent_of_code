# Day 3: Rucksack Reorganization
# https://adventofcode.com/2022/day/3


def get_priority(rucksacks) -> int:
    for item in rucksacks.pop().intersection(*rucksacks):
        return (ord(item) - 38) % 58  # See notes.


priorities = [0, 0]
rucksacks = []
with open("advent_of_code\\2022\\day03.txt") as puzzle_input:
    for rucksack in puzzle_input.read().splitlines():
        # Part 1.
        items_per_compartment = len(rucksack) // 2
        compartments = [set(rucksack[:items_per_compartment])]
        compartments.append(set(rucksack[items_per_compartment:]))
        priorities[0] += get_priority(compartments)
        # Part 2.
        rucksacks.append(set(rucksack))
        if len(rucksacks) == 3:
            priorities[1] += get_priority(rucksacks)
            rucksacks = []

print(priorities)

# Notes:
# I used the following to figure out if the items had a single equation that would
# provide the correct priority. Turns out they did, so I updated the code to use it.
#   for i in range(1, 100):
#       for j in range(1, 100):
#           if (90 - i) % j == 52:
#               if (122 - i) % j == 26:
#                   print(i, j)
