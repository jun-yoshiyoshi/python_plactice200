# コンポジション(オブジェクションを他のオブジェクションと関係づける)
import time


class Manager:
    # 計算ができないマネージャーはエンジニアに計算をしてもらう
    # エンジニアにデータを渡す業務を行う
    # エンジニアから受け取ったデータを出力する
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
        # Secretaryから記録した業務記録を受け取って出力する


class Engineer:
    # エンジニアはマネージャーから受け取り、そのデータを使って計算する
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b


class Secretary:
    # マネージャーの業務状態を記録する
    def __init__(self):
        self.log = []

    def write_log(self, text):
        self.log.append(f"{time.ctime()}:{text}")

    def get_log(self):
        return "\n".join(self.log)
        # 業務記録のリストデータを改行して一まとまりにする。


bob = Manager()
bob.work_a()
# 8
bob.work_b()
# 12
bob.work_c()

bob.work_d()

bob.work_e()
