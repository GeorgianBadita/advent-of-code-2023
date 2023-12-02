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


def solve(mapping, conditions):
    res = 0
    for game_id, game_list in mapping.items():
        keep = True
        for color_to_check, count in conditions.items():
            if not keep:
                break
            for round_ in game_list:
                if color_to_check in round_ and round_[color_to_check] > count:
                    keep = False
                    break

        if keep:
            res += game_id

    return res


path = "./in-day2.txt"

mapping = read_file(path)

print(solve(mapping, {"red": 12, "green": 13, "blue": 14}))
