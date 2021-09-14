# private変数　外部からアクセスしようとする場合にエラーとなる
class Test:
    def __init__(self, pub_v="pub", pri_v="pri"):
        self.pub_v = pub_v
        self.__pri_v = pri_v

    def get_pri_v(self):
        return self.__pri_v
        # __pri_vが戻り値となる取得用メソッド


test = Test()
print(test.pub_v)
print(test.get_pri_v())

# print(test.__pri_v)
