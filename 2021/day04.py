# Day 4: Giant Squid
# https://adventofcode.com/2021/day/4


def board_won(board, draws):
  # Check each row. If all the numbers in any row have
  # been drawn, then this board has won (return True).
  for row in board:
    if all(number in draws for number in row):
      return True
  # Check each column. If all the numbers in any column have
  # been drawn, then this board has won (return True).
  for i in range(5):
    if all(row[i] in draws for row in board):
      return True
  return False


def get_score(board, draws):
  # Calculate the score of a winning
  # board using the specified rules.
  score = 0
  for row in board:
    for number in row:
      if number not in draws:
        score += number
  return score * draws[-1]


# Parse the puzzle input file.
with open("2021\\day04.txt") as puzzle_input:
  draws, *boards = puzzle_input.read().split("\n\n")
  draws = list(map(int, draws.strip().split(",")))
  boards = set(
    tuple(
      tuple(map(int, number.split()))
      for number in row.splitlines()
    )
    for row in boards
  )

# Parts one and two.
won = set()
for draw in range(4, len(draws)):
  # The trick here is to create a new set each iteration using set
  # subtraction to prevent the set size from changing during iterations.
  for board in boards - won:
    if board_won(board, draws[:draw]):
      won.add(board)
      if len(won) in [1, len(boards)]:
        print(get_score(board, draws[:draw]))
      continue
