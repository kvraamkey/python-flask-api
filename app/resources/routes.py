from flask import jsonify
from .auth import auth
from .response import response

# Init route
def initialize_routes(app):
    app.register_blueprint(auth)
    app.register_blueprint(response)

