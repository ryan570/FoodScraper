from flask import Blueprint, render_template

from foodscraper.scraper import fetch_nutrition

display = Blueprint('display', __name__, template_folder='templates')

chase = fetch_nutrition("chase")
lenoir = fetch_nutrition("lenoir")

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