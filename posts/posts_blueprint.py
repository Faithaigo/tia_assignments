import logging
from flask import Blueprint, jsonify
from flask_login import login_required, current_user
from flask_restful import Api, Resource, reqparse

from customErrors import InvalidAPIUsage
from posts.models import Posts
from extensions import db

posts_blueprint = Blueprint('posts', __name__, url_prefix="/blog")

api = Api(posts_blueprint)

logger = logging.getLogger(__name__)

parser = reqparse.RequestParser()
parser.add_argument('title', type=str, help="Title of post")
parser.add_argument('content', type=str, help="Post content")
parser.add_argument('author', type=str, help="Post author")


@posts_blueprint.errorhandler(InvalidAPIUsage)
def bad_request(e):
    return jsonify(e.to_dict()), e.status_code

@posts_blueprint.errorhandler(InvalidAPIUsage)
def unauthorized_access(e):
    return jsonify(e.to_dict()), e.status_code

class BlogPosts(Resource):
    @login_required
    def get(self):
        try:
            all_posts = db.session.execute(db.select(Posts)).scalars().all()
            posts = []
            for post in all_posts:
                p = post.__dict__
                posts.append(p)
            for post in posts:
                post.pop('_sa_instance_state', None)
            return {"posts": posts}, 200
        except Exception as e:
            logger.error('Error occurred: %s', str(e))
            raise

    @login_required
    def post(self):
        try:
            if not current_user:
                raise InvalidAPIUsage('You are not authorized', status_code=401)
            arg = parser.parse_args()
            if not arg["title"]:
                raise InvalidAPIUsage('Please provide a title')
            added_post = Posts(title=arg["title"], content=arg["content"], author=arg["author"])
            db.session.add(added_post)
            db.session.commit()
            return {"message": "Post added successfully"}, 200
        except Exception as e:
            logger.error('Error occurred: %s', str(e))
            raise


class BlogPost(Resource):
    @login_required
    def get(self, post_id):
        try:
            post = db.get_or_404(Posts, post_id)
            return {"id": post.id, "title": post.title, "content": post.content, "author": post.author}, 200
        except Exception as e:
            logger.error('Error occurred: %s', str(e))
            raise

    @login_required
    def put(self, post_id):
        pass

    @login_required
    def delete(self, post_id):
        pass


api.add_resource(BlogPosts, '/posts')
api.add_resource(BlogPost, '/post/<int:post_id>')

posts_blueprint.register_error_handler(400, bad_request)
posts_blueprint.register_error_handler(401, unauthorized_access)
