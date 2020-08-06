from flask import current_app, Blueprint,request, jsonify
from .response import successResponse
auth = Blueprint('auth', __name__)

@auth.route('/signin', methods=['POST'])
def LoginApi():
    # es = current_app.config["es"]
    return successResponse("test mesasage",request.json)

@auth.route('/signup')
def SignupApi():
    # es = current_app.config["es"]
    return successResponse("login response")