def get_headers(request) -> tuple:
    request_setup = request.json().get("setup")
    request_punchline = request.json().get("punchline")

    return request_setup, request_punchline
