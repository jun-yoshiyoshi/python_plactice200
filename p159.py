# フレームワーク (手を加えない)
class Calc:
    # 初期化でカスタマイズ用の関数定義を受取り登録
    def __init__(self, list_data):
        self.operation_dict = {}
        # 入力される処理と対応する関数を格納するための辞書型インスタンス変数
        for t in list_data:
            operation, method = t
            # 入力されたリスト内のデータのインスタンスにする
            self.operation_dict[operation] = method
            # 辞書型のインスタンスにする
            # print(f"辞書型になる前のインスタンス:{operation, method}")
            # print(f"辞書型になった後のインスタンス:{self.operation_dict}")

        # イベントドリブンで電卓として動く

    def run(self):
        while True:
            text = input('please input your calculation:')
            words = text.split()
            if words[0] == 'exit':
                return
            if len(words) < 3:
                # データが欠損している場合
                continue
            if words[0] not in self.operation_dict:
                # 誤入力がある場合
                continue

            # カスタマイズされた関数を呼び出す
            fun = self.operation_dict[words[0]]
            print(fun(int(words[1]), int(words[2])))


def add(a, b):
    return a + b


def decrease(a, b):
    return a - b


calc = Calc([("plus", add), ("minus", decrease)])

calc.run()
