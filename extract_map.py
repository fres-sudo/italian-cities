import json

def generate_city_map(json_file, txt_file):
    with open(json_file) as file:
        data = json.load(file)["Foglio1"]

    city_map = {}

    for element in data:
        region = element["regione"]
        province = element["provincia"]
        city = element["comune"]

        if region not in city_map:
            city_map[region] = {}

        if province not in city_map[region]:
            city_map[region][province] = []

        city_map[region][province].append(city)

    with open(txt_file, 'w') as f:
        for region, provinces in city_map.items():
            f.write('"' + region + '": {\n')
            for province, cities in provinces.items():
                f.write('    "' + province + '": [')
                for idx, city in enumerate(cities):
                    f.write('"' + city + '"')
                    if idx != len(cities) - 1:
                        f.write(", ")
                f.write("],\n")
            f.write("},\n")

# JSON file created earlier
json_file = 'regions-provinces-cities.json'
# Text file where the city map will be written
txt_file = 'city_map.txt'

# Generate the city map into the text file
generate_city_map(json_file, txt_file)

print("City map generated successfully in the file:", txt_file)
