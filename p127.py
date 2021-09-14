# クラスの作成　コンストラクタ(インスタンス生成の初期設定メソッド)　デクストラクタ(メモリ開放メソッド)
class Color:
    def __init__(self, text="red"):
        self.text = text

    def __del__(self):
        print(str(self) + "が破棄されました")
    # デクストラクタは必須ではない


color = Color()
print(color.text)
print(color)

color2 = Color("green")
print(color2.text)
print(color2)
