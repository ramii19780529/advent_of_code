# Day 13: Distress Signal
# https://adventofcode.com/2022/day/13


def comp(left, right):
    if type(left) == int and type(right) == int:
        return left < right
    if type(left) == int:
        left = [left]
    if type(right) == int:
        right = [right]
    # Copy the lists so popping doesn't mess up the original.
    left, right = (left[:], right[:])
    while True:
        if len(left) == 0:
            return True
        if len(right) == 0:
            return False
        l, r = (left.pop(0), right.pop(0))
        if l == r:
            continue
        return comp(l, r)


# Parse the puzzle input file.
with open("advent_of_code\\2022\\day13.txt") as puzzle_input:
    signals = [eval(s) for s in puzzle_input.read().splitlines() if len(s) > 0]

    # Part 1
    good_pairs = []
    for i in range(0, len(signals) // 2):
        if comp(signals[i * 2], signals[i * 2 + 1]):
            good_pairs.append(i + 1)
    print(sum(good_pairs))

    # Part 2
    signals.append([[2]])
    signals.append([[6]])
    # Using bubble sort.
    for i in range(len(signals) - 1, 0, -1):
        for j in range(i):
            if comp(signals[j + 1], signals[j]):
                signals[j], signals[j + 1] = (signals[j + 1], signals[j])
    print((signals.index([[2]]) + 1) * (signals.index([[6]]) + 1))
