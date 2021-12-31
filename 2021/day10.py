# Day 10: Syntax Scoring
# https://adventofcode.com/2021/day/10


# Parse the puzzle input file.
with open("2021\\day10.txt") as puzzle_input:
  navigation_subsystem = [line.strip() for line in puzzle_input]

# Set up two lists containing the open chunk
# characters and the close chunk charaters.
open_chunk = ["(", "[", "{", "<"]
close_chunk = [")", "]", "}", ">"]

# Initialize the variables that will hold the answers.
part_one, part_two = 0, []

# For each line, I look at each character in order. If the characters is
# an open chuck character, I add it's matching close chunk character to
# the end of the close_characters list which will be used as a LIFO
# buffer. If the character is not an open chunk characters, I check to
# see if it is a close chunk character that matches the last character
# in the close_caraters list. If is a close chunk character, but it is
# not a match, then we have a corrupted line, so we add to the score of
# part one and clear the list. If a line is not corrupted and the
# close_character list is not empty, then we have an incomplete line, so
# we calculate the score for part two.
for chunks in navigation_subsystem:
    close_characters, score = [], 0
    for character in chunks:
        if character in open_chunk:
            close_characters.append(close_chunk[open_chunk.index(character)])
        elif character in close_chunk:
            if close_characters:
              if not character == close_characters.pop():
                part_one += [3, 57, 1197, 25137][close_chunk.index(character)]
                close_characters = []
                break
    for character in reversed(close_characters):
        score = score * 5 + close_chunk.index(character) + 1
    if close_characters: part_two.append(score)

# Part one.
print(part_one)

# Part two.
print(sorted(part_two)[(len(part_two) - 1) // 2])
