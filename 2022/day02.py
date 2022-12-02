# Day 2: Rock Paper Scissors
# https://adventofcode.com/2022/day/2

rps_shapes = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors",
}
rps_response = {
    "A": ["C", "A", "B"],
    "B": ["A", "B", "C"],
    "C": ["B", "C", "A"],
}

rps_resp_idx = {"X": 0, "Y": 1, "Z": 2}


def score1(rps):
    if rps_shapes[rps[1]] == "Rock":
        _score = 1
        if rps_shapes[rps[0]] == "Scissors":
            _score += 6
    if rps_shapes[rps[1]] == "Paper":
        _score = 2
        if rps_shapes[rps[0]] == "Rock":
            _score += 6
    if rps_shapes[rps[1]] == "Scissors":
        _score = 3
        if rps_shapes[rps[0]] == "Paper":
            _score += 6
    if rps_shapes[rps[0]] == rps_shapes[rps[1]]:
        _score += 3
    return _score


def score2(rps):
    rps[1] = rps_response[rps[0]][rps_resp_idx[rps[1]]]
    return score1(rps)


# Parse the puzzle input file.
with open("advent_of_code\\2022\\day02.txt") as puzzle_input:
    encrypted_strategy_guide = [
        [shape[0], shape[2]] for shape in puzzle_input.read().splitlines()
    ]
    print(sum(map(score1, encrypted_strategy_guide)))
    print(sum(map(score2, encrypted_strategy_guide)))
