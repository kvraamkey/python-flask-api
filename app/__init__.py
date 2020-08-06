from flask import Flask, jsonify
from .database.db import initialize_es;
from .resources.routes import initialize_routes
from .resources.response import errorResponse

#Define the WSGI application object
app = Flask(__name__)

def create_app():
    # Init app
    clientEs = initialize_es(app)
    
    #Exception Error Handling
    app.register_error_handler(404, errorResponse)
    app.register_error_handler(500, errorResponse)

    #app configuration
    app.config['JSON_SORT_KEYS'] = False
    app.config.update({'es': clientEs})
    initialize_routes(app)
    
    return app

