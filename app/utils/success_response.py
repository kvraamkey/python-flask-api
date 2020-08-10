from flask import jsonify
# success response


def success_response(message, data=None):
    response = {
        "error": False,
        "message": str(message)
    }
    if data:
        response.update({
            # "count": len(data),
            "data": data
        })
    
    return jsonify(response)
