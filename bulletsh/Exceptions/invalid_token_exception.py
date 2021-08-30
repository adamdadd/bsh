class InvalidTokenException(Exception):
    def __init__(self, message="Invalid pushbullet token") -> None:
        self.message = message
        super().__init__(self.message)