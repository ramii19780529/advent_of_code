# Day 9: Rope Bridge
# https://adventofcode.com/2022/day/9

# Parse the puzzle input file.
with open("2022\\day09.txt") as puzzle_input:
    motions = [
        [line.split()[0], int(line.split()[1])]
        for line in puzzle_input.read().splitlines()
    ]

for knots in [2, 10]:
    knot = [[0, 0] for _ in range(knots)]
    visited = {(0, 0)}
    for direction, steps in motions:
        while steps > 0:
            steps -= 1
            for i in range(knots):
                if i == 0:
                    if direction == "R":
                        knot[i][0] += 1
                    elif direction == "L":
                        knot[i][0] -= 1
                    elif direction == "U":
                        knot[i][1] += 1
                    elif direction == "D":
                        knot[i][1] -= 1
                else:
                    x_diff = knot[i - 1][0] - knot[i][0]
                    y_diff = knot[i - 1][1] - knot[i][1]
                    if y_diff > 1:
                        knot[i][1] += 1
                        if x_diff > 0:
                            knot[i][0] += 1
                        elif x_diff < 0:
                            knot[i][0] -= 1
                    elif y_diff < -1:
                        knot[i][1] -= 1
                        if x_diff > 0:
                            knot[i][0] += 1
                        elif x_diff < 0:
                            knot[i][0] -= 1
                    elif x_diff < -1:
                        knot[i][0] -= 1
                        if y_diff > 0:
                            knot[i][1] += 1
                        elif y_diff < 0:
                            knot[i][1] -= 1
                    elif x_diff > 1:
                        knot[i][0] += 1
                        if y_diff > 0:
                            knot[i][1] += 1
                        elif y_diff < 0:
                            knot[i][1] -= 1
            visited.add(tuple(knot[knots - 1]))
    print(len(visited))
