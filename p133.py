# 代入用メソッドsetter
class Test:
    def __init__(self, pub_v="pub", pri_v="pri"):
        self.pub_v = pub_v
        self.__pri_v = pri_v

    def get_pri_v(self):
        return self.__pri_v
        # 取得用メソッド:__pri_v(変数)が戻り値となる

    def set_pri_v(self, pri_v="pri"):
        self.__pri_v = pri_v
        # 代入用メソッド:private変数に代入するためのメソッド


test = Test()
print(test.pub_v)
print(test.get_pri_v())

test.__pri_v = "class Testとは無関係の同名変数"
print("private変数の同名変数："+test.__pri_v)

test.set_pri_v("setterの機能確認")
print("getterの機能確認:"+test.get_pri_v())
