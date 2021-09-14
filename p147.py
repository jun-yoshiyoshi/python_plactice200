# ネストの上位のlocal変数を下位の関数内部で変更する
def scope_test():
    val_1 = "val_1"
    val_2 = "val_2"

    def innerscope_test():
        nonlocal val_1
        val_1 = "宣言してネストされた関数内部でローカル変数を変更"
        val_2 = "宣言せずネストされた関数内部でローカル変数を変更"
    innerscope_test()
    return val_1, val_2


res = scope_test()
print(res)
