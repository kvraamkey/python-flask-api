from flask import Flask
from app.database import initialize_es
from app.routes import initialize_routes
from app.utils import error_response

# Define the WSGI application object
app = Flask(__name__)


def create_app():
    # Init app
    client_es = initialize_es()
    
    # Exception Error Handling
    app.register_error_handler(405, error_response)
    app.register_error_handler(404, error_response)
    app.register_error_handler(500, error_response)

    # app configuration
    app.config['JSON_SORT_KEYS'] = False
    app.config.update({'es': client_es})
    initialize_routes(app)
    
    return app
