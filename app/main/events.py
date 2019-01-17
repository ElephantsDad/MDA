from flask import session
from flask_socketio import emit, join_room, leave_room
from .. import socketio
#from app import RLOC_IMG, RLOC_NAME

@socketio.on('joined', namespace='/game')
def joined(message):
    """Sent by clients when they enter a room.
    A status message is broadcast to all people in the room."""
    room = session.get('room')
    #rloc_img = RLOC_IMG
    #rloc_name = RLOC_NAME
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
