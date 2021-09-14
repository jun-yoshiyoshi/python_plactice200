# map関数 第一引数に関数、第二引数に関数を適用させたいリストデータをとる
# 戻り値は,map object

import random
map_object = map(lambda x: x * (x + 2) * (x * 3), range(10))
print(map_object)
print(list(map_object))

text_list = ['ab', 'cd', 'ef']
map_object = map(lambda x: x.upper(), text_list)
print(list(map_object))


def get_random_list(length):
    return list(map(lambda x: random.randint(0, 100), range(length)))
# map関数を使った特殊な内包表記


print(get_random_list(10))
