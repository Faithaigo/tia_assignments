import os
from flask import Flask
from flask_login import LoginManager
from extensions import db, bcrypt
from dotenv import load_dotenv
from auth.auth_blueprint import auth_blueprint
from auth.models import User



load_dotenv()


app = Flask(__name__)

app.secret_key = os.getenv("LOGIN_SECRET_KEY")

app.register_blueprint(auth_blueprint)



app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql+psycopg2://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_HOST")}:{os.getenv("DB_PORT")}/{os.getenv("DB_NAME")}"

db.init_app(app)

bcrypt.init_app(app)

login_manager = LoginManager()

login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)