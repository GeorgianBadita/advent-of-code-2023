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
                seeds_line = get_num_list_from_string(curr_line, "seeds:", True)
                seeds = [seeds_line[i : i + 2] for i in range(0, len(seeds_line), 2)]
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


def lookup_range(range_start, range_end, maps):
    ans = []
    for start, end, rng in maps:
        if range_start > end or range_end < start:
            continue
        if range_start < start:
            ans += [(range_start, start - 1), (start + rng, min(end, range_end) + rng)]
        else:
            ans += [(range_start + rng, min(end, range_end) + rng)]
        if end > range_end:
            return ans
        range_start = end

    if not ans:
        ans = [(range_start, range_end)]
    return ans


def map_one(seed_range, maps):
    range_ends = [(seed_range[0], seed_range[0] + seed_range[1])]
    for mp in maps:
        ans = []
        for start, end in range_ends:
            ans += lookup_range(start, end, mp)
        range_ends = ans

    return min(range_ends)[0]


def solve(seed_ranges, maps):
    remaps = []
    for mp in maps:
        new_mp = []
        for start, end, rng in mp:
            new_mp.append([end, end + rng - 1, start - end])
        remaps.append(sorted(new_mp))

    return min([map_one(seed_range, remaps) for seed_range in seed_ranges])


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
