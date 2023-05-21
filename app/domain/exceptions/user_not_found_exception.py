class UserNotFoundException(Exception):
    """
    Exception raised when a user not found.
    """

    def __init__(self, message: str = "User not found"):
        self.message = message
        super().__init__(self.message)
