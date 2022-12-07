# Day 7: No Space Left On Device
# https://adventofcode.com/2022/day/7

current_path = []
path_size = {}

# Parse the puzzle input file.
with open("advent_of_code\\2022\\day07.txt") as puzzle_input:
    terminal = [line.split() for line in puzzle_input.read().splitlines()]
    for line in terminal:
        if line[0] == "$":
            if line[1] != "cd":
                continue
            elif line[2] == "/":
                current_path = ["/root"]
            elif line[2] == "..":
                current_path.pop()
            else:
                current_path.append(line[2])
        elif line[0] == "dir":
            continue
        else:
            for i in range(len(current_path)):
                path_size.setdefault("/".join(current_path[: i + 1]), 0)
                path_size["/".join(current_path[: i + 1])] += int(line[0])
    print(sum(v for v in path_size.values() if v <= 100_000))
    print(min(v for v in path_size.values() if v >= (path_size["/root"] - 40_000_000)))
