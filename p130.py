# private変数
class Test:
    def __init__(self, pub_v="pub", pri_v="pri"):
        self.pub_v = pub_v
        self.__pri_v = pri_v


test = Test()
print(test.pub_v)
print(test.__pri_v)
# __pri_vはprivate変数なのでエラーとなる
