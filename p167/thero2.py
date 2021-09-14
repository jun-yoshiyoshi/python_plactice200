from tmap import Map
# 相互参照になるのでimportできない。エラーになる。
# 相互参照になる複数のクラスは異なるモジュールに分けて実装することはできない。


class Hero:
    def __init__(self, _):
        self.map = _

    def test(self):
        self.map.function_a()
        self.map.function_b()


# class Map:
#     def __init__(self):
#         # 自分自身のインスタンスを渡す(相互参照になる)
#         self.hero = Hero(self)
#         # Heroクラスが使うメソッド

#     def function_a(self):
#         print('Map: function a')

#     # Heroクラスでは使わないメソッド
#     def function_b(self):
#         print('Map: function b')

#     def test(self):
#         self.hero.test()


map_ = Map()
map_.test()
# Map: function a
# Map: function b
