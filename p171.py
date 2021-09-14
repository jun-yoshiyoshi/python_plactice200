# オーバーライド（親クラスメソッドの上書き）ポリモーフィズムの実現

class Parent:
    def __init__(self):
        print('Parent__init__()')

    def fun1(self):
        print('Parent fun1()')

    def fun2(self):
        print('Parent fun2()')


class Child(Parent):
    def __init__(self):
        print('Child__init__()')

    def fun1(self):
        print('Chilc fun1()')


c = Child()
# Child__init__()
c.fun1()
c.fun2()
