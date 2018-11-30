#C:\Users\Asus\Projects\Environments\spyfall\Scripts\activate.bat
#cd C:\Users\Asus\MDA
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import SubmitForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '46adde7c15c23ac027ed4ba9d69ee4d2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), nullable=False)
    image_file = db.Column(db.String(20))

    def __repr__(self):
        return f"User('{self.username}', '{self.image_file}')"

class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), nullable=False)
    image_file = db.Column(db.String(20))

    def __repr__(self):
        return f"Location('{self.name}', '{self.image_file}')"

@app.route("/", methods=['GET', 'POST'])
def home():
    form = SubmitForm()
    if form.validate_on_submit():
        return game()
    else:
        return render_template('home.html', form=form)

@app.route("/rules")
def rules():
    return render_template('rules.html', title="Правила игры")

@app.route("/locations")
def locations():
    return render_template('locations.html', title="Локации")

@app.route("/about")
def about():
    return render_template('about.html', title="О разработчиках")

@app.route("/game")
def game():
    users = User.query.all()
    return render_template('game.html', title="Игра", users=users)

if __name__ == '__main__':
    app.run(debug=True)
