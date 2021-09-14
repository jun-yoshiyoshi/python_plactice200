# 多重継承

class Parent1:
    def print_hello(self):
        print('hello')


class Parent2:
    def print_world(self):
        print('world')


class Child(Parent1, Parent2):
    def print_python(self):
        print('python')


c = Child()
c.print_hello()
c.print_world()
c.print_python()
