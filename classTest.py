#直接使用类
class ClassA():
    var = "12321"
    @classmethod
    def fun1(cls):
        print(cls.var)

#类的实例化
class ClassB(object):
    var = "12321"
    def fun1(self):
        print(self.var)