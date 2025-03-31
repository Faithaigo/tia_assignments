from flask import Blueprint
from flask_login import login_required, current_user
from flask_restful import Api, Resource, reqparse
from posts.models import Posts
from extensions import db

posts_blueprint = Blueprint('posts', __name__, url_prefix="/blog")

api = Api(posts_blueprint)

parser = reqparse.RequestParser()
parser.add_argument('title', type=str, help="Title of post")
parser.add_argument('content', type=str, help="Post content")
parser.add_argument('author', type=str, help="Post author")


class BlogPosts(Resource):
    @login_required
    def get(self):
        all_posts = db.session.execute(db.select(Posts)).scalars().all()
        posts = []
        for post in all_posts:
            p = post.__dict__
            posts.append(p)
        for post in posts:
            post.pop('_sa_instance_state', None)
        return {"posts": posts}, 200

    @login_required
    def post(self):
        if not current_user:
            return {"message": "You are not authorized"}, 403
        arg = parser.parse_args()
        added_post = Posts(title=arg["title"], content=arg["content"], author=arg["author"])
        db.session.add(added_post)
        db.session.commit()
        return {"message": "Post added successfully"}, 200


class BlogPost(Resource):
    @login_required
    def get(self, post_id):
        post = db.get_or_404(Posts, post_id)
        return {"id": post.id, "title": post.title, "content": post.content, "author": post.author}, 200

    @login_required
    def put(self, post_id):
        pass

    @login_required
    def delete(self, post_id):
        pass


api.add_resource(BlogPosts, '/posts')
api.add_resource(BlogPost, '/post/<int:post_id>')
