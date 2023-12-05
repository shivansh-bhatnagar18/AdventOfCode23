def read_maps(file_path):
    maps = {}
    current_key = None

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()

            if line.startswith('seed-to-soil map'):
                current_key = 'seed-to-soil'
                maps[current_key] = []
            elif line.startswith('soil-to-fertilizer map'):
                current_key = 'soil-to-fertilizer'
                maps[current_key] = []
            elif line.startswith('fertilizer-to-water map'):
                current_key = 'fertilizer-to-water'
                maps[current_key] = []
            elif line.startswith('water-to-light map'):
                current_key = 'water-to-light'
                maps[current_key] = []
            elif line.startswith('light-to-temperature map'):
                current_key = 'light-to-temperature'
                maps[current_key] = []
            elif line.startswith('temperature-to-humidity map'):
                current_key = 'temperature-to-humidity'
                maps[current_key] = []
            elif line.startswith('humidity-to-location map'):
                current_key = 'humidity-to-location'
                maps[current_key] = []
            elif line.startswith('seeds:'):
                seeds = line.split(':')[1].strip().split()
                maps['seeds'] = [int(seed) for seed in seeds]
            elif line:
                if current_key:
                    values = line.split()
                    maps[current_key].append([int(value) for value in values])

    return maps

file_path = '../Data/almanac.txt'
maps_data = read_maps(file_path)
print(maps_data)

def seed_to_soil(seed):
    dataset = maps_data['seed-to-soil']
    for element in dataset:
        if seed >= element[1] and seed <= element[1] + element[2] - 1:
            return element[0] + seed - element[1]
    return seed
def soil_to_fertilizer(seed):
    dataset = maps_data['soil-to-fertilizer']
    for element in dataset:
        if seed >= element[1] and seed <= element[1] + element[2] - 1:
            return element[0] + seed - element[1]
    return seed
def fertilizer_to_water(seed):
    dataset = maps_data['fertilizer-to-water']
    for element in dataset:
        if seed >= element[1] and seed <= element[1] + element[2] - 1:
            return element[0] + seed - element[1]
    return seed
def water_to_light(seed):
    dataset = maps_data['water-to-light']
    for element in dataset:
        if seed >= element[1] and seed <= element[1] + element[2] - 1:
            return element[0] + seed - element[1]
    return seed
def light_to_temperature(seed):
    dataset = maps_data['light-to-temperature']
    for element in dataset:
        if seed >= element[1] and seed <= element[1] + element[2] - 1:
            return element[0] + seed - element[1]
    return seed
def temperature_to_humidity(seed):  
    dataset = maps_data['temperature-to-humidity']
    for element in dataset:
        if seed >= element[1] and seed <= element[1] + element[2] - 1:
            return element[0] + seed - element[1]
    return seed
def humidity_to_location(seed):
    dataset = maps_data['humidity-to-location']
    for element in dataset:
        if seed >= element[1] and seed <= element[1] + element[2] - 1:
            return element[0] + seed - element[1]
    return seed


locations = []
for seed in maps_data['seeds']:
    seed = seed_to_soil(seed)
    seed = soil_to_fertilizer(seed)
    seed = fertilizer_to_water(seed)
    seed = water_to_light(seed)
    seed = light_to_temperature(seed)
    seed = temperature_to_humidity(seed)
    seed = humidity_to_location(seed)
    locations.append(seed)

print(locations)
print(min(locations))