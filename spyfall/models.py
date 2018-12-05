from spyfall import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), nullable=False)
    image_file = db.Column(db.String(20))
    role = db.Column(db.String(20))

    def __repr__(self):
        return f"User('{self.username}', '{self.image_file}')"

class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), nullable=False)
    image_file = db.Column(db.String(20))

    def __repr__(self):
        return f"Location('{self.name}', '{self.image_file}')"
