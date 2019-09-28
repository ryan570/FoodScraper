import json
import jsonpickle

def write_data(data, file):
    with open (file, 'w') as f:
        json.dump(data, f, indent=4)

def read_data(file):
    with open(file) as f:
        current = json.load(f)
    return current

def write_items(data, file):
    json_data = {}
    for timeslot in data:
        current = [jsonpickle.encode(item) for item in data[timeslot]]
        json_data[timeslot] = current
    write_data(json_data, file)

def read_items(file):
    data = {}
    json_data = read_data(file)

    for timeslot in json_data:
        current = [jsonpickle.decode(item) for item in json_data[timeslot]]
        data[timeslot] = current
    
    return data
    
def append_data(new_data):
    current = read_data()
    
    for timeslot in new_data:
        for key in new_data[timeslot]:
            if key not in current:
                current[key] = new_data[timeslot][key]

    write_data(current, 'protein.json')