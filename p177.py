# クラスメソッド
class MyClass1:
    def __init__(self, a="abc"):
        self.a = a
        # インスタンス変数

    def print_a(self):
        print(self.a)
        # インスタンス変数aを持つメソッド

    def print_hello(self):
        print("hello")
        # インスタンス変数を持たないメソッド
        # クラスメソッドとして定義できる。

    @classmethod
    def print_bye(cls):
        print("bye")


MyClass1().print_a()
MyClass1().print_hello()
MyClass1.print_bye()
print("-"*5)

# clsとは何か


class MyClass2:
    a = "A"
    # クラス変数
    # @classmethod(プロパティ):関数やメソッドの働きを定義する宣言

    @classmethod
    def print_hello(cls):
        print(cls.a)
        print(type(cls))


MyClass2.print_hello()
# クラスメソッドの中からもクラス自身(cls)が参照され、"A"が出力される。
print("-" * 5)

# クラスメソッドの作用


class MyClass3:
    d = 'クラス変数'
    # クラス変数

    def print_self_e(self):
        print(self.d)  # インスタンス変数dの出力

    def set_self_e(self, d):
        self.d = d  # インスタンス変数dの入力

    @classmethod
    def print_cls_d(cls):
        print(cls.d)  # クラス変数dの出力

    @classmethod
    def set_cls_d(cls, d):
        cls.d = d  # クラス変数dの入力


# インスタンス変数はクラス変数を参照している。
MyClass3().print_self_e()
MyClass3.print_cls_d()
print("#クラス変数の入力を変更")
# クラス変数の入力値を変更
MyClass3.set_cls_d("変更されたクラス変数")
MyClass3().print_self_e()
MyClass3.print_cls_d()
print("MyClass3()を変数mc1,mc2の初期値に設定")
mc1 = MyClass3()
mc2 = MyClass3()
mc1.print_self_e()
mc1.print_cls_d()
mc2.print_self_e()
mc2.print_cls_d()
print("mc1のインスタンス変数の入力を変更")
mc1.set_self_e("EE")
mc1.print_self_e()
mc1.print_cls_d()
print("mc2のインスタンス変数に入力なし")
mc2.print_self_e()
mc2.print_cls_d()
