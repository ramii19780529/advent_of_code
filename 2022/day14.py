# Day 14: Regolith Reservoir
# https://adventofcode.com/2022/day/14

# Parse the puzzle input file.
with open("advent_of_code\\2022\\day14.txt") as puzzle_input:
    cave = set()
    for path in puzzle_input.read().splitlines():
        lines = path.split("->")
        x1, y1 = lines[0].strip().split(",")
        x1, y1 = int(x1), int(y1)
        # Add the rocks to the cave.
        cave.add((x1, y1))
        for i, line in enumerate(lines[1:]):
            x2, y2 = line.strip().split(",")
            x2, y2 = int(x2), int(y2)
            while not x1 == x2:
                if x1 > x2:
                    x1 -= 1
                else:
                    x1 += 1
                cave.add((x1, y1))
            while not y1 == y2:
                if y1 > y2:
                    y1 -= 1
                else:
                    y1 += 1
                cave.add((x1, y1))

    # Find the limits of the cave.
    x_min = min(rock[0] for rock in cave)
    x_max = max(rock[0] for rock in cave)
    y_max = max(rock[1] for rock in cave) + 2  # Account for the floor in part two.

    # Add the floor used in part two.
    for x in range(x_min - 10000, x_max + 10000):
        cave.add((x, y_max))

    sand = 0
    y_sand = 0
    part1 = True
    # Drop sand until no more sand can fit.
    while y_sand < y_max and (500, 0) not in cave:
        # Check to see if part 1 is satisfied.
        if part1 and y_sand > y_max - 2:
            print(sand - 1)
            part1 = False
        sand += 1
        x_sand = 500
        y_sand = 0
        # Track path of sand until it comes to a rest then add it to the cave.
        while y_sand < y_max:
            if (x_sand, y_sand + 1) not in cave:
                y_sand += 1
                continue
            elif (x_sand - 1, y_sand + 1) not in cave:
                x_sand -= 1
                y_sand += 1
                continue
            elif (x_sand + 1, y_sand + 1) not in cave:
                x_sand += 1
                y_sand += 1
                continue
            cave.add((x_sand, y_sand))
            break
    print(sand)
