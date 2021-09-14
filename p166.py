# 内包表記
# リスト内包表記
import random
l = [_ for _ in range(10)]
print("l", l)
l2 = [_ for _ in range(10) if _ % 2 == 0]
print("l2", l2)


# 辞書内包表記１
t_list = [("apple", "red"), ("book", "paper"), ("cat", "animal"), ("day", "sun")]
d = {key.upper(): value for key, value in t_list}
print("t_list", t_list)
print("d", d)

# 辞書内包表記２ 辞書データ内のkeysとvaluesの入れ替え
d2 = {value.upper(): key for key, value in d.items()}
print("d2", d2)

t_list2 = [("apple", "red"), ("book", "paper"), ("cat", "animal"), ("car", "red")]
d3 = {value.upper(): key for key, value in t_list2}
print("d3", d3)
# "RED"のバリューが"car"で上書きされる

# セット内包表記
l3 = [random.randint(1, 5) for _ in range(10)]
s = {_ for _ in l3}
print("l3", l3)
print("s:", s)
