def read_file(path):
    mapping = {}

    with open(path, "r") as f:
        all_lines = f.readlines()

        for line in all_lines:
            game_part, cubes_part = line.split(":")
            game_id = int(game_part.split(" ")[-1].strip())
            rounds = cubes_part.split(";")

            shown_list = []
            for rd in rounds:
                map_for_round = {}
                splits_in_round = rd.strip().split(",")
                for spl in splits_in_round:
                    num_and_color = spl.strip().split(" ")
                    color = num_and_color[-1].strip()
                    num = int(num_and_color[0].strip())

                    map_for_round[color] = num
                shown_list.append(map_for_round)
            mapping[game_id] = shown_list

    return mapping


def solve(mapping):
    res = 0
    for _, game_list in mapping.items():
        max_colors = {}
        for round_ in game_list:
            for color, count in round_.items():
                max_colors[color] = max(max_colors.get(color, 0), count)

        power = 1
        for _, v in max_colors.items():
            power *= v

        res += power

    return res


path = "./in-day2.txt"

mapping = read_file(path)

print(solve(mapping))
