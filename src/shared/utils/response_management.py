import xmltodict


def build_error_response(method: str, error_type: str, details: str) -> dict:
    """
    Standardizes error responses for SOAP client exceptions.

    args:
        method (str): The name of the SOAP method where the error occurred.
        error_type (str): The category of exception (ConnectionError, TimeoutException, etc).
        details (str): Technical description, traceback, or custom error message.
    """
    return {
        "status" : "error",
        "error" : {
            "method" : method,
            "error_type" : error_type,
            "details" : details
        }
    }

def clear_response(response) -> dict:

    response_parsed = xmltodict.parse(response.text)
    cleaned_response = response_parsed["soap:Envelope"]["soap:Body"]

    return cleaned_response
