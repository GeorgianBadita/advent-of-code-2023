def read_file(path):
    graph = {}
    with open(path, "r") as f:
        lines = f.readlines()
        pattern = lines[0].strip()

        for line in lines[2:]:
            source, dest = line.split(" = ")
            source = source.strip()
            dests = dest.split(", ")
            left_dest = dests[0][1:].strip()
            right_dest = dests[1].strip()
            if right_dest[-1] == ")":
                right_dest = right_dest[:-1]
            graph[source] = [left_dest, right_dest]

    return pattern, graph


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return a * b // gcd(a, b)


def lcm_list(l):
    if len(l) < 2:
        raise ValueError("Cannot compute lcm for list with less than 2 elements")

    if len(l) == 2:
        return lcm(l[0], l[1])

    return lcm(l[0], lcm_list(l[1:]))


def solve_one(pattern, graph, node):
    pat_idx = 0
    steps = 0
    while node[-1] != "Z":
        steps += 1
        direction = pattern[pat_idx]

        if direction == "L":
            node = graph[node][0]
        else:
            node = graph[node][1]
        pat_idx = (pat_idx + 1) % len(pattern)

    return steps


def solve(pattern, graph):
    start_nodes = []

    for node in graph:
        if node[-1] == "A":
            start_nodes.append(node)

    return lcm_list(
        list(map(lambda node: solve_one(pattern, graph, node), start_nodes))
    )


file_path = "./in-day8.txt"
pattern, graph = read_file(file_path)

print(solve(pattern, graph))
