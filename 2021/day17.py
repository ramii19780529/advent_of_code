# Day 17: Trick Shot
# https://adventofcode.com/2021/day/17


def step(x_velocity, y_velocity):
    # This generator returns the x, y position along with the current
    # velocity of x after each step using the initial x an y velocities.
    x = 0
    y = 0
    while True:
        x += x_velocity
        y += y_velocity
        y_velocity -= 1
        x_velocity -= (x_velocity >= 0) - (x_velocity <= 0)
        yield x, y, x_velocity


# Parse the puzzle input file.
with open("2021\\day17.txt") as puzzle_input:
    area = puzzle_input.read().strip()[13:].split(", ")
    min_box_x, max_box_x = map(int, area[0][2:].split(".."))
    min_box_y, max_box_y = map(int, area[1][2:].split(".."))

# The minimum x velocity is the lowest velocity that will allow the
# probe to enter the target area as the velocity drops to zero. Based
# on the way the x velocity is handled, we can think of the minimum x
# of the target box as a triangle number, so we can estimate the
# starting velocity by reversing the triangle.
min_x_velocity = int((min_box_x * 2) ** 0.5)

# The maximum x velocity is going to be the velocity that will hit the
# maximum x in the target area after just one step, which means it is
# equal to the maximum x in the target area. I'm adding one here because
# it is used in a range.
max_x_velocity = max_box_x + 1

# The minimum y velocity is actually just the minimim y in the target
# area. Anything less than that will miss the target area, anything more
# will not hit the edge cases.
min_y_velocity = min_box_y

# The maximum y velocity is the absolute value of the minimum y in the
# target area minus one. A maximim higher than that value will always
# overshoot the target area. I don't subtract the one here since it is
# used in a range.
max_y_velocity = abs(min_box_y)

# Parts one and two.
# This is basically a brute force solve limited by ranges that hit the
# edge cases. I bet there is some fancy math equation to figure this
# out faster, but I don't know it.
data = set()
for y_velocity in range(min_y_velocity, max_y_velocity):
    for x_velocity in range(min_x_velocity, max_x_velocity):
        max_y = 0
        for x, y, current_x_velocity in step(x_velocity, y_velocity):
            if y < min_box_y:
                break
            if current_x_velocity == 0 and (min_box_x > x > max_box_x):
                break
            if y > max_y:
                max_y = y
            if min_box_x <= x <= max_box_x and min_box_y <= y <= max_box_y:
                data.add((x_velocity, y_velocity, max_y))
                break
print(max(data, key=lambda x: x[2])[2])
print(len(data))
