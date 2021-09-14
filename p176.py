# クラス変数、クラス定数
class MyClass:
    # クラス変数
    a = "A"
    # クラス定数
    c = 5

    def __init__(self):
        self.b = "B"
        # インスタンス変数

    def set_ab(self, a, b):
        # クラス変数の利用
        MyClass.a = a
        self.b = b

    def print_ab(self):
        print(MyClass.a * MyClass.c)
        # クラス定数の利用
        print(self.b)


mycls_a = MyClass()
mycls_b = MyClass()

mycls_a.print_ab()
mycls_b.print_ab()


mycls_a.set_ab("AA", "BB")
mycls_a.print_ab()
mycls_b.print_ab()


# クラス定数の用例
class Color:
    BLACK = "000000"
    GRAY = "808080"
    WHITE = "ffffff"
    BLUE = "0000ff"
    GREEN = "00ff00"
    RED = "ff0000"


print(Color.RED)
print(Color.BLACK)
