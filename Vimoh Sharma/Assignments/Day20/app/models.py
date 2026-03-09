from . import db

class Event(db.Model):

    __tablename__ = "events"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    total_seats = db.Column(db.Integer)
    available_seats = db.Column(db.Integer)


class Registration(db.Model):

    __tablename__ = "registrations"

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100))
    event_id = db.Column(db.Integer, db.ForeignKey("events.id"))


class Order(db.Model):

    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100))
    quantity = db.Column(db.Integer)
    price = db.Column(db.Integer)


class Book(db.Model):

    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    author = db.Column(db.String(100))
    copies = db.Column(db.Integer)