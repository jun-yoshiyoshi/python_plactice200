# 変数のスコープ(範囲) 関数
global_v = "global"


def scope_test():
    print(f"関数内部からglobal変数の参照:{global_v}")


scope_test()
print("-"*10)


def scope2_test():
    global_v = "宣言無く関数内部でglobal変数を変更"
    local2_v = "local"
    print(f"1:{global_v}")
    print(f"2:{local2_v}")


scope2_test()
# 関数内部でglobal変数を変更しても外部には引き継がれない
print(f"3:{global_v}")
# print(f"4:{local2_v}")
# 関数内部のlocal変数は外部から参照できずエラーになる
print("-"*10)


def scope3_test():
    global global_v
    global_v = "宣言して関数内部でglobal変数を変更"
    local3_v = "local"
    print(f"5:{global_v}")
    print(f"6:{local3_v}")


scope3_test()
print(f"7:{global_v}")
# print(f"8:{local3_v}")
# 関数内部のlocal変数は外部から参照できずエラーになる
