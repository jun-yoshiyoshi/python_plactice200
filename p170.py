
# issubclass関数、__base__メソッド
# 1.すでに利用している自分が作った既存のクラスを継承する場合(コンポジションで実現できる場合が多い)

class MyClassA:
    pass


class MyClassB(MyClassA):
    pass


class MyClassC(MyClassB):
    pass


class MyClassD(MyClassA):
    pass


print(issubclass(MyClassB, MyClassA))
# True
print(issubclass(MyClassA, MyClassB))
# False
print(issubclass(MyClassC, MyClassA))
# True 孫でもTrueを返す
print(issubclass(MyClassD, MyClassB))
# False

# type関数と組み合わせてインスタンスの親子関係の確認ができる
a, b = MyClassA(), MyClassB()
print(issubclass(type(b), type(a)))


# サブクラスから親クラスを呼び出す
print(MyClassA.__base__)
# <class 'object'>
print(MyClassB.__base__)
# <class '__main__.MyClassA'>
print(MyClassC.__base__)
# <class '__main__.MyClassB'>
