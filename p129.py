# 複数インスタンスの生成
class Color:
    def __init__(self, r_name="red", g_name="green", b_name="blue"):
        self.r_name = r_name
        self.g_name = g_name
        self.b_name = b_name

    def name_p(self, delim=","):
        r, g, b = self.r_name, self.g_name, self.b_name
        print(f"{r}{delim}{g}{delim}{b}")


color_1, color_2 = Color("赤", "緑", "青"), Color(g_name="midori")

color_1.name_p("|")
color_2.name_p()


color_1.r_name, color_2.r_name = "あか", "きいろ"

color_1.name_p("#")
color_2.name_p("-")
