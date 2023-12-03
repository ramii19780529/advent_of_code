# Day 2: Cube Conundrum
# https://adventofcode.com/2023/day/2

full_game_set = set()
impossible_game_set = set()
game_power = []

# Parse the puzzle input file.
with open(r"advent_of_code\2023\day02.txt") as puzzle_input:
    games = puzzle_input.read().splitlines()
    for game in games:
        colors = {"red": [0, 0], "green": [0, 0], "blue": [0, 0]}
        gameId, grabs = game.split(":")
        gameId = int(gameId.split()[1])
        full_game_set.add(gameId)
        grabs = grabs.split(";")
        for grab in grabs:
            colors["red"][0], colors["green"][0], colors["blue"][0] = 0, 0, 0
            for color in grab.split(","):
                cubes, color_key = color.split()
                colors[color_key] = [int(cubes), max(colors[color_key][1], int(cubes))]
                if (
                    colors["red"][0] > 12
                    or colors["green"][0] > 13
                    or colors["blue"][0] > 14
                ):
                    impossible_game_set.add(gameId)
        game_power.append(
            max(colors["red"][1], 1)
            * max(colors["green"][1], 1)
            * max(colors["blue"][1], 1)
        )

# Part one.
print(sum(full_game_set - impossible_game_set))

# Part two.
print(sum(game_power))
