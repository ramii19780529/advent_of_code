# Day 22: Monkey Map
# https://adventofcode.com/2022/day/22

# Part 1 Solved.
# Part 2 Not Solved.

# Parse the input.
with open("2022\\day22.txt") as puzzle_input:
    board, path = puzzle_input.read().split("\n\n")
    board = [list(row) for row in board.splitlines()]
    max_x = max(len(row) for row in board)
    for y in range(len(board)):
        while len(board[y]) < max_x:
            board[y].append(" ")
    player = [0, board[0].index(".")]
    direction = 0
    board[player[0]][player[1]] = [">", "V", "<", "^"][direction]
    moves = "0"
    path += "X"
    for i in path:
        if i in ("RLX"):
            moves = int(moves)
            wrapped = False
            last_tile = player[:]
            while moves:
                y, x = [(0, 1), (1, 0), (0, -1), (-1, 0)][direction]
                next_y = (player[0] + y) % len(board)
                next_x = (player[1] + x) % len(board[next_y])
                next_tile = board[next_y][next_x]
                if next_tile == "#":
                    moves = 0
                    if wrapped:
                        player = last_tile[:]
                else:
                    player[0] = next_y
                    player[1] = next_x
                    if next_tile in ".>V<^":
                        board[player[0]][player[1]] = [">", "V", "<", "^"][direction]
                        moves -= 1
                        wrapped = False
                        last_tile = player[:]
                    elif next_tile == " ":
                        wrapped = True
            if i in "RL":
                direction = (direction + [-1, 1][i == "R"]) % 4
                board[player[0]][player[1]] = [">", "V", "<", "^"][direction]
            moves = "0"
        else:
            moves += i

print(1000 * (player[0] + 1) + 4 * (player[1] + 1) + direction)

# [print("".join(i)) for i in board]
