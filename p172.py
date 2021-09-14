# 呼び出し「オーバーライドした子のクラスメソッド」から「オーバーライドされた親のクラスメソッド」を呼び出す
# super()関数
class Register:
    def __init__(self, dbip):
        self.dbip = dbip

    def register(self, text):
        print('write "{}" to DB Server at {}'.format(text, self.dbip))


class ConsoleRegister(Register):
    def __init__(self, dbip):
        super().__init__(dbip)  # Register.__init__(dbip)

    def register(self):
        text = 'input from Console'
        super().register(text)  # Register.__init__(dbip)


class WebRegister(Register):
    def __init__(self, dbip):
        super().__init__(dbip)

    def register(self):
        text = 'input from REST'
        super().register(text)


c = ConsoleRegister('10.0.0.1')
c.register()
# write "input from Console" to DB Server at 10.0.0.1

w = WebRegister('10.0.0.1')
w.register()
# write "input from REST" to DB Server at 10.0.0.1
