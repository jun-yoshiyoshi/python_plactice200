# classの詳細理解　selfとは何か

class my_class:
    def __init__(self):
        print("コンストラクタ")

    def method(self, a):
        print(a)

    def method2(self):
        print(f"self のデータ型:{type(self)}")
        print(f"selfをprint:{self}")


instance = my_class()

instance.method("テスト")

instance.method2()
# メソッドは、空欄に見えるが、実際にはselfを第一引数にしていることが分かる。
