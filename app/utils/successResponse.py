from flask import jsonify

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

