from flask import jsonify, request
from importlib import import_module
from app.resources import auth
from app.utils import error_response


def initialize_routes(app):
    app.register_blueprint(auth)
    es_client_connection = app.config["es"]

    @app.route('/')
    def api():
        return jsonify(title='VantageX API', version="v1.0.0")

    @app.route('/', methods=['POST'])
    @app.route('/<string:controller>', methods=['POST'])
    @app.route('/<string:controller>/<string:action>', methods=['POST'])
    def route(controller=None, action=None):
        try:
            controller_path = f'app.controllers.{controller}.{action}'
            module = import_module(controller_path)
            module_action = getattr(module, action)
            return module_action(dict(body=request.json, es=es_client_connection))
        except ModuleNotFoundError as e:
            return error_response('A valid [controller] or [action] is required.')
        except Exception as e:
            return error_response(e)
