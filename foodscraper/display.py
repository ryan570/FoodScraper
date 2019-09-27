from flask import Blueprint, render_template

from item import Item
from scraper import check_menu, get_protein
from cache import write_data, read_data

display = Blueprint('display', __name__, template_folder='templates')

chase = get_protein("chase")
write_data(chase, 'chase.json')
lenoir = get_protein("lenoir")
write_data(lenoir, 'lenoir.json')
#chase = read_data('chase.json')

@display.route('/')
def home():
    return render_template('home.html')

@display.route('/<string:hall>')
def hall(hall):
    data = chase

    menu = {}
    timeslots = []

    for timeslot in data:
        timeslots.append(timeslot)
        food = []
        for item in data[timeslot]:
            food.append(Item(item, data[timeslot][item]))
        menu[timeslot] = food

    first = timeslots.pop(0)
    timeslots.reverse()
    timeslots.insert(0, first)

    return render_template('display.html', food=menu, timeslots=timeslots)
