# Day 13: Transparent Origami
# https://adventofcode.com/2021/day/13


def fold_x(x, dots):
    # I used a pencil and paper to work out how to fold a grid along an
    # x axis and came up with this method. Using a set to track the dots
    # worked really well. This function also returns the x that was
    # passed in to be set as the new max.
    for dot in dots.copy():
        if x <= dot[0] <= (x * 2):
            dots.add(((x * 2) - dot[0], dot[1]))
        elif dot[0] > (x * 2):
            dots.remove(dot)
    return x


def fold_y(y, dots):
    # I used a pencil and paper to work out how to fold a grid along an
    # y axis and came up with this method. Using a set to track the dots
    # worked really well. This function also returns the y that was
    # passed in to be set as the new max.
    for dot in dots.copy():
        if y <= dot[1] <= (y * 2):
            dots.add((dot[0], (y * 2) - dot[1]))
        elif dot[1] > (y * 2):
            dots.remove(dot)
    return y


def get_dots(x_border, y_border, show):
    # This is used to return the total number of dots within the border
    # for part one after the first fold. Then it is used to print out all
    # dots on the console to make letters that can be read.
    total_dots = 0
    for y in range(y_border):
        for x in range(x_border):
            dot = " #"[(x, y) in dots]
            if show:
                print(dot, end=" ")
            total_dots += [0, 1][dot == "#"]
        if show:
            print("")
    return total_dots


# Parse the puzzle input file.
with open("2021\\day13.txt") as puzzle_input:
    data = puzzle_input.read().split("\n\n")
    dots = set(tuple(map(int, dot.split(","))) for dot in data[0].splitlines())
    folds = [
        [fold.split("=")[0][-1], int(fold.split("=")[1])]
        for fold in data[1].splitlines()
    ]

# Get the initial max x and y in the grid of dots.
# This is required for part 1.
max_x = max(dot[0] for dot in dots) + 1
max_y = max(dot[1] for dot in dots) + 1

# Parts one and two.
for i, fold in enumerate(folds):
    if fold[0] == "x":
        max_x = fold_x(fold[1], dots)
    if fold[0] == "y":
        max_y = fold_y(fold[1], dots)
    if i == 0:
        print(get_dots(max_x, max_y, False))
get_dots(max_x, max_y, True)
