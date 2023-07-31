"""
类的继承
"""
class UserInfo(object):
    lv = 5

    def __init__(self, name, age, account):
        self.name = name
        self._age = age
        self.__account = account

    def get_account(self):
        return self.__account


class UserInfo2(UserInfo):
    pass


"""
调用父类方法
"""
if __name__ == '__main__':
    user = UserInfo('ASD', 18, 'DA')
    print(user.get_account());
