class EmptyFileError(Exception):
    def __init__(self, message="File is empty"):
        self.message = message
        super().__init__(self.message)