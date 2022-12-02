# Day 1: Calorie Counting
# https://adventofcode.com/2022/day/1

# Parse the puzzle input file.
with open("advent_of_code\\2022\\day01.txt") as puzzle_input:
    elf_calories = sorted(
        [
            sum(map(int, elf_snacks.splitlines()))
            for elf_snacks in puzzle_input.read().split("\n\n")
        ]
    )
    print(elf_calories[-1])
    print(sum(elf_calories[-3:]))
