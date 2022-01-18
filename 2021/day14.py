# Day 14: Extended Polymerization
# https://adventofcode.com/2021/day/14


def optimize_polymer(pairs, rules):
    # Return new pairs by splitting each pair in the existing pairs and
    # combining the letters with the new element from the rules in the
    # correct order, adding the original pairs total count to the new
    # pairs' count.
    new_pairs = {}
    for pair, count in pairs.items():
        for new_pair in [pair[0] + rules[pair], rules[pair] + pair[1]]:
            new_pairs[new_pair] = new_pairs.get(new_pair, 0) + count
    return new_pairs


def the_answer(pairs):
    # First, we get count of all elements in the pairs. We can only count
    # the second letter in each pair since the first letter is always a
    # duplicate of the second letter in the prior part. The one excpetion
    # to this, is the first pair. Since it has no prior pair, both letters
    # must be counted. Then we apply the rules for the answer by returning
    # the difference between the element with the highest count and the
    # element with the lowest count.
    elements = {}
    for i, pair in enumerate(pairs):
        if i == 0:
            elements[pair[0]] = pairs[pair]
        elements[pair[1]] = elements.get(pair[1], 0) + pairs[pair]
    return max(elements.values()) - min(elements.values())


# Parse the puzzle input file.
with open("2021\\day14.txt") as puzzle_input:
    polymer_template, pair_insertion_rules = puzzle_input.read().split("\n\n")
    pair_insertion_rules = {
        pair_insertion.split(" -> ")[0]: pair_insertion.split(" -> ")[1]
        for pair_insertion in pair_insertion_rules.splitlines()
    }

# Create an dict that holds a count of all unique pairs in the polymer
# template indexed by the pair. This will be used to track the pairs
# created in each step. Since the question doesn't ask for the full
# polymer string, we don't need to keep track of that.
polymer_pairs = {
    pair: polymer_template.count(pair)
    for pair in [polymer_template[i : i + 2] for i in range(len(polymer_template) - 1)]
}

# Parts one and two.
for i in range(40):
    polymer_pairs = optimize_polymer(polymer_pairs, pair_insertion_rules)
    if i in (9, 39):
        print(the_answer(polymer_pairs))
