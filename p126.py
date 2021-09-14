def func(_):
    return int(_) * 5


print(func(5))
print((lambda _: _*5)(5))


def func_conv(_):
    if " " in _:
        res = _.title()
    else:
        res = _.upper()
    return res


print(func_conv("helloworld"))
print(func_conv("hello world"))

print((lambda _: _.title() if " " in _ else _.upper())("helloworld"))
print((lambda _: _.title() if " " in _ else _.upper())("hello world"))

l = ["helloworld", "hello world"]
for i in map(lambda _: _.title() if " " in _ else _.upper(), l):
    print(i)
