# クロージャ　テンプレートとなる関数からカスタム関数を生成

# 関数を作る関数　クロージャ
def adder(x):
    def fun(y):
        return x + y
    return fun


adder5 = adder(5)
print(adder5(10))
# 15

adder7 = adder(7)
print(adder7(10))
