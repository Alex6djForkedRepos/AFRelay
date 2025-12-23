
def build_error_response(error_type: str, method: str, details: str) -> dict:
    return {
        "status" : "error",
        "error" : {
            "method" : method,
            "error_type" : error_type,
            "details" : details
        }
    }