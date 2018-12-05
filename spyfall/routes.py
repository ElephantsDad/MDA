from flask import render_template, url_for, flash, redirect
from spyfall import app, db
from spyfall.forms import SubmitForm
from spyfall.models import User, Location

@app.route("/", methods=['GET', 'POST'])
def home():
    form = SubmitForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        db.session.add(user)
        db.session.commit()
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
    current_user = User.query.order_by('id').first()
    return render_template('game.html', title="Игра", users=users, current_user=current_user)
