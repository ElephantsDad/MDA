from flask import render_template, url_for, flash, redirect, jsonify, request
from spyfall import app, db
from spyfall.forms import SubmitForm, SendMessageForm
from spyfall.models import User, Location
import pusher

pusher_client = pusher.Pusher(
  app_id='675900',
  key='1b9338044af70a030649',
  secret='3d85c8e41b8ac08481fd',
  cluster='ap3',
  ssl=True
)

@app.route("/", methods=['GET', 'POST'])
def home():
    form = SubmitForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        db.session.add(user)
        db.session.commit()
        return game()
        #pusher_client.trigger('my-channel', 'my-event', {'message': 'hello world'})
        #return render_template('home.html', form=form) #потом поменять на return game()
    else:
        #pusher_client.trigger('my-channel', 'my-event', {u'message': u'why'})
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

@app.route("/message", methods=['GET', 'POST'])
def message():
    try:
        username = request.form.get('username')
        message = request.form.get('message')
        pusher_client.trigger('chat-channel', 'new-message', {'username' : username, 'message' : message})
        return jsonify({'result' : 'success'})
    except:
        return jsonify({'result' : 'failure'})

@app.route("/game", methods=['GET', 'POST'])
def game():
    form = SendMessageForm()
    users = User.query.limit(7).all()
    current_user = User.query.order_by('-id').first()
    #pusher_client.trigger('my-channel', 'my-event', {u'message': u'why'})
    return render_template('game.html', title="Игра", users=users, current_user=current_user, form=form)
