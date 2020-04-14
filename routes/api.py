from flask import Flask
import flask_restful as restful
from performance_python.app.Controller.UserController import User
from performance_python.app.Controller.TmpController import Tmp

app = Flask(__name__)
api = restful.Api(app)

api.add_resource(User, '/api/foo', '/api/foo/<str:id>')
api.add_resource(Tmp, '/api/bar', '/api/bar/<str:id>')
