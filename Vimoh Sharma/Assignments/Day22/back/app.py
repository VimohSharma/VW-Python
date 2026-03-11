

from flask import Flask
from config import Config
from models import db
from routes import task_routes
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(Config)

CORS(app)

db.init_app(app)

app.register_blueprint(task_routes)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)