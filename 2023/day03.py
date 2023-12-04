# Day 3: Gear Ratios
# https://adventofcode.com/2023/day/3

from functools import reduce


with open(r"advent_of_code\2023\day03.txt") as puzzle_input:
    engine_schematic = puzzle_input.read().splitlines()
    maxRow = len(engine_schematic)
    maxColumn = len(engine_schematic[0])

    # store the row, start, and end position of each number in a list
    numbers = []
    for row, data in enumerate(engine_schematic):
        start = -1
        for column, chr in enumerate(data):
            if chr.isdigit():
                if start < 0:
                    start = column
            if start >= 0 and not chr.isdigit():
                numbers.append([row, start, column - 1])
                start = -1
            if start >= 0 and column == maxColumn - 1:
                if start >= 0:
                    numbers.append([row, start, column])

    # Part 1: add the number to the parts list if any neighbor of the number is not a digit nor a dot
    # Part 2: if a neighbor is *, use the * location as a key in a dict, add the number to the list for each * location
    part_numbers = []
    links = {}
    for number in numbers:
        is_part_number = False
        gear_links = []
        for row in range(max(number[0] - 1, 0), min(number[0] + 2, maxRow)):
            for column in range(max(number[1] - 1, 0), min(number[2] + 2, maxColumn)):
                chr = engine_schematic[row][column]
                if not (chr.isdigit() or chr == "."):
                    is_part_number = True
                    if chr == "*":
                        gear_links.append((row, column))
        if is_part_number:
            part_number = int(
                "".join(engine_schematic[number[0]][number[1] : number[2] + 1])
            )
            part_numbers.append(part_number)
            for gear_link in gear_links:
                if gear_link in links:
                    links[gear_link].append(part_number)
                else:
                    links[gear_link] = [part_number]

    # Part one.
    print(sum(part_numbers))

    # Part two.
    print(
        sum(
            reduce(lambda x, y: x * y, links[link])  # fancy way to multiply
            for link in links
            if len(links[link])
            > 1  # Only include * locations that have more than 1 number.
        )
    )
