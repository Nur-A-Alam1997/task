from YN import db

class Items():
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    food_name = db.Column(db.TEXT)
    available = db.Column(db.TEXT)
    price = db.Column(db.TEXT)

    def __init__(self, name, age):
        self.food_name = food_name
        self.available = available
        self.price = price