import json

def write_data(data):
    with open ('cache.json', 'w') as f:
        json.dump(data, f, sort_keys=True, indent=4)

def read_data():
    with open('cache.json') as f:
        current = json.load(f)
    return current

def append_data(new_data):
    current = read_data()
    
    for timeslot in new_data:
        for key in new_data[timeslot]:
            if key not in current:
                current[key] = new_data[timeslot][key]

    write_data(current)