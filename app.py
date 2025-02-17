from flask import Flask, jsonify


app = Flask(__name__)


#create post
@app.route('/blog/add',methods=["POST"])
def create_post():
    #logic for creating blog post here
    return 'Blog created successfully'

#get blog post
@app.route('/blog')
def get_all_posts():
    blogs = [{
        "title":"First blog",
        "content":"Test first blog"
    }]
    return jsonify(blogs)

#get single post
@app.route('/blog/<int:post_id>')
def get_single_post(post_id):
    blog = {
        "id":post_id,
        "title":"Blog one",
        "content":"Blog one content"
    }
    return jsonify(blog)

#update post
@app.route('/blog/<int:post_id>', methods=["PUT"])
def update_post(post_id):
    return f'Blog post #{post_id} updated successfully'

#delete post
@app.route('/blog/<int:post_id>', methods=["DELETE"])
def delete_post(post_id):
    return f'Blog post #{post_id} deleted successfully'



if __name__ == "__main__":
    app.run()