class ResponseError(Exception):
    def __init__(self) -> None:
        self.message = "Oops something went wrong"
