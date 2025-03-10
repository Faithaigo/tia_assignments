import os
from flask import Flask
from flask_login import LoginManager
from utils import db, bcrypt
from auth.models import User
from auth.auth_blueprint import auth_blueprint
from posts.posts_blueprint import posts_blueprint



app = Flask(__name__)
app.register_blueprint(auth_blueprint)
app.register_blueprint(posts_blueprint)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config["SECRET_KEY"] = os.getenv("CSRF_KEY")


db.init_app(app)

bcrypt.init_app(app)

login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)