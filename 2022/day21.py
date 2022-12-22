# Day 21: Monkey Math
# https://adventofcode.com/2022/day/21


def monkey_math(monkey: str, num: int = None) -> int:
    # Uses a dictionary from of monkeys and their jobs from the
    # input file to traverse the equation and return the answer.

    # This base case was added for part two so
    # we can try different numbers for "humn".
    if num and monkey == "humn":
        return num

    # Get the job of the monkey passed.
    job = monkeys[monkey]

    # If there is only a single item in the job then
    # we have a number to return as the base case.
    if len(job) == 1:
        return int(job[0])

    # If more than one item was found in the job, then we need to
    # pass the monkeys back into this function and then perform
    # the required operation when they return from the stack.
    if job[1] == "+":
        return monkey_math(job[0], num) + monkey_math(job[2], num)
    elif job[1] == "-":
        return monkey_math(job[0], num) - monkey_math(job[2], num)
    elif job[1] == "*":
        return monkey_math(job[0], num) * monkey_math(job[2], num)
    elif job[1] == "/":
        return monkey_math(job[0], num) / monkey_math(job[2], num)


# Parse the input.
with open("advent_of_code\\2022\\day21.txt") as puzzle_input:
    monkeys = {
        monkey[0]: monkey[1].split()
        for monkey in [line.split(":") for line in puzzle_input.read().splitlines()]
    }

    # Part 1
    print(round(monkey_math("root")))

    # Part 2 (Assuming the left tree always has "humn" in it.)
    # I think I might have cheated a bit here. I was going to
    # review all the equations, simplify them and come up with
    # a way to calculate the right value, but then I realized
    # that a simple binary search would work since the recurive
    # function seems fast enough... so here it is.
    target = monkey_math(monkeys["root"][2])
    low = 0
    high = 100_000_000_000_000_000_000
    while high > low:
        mid = (high + low) // 2
        test = monkey_math(monkeys["root"][0], mid)
        if test == target:
            print(mid)
            break
        if test < target:
            high = mid - 1
        if test > target:
            low = mid + 1
