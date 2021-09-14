# コンポジションのアップデート。　セクレタリーはマネージャーとクライアントのアポイントを調整する。
# 新しくクライアントクラスを作り、メインクラスに最小限の変更を加え、サブクラスをアップデートする。
import time
from p157_s import Secretary
from p157_c import Client
from p156_e import Engineer


class Manager:

    def __init__(self):
        self.tom = Engineer()
        self.mari = Secretary()

    def check_schedule(self):
        schedule = self.mari.get_schedule()
        print(schedule)

    def get_secretary(self):
        return self.mari

    def work_a(self):
        self.mari.write_log("start")
        result = self.tom.add(5, 3)
        time.sleep(1)
        print(result)
        self.mari.write_log("end")

    def work_b(self):
        self.mari.write_log("start")
        result = self.tom.add(8, 4)
        time.sleep(2)
        print(result)
        self.mari.write_log("end")

    def work_c(self):
        self.mari.write_log("start")
        result = self.tom.multiply(5, 3)
        time.sleep(3)
        print(result)
        self.mari.write_log("end")

    def work_d(self):
        self.mari.write_log("start")
        result = self.tom.multiply(8, 4)
        time.sleep(4)
        print(result)
        self.mari.write_log("end")

    def work_e(self):
        print(self.mari.get_log())
