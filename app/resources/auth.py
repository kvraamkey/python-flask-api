from flask import current_app, Blueprint
from elasticsearch import exceptions
from app.utils import successResponse, errorResponse

auth = Blueprint('auth', __name__)


@auth.route('/signing', methods=['POST'])
def login():
    elastic_client = current_app.config["es"]
    try:
        # query_body = {
        #     "query": {
        #         "match_all": {}
        #     },
        #     "size": 10,
        # }
        # result = elastic_client.search(index="o365_azure_ad_users", body=query_body)
        return successResponse("test mesasage", 'result')
    except exceptions.ConnectionError as err:
        return errorResponse(err)
    except Exception as e:
        return errorResponse(e)


@auth.route('/signup')
def signup():
    return successResponse("signup response")
