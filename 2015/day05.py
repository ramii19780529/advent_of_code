# Day 5: Doesn't He Have Intern-Elves For This?
# https://adventofcode.com/2015/day/5


# Parse the puzzle input file.
with open("advent_of_code\\2015\\day05.txt") as puzzle_input:
    strings = puzzle_input.read().splitlines()

# Part one.
naughty_combos = ("ab", "cd", "pq", "xy")
vowels = ("a", "e", "i", "o", "u")
letters = "abcdefghijklmnopqrstuvwxyz"
doubles = tuple(combo[0] + combo[1] for combo in zip(letters, letters))
nice_count = 0
for string in strings:
    nice = True
    vowel_count = 0
    double_count = 0
    if string[0] in vowels:
        vowel_count += 1
    for i in range(len(string) - 1):
        combo = string[i : i + 2]
        if combo in naughty_combos:
            nice = False
        if combo in doubles:
            double_count += 1
        if string[i + 1] in vowels:
            vowel_count += 1
    if vowel_count < 3:
        nice = False
    if double_count == 0:
        nice = False
    if nice:
        nice_count += 1
print(nice_count)

# Part two.
letters = "abcdefghijklmnopqrstuvwxyz"
nice_count = 0
for string in strings:
    a = False
    b = False
    for i in range(14):
        if not a and string[i] == string[i + 2]:
            a = True
        if not b and string[i : i + 2] in string[i + 2 :]:
            b = True
    if a and b:
        nice_count += 1
print(nice_count)
