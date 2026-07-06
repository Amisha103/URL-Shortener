from dotenv import load_dotenv

load_dotenv()

from flask import Flask
from flask_migrate import Migrate

from config import Config
from database import db
from models import URL
from routes import url_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

migrate = Migrate(app, db)

app.register_blueprint(url_bp)

@app.route("/")
def home():
    return "URL Shortener API Running"

if __name__ == "__main__":
    app.run(debug=True)