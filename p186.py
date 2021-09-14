# カスタム例外クラスの作成 自分で作る例外クラスで処理する

class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


try:
    raise MyError('my error happens')

except MyError as e:
    print(type(e))
    print(e)

'''
例外クラスを省略してtry/catchを使うこともできます。
ただ、その場合は暗黙的にBaseExceptionを対象として例外処理がされるため、可能な限り利用は避けて下さい。
例えば以下のコードですとpythonのプログラムを終了するexit関数ですら例外として処理されてしまいます。
try:
    exit()
except:
    print('error')
自分が意図していない例外処理が働いてしまわないように注意をしてください。   
'''
