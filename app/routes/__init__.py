from flask import jsonify
from app.resources import auth

# Init route
def initialize_routes(app):
    app.register_blueprint(auth)

