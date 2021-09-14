# 変数のスコープ(範囲) if文と　for文
global_v = "global"

# if文と変数
if True:
    # ifブロックからでもグローバル変数は参照できる
    print("0:{0}".format(global_v))
    # ifブロックからでもグローバル変数を変更できる
    global_v = "if1_local"
    # ifブロックからローカル変数を設定できるし、当然に変更できる
    local_v = "if2_local"
    print("1:{0}".format(global_v))
    print("2:{0}".format(local_v))
print("3変更されたgloval_v:{0}".format(global_v))
print("4:{0}".format(local_v))

print("-"*10)

for _ in range(3):
    # forブロックからグローバルへンスは参照できる
    print("0:{0}".format(global_v))
    # forブロックからグローバル変数の変更できる
    global_v = "for1_local"
    local_v = "for2_local"
    print("1:{0}".format(global_v))
    print("2:{0}".format(local_v))
print("-"*10)
print("3変更されたglobal_v:{0}".format(global_v))
print("4:{0}".format(local_v))
