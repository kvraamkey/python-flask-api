from flask import current_app, Blueprint, request, jsonify
from elasticsearch import exceptions
from app.utils import successResponse, errorResponse
auth = Blueprint('auth', __name__)

@auth.route('/signin', methods=['POST'])
def LoginApi():
    
    elastic_client = current_app.config["es"]

    try:
        query_body = {
            "query": {
                "match_all": {}
            },
            "size": 10,
        }
        result = elastic_client.search(index="o365_azure_ad_users", body=query_body)
        return successResponse("test mesasage", result)
    except exceptions.ConnectionError as err:
        return errorResponse(err)
    except Exception as e:
        return errorResponse(e)

@auth.route('/signup')
def SignupApi():
    return successResponse("signup response")