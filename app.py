import os
from flask import Flask
from extensions import db
from dotenv import load_dotenv



load_dotenv()


app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql+psycopg2://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_HOST")}:{os.getenv("DB_PORT")}/{os.getenv("DB_NAME")}"

db.init_app(app)



with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)