pos_moves = {
    ("|", (1, 0)): (1, 0),
    ("|", (-1, 0)): (-1, 0),
    ("-", (0, -1)): (0, -1),
    ("-", (0, 1)): (0, 1),
    ("F", (-1, 0)): (0, 1),
    ("F", (0, -1)): (1, 0),
    ("7", (0, 1)): (1, 0),
    ("7", (-1, 0)): (0, -1),
    ("L", (1, 0)): (0, 1),
    ("L", (0, -1)): (-1, 0),
    ("J", (1, 0)): (0, -1),
    ("J", (0, 1)): (-1, 0),
}


def read_file(file_path):
    with open(file_path, "r") as f:
        lines = [list(line.strip()) for line in f.readlines()]
        for row in range(len(lines)):
            for col in range(len(lines[0])):
                if lines[row][col] == "S":
                    return (row, col, lines)

    raise ValueError("No S found in input")


def valid_coords(row, col, matrix):
    return row >= 0 and row < len(matrix) and col >= 0 and col < len(matrix[0])


def determine_s_pipe(s_row, s_col, matrix):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for d in range(len(dx)):
        allowed_vals = []
        for mv in pos_moves.keys():
            if mv[1] == (dx[d], dy[d]):
                allowed_vals.append(mv[0])

        new_row = s_row + dx[d]
        new_col = s_col + dy[d]

        if (
            valid_coords(new_row, new_col, matrix)
            and matrix[new_row][new_col] in allowed_vals
        ):
            return "|" if dx[d] else "-", (dx[d], dy[d])


def solve(s_row, s_col, matrix):
    pipe, direction = determine_s_pipe(s_row, s_col, matrix)
    path = []

    new_row, new_col = (s_row, s_col)
    while not path or path[-1] != (s_row, s_col):
        direction = pos_moves[pipe, direction]
        new_row, new_col = new_row + direction[0], new_col + direction[1]

        pipe = matrix[new_row][new_col]
        path.append((new_row, new_col))

    path.pop()
    path = [(s_row, s_col)] + path
    return len(path) // 2


file_path = "./in-day10.txt"

s_row, s_col, matrix = read_file(file_path)

print(solve(s_row, s_col, matrix))
