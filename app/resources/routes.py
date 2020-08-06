from flask import jsonify
from .auth import auth

# Init route
def initialize_routes(app):
    app.register_blueprint(auth)

