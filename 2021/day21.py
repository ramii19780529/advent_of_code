# Day 21: Dirac Dice
# https://adventofcode.com/2021/day/21


class Die:
    def __init__(self, sides):
        self.roll = 0
        self.rolls = 0
        self.sides = sides

    def __iter__(self):
        return self

    def __next__(self):
        self.roll += 1
        self.rolls += 1
        if self.roll > self.sides:
            self.roll = 1
        return self.roll


def get_rolls(die, number_of_rolls):
    while number_of_rolls > 0:
        yield next(die)
        number_of_rolls -= 1


def dirac(a_position, b_position, a_score=0, b_score=0, memo={}):
    # Memoize this recursive function to improve performace.
    key = (a_position, b_position, a_score, b_score)
    if key in memo:
        return memo[key]
    # b_score is always the most recently updated score due
    # to swaping a and b for each level to simulate turns.
    if b_score >= 21:
        return (0, 1)
    a_win_bucket = 0
    b_win_bucket = 0
    # This creates a list of all possible total
    # roll amounts for the next three roles.
    for n in tuple(
        a + b + c for a in range(1, 4) for b in range(1, 4) for c in range(1, 4)
    ):
        # Calculate the position of player a for this roll (n).
        next_a_position = (((a_position - 1) + n) % 10) + 1
        # Pass in a as b and b as a to take turns.
        b_wins, a_wins = dirac(
            b_position, next_a_position, b_score, a_score + next_a_position, memo
        )
        a_win_bucket += a_wins
        b_win_bucket += b_wins
    memo[key] = (a_win_bucket, b_win_bucket)
    return memo[key]


# Parse the puzzle input file.
with open("2021\\day21.txt") as puzzle_input:
    players = {
        player: [int(line.split(":")[1]), 0]
        for player, line in enumerate(puzzle_input.read().splitlines())
    }
    player_1_start = players[0][0]
    player_2_start = players[1][0]

# Part one.
d100 = Die(100)
while all(data[1] < 1000 for data in players.values()):
    for player in players:
        for roll in get_rolls(d100, 3):
            players[player][0] = (((players[player][0] - 1) + roll) % 10) + 1
        players[player][1] += players[player][0]
for player, data in players.items():
    if data[1] < 1000:
        print(data[1] * d100.rolls)

# Part two.
print(max(dirac(player_1_start, player_2_start)))
