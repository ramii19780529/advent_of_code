# Day 17: Pyroclastic Flow
# https://adventofcode.com/2022/day/17

# Read the directions at the bottom to set these:
# Part 2 will not calculate if these are not set correctly.
# block_start, block_height, block_rocks = (26, 79 - 26, 7 * 5)  # Example
block_start, block_height, block_rocks = (353, 3131 - 353, 349 * 5)


def move_rock(rock, y, x):
    # Moves a rock and checks the left/right bounds for wall collisions.
    # Does not check for other rock collisions.
    return (
        rock
        if sum(0 if 0 <= (r[1] + x) <= 6 else 1 for r in rock) > 0
        else set((r[0] + y, r[1] + x) for r in rock)
    )


# Parse the input into a list.
with open("advent_of_code\\2022\\day17.txt") as puzzle_input:
    jets = list(puzzle_input.read().strip())
    # Hard coding the rocks here.
    rocks = [
        {(0, 2), (0, 3), (0, 4), (0, 5)},
        {(0, 3), (1, 2), (1, 3), (1, 4), (2, 3)},
        {(2, 4), (1, 4), (0, 2), (0, 3), (0, 4)},
        {(0, 2), (1, 2), (2, 2), (3, 2)},
        {(0, 2), (0, 3), (1, 2), (1, 3)},
    ]
    # Put a base at 0 so the first rock top land at 1.
    chamber = {(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6)}
    top = 0
    top_log = set()
    rock = None
    rock_number = 0
    stop_rock = 0
    repeated_height = 0
    jet_number = 0
    while rock_number < 2022:
        # Get the next rock if we don't have a rock to move.
        if rock is None:
            # Rocks start in position 0, so we need to move the rock to the top + four
            # to get a clearence of 3 between the top and the bottom.
            rock = move_rock(rocks[rock_number % 5], top + 4, 0)
        # Get the direction of the next jet of gas.
        jet = jets[jet_number % len(jets)]
        jet_number += 1
        # Move the rock left or right.
        jet_test = move_rock(rock, 0, [-1, 1][jet == ">"])
        # If the rock did not hit anything, use the new location.
        if not jet_test.intersection(chamber):
            rock = jet_test
        # Move the rock down.
        hit_test = move_rock(rock, -1, 0)
        # If the rock didn't hit anything, use the new location.
        if not hit_test.intersection(chamber):
            rock = hit_test
        else:  # The rock hit something.
            chamber.update(rock)
            top = max(max(r[0] for r in rock), top)
            rock = None
            if rock_number % 5 == 0:
                top_log.add(top)
                if top == block_start:
                    repeated_height = (
                        (1_000_000_000_000 - rock_number) // block_rocks
                    ) * block_height - 1
                    stop_rock = rock_number + (
                        (1_000_000_000_000 - rock_number) % block_rocks
                    )
                if rock_number == stop_rock and stop_rock > 0:
                    print(f"Part 2: {top + repeated_height}")
            rock_number += 1
            if rock_number == 2022:
                print(f"Part 1: {top}")


# I used this to manually determine the patter matching.
# I would like to do this via code at some point.
# Run the script as-is to generate the output used below.
# Steps:
# 1 - Get the line number where the output starts repeating. I do this by selecting the
#     first line that has an * along with the next 14 lines and I search. If there are
#     no results, I repeat the process starting with the next line having an * until I
#     find the first one that repeats. This line number is the block_start.
# 2 - Next, take difference between the block_start line number and the first line
#     number where it starts to repeat. This is your block_size.
# 3 - Select the text of an entire block and count how many * it contains and multiply
#     that by five. This is your block_rocks.
# Ex: Using the example, the values are:
#        block_start = 26
#        block_height = 79 - 26
#        block_rocks = 7 * 5
with open("advent_of_code\\2022\\day17.out", "w") as puzzle_output:
    for y in range(1, top):
        for x in range(7):
            puzzle_output.write(".#"[(y, x) in chamber])
        if y in top_log:
            puzzle_output.write("*")
        puzzle_output.write("\n")
