# スタティックメソッド

class MyClass:
    a = "A"


@staticmethod
def print_a():
    print(MyClass.a)


MyClass.print_a()


class MyUtil:
    @staticmethod
    def function1():
        pass

    @staticmethod
    def function2():
        pass

    @staticmethod
    def function3():
        pass
