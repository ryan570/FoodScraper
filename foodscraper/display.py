from flask import Blueprint, render_template

from item import Item
#from scraper import check_menu, get_protein
from cache import write_data, read_data

display = Blueprint('display', __name__, template_folder='templates')

#chase = get_protein("chase")
#write_data(chase, 'menu.json')
chase = read_data('menu.json')

@display.route('/')
def home():
    return render_template('home.html')

@display.route('/<string:hall>')
def hall(hall):
    data = chase

    food = []

    for timeslot in data:
        for item in data[timeslot]:
            food.append(Item(item, data[timeslot][item]))

    return render_template('display.html', food=food)
