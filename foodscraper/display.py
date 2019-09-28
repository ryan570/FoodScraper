import jsonpickle
from flask import Blueprint, render_template

from cache import read_items, write_items
from item import Item
from scraper import check_menu, fetch_nutrition

display = Blueprint('display', __name__, template_folder='templates')

lenoir = read_items('lenoir.json')
chase = read_items('chase.json')

def update():
    lenoir = fetch_nutrition("lenoir")
    chase = fetch_nutrition("chase")

    #write_items(lenoir, 'lenoir.json')
    #write_items(chase, 'chase.json')

@display.route('/')
def home():
    return render_template('home.html')

@display.route('/<string:hall>')
def hall(hall):
    data = chase if hall == "chase" else lenoir

    timeslots = []

    for timeslot in data:
        timeslots.append(timeslot)

    return render_template('display.html', food=data, timeslots=timeslots)