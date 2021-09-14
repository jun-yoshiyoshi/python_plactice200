# 例外発生のコントロール　ネットワーク上のレスポンスに依存するプログラムなど

try:
    a = 0
    if (a == 0):
        raise Exception("hello")
        5/a
except Exception as e:
    print(type(e))
    print(e)

''' 
Pythonはraiseキーワードを使って例外発生を意図的に行える。
この例の場合、0での除算は禁止事項のため、除数が０出ないかをif文でチェックしています。
そして、0であった場合にはZeroDivisionErrorを出さないよう、raiseを使ってコントロールできる
Exceptionを発生させています。
'''
