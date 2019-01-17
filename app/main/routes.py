from flask import session, redirect, url_for, render_template, request
from . import main
from .forms import LoginForm, SendMessageForm
from app import RLOC_IMG, RLOC_NAME

Locations = [
        {
            'name': 'Деревня',
            'image': 'location_1.jpg'
        },
        {
            'name': 'Маяк',
            'image': 'location_2.jpg'
        },
        {
            'name': 'Затерянный остров',
            'image': 'location_3.jpg'
        },
        {
            'name': 'Встреча алкоголиков',
            'image': 'location_4.jpg'
        },
        {
            'name': 'Парк аттракционов',
            'image': 'location_5.jpg'
        },
        {
            'name': 'Улица',
            'image': 'location_6.jpg'
        },
        {
            'name': 'Космос',
            'image': 'location_7.jpg'
        },
        {
            'name': 'Гримерка',
            'image': 'location_8.jpg'
        },
        {
            'name': 'Цирк',
            'image': 'location_9.jpg'
        }
]

def RandomLocation():
    import random
    x = random.randint(0,8)
    return(Locations[x])

@main.route('/', methods=['GET', 'POST'])
def index():
    """Home page"""
    form = LoginForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['room'] = form.room.data
        rloc = RandomLocation()
        session['rloc_img'] = rloc['image']
        session['rloc_name'] = rloc['name']
        #RLOC_NAME = rloc['name']
        #RLOC_IMG = rloc['image']
        return redirect(url_for('.game'))
    elif request.method == 'GET':
        form.name.data = session.get('name', '')
        form.room.data = session.get('room', '')
    return render_template('index.html', form=form)


@main.route('/game')
def game():
    """Chat room. The user's name and room must be stored in
    the session."""
    form = SendMessageForm()
    name = session.get('name', '')
    room = session.get('room', '')
    rloc_name = session.get('rloc_name', '')
    rloc_img = session.get('rloc_img', '')
    if name == '' or room == '':
        return redirect(url_for('.index'))
    return render_template('game.html', name=name, form=form, room=room, title="Игра", current_user="нешпион", rloc_name=rloc_name, rloc_img=rloc_img)

@main.route('/rules')
def rules():
    return render_template('rules.html', title="Правила игры")

@main.route('/locations')
def locations():
    return render_template('locations.html', title="Локации")

@main.route('/about')
def about():
    return render_template('about.html', title="О разработчиках")
