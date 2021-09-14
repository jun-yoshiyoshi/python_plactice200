# コンポジションのアップデート。　p155.pyに全てのログを残す機能を追加する
# メインとなるクラスを触らず、サブクラスをアップデートする。

import time


class Secretary:
    def __init__(self):
        self.logfile = "インスタンス変数logfileを作り、初期値を定める"

    def write_log(self, text):
        log = f"{time.ctime()}:{text}\n"
        f = open(self.logfile, "a")
        # open関数の引数"a"は"追記用読み込み"
        f.write(log)
        # 読み込んだファイルに書き込み
        f.close()
        # 読み込んだファイルを閉じる

    def get_log(self):
        f = open(self.logfile, "r")
        log = f.read()
        f.close()
        return log
