class User:

    def __init__(self, name):
        self.__name = self.__validate_name(name)
        self.__type = self.__set_type()

    def __validate_name(self, value):
        if isinstance(value, str):
            return value
        else:
            raise ValueError('\'name\' must be a instance of string')

    def __set_type(self):
        return 0

    @property
    def is_admin(self):
        return self.__type


class Admin(User):

    def __init__(self, name):
        super().__init__(name)

    def __set_type(self):
        return 1
