# クラスの承継
class ClassA:
    def __init__(self, x=2, y=3):
        self.var_a = 'class a'
        self.x = x
        self.y = y

    def print_a(self):
        print('ClassAのメソッド'*self.x + self.var_a)
        print(str(self.y))


class ClassB(ClassA):
    # <---継承の宣言
    def __init__(self, x=1, y=1):
        self.var_b = 'class b'
        super().__init__(x, y)
        self.x = x
        self.y = y
        # super().  <---親クラスの初期化。引数の数は親クラスに依存している。
        # 第一引数はselfをとって初期化している。引数が二つ以上ある場合はその初期化を行う。引数を渡さないとエラーになる。

    def print_b(self):
        print('ClassBのメソッド'*self.x + self.var_b)
        print('parent of ' + self.var_b + ' is ' + self.var_a)
        print(str(self.y))


a = ClassA()
b = ClassB()

a.print_a()
b.print_b()
b.print_a()

# 具体的にはどのような場合に継承を使うべきか。
# 1.すでに利用している自分が作った既存のクラスを継承する場合
# 2.標準ライブラリやほかの人が作ったクラスを継承する場合
# 3.親に多数の子供がいる場合
# 4.GUIを利用する場合
