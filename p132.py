# private変数と混同しやすい同名の変数
class Test:
    def __init__(self, pub_v="pub", pri_v="pri"):
        self.pub_v = pub_v
        self.__pri_v = pri_v

    def get_pri_v(self):
        return self.__pri_v
        # 取得用メソッド:__pri_vが戻り値となる


test = Test()
print(test.pub_v)
print(test.get_pri_v())

test.__pri_v = "class Testとは無関係の同名変数"
print("取得用メソッドの機能確認："+test.get_pri_v())
print("private変数の同名変数："+test.__pri_v)
