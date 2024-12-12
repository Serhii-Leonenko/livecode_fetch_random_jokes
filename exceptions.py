class ResponseError(Exception):
    def __init__(self):
        self.message = "Oops something went wrong"