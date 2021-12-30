# Day 16: Packet Decoder
# https://adventofcode.com/2021/day/16


class HexStringBitReader:
    # I decided to make a class to read the stream of hex characters as
    # ints so tracking the index would be managed in the object instead
    # of manually after each read of the string, and without destroying 
    # the original data.

    def __init__(self, hex_string):
        self.index = 0
        self.bin_data = ""
        for h in hex_string:
            self.bin_data += bin(int(h, 16))[2:].zfill(4)

    def get_int(self, bits):
        self.index += bits
        return int(self.bin_data[self.index - bits : self.index], 2)


def get_header(data):
    return data.get_int(3), data.get_int(3)


def get_sub_packets(data):
    results = []
    length_type = data.get_int(1)
    if length_type == 0:
        length = data.get_int(15) + data.index
        while data.index < length:
            results.append(read_packets(data))
    if length_type == 1:
        length = data.get_int(11)
        while length:
            length -= 1
            results.append(read_packets(data))
    return results


def sub_packet_sum(data):
    return sum(get_sub_packets(data))


def sub_packet_product(data):
    product = 1
    for n in get_sub_packets(data):
        product *= n
    return product


def sub_packet_min(data):
    return min(get_sub_packets(data))


def sub_packet_max(data):
    return max(get_sub_packets(data))


def sub_packet_literal(data):
    number = 0
    while True:
        another_nibble = data.get_int(1)
        nibble = data.get_int(4)
        number = number<<4 | nibble
        if not another_nibble:
            break
    return number


def sub_packet_gt(data):
    results = get_sub_packets(data)
    return results[0] > results[1]


def sub_packet_lt(data):
    results = get_sub_packets(data)
    return results[0] < results[1]


def sub_packet_equal(data):
    results = get_sub_packets(data)
    return results[0] == results[1]


def read_packets(data):
    global versions
    version, type_id = get_header(data)
    versions += version
    if type_id == 0:
        return sub_packet_sum(data)
    elif type_id == 1:
        return sub_packet_product(data)
    elif type_id == 2:
        return sub_packet_min(data)
    elif type_id == 3:
        return sub_packet_max(data)
    elif type_id == 4:
        return sub_packet_literal(data)
    elif type_id == 5:
        return sub_packet_gt(data)
    elif type_id == 6:
        return sub_packet_lt(data)
    elif type_id == 7:
        return sub_packet_equal(data)
    else:
        return 0


# Parse the puzzle input file.
with open("2021\\day16.txt") as puzzle_input:
  bits = HexStringBitReader(puzzle_input.read().strip())

# Parts one and two.
versions = 0
transmission = read_packets(bits)
print(versions)
print(transmission)
