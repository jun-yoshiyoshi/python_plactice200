# クラスの特殊属性 __str__()メソッド

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print('name:' + self.name)
        print('age:' + str(self.age))


u = User("taro", 25)
u.print_info()
print(u)


class Customer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print('name:' + self.name)
        print('age:' + str(self.age))

    def __str__(self):
        return f'name:{self.name},age:{self.age}'


c = Customer("jiro", 20)
c.print_info()
print(c)
