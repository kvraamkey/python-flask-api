from flask import jsonify

#error response
def errorResponse(e):
    return jsonify(error=True, message=str(e))
