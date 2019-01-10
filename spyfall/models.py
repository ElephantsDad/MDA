from spyfall import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), nullable=False)
    def __repr__(self):
        return f"User('{self.username}')"

class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), nullable=False)
    image_file = db.Column(db.String(20))
    def __repr__(self):
        return f"Location('{self.name}', '{self.image_file}')"

class Messages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(15), nullable=False)
    receiver = db.Column(db.String(20), nullable=False)
    time_stamp = db.Column(db.Time, nullable=False)
    text = db.Column(db.String(200), nullable=False)
    effect = db.Column(db.String(50))
    def __repr__(self):
        return f"Location('{self.author}', '{self.receiver}', '{self.time_stamp}', '{self.text}', '{self.effect}')"

class Effects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), nullable=False)
    description = db.Column(db.String(50))
    def __repr__(self):
        return f"Effects('{self.name}', '{self.description}')"

class Room_User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room = db.Column(db.Integer, nullable=False)
    user = db.Column(db.Integer, nullable=False)


class Rooms(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(15), nullable=False)
    spy = db.Column(db.String(20), nullable=False)
    start_time = db.Column(db.Time, nullable=False)
    def __repr__(self):
        return f"Rooms('{self.location}', '{self.spy}')"

class Guess_Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room = db.Column(db.Integer, nullable=False)
    try_left = db.Column(db.Integer, nullable=False)
