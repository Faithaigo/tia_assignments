from flask import Flask, jsonify, render_template
from datetime import date
from flask import request



app = Flask(__name__)


@app.route('/')
def home():
    
    today = date.today()
    posts = [{
        "id":1,
        "title":"First post",
        "content":"Post content goes here",
        "author":"John Doe",
        "date":today
    },
    {
        "id":2,
        "title":"First post",
        "content":"Post content goes here",
        "author":"John Doe",
        "date":today
    },
      {
        "id":3,
        "title":"First post",
        "content":"Post content goes here",
        "author":"John Doe",
        "date":today
    }]
    return render_template("index.html", posts=posts)

@app.route('/posts')
def posts():
    today = date.today()
    posts = [{
        "id":1,
        "title":"First post",
        "content":"Post content goes here",
        "author":"John Doe",
        "date":today
    },
    {
        "id":2,
        "title":"First post",
        "content":"Post content goes here",
        "author":"John Doe",
        "date":today
    },
    {
        "id":3,
        "title":"First post",
        "content":"Post content goes here",
        "author":"John Doe",
        "date":today
    },
        {
        "id":4,
        "title":"First post",
        "content":"Post content goes here",
        "author":"John Doe",
        "date":today
    }]
    return render_template("posts.html", posts=posts)

@app.route('/new_post', methods=["POST","GET"])
def new_post():
    if request.method == "GET":
        return render_template("new_post.html")
    else:
        return "Save post implementation"

@app.route('/post/<int:post_id>')
def view_post(post_id):
    today = date.today()
    post = {
        "id":post_id,
        "title":"First post",
        "content":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque sit amet blandit massa, ac bibendum lectus. Sed molestie rutrum risus in imperdiet. Nullam imperdiet felis ante, a semper metus molestie at. Pellentesque cursus nisi vitae libero eleifend convallis. Fusce",
        "author":"John Doe",
        "date":today
    }
    return render_template("post.html", post=post)




if __name__ == "__main__":
    app.run(debug=True)