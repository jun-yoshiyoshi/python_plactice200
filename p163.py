# filter関数 第一引数に条件、第２引数にリスト型データ
# 戻り値はfilter object

def is_even(x):
    return x % 2 == 0


filter_object = filter(is_even, range(20))
print(filter_object)
print(list(filter_object))

filter_object = filter(lambda x: x % 3 == 0, range(20))
print(list(filter_object))
