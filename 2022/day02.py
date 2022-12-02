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


def score1(rps):
    p1, p2 = rps.split()
    if rps_shapes[p2] == "Rock":
        _score = 1
        if rps_shapes[p1] == "Scissors":
            _score += 6
    if rps_shapes[p2] == "Paper":
        _score = 2
        if rps_shapes[p1] == "Rock":
            _score += 6
    if rps_shapes[p2] == "Scissors":
        _score = 3
        if rps_shapes[p1] == "Paper":
            _score += 6
    if rps_shapes[p1] == rps_shapes[p2]:
        _score += 3
    return _score


rps_response = {
    "A": ["C", "A", "B"],
    "B": ["A", "B", "C"],
    "C": ["B", "C", "A"],
}

rps_resp_idx = {"X": 0, "Y": 1, "Z": 2}


def score2(rps):
    p1, p2 = rps.split()
    p2 = rps_response[p1][rps_resp_idx[p2]]
    return score1(p1 + " " + p2)


# Parse the puzzle input file.
with open("advent_of_code\\2022\\day02.txt") as puzzle_input:
    encrypted_strategy_guide = puzzle_input.read().splitlines()
    print(sum(map(score1, encrypted_strategy_guide)))
    print(sum(map(score2, encrypted_strategy_guide)))
