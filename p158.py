# 関数渡し(関数は他のデータと同様にオブジェクトとして扱える)

def fun1(fun, text):
    fun(text)


def fun2(text):
    print("hello!" + text)


fun1(fun2, "world!")
