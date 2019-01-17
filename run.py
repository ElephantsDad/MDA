from flask import Flask
from flask import session, redirect, url_for, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO
from flask_migrate import Migrate
from forms import LoginForm, SendMessageForm
from flask_socketio import SocketIO, emit, join_room, leave_room
from datetime import datetime

app = Flask(__name__)

app.debug = True
app.config['SECRET_KEY'] = 'gjr39dkjn344_!67#'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

socketio = SocketIO(app)
db = SQLAlchemy(app)
migrate = Migrate(app,db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), nullable=False)
    session_id = db.Column(db.String(200), nullable=False)
    isready = db.Column(db.Boolean, default='False')
    room = db.relationship('Rooms', backref='spy')
    def __repr__(self):
        return f"User('{self.username}')"

class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), nullable=False)
    image_file = db.Column(db.String(20))
    rooms = db.relationship('Rooms', backref='place')
    def __repr__(self):
        return f"Location('{self.name}', '{self.image_file}')"

chats = db.Table('chats',
    db.Column('room_id', db.Integer, db.ForeignKey('rooms.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
    )

class Rooms(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    s_id = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'))
    spy_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    players = db.relationship('User', secondary=chats, backref=db.backref('chatroom'))

    def __repr__(self):
        return f"Rooms('{self.location}', '{self.spy}')"


@app.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['room'] = form.room.data
        return redirect(url_for('.game'))
    elif request.method == 'GET':
        form.name.data = session.get('name', '')
        form.room.data = session.get('room', '')
    return render_template('index.html', form=form)

@app.route('/rules')
def rules():
    return render_template('rules.html', title="Правила игры")

@app.route('/locations')
def locations():
    return render_template('locations.html', title="Локации")

@app.route('/about')
def about():
    return render_template('about.html', title="О разработчиках")

@app.route('/game')
def game():
    """Chat room. The user's name and room must be stored in
    the session."""
    form = SendMessageForm()
    name = session.get('name', '')
    room = session.get('room', '')
    if name == '' or room == '':
        return redirect(url_for('.index'))
    return render_template('game.html', name=name, form=form, room=room, title="Игра", current_user='шпион')

@socketio.on('joined', namespace='/game')
def joined(message):
    """Sent by clients when they enter a room.
    A status message is broadcast to all people in the room."""
    room = session.get('room')
    join_room(room)
    emit('status', {'msg': session.get('name') + ' присоединился/ась к игре ' + session.get('room')}, room=room)

@socketio.on('text', namespace='/game')
def text(message):
    """Sent by a client when the user entered a new message.
    The message is sent to all people in the room."""
    room = session.get('room')
    emit('message', {'msg': session.get('name') + ': ' + message['msg']}, room=room)

@socketio.on('left', namespace='/game')
def left(message):
    """Sent by clients when they leave a room.
    A status message is broadcast to all people in the room."""
    room = session.get('room')
    leave_room(room)
    emit('status', {'msg': session.get('name') + ' покинул/а чат.'}, room=room)


if __name__ == '__main__':
    socketio.run(app)
