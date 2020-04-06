"""Definition for error that may be raised by this library."""


class EdgeQLLoadError(Exception):
    """Error that raised if there is an error to load queries."""


class EdgeQLParsingError(Exception):
    """Error that raised if there is an error in parsing query."""
