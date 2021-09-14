# インスタンス変数とローカル変数(p128.py)

class user_info:
    def __init__(self, name, birth, address):
        # コンストラクタに渡されている３つの引数はメソッド内のただの変数（ローカル変数）
        self.name = name
        self.birth = birth
        self.address = address
        # メソッド内で直接インスタンスに変更を生じるのは、"self.name","self.birth","self.address"の３つの明示されたインスタンス変数


class my_class:
    def __init__(self):
        self.a = 0
        b = 0

    def set_a(self, v):
        self.a = v

    def get_a(self):
        return self.a

    def set_b(self, value):
        b = value

    def get_b(self):
        return b  # 000 #"abc"


instance = my_class()

instance.set_a(3)
print(instance.get_a())

instance.set_b(5)
print(instance.get_b())
# get_bのインスタンス変数bの初期値が設定されていないためエラーになる。
# インスタンス変数bの代わりに000や""abc"を戻り値とすると実行できる。
