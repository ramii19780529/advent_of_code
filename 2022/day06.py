# Day 6: Tuning Trouble
# https://adventofcode.com/2022/day/6


def find_start(datastream, start, length):
    for i in range(start, len(datastream) - length):
        if len(set(datastream[i : i + length])) == length:
            print(i + length)
            break
    return i + length


# Parse the puzzle input file.
with open("2022\\day06.txt") as puzzle_input:
    datastream = puzzle_input.read()
    part1 = find_start(datastream, 0, 4)
    part2 = find_start(datastream, part1, 14)
