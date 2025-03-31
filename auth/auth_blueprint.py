import logging
from flask import Blueprint,jsonify
from flask_login import login_user, logout_user
from auth.models import User
from extensions import db,bcrypt
from flask_restful import Resource, reqparse, Api
from customErrors import InvalidAPIUsage


logger = logging.getLogger(__name__)
auth_blueprint = Blueprint('auth', __name__, url_prefix="/auth")

api = Api(auth_blueprint)

parser = reqparse.RequestParser()

parser.add_argument('full_name', type=str)
parser.add_argument('email', type=str)
parser.add_argument('password', type=str)

@auth_blueprint.errorhandler(InvalidAPIUsage)
def bad_request(e):
    return jsonify(e.to_dict()), e.status_code

class RegisterUser(Resource):
    def post(self):
        try:
            args = parser.parse_args()
            if not args['full_name']:
                raise InvalidAPIUsage("Please provide a full name")
            hashed_password = bcrypt.generate_password_hash(args['password']).decode('utf-8')
            new_user = User(full_name=args['full_name'], email=args['email'], password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            return {"message":"User registered successfully"}, 201
        except Exception as e:
            logger.error('Error occurred: %s', str(e))
            raise

class Login(Resource):
    def post(self):
        try:
            args = parser.parse_args()
            if not args['email']:
                raise InvalidAPIUsage("Please provide an email address")
            user = User.query.filter_by(email=args['email']).first()
            if not user:
                raise InvalidAPIUsage("User does not exist")
            is_password = bcrypt.check_password_hash(user.password, args['password'])
            if user and is_password:
                login_user(user)
                return {"message":"Logged in successfully"}, 200
            else:
                return {"message":"Wrong username or password"}, 401
        except Exception as e:
            logger.error('Error occurred: %s', str(e))
            raise

class Logout(Resource):
    def post(self):
        logout_user()
        return {"message":"User logged out successfully"}, 200

api.add_resource(RegisterUser, '/register')
api.add_resource(Login,'/login')
api.add_resource(Logout,'/logout')

auth_blueprint.register_error_handler(400, bad_request)
