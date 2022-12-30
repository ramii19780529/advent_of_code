# Day 20: Grove Positioning System
# https://adventofcode.com/2022/day/20


def decrypt(encrypted_grove_coordinates, mixes, decryption_key):
    decrypted_grove_coordinates = [
        (number * decryption_key, index)
        for index, number in enumerate(encrypted_grove_coordinates)
    ]
    mixer = decrypted_grove_coordinates[:]
    for _ in range(mixes):
        # print([mix[0] for mix in mixer])
        for mix in decrypted_grove_coordinates:
            if mix[0] == 0:
                continue
            mixer.pop(index := mixer.index(mix))
            mixer.insert((index + mix[0]) % len(mixer), mix)
    return [mix[0] for mix in mixer]


def score(data: list):
    index = data.index(0)
    print(sum(data[(index + offset) % len(data)] for offset in [1000, 2000, 3000]))


with open("2022\\day20.txt") as puzzle_input:
    encrypted_grove_coordinates = tuple(map(int, puzzle_input))
    score(decrypt(encrypted_grove_coordinates, 1, 1))
    score(decrypt(encrypted_grove_coordinates, 10, 811589153))
