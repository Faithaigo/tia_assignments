from flask import Blueprint
from flask_login import login_user, logout_user
from auth.models import User
from extensions import db,bcrypt
from flask_restful import Resource, reqparse, Api

auth_blueprint = Blueprint('auth', __name__, url_prefix="/auth")

api = Api(auth_blueprint)

parser = reqparse.RequestParser()

parser.add_argument('full_name', type=str)
parser.add_argument('email', type=str)
parser.add_argument('password', type=str)

class RegisterUser(Resource):
    def post(self):
        args = parser.parse_args()
        hashed_password = bcrypt.generate_password_hash(args['password']).decode('utf-8')
        new_user = User(full_name=args['full_name'], email=args['email'], password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return {"message":"User registered successfully"}, 201

class Login(Resource):
    def post(self):
        args = parser.parse_args()
        user = User.query.filter_by(email=args['email']).first()
        is_password = bcrypt.check_password_hash(user.password, args['password'])
        if user and is_password:
            login_user(user)
            return {"message":"Logged in successfully"}, 200
        else:
            return {"message":"Wrong username or password"}, 401

class Logout(Resource):
    def post(self):
        logout_user()
        return {"message":"User logged out successfully"}, 200

api.add_resource(RegisterUser, '/register')
api.add_resource(Login,'/login')
api.add_resource(Logout,'/logout')
