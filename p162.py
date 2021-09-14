# ラムダ関数

funcs = [(lambda x, y: x + y), (lambda x, y: x - y), (lambda x, y: x * y), (lambda x, y: x ** y)]

for fun in funcs:
    print(fun(5, 10))
