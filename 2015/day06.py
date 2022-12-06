# Day 6: Probably a Fire Hazard
# https://adventofcode.com/2015/day/6

# Parse the puzzle input file.
with open("advent_of_code\\2015\\day06.txt") as puzzle_input:
    directions = [
        [x[0], *map(int, x[1].split(",")), *map(int, x[3].split(","))]
        for x in [
            line.replace("turn", "").split()
            for line in puzzle_input.read().splitlines()
        ]
    ]

# Part one.
lights = [[0 for _ in range(1000)] for _ in range(1000)]
for d in directions:
    if d[0] == "on":
        light = 1
    if d[0] == "off":
        light = 0
    for y in range(d[1], d[3] + 1):
        for x in range(d[2], d[4] + 1):
            if d[0] == "toggle":
                lights[y][x] = 0 if lights[y][x] == 1 else 1
            else:
                lights[y][x] = light

print(sum(sum(light) for light in lights))

# Part two.
lights = [[0 for _ in range(1000)] for _ in range(1000)]
for d in directions:
    if d[0] == "on":
        light = 1
    if d[0] == "off":
        light = -1
    if d[0] == "toggle":
        light = 2
    for y in range(d[1], d[3] + 1):
        for x in range(d[2], d[4] + 1):
            lights[y][x] += light
            if lights[y][x] < 0:
                lights[y][x] = 0

print(sum(sum(light) for light in lights))
