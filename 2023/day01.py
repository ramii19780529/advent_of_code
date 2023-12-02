# Day 1: Trebuchet?!
# https://adventofcode.com/2023/day/1


# Extract the first and last digit from each line
# in the "newly-improved" calibration document and
# create a new calibration number for each line by
# combining those two digits. Finally sum the new
# calibration numbers and return the answer.
def sum_calibration_values(calibration_doc):
    return sum(
        [
            int(f"{digits[0]}{digits[-1]}")
            for digits in [
                [character for character in line if character.isdigit()]
                for line in calibration_doc
            ]
        ]
    )


# Buils a list of replacement values and was the crux of part two.
# More difficult than usual for day 1. The key is to change all the
# numbers, even when the characters would be replaced by another.
# For example: eighthree can easily be converted incorrectly into
# eigh3 with reduces to 3 but in our case it we need it to becomes
# eight8eighthree3three to reduce it to 83.
swaps = (
    ("one", "one1one"),
    ("two", "two2two"),
    ("three", "three3three"),
    ("four", "four4four"),
    ("five", "five5five"),
    ("six", "six6six"),
    ("seven", "seven7seven"),
    ("eight", "eight8eight"),
    ("nine", "nine9nine"),
)


# Swap the text numbers for real numbers here.
def get_swapped(text):
    for index, line in enumerate(text):
        for old, new in swaps:
            line = new.join(line.split(old))
        text[index] = line
    return text


# Parse the puzzle input file.
with open(r"advent_of_code\2023\day01.txt") as puzzle_input:
    calibration_doc = puzzle_input.read().splitlines()

# Part one.
print(sum_calibration_values(calibration_doc))

# Part two.
print(sum_calibration_values(get_swapped(calibration_doc)))
