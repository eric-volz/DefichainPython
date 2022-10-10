from typing import Optional


class DerivationError(Exception):
    """
    Bad derivation index
    """

    def __init__(self, error_message: str, error_detail: Optional[str] = None):
        self.error_message = error_message
        self.error_detail = error_detail

    def __str__(self):
        if self.error_detail:
            return f"{self.error_message}, {self.error_detail}"
        return f"{self.error_message}"
