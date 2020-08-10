from flask import jsonify

# error response


def error_response(e: object) -> object:
    return jsonify(error=True, message=str(e))
