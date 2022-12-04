# Day 3: Rucksack Reorganization
# https://adventofcode.com/2022/day/3


def get_priority(rucksacks) -> int:
    for item in rucksacks.pop().intersection(*rucksacks):
        if ord(item) >= 97:
            return ord(item) - 96
        return ord(item) - 38


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
