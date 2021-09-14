# 高度な例外処理 else finally
# else: 例外が発生しなかった場合にのみ処理される
# finally:　例外が発生してもしなくても処理を行う

try:
    print('1: start of try')
    5 / 0
    print('2: end of try')
except Exception:
    print('3: error happens')

else:
    print("4: error doesn' t happen")

finally:
    print('5: finally')


try:
    print('1: start of try')
    # 5/0
    print('2: end of try')
except Exception:
    print('3: error happens')
else:
    print("4: error doesn' t happen")
finally:
    print(' 5: finally')
