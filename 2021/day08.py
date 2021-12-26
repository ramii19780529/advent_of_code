# Day 8: Seven Segment Search
# https://adventofcode.com/2021/day/8


# My original approach was to identify the digits that have unique
# segments, then compare segments to narrow down the other digits.
# That approach worked, but I heard about a different technique from
# a crypto developer. In this approach, I calculate the frequency of
# all digit segments in the correct display. Each digit is then
# assigned a number by summing the frequencies of each segment used
# in that digit. This same process can be used to generate numbers for
# the scrambled digit segments from the puzzle and used as a key into
# the one calculated using the correct display.


def get_frequencies(digits):
  # This returns a dict containing the count
  # of each segment across all digits.
  frequencies = {}
  for digit in digits:
    for segment in digit:
      frequencies[segment] = frequencies.get(segment, 0) + 1
  return frequencies


def sum_segments(digit, frequencies):
  # This returns the sum of segment frequencies in the provided digit.
  return sum(frequencies[segment] for segment in digit)


# Parse the puzzle input file.
with open("2021\day08.txt") as puzzle_input:
  signals = [
    [digits.strip().split(" ")
    for digits in signal.split("|")]
    for signal in puzzle_input.read().splitlines()
  ]

# This dict holds the correct digit for each group of segments.
display_digits = {
  'abcefg':0, 'cf':1, 'acdeg':2, 'acdfg':3, 'bcdf':4,
  'abdfg':5, 'abdefg':6, 'acf':7, 'abcdefg':8, 'abcdfg':9
}

# Create the decoder using the segment frequency by summing
# the segment frequency for all segments within each digit.
display_frequencies = get_frequencies(display_digits)
decoder = {
  sum_segments(digit, display_frequencies): display_digits[digit]
  for digit in display_digits
}

# Parts one and two.
part_one = 0
part_two = 0
for signal_digits, digits in signals:
  signal_frequencies = get_frequencies(signal_digits)
  display_number = 0
  for exp, digit in enumerate(digits):
    display_digit = decoder[sum_segments(digit, signal_frequencies)]
    if display_digit in [1, 4, 7, 8]: part_one += 1
    display_number += display_digit * 10 ** (3 - exp)
  part_two += display_number
print(part_one)
print(part_two)
