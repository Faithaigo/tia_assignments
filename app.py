from flask import Flask, render_template



app = Flask(__name__)


@app.route('/')
def index():
    posts = [
        {
            id:1,
            "title":"First Post",
            "content":"Post content",
            "author":"John Doe"
        },
          {
            id:2,
            "title":"First Post",
            "content":"Post content",
            "author":"John Doe"
        }
    ]
    return render_template("index.html", posts=posts)


@app.route('/posts')
def posts():
    posts = [
        {
            id:1,
            "title":"First Post",
            "content":"Post content",
            "author":"John Doe"
        },
          {
            id:2,
            "title":"First Post",
            "content":"Post content",
            "author":"John Doe"
        }
    ]
    return render_template("posts.html", posts=posts)

@app.route('/new_post', methods=["POST","GET"])
def new_post():
    return render_template("new_post.html")

@app.route('/delete_post', methods=["PUT"])
def delete_post():
    pass

@app.route('/edit_post', methods=["DELETE"])
def edit_post():
    pass

@app.route('/register', methods=["GET"])
def register():
    return render_template("register.html")


@app.route('/login', methods=["GET"])
def login():
    return render_template("login.html")

if __name__ == '__main__':
    app.run(debug=True)