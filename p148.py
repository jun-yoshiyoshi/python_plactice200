global_v = "global"


def scope_test():
    # print(f"宣言無しでglobal_vを参照:{global_v}")
    global global_v
    print(f"関数内で宣言後にglobal_vを参照:{global_v}")
    # 関数ブロックからグローバル変数の変更
    global_v = "関数内で宣言後にglobal_vを変更"
    local_v = "ローカル変数"
    print(f"1:{global_v}")
    print(f"2:{local_v}")


scope_test()
print(f"3:{global_v}")
# print(f"4:{local_v}")
