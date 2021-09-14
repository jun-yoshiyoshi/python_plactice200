# スタックトレース　正しくエラーをキャッチする
'''
エラー出力はスタックトレースと呼ばれ、コードのどこでどのように失敗しているかの詳細を出力してくれます。
'''


class A:
    def test(self, b):
        return b.div(0)


class B:
    def div(self, value):
        return 5/value


a = A()
b = B()
value = a.test(b)

'''
実行すると0による割り算が発生し、エラーとなる。
スタックトレースは
Traceback (most recent call last):
  File   _______  \p188.py", line 21, in <module>
    value = a.test(b)
  File " ________  \p188.py", line 11, in test
    return b.div(0)
  File " _________\p188.py", line 16, in div
    return 5/value
ZeroDivisionError: division by zero

“return 5/ value” を実行し、そこで ZeroDivisionErrorとなったことが分かります。

'''
