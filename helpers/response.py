from typing import Any, Optional
# pyrefly: ignore [missing-import]
from flask import jsonify

def http_response(
    code: int,
    is_success: bool,
    message: str,
    data: Optional[Any] = None,
):
    response_body = {
        "status": {
            "code": code,
            "isSuccess": is_success,
        },
        "message": message,
        "data": data,
    }

    return jsonify(response_body), code