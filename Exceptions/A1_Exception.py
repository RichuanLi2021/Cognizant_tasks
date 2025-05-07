class OperationNotFoundError(Exception):
    """ Exception raised when an operation is not found.
    """
    def __init__(self, message, input_value):
        super().__init__(message)
        self.input_value = input_value
