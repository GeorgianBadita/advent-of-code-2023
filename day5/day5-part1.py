def get_num_list_from_string(string, to_split_by, split_parts=False):
    lst = []
    split = string.split(to_split_by)
    for num in split:
        if not num:
            continue
        if not split_parts:
            lst.append(int(num.strip()))
        else:
            for n in num.split(" "):
                if n:
                    lst.append(int(n.strip()))
    return lst


def read_file(path):
    seeds = []
    seed_to_soil = []
    soil_to_fertilizer = []
    fertilizer_to_water = []
    water_to_light = []
    light_to_temperature = []
    temperature_to_humidity = []
    humidity_to_location = []

    with open(path, "r") as f:
        lines = f.readlines()
        idx = 0
        while idx < len(lines):
            curr_line = lines[idx].strip()
            if not curr_line:
                idx += 1
                continue

            if curr_line.startswith("seeds:"):
                seeds.extend(get_num_list_from_string(curr_line, "seeds:", True))
                idx += 1
                continue

            if curr_line.startswith("seed-to-soil map:"):
                idx += 1
                while idx < len(lines) and lines[idx].strip():
                    curr_line = lines[idx]
                    seed_to_soil.append(get_num_list_from_string(curr_line, " "))
                    idx += 1
                continue

            if curr_line.startswith("soil-to-fertilizer map:"):
                idx += 1
                while idx < len(lines) and lines[idx].strip():
                    curr_line = lines[idx]
                    soil_to_fertilizer.append(get_num_list_from_string(curr_line, " "))
                    idx += 1
                continue

            if curr_line.startswith("fertilizer-to-water map:"):
                idx += 1
                while idx < len(lines) and lines[idx].strip():
                    curr_line = lines[idx]
                    fertilizer_to_water.append(get_num_list_from_string(curr_line, " "))
                    idx += 1
                continue

            if curr_line.startswith("water-to-light map:"):
                idx += 1
                while idx < len(lines) and lines[idx].strip():
                    curr_line = lines[idx]
                    water_to_light.append(get_num_list_from_string(curr_line, " "))
                    idx += 1
                continue

            if curr_line.startswith("light-to-temperature map:"):
                idx += 1
                while idx < len(lines) and lines[idx].strip():
                    curr_line = lines[idx]
                    light_to_temperature.append(
                        get_num_list_from_string(curr_line, " ")
                    )
                    idx += 1
                continue

            if curr_line.startswith("temperature-to-humidity map:"):
                idx += 1
                while idx < len(lines) and lines[idx].strip():
                    curr_line = lines[idx]
                    temperature_to_humidity.append(
                        get_num_list_from_string(curr_line, " ")
                    )
                    idx += 1
                continue

            if curr_line.startswith("humidity-to-location map:"):
                idx += 1
                while idx < len(lines) and lines[idx].strip():
                    curr_line = lines[idx]
                    humidity_to_location.append(
                        get_num_list_from_string(curr_line, " ")
                    )
                    idx += 1
                continue

            idx += 1

    return (
        seeds,
        seed_to_soil,
        soil_to_fertilizer,
        fertilizer_to_water,
        water_to_light,
        light_to_temperature,
        temperature_to_humidity,
        humidity_to_location,
    )


def one_transition(source, transition):
    destination_category, source_category, rng = transition
    if source_category <= source <= source_category + rng:
        return destination_category + source - source_category, True
    return source, False


def map_seed_to_location(start, maps):
    for curr_map in maps:
        for transition in curr_map:
            next_val, mapped = one_transition(start, transition)
            if mapped:
                start = next_val
                break
    return start


def solve(seeds, maps):
    return min(list(map(lambda seed: map_seed_to_location(seed, maps), seeds)))


file_path = "./in-day5.txt"

(
    seeds,
    seed_to_soil,
    soil_to_fertilizer,
    fertilizer_to_water,
    water_to_light,
    ligt_to_temperature,
    temperature_to_humidity,
    humidity_to_location,
) = read_file(file_path)

print(
    solve(
        seeds,
        [
            seed_to_soil,
            soil_to_fertilizer,
            fertilizer_to_water,
            water_to_light,
            ligt_to_temperature,
            temperature_to_humidity,
            humidity_to_location,
        ],
    )
)
