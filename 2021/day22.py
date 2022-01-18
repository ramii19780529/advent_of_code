# Day 22: Reactor Reboot
# https://adventofcode.com/2021/day/22


def overlaps(a, b):
    """Return true if the low value of "a" is less than or equal to the
    high value of "b" and high value of "a" is greater than or equal to
    the low value of "b" for x, y, and z. If this is true, then "a" and
    "b" share at least 1 cube.
    """
    return (
        a[0] <= b[1]
        and a[1] >= b[0]
        and a[2] <= b[3]
        and a[3] >= b[2]
        and a[4] <= b[5]
        and a[5] >= b[4]
    )


def get_overlap(a, b):
    """Return a cuboid representing the section of cubes shared between
    cuboid "a" and "b" by simply taking the maximim "a" and "b" low
    values, and the minimum "a" and "b" high values for x, y, and z.
    """
    return (
        max(a[0], b[0]),
        min(a[1], b[1]),
        max(a[2], b[2]),
        min(a[3], b[3]),
        max(a[4], b[4]),
        min(a[5], b[5]),
    )


def get_area(cuboid):
    """Return the simple area of a cuboid, which is the product of the
    difference + 1 between the high and low values for x, y, and z.
    """
    return (
        (cuboid[1] - cuboid[0] + 1)
        * (cuboid[3] - cuboid[2] + 1)
        * (cuboid[5] - cuboid[4] + 1)
    )


def get_region(steps, low, high):
    """Retrun the steps occuring within the specified range. This was
    added after solving part two in order to solve part one using the
    same method as part two since it is more efficient then the brute
    force algorithm I originally applied for part one.
    """
    return [
        (
            step_type,
            tuple(
                (
                    max(step_cuboid[0], low),
                    min(step_cuboid[1], high),
                    max(step_cuboid[2], low),
                    min(step_cuboid[3], high),
                    max(step_cuboid[4], low),
                    min(step_cuboid[5], high),
                )
            ),
        )
        for step_type, step_cuboid in reboot_steps
        if overlaps(step_cuboid, (low, high, low, high, low, high))
    ]


def execute_steps(steps):
    # This was a bit tricky for me. I tried many different ways to track
    # the cubes, but had to search the internet for a method that worked.
    # I"ve implemented a method that adds the "on" cuboid in each step to
    # a dictionary and subtracts the intersection of the current step from
    # each of the prior steps. The trick is to subtract the total value
    # from the original step for each intersection.
    reactor = {}
    for step_type, step_cuboid in steps:
        for reactor_cuboid, value in list(reactor.items()):
            if overlaps(step_cuboid, reactor_cuboid):
                overlap_cuboid = get_overlap(step_cuboid, reactor_cuboid)
                reactor[overlap_cuboid] = reactor.get(overlap_cuboid, 0) - value
        if step_type == "on":
            reactor[step_cuboid] = reactor.get(step_cuboid, 0) + 1
    return sum(get_area(cuboid) * value for cuboid, value in reactor.items())


# Parse the puzzle input file.
with open("2021\\day22.txt") as puzzle_input:
    filter = {
        ord("x"): "",
        ord("y"): "",
        ord("z"): "",
        ord("="): "",
        ord(" "): "..",
        ord(","): "..",
    }
    reboot_steps = [
        ((step := line.split(".."))[0], tuple(map(int, step[1:])))
        for line in puzzle_input.read().translate(filter).splitlines()
    ]

# Part one.
print(execute_steps(get_region(reboot_steps, -50, 50)))

# Part two.
print(execute_steps(reboot_steps))
