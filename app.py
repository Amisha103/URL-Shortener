from flask import Flask
from flask_migrate import Migrate
from dotenv import load_dotenv

from config import Config
from database import db
from models import URL

load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

migrate = Migrate(app, db)

@app.route("/")
def home():
    return "Database Connected Successfully"

if __name__ == "__main__":
    app.run(debug=True)