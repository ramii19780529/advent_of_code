# Day 10: Cathode-Ray Tube
# https://adventofcode.com/2022/day/10

# Parse the puzzle input file.
with open("2022\\day10.txt") as puzzle_input:
    instructions = iter([line.split() for line in puzzle_input.read().splitlines()])
    next_instruction = 1
    next_move = 0
    sample_cycles = [20, 60, 100, 140, 180, 220]
    samples = []
    sprite = 1
    screen = []
    for cycle in range(1, 241):
        if cycle == next_instruction:
            instruction = next(instructions)
            sprite += next_move
            next_move = 0
            next_instruction += 1
            if instruction[0] == "addx":
                next_instruction += 1
                next_move = int(instruction[1])
        if cycle in sample_cycles:
            samples.append(cycle * sprite)
        screen.append("#" if sprite - 1 <= (cycle - 1) % 40 <= sprite + 1 else ".")

# Part 1
print(sum(samples))

# Part 2
for x in range(len(screen) // 40):
    print("".join(screen[x * 40 : x * 40 + 40]))
