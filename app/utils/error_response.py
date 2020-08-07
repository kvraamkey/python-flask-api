from flask import jsonify

# error response


def error_response(e):
    return jsonify(error=True, message=str(e))
