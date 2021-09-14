# reduce関数(畳み込み)　第一引数に作用させる関数、第二引数にリスト型データ
# 戻り値は第一引数の関数に依存
import random
import functools


def adder(a, b):
    # 第一引数、第二引数はともにint型になる。
    return a + b


result = functools.reduce(adder, range(1, 7))
# reduce関数を用いることでリスト型を入力できるようになる
print(result)


def get_bigger(a, b):
    if (a > b):
        return a
    else:
        return b


l = [random.randint(0, 100) for _ in range(10)]

biggest = functools.reduce(get_bigger, l)
print(l)
print(biggest)
