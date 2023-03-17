class NoneError(Exception):
    def __init__(self, message="Value cannot be empty"):
        super().__init__(message)

class Expected:
    
    def __init__(self, value):
        self.__value__ = value

        """_summary_
        Validates the given value or expression and throws exception if it's undefined or false 
        """
    def to_be_truthy(self, error):
        if self.__value__ is None:
            raise error
        if self.__value__ is bool and self.__value__ == False:
            raise error
        if self.__value__ is int and self.__value__ == 0:
            raise error

        """_summary_
        Validates the given value or expression and throws exception if it's other than undefined or false 
        """
    def to_be_falsy(self, error):
        if self.__value__ is None:
            return
        if self.__value__ is bool and self.__value__ == False:
            return
        if self.__value__ is int and self.__value__ == 0:
            return
        raise error
    
    def to_equal(self, value, error):
        if self.__value__ is value:
            return
        raise error

def expect(value):
    return Expected(value)

