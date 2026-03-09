from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import *

db = SQLAlchemy()

def create_app():

    app = Flask(__name__)

    app.config.from_object("config")

    db.init_app(app)

    # Import blueprints AFTER db is created
    from .events.routes import events_bp
    from .orders.routes import orders_bp
    from .library.routes import library_bp

    app.register_blueprint(events_bp)
    app.register_blueprint(orders_bp)
    app.register_blueprint(library_bp)

    with app.app_context():
        db.create_all()

    return app