# コンポジションのアップデート。　p155.pyに全てのログを残す機能を追加する
# メインとなるクラスを触らず、サブクラスをアップデートする。
import time
from p156_e import Engineer
from p156_s import Secretary


class Manager:

    def __init__(self):
        self.tom = Engineer()
        self.mari = Secretary()

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


bob = Manager()
bob.work_a()
bob.work_b()
bob.work_c()
bob.work_d()
bob.work_e()
