# Day 16: Proboscidea Volcanium
# https://adventofcode.com/2022/day/16


def score(route):
    return sum(valves[valve][0] * time for valve, time in route.items())


def routes(valves, time, start="AA", route={}):
    # This returns all combinations of valves that can be reached in "time" starting
    # from valve AA, including the time the valve was reached.
    for valve in valves:
        # Skip the valve if we can't get to it in time.
        if (new_time := (time - distance[start][valve] - 1)) <= 0:
            continue
        yield from routes(
            valves - {valve},
            new_time,
            valve,
            route | {valve: new_time},
        )
    yield route


# Parse the input into a dictionary as {Valve Label: Flow Rate, [Neighboring Valves]}.
with open("advent_of_code\\2022\\day16.txt") as puzzle_input:
    valves = {
        v[1]: [int(v[5]), v[10:]]
        for v in [
            scan.replace(";", "").replace(",", "").replace("=", " ").split()
            for scan in puzzle_input.read().splitlines()
        ]
    }
    # Build a dictionary table of distances using the Floyd-Warshall algorithm.
    distance = {}
    for i in valves:
        distance[i] = {}
        for j in valves:
            if j == i:  # The cost to itself is 0.
                distance[i][j] = 0
            elif j in valves[i][1]:  # The cost to neighbors is 1 second.
                distance[i][j] = 1
            else:  # The cost to anywhere else is infinity (currently unknown).
                distance[i][j] = float("inf")
    for k in valves:
        for i in valves:
            for j in valves:
                if distance[i][j] > (new_distance := (distance[i][k] + distance[k][j])):
                    distance[i][j] = int(new_distance)
    # Only traverse the working valves (perfomance improvement).
    working_valves = {valve for valve in valves if valves[valve][0] > 0}

    # Part 1
    print(max(map(score, routes(working_valves, 30))))

    # Part 2
    max_scores = {}
    # Get all the routes we can cover within 26 seconds.
    for route in routes(working_valves, 26):
        # Get the score for each possible route.
        route_score = score(route)
        # Create a frozen set to insure the valve combinations in the
        # route are unique and immutable so it can be used as a key.
        route_key = frozenset(route)
        # Set the max score of the route to the highest score found.
        if route_score > max_scores.get(route_key, 0):
            max_scores[route_key] = route_score
    # Get the max score from two routes with no intersections.
    print(
        max(
            score_a + score_b
            for route_a, score_a in max_scores.items()
            for route_b, score_b in max_scores.items()
            if not route_a & route_b
        )
    )
