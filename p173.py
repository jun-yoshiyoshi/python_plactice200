# ポリモーフィズム
# 1.呼び出されるメソッドは親クラスで実装する
# 2.共通する処理は親クラスに任せる
# 3.子クラスは親クラスとの差分のみ実装する

class Graphic:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def draw(self):
        print("Error")


rectangle = '''({},{})
#######
#     #
#     #
#######
({},{})'''


class Rectangle(Graphic):
    def draw(self):
        print(rectangle.format(self.x1, self.y1, self.x2, self.y2))


triangle = '''({},{})
#
# #
#   #
#     #
#########
({},{})'''


class Triangle(Graphic):
    def draw(self):
        print(triangle.format(self.x1, self.y1, self.x2, self.y2))


# 1.どの図形、座標とするか
graphic_type = 'rectangle'
#graphic_type = 'triangle'
x1, y1, x2, y2 = 1, 2, 3, 4
#x1, y1, x2, y2 = 5, 6, 7, 8
# 2.入力された図形に応じて子クラスのインスタンスを作成
if (graphic_type == 'rectangle'):
    graphic = Rectangle(x1, y1, x2, y2)
elif (graphic_type == "triangle"):
    graphic = Triangle(x1, y1, x2, y2)
else:
    graphic = Graphic(x1, y1, x2, y2)

# 2.オーバーライドされた親クラスも持つメソッドの呼び出し
graphic.draw()
