# メソッドの定義
class Color:
    def __init__(self, r_name="red", g_name="green", b_name="blue"):
        self.r_name = r_name
        self.g_name = g_name
        self.b_name = b_name

    def name_p(self, delim=","):
        r, g, b = self.r_name, self.g_name, self.b_name
        print(f"{r}{delim}{g}{delim}{b}")

    def __del__(self):
        print(str(self) + "が破棄されました")


color = Color("赤", "緑", "青")
color.name_p("|")
