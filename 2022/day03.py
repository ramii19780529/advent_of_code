# Day 3: Rucksack Reorganization
# https://adventofcode.com/2022/day/3


def priority(item) -> int:
    if ord(item) >= 97:
        return ord(item) - 96
    return ord(item) - 38


def find_dup_item_priority(rucksack) -> int:
    items_per_compartment = len(rucksack) // 2
    compartment_a = rucksack[:items_per_compartment]
    compartment_b = rucksack[items_per_compartment:]
    for item in compartment_a:
        if item in compartment_b:
            return priority(item)


def find_badge_priority(elf_group) -> int:
    for item in elf_group[0]:
        if item in elf_group[1] and item in elf_group[2]:
            return priority(item)


part_1 = 0
part_2 = 0
elf_group = []
with open("advent_of_code\\2022\\day03.txt") as puzzle_input:
    for rucksack in puzzle_input.read().splitlines():
        part_1 += find_dup_item_priority(rucksack)
        elf_group.append(rucksack)
        if len(elf_group) == 3:
            part_2 += find_badge_priority(elf_group)
            elf_group = []

print(part_1)
print(part_2)
