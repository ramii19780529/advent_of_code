# Day 4: The Ideal Stocking Stuffer
# https://adventofcode.com/2015/day/4


import hashlib


# Parse the puzzle input file.
with open("2015\\day04.txt") as puzzle_input:
    secret_key = puzzle_input.read().strip()

# Parts one and two.
# Brute forced this one. I don't know enough about hashing
# algorithms to come up with a mathmetical solution.
part_one, part_two, number = None, None, 0
while True:
    number += 1
    str2hash = secret_key + str(number)
    result = hashlib.md5(str2hash.encode())
    hex_output = result.hexdigest()
    if not part_one and hex_output[:5] == "00000":
        part_one = number
    if not part_two and hex_output[:6] == "000000":
        part_two = number
    if part_one and part_two:
        break
print(part_one)
print(part_two)
