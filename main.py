from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

names = {"ankit": {"age": 25, "gender": "male"},
         "charlie": {"age": 24, "gender": "male"}
         }

class HelloWorld(Resource):
    def get(self, name):
        return {"data": names[name]}

    def post(self, name):
        return {"data": {"name": "Post " + name}}


api.add_resource(HelloWorld, "/hello-world/<string:name>")

if __name__ == "__main__":
    app.run(debug=True)
