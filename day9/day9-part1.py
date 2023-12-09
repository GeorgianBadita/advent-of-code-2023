def read_input(path):
    with open(path, "r") as f:
        lines = f.readlines()
        return list(map(lambda line: [int(x.strip()) for x in line.split(" ")], lines))


def extrapolate_one(sequence):
    sequences = [sequence]
    all_equal = False

    while not all_equal:
        all_equal = True
        new_sequence = []
        curr_sequence = sequences[-1]
        for idx in range(1, len(curr_sequence)):
            diff = curr_sequence[idx] - curr_sequence[idx - 1]
            if len(new_sequence) > 0:
                if diff != new_sequence[-1]:
                    all_equal = False

            new_sequence.append(diff)

        sequences.append(new_sequence)

    last_sequence_idx = len(sequences) - 1
    sequences[last_sequence_idx].append(sequences[last_sequence_idx][-1])
    last_sequence_idx -= 1

    while last_sequence_idx >= 0:
        next_sequence = sequences[last_sequence_idx + 1]
        curr_sequence = sequences[last_sequence_idx]
        curr_sequence.append(curr_sequence[-1] + next_sequence[-1])
        last_sequence_idx -= 1

    return sequences[0][-1]


def solve(sequences):
    return sum(list(map(lambda sequence: extrapolate_one(sequence), sequences)))


path = "./in-day9.txt"

sequences = read_input(path)

print(solve(sequences))
