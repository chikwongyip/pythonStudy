class UserInfo(object):
    lv = 5

    def __init__(self, name, age, account):
        self.name = name
        self.age = age
        self.account = account

    def get_account(self):
        return self.account

    @classmethod
    def get_name(cls):
        return cls.lv

    @property
    def get_age(self):
        return self.age


"""
对UserInfo类进行重写
"""


class UserInfo2(UserInfo):
    def __init__(self, name, age, account, sex):
        super(UserInfo2, self).__init__(name, age, account)
        self.sex = sex


if __name__ == '__main__':
    user = UserInfo2('ZHIGUANG', 18, 123213, 'Male')
    print(user.__dict__)
    print(user.get_name())
