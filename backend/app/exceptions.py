class NumerologyError(Exception):
    """Base exception for numerology calculation errors."""
    pass

class InvalidDataError(NumerologyError):
    """Raised when birthdate values are invalid"""
    pass

class InvalidReducitonLevelError(NumerologyError):
    """Raised when reduciton level is out of valid range."""
    pass

class InvalidCalculationParametersError(NumerologyError):
    """Raised when calculation parameters are invalid"""
    pass

class InvalidTypeError(NumerologyError):
    """Raised when input data types are invalid"""
    pass
