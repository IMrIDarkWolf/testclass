from permissions import Permission
from users import User


class View(object):

    def __init__(self, permission=None):
        self.__user = None
        self.__permission = self.validate_permission(permission)

    def validate_permission(self, value):

        if not value or isinstance(value, Permission):
            return value
        else:
            raise TypeError(f'\'permission\' must be instance of {type(Permission)}')

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, value):
        if isinstance(value, User):
            self.__user = value
        else:
            raise TypeError(f'\'user\' myst be instance of {type(User)}')

    @property
    def data(self):
        if not self.__user:
            raise AttributeError('\'user\' is not exist')

        if not self.__permission:
            return 'something data'

        return 'data'  # TODO: modified it to check permissions


class UserView(View):

    def __init__(self, permission=None):
        super().__init__(permission=permission)
        self.user = User('Вася')
