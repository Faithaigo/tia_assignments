import os
from flask import Flask, jsonify
from flask_login import LoginManager
from extensions import db, bcrypt
from dotenv import load_dotenv
from auth.auth_blueprint import auth_blueprint
from auth.models import User
from posts.posts_blueprint import posts_blueprint



load_dotenv()


app = Flask(__name__)

app.secret_key = os.getenv("LOGIN_SECRET_KEY")

app.register_blueprint(auth_blueprint)
app.register_blueprint(posts_blueprint)

app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql+psycopg2://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_HOST")}:{os.getenv("DB_PORT")}/{os.getenv("DB_NAME")}"

db.init_app(app)

bcrypt.init_app(app)

login_manager = LoginManager()

login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(message=str(e), status=404), 404

@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify(message=str(e), status=405), 405

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)