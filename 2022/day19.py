# Day 19: Not Enough Minerals
# https://adventofcode.com/2022/day/19

from math import prod

ORE = 0
CLAY = 1
OBSIDIAN = 2
GEODE = 3


# This takes a very long time.
# With my data, part one ~60 seconds, part two ~200 seconds.
# It needs to be optimized.
def play(blueprints: dict, time: int, count: int) -> int:

    total = []

    for id in range(1, count + 1):
        cost = blueprints[id]

        score = 0
        memo = set()
        stack = [[[1, 0, 0, 0], [0, 0, 0, 0], time]]

        # Calculate the number of bots required to gather enough
        # of a resource to build a bot on each turn.
        max_bots = []
        max_bots.append(max([cost[0][0], cost[1][0], cost[2][0], cost[3][0]]))
        max_bots.append(max([cost[0][1], cost[1][1], cost[2][1], cost[3][1]]))
        max_bots.append(max([cost[0][2], cost[1][2], cost[2][2], cost[3][2]]))
        max_bots.append(time)

        while stack:

            bots, resource, turns = stack.pop()

            # If this is the last turn we have a base case.
            # Check if we have a new high score and save it.
            if turns == 0:
                score = max(resource[GEODE], score)
                continue

            # If the current score is greater than the max
            # score this path can get, we end this game.
            # This helps when using DFS.
            max_score = (
                resource[GEODE] + (bots[GEODE] * turns) + (turns * (turns - 1) / 2)
            )
            if score > max_score:
                continue

            # Use memoization to catch duplicate paths and end them.
            mem = (tuple(bots), tuple(resource), turns)
            if mem in memo:
                continue
            memo.add(mem)

            # Build a bot if we have the resources to build a
            # bot and we have less bots producing a resource
            # than the number of that resource required to build
            # the bot that uses the most of that resource.
            factory = []
            for bot in range(4):
                if (
                    resource[ORE] >= cost[bot][ORE]
                    and resource[CLAY] >= cost[bot][CLAY]
                    and resource[OBSIDIAN] >= cost[bot][OBSIDIAN]
                    and bots[bot] < max_bots[bot]
                ):
                    factory.append(bot)

            # Update our resources with the number
            # of bots we currently have running.
            for i in range(4):
                resource[i] += bots[i]

            # For every bot we can / should create,
            # build the bot, update the resources
            # and start a new path.
            for bot in factory:
                _bots = bots[:]
                _bots[bot] += 1
                _resource = resource[:]
                for r in range(3):
                    _resource[r] -= cost[bot][r]
                stack.append((_bots, _resource, turns - 1))

            # Maybe try to stop extra paths from being followed here.
            stack.append((bots, resource, turns - 1))

        print(f"Blueprint: {id} - {score}")
        total.append((score, id))
    return total


# Parse the input.
with open("advent_of_code\\2022\\day19.txt") as puzzle_input:
    blueprints = {
        int(line[1][:-1]): (
            (int(line[6]), 0, 0),
            (int(line[12]), 0, 0),
            (int(line[18]), int(line[21]), 0),
            (int(line[27]), 0, int(line[30])),
        )
        for line in [line.split() for line in puzzle_input.read().splitlines()]
    }

    part1 = play(blueprints, 24, 30)
    print(sum(result[0] * result[1] for result in part1))

    part2 = play(blueprints, 32, 3)
    print(prod(result[0] for result in part2))
