# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:chinmay123@localhost/postNew'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
ma = Marshmallow(app)


class PostNew(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    checked = db.Column(db.Boolean, default=True)
    type = db.Column(db.String(100))
    description = db.Column(db.String(200))
    age = db.Column(db.Integer)
    date = db.Column(db.DateTime())

    def __init__(self, name, checked, type, description, age, date):
        self.name = name
        self.checked = checked
        self.type = type
        self.description = description
        self.age = age
        self.date = date


class PostSchema(ma.Schema):
    class Meta:
        fields = ("name", "checked", "type", "description", "age", "date")


post_schema = PostSchema()  # Two or more queryset
posts_schema = PostSchema(many=True)


@app.route('/post', methods=['POST'])
def add_post():
    name = request.json['name']
    checked = request.json['checked']
    type = request.json['type']
    description = request.json['description']
    age = request.json['age']
    date = request.json['date']

    my_posts = PostNew(name, checked, type, description, age, date)
    db.session.add(my_posts)
    db.session.commit()

    return post_schema.jsonify(my_posts)


@app.route('/post_details/<id>/', methods=['GET'])
def post_details(id):
    post = PostNew.query.get(id)
    return post_schema.jsonify(post)


# updating post
@app.route('/post_update/<id>/', methods=['PUT'])
def post_update(id):
    post = PostNew.query.get(id)

    name = request.json['name']
    description = request.json['description']
    age = request.json['age']

    post.name = name
    post.description = description
    post.author = age

    db.session.commit()
    return post_schema.jsonify(post)


@app.route('/get', methods=['GET'])
def get_post():
    all_posts = PostNew.query.all()
    result = posts_schema.dump(all_posts)
    return jsonify(result)


# deleting post
@app.route('/post_delete/<id>/', methods=['DELETE'])
def post_delete(id):
    post = PostNew.query.get(id)
    db.session.delete(post)
    db.session.commit()

    return post_schema.jsonify(post)


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    app.run(debug=True)
