#　メソッドのオーバーロード(技法)
#　引数の異なる同名のメソッドを定義した場合に、引数の型に応じて呼び出されるメソッドが変わる(原則できない)。
# 「デフォルト引数」や「可変長引数」などを用いて、疑似的にオーバーロードの機能を持たせる。


class MyClass:
    def test(self, a, b, c="C", d="D"):  # デフォルト引数
        print(a, b, c, d)


mc = MyClass()
mc.test("AA", "BB")
mc.test("AA", "BB", "CC")
# 引数が２つでも３つでも同じクラスメソッドが呼び出されている


class MyClass2:
    def test2(self, *args):  # 可変長引数（引数の個数が決まっていない）
        n = 0
        for _ in args:
            n += _
        return n


mc2 = MyClass2()
print(mc2.test2(1))
print(mc2.test2(1, 2))
print(mc2.test2(1, 2, 3))
