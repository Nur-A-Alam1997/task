from YN import app
from YN.items import Items
from flask import request, session, render_template

@app.route('/admin')
def admin():
    # db.session.execute('CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY AUTOINCREMENT, food_name TEXT NOT NULL UNIQUE, available TEXT NOT NULL, price TEXT NOT NULL)')
    return render_template('shop.html')


@app.route("/")
def home():
    return "hello!! welcome to yummy noodles"