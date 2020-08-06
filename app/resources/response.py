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
        response.update({"count": len(data),"data": data })
    return jsonify(response)

#404
@response.app_errorhandler(404)
def handle_404(err):
    return errorResponse(err)

#500
@response.app_errorhandler(500)
def handle_500(err):
    return jsonify({
        "error" : true,
        "message": "Something went wrong",
        "status": 500
    })

#405
@response.app_errorhandler(405)
def handle_500(err):
    return errorResponse(err)
