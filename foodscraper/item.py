class Item:
    def __init__(self, name, calories, sodium, protein):
        self.name = name
        self.calories = calories
        self.sodium = sodium
        self.protein = protein

def create_item(name, data):
    return Item(name, data['calories'], data['sodium'], data['protein'])