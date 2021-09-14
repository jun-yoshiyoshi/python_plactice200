from thero import Hero


class Mapping:
    def __init__(self):
        # 自分自身のインスタンスを渡す(相互参照になる)
        self.hero = Hero(self)
        # Heroクラスが使うメソッド

    def function_a(self):
        print('Map: function a')

    # Heroクラスでは使わないメソッド
    def function_b(self):
        print('Map: function b')

    def test(self):
        self.hero.test()
