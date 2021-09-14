# 例外処理  基本は返り値チェックとtry/catchの２パターン
# Exception 例外クラス
'''返り値チェック
ある関数を呼び出した時、処理に失敗したときの返り値があるとき、その返り値をチェックして例外処理を行う。'''

i = "23456".find("23")
print(i)

i = "23456".find("hello")
print(i)
# 返り値によって例外処理（if文）を作る

print("-"*10)

i = "23456".index("23")
print(i)

# i = "23456".index("hello")
# print(i)
print("-"*10)

''' try/chatch
エラーが生じる可能性があり、対処が必要な個所をtryブロックにし、エラーが生じたときにexceptブロックに飛ばす。'''


def contains(text1, text2):
    try:
        text1.index(text2)
        return True
    except Exception:  # Exceptionは例外クラス
        return False


print(contains("12345", "34"))

print(contains("12345", "hello"))

print("-"*10)

print('1:outside of try/ catch')

try:
    print('2:inside of try scope')
    5 / 0
    print('3:inside of try scope')
except Exception as e:  # 例外を変数に格納する
    print('4:inside of except(catch) scope')
    print(type(e))
    print(e)

print('5:outside of try/ catch')
