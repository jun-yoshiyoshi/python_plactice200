# ドキュメンテーション　docstring 特殊属性　__doc__
import p182_2


def test_function(x, y):
    """ドキュメントを試す関数(何を目的としたクラス・関数・モジュール・メソッドか )

    引数: 
        x (int): ひとつ目の引数
        y (str): ふたつ目の引数 
    返り値: 
        str:引数を結合した文字列 
        """

    return str(x) + y


# help(test_function)
print("-"*10)
help(p182_2.test_function2)
print("-"*10)
print(p182_2.test_function2.__doc__)
