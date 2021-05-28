from flask import Flask, jsonify, request
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from config import SQLALCHEMY_DATABASE_URI

app = Flask(__name__)

client = app.test_client()

engine = create_engine(SQLALCHEMY_DATABASE_URI)
session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = session.query_property()

from models import *

Base.metadata.create_all(bind=engine)


@app.route('/posts', methods=['GET'])
def get_list_posts():
    all_posts = Post.query.all()
    serialized = []
    for post in all_posts:
        serialized.append({
            "id": post.id,
            "title": post.title,
            "description": post.description,
            "owner": "username"
        })
    return jsonify(serialized)


@app.route('/posts', methods=['POST'])
def add_post():
    new_post = Post(**request.json)
    session.add(new_post)
    session.commit()
    serialized = {
        "id": new_post.id,
        "title": new_post.title,
        "description": new_post.description,
        "owner": "username"
    }
    return jsonify(serialized)


@app.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    new_post = Post.query.filter(Post.id == post_id).first()
    params = request.json
    if not new_post:
        return {'message': 'no post with this id'}, 400
    for key, value in params.items():
        setattr(new_post, key, value)
    session.commit()
    serialized = {
        "id": new_post.id,
        "title": new_post.title,
        "description": new_post.description,
        "owner": "username"
    }
    return serialized


@app.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    dld_post = Post.query.filter(Post.id == post_id).first()
    if not dld_post:
        return {'message': 'no post with this id'}, 400
    session.delete(dld_post)
    session.commit()
    return '', 204


@app.teardown_appcontext
def shutdown_session(exception=None):
    session.remove()


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
