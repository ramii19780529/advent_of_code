# Day 2: Rock Paper Scissors
# https://adventofcode.com/2022/day/2

# Parse the puzzle input file.
with open("advent_of_code\\2022\\day02.txt") as puzzle_input:
    esg = [[ord(r[0]) - 64, ord(r[2]) - 87] for r in puzzle_input.readlines()]
    print(sum((p2 - p1 + 1) % 3 * 3 + p2 for p1, p2 in esg))
    print(sum((p2 + p1) % 3 + 1 + (p2 - 1) * 3 for p1, p2 in esg))

# Notes:
# A, B, C in ASCII is 65, 66, and 67 (Subtracting 64 gives us 1, 2, and 3)
# X, Y, Z in ASCII is 88, 89, and 90 (Subtracting 87 gives us 1, 2, and 3)
# In Rock Paper Scissors, the item directly to the right always wins.

# Part 1:

#  A (1), X (1) = Tie (3 points, plus 1 for X)
#  B (2), Y (2) = Tie (3 points, plus 2 for Y)
#  C (3), Z (3) = Tie (3 points, plus 3 for Z)
#  A (1), Y (2) = Win (6 points, plus 2 for Y)
#  B (2), Z (3) = Win (6 points, plus 3 for Z)
#  C (3), X (1) = Win (6 points, plus 1 for X)
#  A (1), Z (3) = Lose (0 points, plus 3 for Z)
#  B (2), X (1) = Lose (0 points, plus 1 for X)
#  C (3), Y (2) = Lose (0 points, plus 2 for Y)

# The Tie / Win / Lose points are multiples of 3, so if we can come up with a way to get
# 1 for Ties, 2 for Wins and 0 for Losses we can just multiply that by 3.

# Looking for a result of 1 for Ties, we know that Tied rounds have to be the same (1v1,
# 2v2, 3v3) etc.. So, we can take the difference between the two hands (always zero) and
# just add 1 to always get a 1 for Ties.
# Cases: 1v1, 2v2, 3v3
# Solution: (p2 - p1 + 1) * 3

# Looking for a result of 2 for Wins, we know that player two wins if they play the next
# item in the list. For example, if player one plays Paper (2) player two must play
# Scissors (3). So if we subtract player one's item from player two's item, and add 1,
# we will always get 2 if we Win, which is what we need.
# We run into an edge case here; what if player one plays Scissors (3)? Player two must
# play Rock (1) to win. Our goal is still a result of 2, but Rock (1) minus Scissors (3)
# plus 1 is -1.  I like the modulo operation for these types of things becasue -1 % 3 is
# 2, which is what we need for a Win. I verified the new solution still works with Ties.
# Cases: 1v2, 2v3, 3v1
# Solution: (p2 - p1 + 1) % 3 * 3

# The last case is for Losses, where player two plays the prior item in the list. For
# example, if player one plays Paper (2) player two must play Rock (1). Our goal for
# this is to get 0, and Rock (1) minus Paper (2) plus 1 is 0, perfect!
# We can hit an edge case here as well. If player one plays Rock (1), player two must
# play Scissors (3), and Scissors (3) minus Rock (1) plus 1 is 3... modulo saves the
# day again since 3 % 3 is 0.
# Cases: 1v3, 2v1, 3v2
# Solution: (p2 - p1 + 1) % 3 * 3

# Finally, we just add the value of the hand player two played to get a final score.
# Solution (p2 - p1 + 1) % 3 * 3 + p2

# Part 2: I basically followed the same procedure using the part 2 rules.

# About the Python functions... .readlines() returns a list containing one line from the
# file per element in the list and we cycle over that list using the variable r in the
# inline for loop. The for loop passed each element in the list to the function to the
# left. This can get confusing as is commonly known as "golf", which is not recommended
# for production code, but is used by programmers trying to do more work with less code.
# I use the index of 0 and 2 from the line in r to get the ABCs and XYZs then use ORD to
# convert them to ASCII and subtract as described in my notes above. Using the square
# brackets returns a list, so esg ends up being a list of list. Each list item contains
# a list of two values, which are players hands (values 1, 2, or 3). To solve for part 1
# and part 2 I pull both player one and player two hands out of the array into p1 and p2
# which are used in the solution above to create a new list containing the points for
# each game, then I use SUM to sub all the values in the new list.
