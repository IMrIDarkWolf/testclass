class Permission(object):

    def __init__(self):
        self.__types = set()

    def add_type(self, _type):
        if isinstance(_type, int):
            self.__types.add(_type)
        else:
            raise TypeError(f'\'_type\' must be instance of {type(int)}')

    def check_permission(self, view):
        if view.user.is_admin not in self.__types:
            return False
        return True


class AdminPermission(Permission):

    def __init__(self):
        super().__init__()

        self.add_type(1)


class UserPermission(AdminPermission):

    def __init__(self):
        super().__init__()
        self.add_type(0)

