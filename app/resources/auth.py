from flask import current_app, Blueprint
from elasticsearch import exceptions
from app.utils import error_response, success_response
auth = Blueprint('auth', __name__)


@auth.route('/signing', methods=['POST'])
def login():
    elastic_client = current_app.config["es"]
    try:
        query_body = {
            "query": {
                "match_all": {}
            },
            "size": 10,
        }
        result = elastic_client.search(index="cimlogs_dev", body=query_body)
        return success_response("test mesasage", result)
    except exceptions.ConnectionError as err:
        return error_response(err)
    except Exception as e:
        return error_response(e)


@auth.route('/signup')
def signup():
    return error_response("signup response")
