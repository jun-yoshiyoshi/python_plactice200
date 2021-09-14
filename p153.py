# _と__の機能　が、

class test_private:
    def __init__(self):
        self._var1 = 'v1'
        self.__var2 = 'v2'

    def _method1(self):
        print('先頭に_がついた変数、メソッドは外部からアクセスできる')

    def __method2(self):
        print('先頭に__がつく変数、メソッドは外部からアクセスできない')

    def method3(self):
        print(self._var1)
        print(self.__var2)
        self._method1()
        self.__method2()


instance = test_private()
print(instance._var1)
print(instance._method1())
# print(instance.__var2)
# print(instance.__method2())
print(instance.method3())

print(dir(instance))
# マンダリン具処理されたリストを出力

instance._test_private__var2 = "マンダリング処理された__var2"
print(instance.method3())
