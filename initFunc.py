
class ClassA(object):
    """
    初始化函数类创建时候触发
    可以传递参数
    """
    def __int__(self, param):
        print('init successful')
    """
    析构函数 类销毁时候触发
    """
    def __del__(self):
        print("instance delete")