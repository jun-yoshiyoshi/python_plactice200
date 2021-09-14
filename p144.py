# 実行中ファイル、モジュールのファイル名、モジュール名(path)の取得

import mojule_2


def main():
    print(__file__ + "は実行中のモジュールです。")


print("__ name__：" + __name__)
print("__ file__：" + __file__ + "\n")

if __name__ == "__main__":
    main()
# 実行中モジュールかの判定を行い、真のとき main()　を実行。
