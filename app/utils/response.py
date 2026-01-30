from fastapi import status

def success_response(message: str, data=None, code: int = status.HTTP_200_OK):
    return {
        "success": True,
        "code": code,
        "message": message,
        "data": data,
        "error": None
    }


def error_response(message: str, code: int = status.HTTP_400_BAD_REQUEST, error_type: str = "ERROR"):
    return {
        "success": False,
        "code": code,
        "message": message,
        "data": None,
        "error": {
            "type": error_type
        }
    }