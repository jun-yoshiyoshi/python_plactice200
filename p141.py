# 簡単なジェネレーター
def power_gene():
    for num in range(1, 6):
        print(f"{num}の{num}乗")
        yield num ** num


def power_gene2():
    num = 1
    while True:
        yield num ** num
        num += 1


for res in power_gene():
    pass

print("-" * 10)

for res in power_gene():
    print(res)

print("-" * 10)
pg = power_gene2()
for _ in range(5):
    print(next(pg))
