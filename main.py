from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Video(name={self.name}, views={self.views}, likes={self.likes})"


# db.create_all() to be run only once

# videos = {}

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Please send a name", required=True)
video_put_args.add_argument("views", type=int, help="Please send a views", required=True)
video_put_args.add_argument("likes", type=int, help="Please send a likes", required=True)


def abort_if_video_id_doesnt_exits(video_id):
    if video_id not in videos:
        abort(404, message="video id is not valid...")

def abort_if_video_id_exits(video_id):
    if video_id in videos:
        abort(409, message="video already exists with that id...")

class Video(Resource):
    def get(self, video_id):
        abort_if_video_id_doesnt_exits(video_id)
        return videos[video_id]

    def put(self, video_id):
        # print(request.form['likes'])  this is the first method to get body but better to use reqparse

        abort_if_video_id_exits(video_id)
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201

    def delete(self, video_id):
        abort_if_video_id_doesnt_exits(video_id)
        del videos[video_id]
        return '', 204


api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)
