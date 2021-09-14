# オブジェクト指向におけるsetterとgetterの機能　詳細理解(p130.pyから)
class Test:
    def __init__(self, pri_v="pri"):
        self.__pri_v = pri_v
        # インスタンス変数は全てプライベート化する

    def get_pri_v(self):
        return self.__pri_v
        # プライベート化されたインスタンス変数をgetterメソッドを使って出力する。

    def set_pri_v(self, pri_v="pri"):
        self.__pri_v = pri_v
        # 必要なものだけ外部からも変更できるようにする


test = Test()
print(test.get_pri_v())

test.set_pri_v("setterメソッドを使えば関数内部のプライベート関数に入力できる")
print("getterメソッドでプライベート化されているインスタンスを出力できる:"+test.get_pri_v())
