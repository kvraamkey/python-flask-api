from flask import current_app, Blueprint, jsonify
response = Blueprint('response', __name__)

#error response
def errorResponse(e):
    return jsonify(error=True, message=str(e))

#success response
def successResponse(message, data):
    response = {
        "error": False,
        "message": str(message)
    }
    if (data):
        response.update({
            "count": len(data),
            "data": data
        })
    
    return jsonify(response)

