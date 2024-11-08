"""6 - Custom exceptions."""


class ZeroTotalError(Exception):
    """Error for zero total to process."""


class NegativeTotalError(Exception):
    """Error for negative total to process."""


class UserDoesNotExistsError(Exception):
    """Error for user that doesnt exists"""


class ZeroBalanceError(Exception):
    """Error for zero balance while trying to transfer"""


class IncorrectTableError(Exception):
    """Error to prevent usage of incorrect table name."""
