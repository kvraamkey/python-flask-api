from flask import current_app, Blueprint,request, jsonify
from .response import successResponse, errorResponse
auth = Blueprint('auth', __name__)

@auth.route('/signin', methods=['POST'])
def LoginApi():
    # es = current_app.config["es"]
    try:
        return successResponse("test mesasage",request)
    except Exception as e:
        return errorResponse(e)

@auth.route('/signup')
def SignupApi():
    return successResponse("signup response")