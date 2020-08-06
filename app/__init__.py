from flask import Flask, jsonify
from .database.db import initialize_es;
from .resources.routes import initialize_routes

#Define the WSGI application object
app = Flask(__name__)

def create_app():
    # Init app
    isEsConnected = initialize_es(app)
    app.config['JSON_SORT_KEYS'] = False
    app.config.update({'es': isEsConnected})
    initialize_routes(app)
    return app

