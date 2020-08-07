# from flask import jsonify, request
# from importlib import import_module
from app.resources import auth
from app.utils import error_response, success_response
from app.controllers.auth import login


# Init route


def initialize_routes(app):
    app.register_blueprint(auth)

    # @app.route('/')
    # def api():
    #     return jsonify(title='VantageX API', version="v1.0.0")
    #
    # @app.route('/', methods=['POST'])
    # @app.route('/<string:controller>', methods=['POST'])
    # @app.route('/<string:controller>/<string:action>', methods=['POST'])
    # def route(controller=None, action=None):
    #     if not controller or not action:
    #         return error_response("A valid [controller] or [action] is required.")
    #     else:
    #         try:
    #             request_body = {"postData": request.json}
    #
    #             module = import_module('app.controllers.auth.login')
    #
    #             print(module)
    #             return success_response('success', request_body)
    #         except Exception as e:
    #             return error_response(e)
