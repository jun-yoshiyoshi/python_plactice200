# イテレータのクラス実装
class PowerIter:
    def __init__(self, val):
        self.val = val

    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        if self.num > self.val:
            raise StopIteration
        res = self.num ** self.num
        self.num += 1
        return res


power_iter = PowerIter(10)
for p in power_iter:
    print(p)
