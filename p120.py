l_0 = []
for _ in range(1, 10):
    l_0.append(_)

l_1 = [_ for _ in range(1, 10)]

print(f"{l_0}\n{l_1}")

l_2 = []
for _ in range(1, 30):
    if _ % 3 != 0:
        l_2.append(_)

l_3 = [_ for _ in range(1, 30) if _ % 3 != 0]
print(f"{l_2}\n{l_3}")

l_4 = []
for _ in range(1, 30):
    if _ % 3 != 0:
        l_4.append(_)
    else:
        l_4.append(_*10)

l_5 = [_ if _ % 3 != 0 else _*10 for _ in range(1, 30)]
print(f"{l_4}\n{l_5}")

d = {i: i ** 2 for i in range(10)}
print(d)

d = {i: i ** 2 for i in range(1, 10)}
print(d)
