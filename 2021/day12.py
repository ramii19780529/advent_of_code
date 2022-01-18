# Day 12: Passage Pathing
# https://adventofcode.com/2021/day/12


def add_caves(start_cave, end_cave):
    # Add a start cave and and end cave to the cave map.
    # Skip any cave map where the start cave would be an
    # end, or the end cave would be a start.
    global cave_map
    if not (start_cave == "end" or end_cave == "start"):
        if start_cave in cave_map:
            cave_map[start_cave].append(end_cave)
        else:
            cave_map[start_cave] = [end_cave]


def find_path(cave, repeat, path=tuple(), memo={}):
    # Keep following all the caves until we hit the end, then return 1.
    # I added memoization here to improve performace, but it wasn't really
    # needed with the give data set. It ran find without it.
    global cave_map
    key = (cave, repeat, path)
    if key in memo:
        return memo[key]
    if cave == "end":
        return 1
    # The following if block allows a single small cave to be visited
    # twice if repeat is True. This was added for part two.
    if cave.islower():
        if cave in path:
            if repeat:
                repeat = False
            else:
                return 0
        path = (*path, cave)
    for next_cave in cave_map[cave]:
        memo[key] = memo.get(key, 0) + find_path(next_cave, repeat, path, memo)
    return memo[key]


# Parse the puzzle input file.
# Figuring out how to stage the data was the hard part for me. I got
# ideas from a few different people on the Python Discord server.
with open("2021\\day12.txt") as puzzle_input:
    cave_map = {}
    for connection in puzzle_input:
        caves = connection.strip().split("-")
        add_caves(caves[0], caves[1])
        add_caves(caves[1], caves[0])

# Part one.
print(find_path("start", False))

# Part two.
print(find_path("start", True))
