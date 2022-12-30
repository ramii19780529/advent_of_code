# Day 5: Supply Stacks
# https://adventofcode.com/2022/day/5

stacks = {
    "9000": [[], [], [], [], [], [], [], [], []],
    "9001": [[], [], [], [], [], [], [], [], []],
}

# Parse the puzzle input file.
with open("2022\\day05.txt") as puzzle_input:
    stack_data, moves = puzzle_input.read().split("\n\n")
    # Populate Stacks
    for crates in stack_data.splitlines()[:-1]:
        for i in range(9):
            crate = crates[i * 4 + 1 : i * 4 + 2].strip()
            if crate:
                stacks["9000"][i].insert(0, crate)
                stacks["9001"][i].insert(0, crate)
    # Move Crates
    for n, source, target in [
        [int(move[1]), int(move[3]) - 1, int(move[5]) - 1]
        for move in [move.split() for move in moves.splitlines()]
    ]:
        # Part 1
        stacks["9000"][target].extend(reversed(stacks["9000"][source][-n:]))
        del stacks["9000"][source][-n:]
        # Part 2
        stacks["9001"][target].extend(stacks["9001"][source][-n:])
        del stacks["9001"][source][-n:]

print("".join(s[-1] for s in stacks["9000"]))
print("".join(s[-1] for s in stacks["9001"]))
