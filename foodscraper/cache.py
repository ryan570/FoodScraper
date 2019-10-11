import json

def write_data(data, file, sort):
    with open (file, 'w') as f:
        json.dump(data, f, indent=4, sort_keys=sort)

def read_data(file):
    with open(file) as f:
        current = json.load(f)
    return current

def append_data(new_data):
    current_data = read_data('cache.json')

    for item in new_data:
        current_data[item] = new_data[item]

    write_data(current_data, 'cache.json', True)