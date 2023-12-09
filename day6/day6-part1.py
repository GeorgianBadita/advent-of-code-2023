import math


def read_input(file):
    with open(file, "r") as f:
        lines = f.readlines()
        times = [
            int(x.strip())
            for x in list(
                filter(lambda x: x.strip(), lines[0].split(":")[1].split(" "))
            )
        ]
        distances = [
            int(x.strip())
            for x in list(
                filter(lambda x: x.strip(), lines[1].split(":")[1].split(" "))
            )
        ]

        return [(times[idx], distances[idx]) for idx in range(len(times))]


def solve_one(time, distance):
    # Inequality is in the form x^2 - time*x + distance < 0
    delta = time * time - 4 * distance

    if delta <= 0:
        return 0

    x1 = (time + math.sqrt(delta)) / 2
    x2 = (time - math.sqrt(delta)) / 2

    x2 = max(x2, 0)
    x1 = min(x1, time)

    if math.floor(x1) != x1:
        x1 = math.floor(x1)
    else:
        x1 = int(x1) - 1

    if math.ceil(x2) != x2:
        x2 = math.ceil(x2)
    else:
        x2 = int(x2) + 1

    return x1 - x2 + 1


def solve(races_setup):
    res = 1
    for time, distance in races_setup:
        res *= solve_one(time, distance)
    return res


path = "/Users/marin-georgianbadita/Programming/advent-of-code-2023/day6/in-day6.txt"

races_setup = read_input(path)

print(solve(races_setup))
