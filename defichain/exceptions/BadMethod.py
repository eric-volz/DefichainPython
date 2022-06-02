class BadMethod(Exception):
    """
    The called method is not existent.
    """
    def __init__(self, msg):
        self.message = msg
        super().__init__(f"Bad Method(405): {self.message}")
