# Day 11: Monkey in the Middle
# https://adventofcode.com/2022/day/11

import math
import copy

# Parse the puzzle input file.
with open("2022\\day11.txt") as puzzle_input:
    monkeys = [
        [
            [*map(int, monkey[0].split(":")[1].split(","))],  # item worry levels
            monkey[1].split("=")[1].replace("old", "worry_level"),  # worry operation
            int(monkey[2].split()[-1]),  # the test equation
            int(monkey[3].split()[-1]),  # throw to this monkey if true
            int(monkey[4].split()[-1]),  # throw to this monkey if false
            0,  # count the number of times this monkey inspected
            {},  # keep track of worry levels we already know about
        ]
        for monkey in [
            line.splitlines()[1:] for line in puzzle_input.read().split("\n\n")
        ]
    ]


def monkey_business(rounds, monkeys, divide):

    # This was added for part 2 to keep the performance in check. I needed to make
    # sure the test had the same result while keeping the worry levels as small as
    # possible. Modulo of the worry level using the LCM works.
    lcm = math.lcm(*[monkey[2] for monkey in monkeys])

    for _ in range(rounds):
        for monkey in monkeys:
            for worry_level in monkey[0]:
                if worry_level not in monkey[6]:
                    new = eval(monkey[1])
                    if divide:
                        new //= 3
                    new %= lcm  # added for 2 two performance.
                    monkey[6][worry_level] = [
                        monkey[3] if (new % monkey[2]) == 0 else monkey[4],
                        new,
                    ]
                monkey[5] += 1
                monkeys[monkey[6][worry_level][0]][0].append(monkey[6][worry_level][1])
            monkey[0] = []
    return math.prod(
        monkey[5] for monkey in sorted(monkeys, key=lambda monkey: monkey[5])[-2:]
    )


print(monkey_business(20, copy.deepcopy(monkeys), True))
print(monkey_business(10000, copy.deepcopy(monkeys), False))
