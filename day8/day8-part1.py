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


def solve(pattern, graph):
    node = "AAA"
    pat_idx = 0
    steps = 0
    while node != "ZZZ":
        steps += 1
        direction = pattern[pat_idx]

        if direction == "L":
            node = graph[node][0]
        else:
            node = graph[node][1]
        pat_idx = (pat_idx + 1) % len(pattern)

    return steps


file_path = "./in-day8.txt"
pattern, graph = read_file(file_path)

print(solve(pattern, graph))
