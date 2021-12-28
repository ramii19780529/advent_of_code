# Day 3: Binary Diagnostic
# https://adventofcode.com/2021/day/3


def sum_bits(data, bit):
  # Count how many ones and zeros are
  # in the location specified by bit.
  ones, zeros = 0, 0
  for binary_number in data:
    ones += binary_number[bit] == "1"
    zeros += binary_number[bit] == "0"
  return ones, zeros


def most(data, bit):
  # Return the most common bit in the data in
  # the location specified by the bit variable.
  ones, zeros = sum_bits(data, bit)
  return "01"[ones >= zeros]


def least(data, bit):
  # Return the least common bit in the data in
  # the location specified by the bit variable.
  ones, zeros = sum_bits(data, bit, )
  return "10"[ones >= zeros]


def common_bits(data, bit_function, bits):
  # Used for part one to find the least / most common bit for each
  # position in the list of 12 digit binary numbers. The "bit_function"
  # accepts the functions "least" or "most".
  return "".join([bit_function(data, bit) for bit in range(bits)])


def filter_bits(data, bit_function, bits):
  # Filtering the list while recounting was hard. I had to rework my
  # first solution to break out the most / least function by bit.
  for bit in range(bits):
    # This keeps rebuilding data with the remaining binary numbers
    # that match the most / least bit until only one remains.
    data = [
      binary_number
      for binary_number in data
      if binary_number[bit] == bit_function(data, bit)
    ] or data
  return data[0]


# Parse the puzzle input file.
with open("2021\\day03.txt") as puzzle_input:
  diagnostic_report = puzzle_input.read().splitlines()

# Part one.
gamma_rate = common_bits(diagnostic_report, most, 12)
epsilon_rate = common_bits(diagnostic_report, least, 12)
power_consumption = int(gamma_rate, 2) * int(epsilon_rate, 2)
print(power_consumption)

# Part two.
oxygen_generator_rating = filter_bits(diagnostic_report, most, 12)
co2_scrubber_rating = filter_bits(diagnostic_report, least, 12)
life_support_rating = (
    int(oxygen_generator_rating, 2)
  * int(co2_scrubber_rating, 2)
)
print(life_support_rating)
