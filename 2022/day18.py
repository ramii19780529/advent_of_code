# Day 18: Boiling Boulders
# https://adventofcode.com/2022/day/18


# Parse the input.
with open("advent_of_code\\2022\\day18.txt") as puzzle_input:
    cubes = {(*map(int, line.split(",")),) for line in puzzle_input.read().splitlines()}

    # This was added for part 2 but I found that the performace was better
    # If I limited the neighors to within the fill since we don't need to
    # look at anything outside the fill. So I moved it up here and updated
    # the neighbors function to use it.
    # Fill in all the locations not used by the droplet with at least one
    # extra location between the edge of the fill and the droplet.
    min_x = min(cube[0] for cube in cubes) - 1
    min_y = min(cube[1] for cube in cubes) - 1
    min_z = min(cube[2] for cube in cubes) - 1
    max_x = max(cube[0] for cube in cubes) + 2
    max_y = max(cube[1] for cube in cubes) + 2
    max_z = max(cube[2] for cube in cubes) + 2
    fill = {
        (x, y, z)
        for x in range(min_x, max_x)
        for y in range(min_y, max_y)
        for z in range(min_z, max_z)
    } - cubes

    def neighbors(x, y, z):
        # Return the locations in the fill that
        # are adjacent to location passed in.
        return {
            (x - 1, y, z),
            (x + 1, y, z),
            (x, y - 1, z),
            (x, y + 1, z),
            (x, y, z - 1),
            (x, y, z + 1),
        } & fill

    # Part 1
    # For each cube we sum the number of sides not touching a another cube.
    print(sum(len(neighbors(*cube) - cubes) for cube in cubes))

    # Part 2
    # Start with a corner of the fill we created to insure we are outsize of the
    # droplet. As long as the droplet doesn't have a hole, we can use DFS to select
    # all connecting locations, creating a shell around the droplet.
    stack = [(min_x, min_y, min_z)]
    shell = set()
    while stack:
        cube = stack.pop()
        shell.add(cube)
        # Explore neighors in the fill that we haven't added to the shell yet.
        stack.extend(neighbors(*cube) - shell)
    # For each cube we sum the number of sides touching the shell.
    print(sum(len(neighbors(*cube) & shell) for cube in cubes))
