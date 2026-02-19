from flask import Flask, render_template
from menu_data import MENU_CATEGORIES

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/menu')
def menu():
    return render_template('menu.html', categories=MENU_CATEGORIES)


@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


@app.route('/reviews')
def reviews():
    return render_template('reviews.html')


if __name__ == '__main__':
    app.run(debug=True)
