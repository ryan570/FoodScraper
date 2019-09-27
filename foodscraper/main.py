import datetime

from cache import append_data, read_data
from scraper import check_menu, get_protein

def fetch_protein(hall):
    food = check_menu(hall)
    cache = read_data('protein.json')

    for timeslot in food:
        for element in food[timeslot]:
            if element in cache:
                food[timeslot][element] = cache[element]

    return food

def update_cache():
    data = get_protein("Chase")
    data.update(get_protein("Lenoir"))
    append_data(data)

if __name__ == '__main__':
    #update_cache()
    #fetch_protein("Chase")
    pass