# 例外クラス　Exception OSError IndexError

'''
OSError: 出入力のエラーを扱う。
IndexError: リストの範囲外にアクセスした場合を扱う。
このエラークラスとその使い方について覚えておくべきことは3つあります。 
1.「発生したエラーの種類に応じ、呼び出されるエラーのクラスが異なる」 
たとえば、IOErrorはまったく関係ないエラーである0による除算では利用されません。 
そのため、エラーパターンを想定し、好きなだけexceptブロックを作ることができます(3)。
'''
try:
    f = open('helloworld.txt', 'r')
except OSError:
    print('os error')
except Exception:
    print('exception')

'''
2.「exceptに親クラスを指定した場合は子クラスのエラーも対応できる」 
たとえばOSErrorの例外は親クラスであるExceptionで対応可能です。 
サンプルプログラムの「except Exception as e」のeに ExceptionクラスではなくZeroDivisionError のクラスのインスタンスが入っていたことでも分かります。
次のプログラムを実行すると、2番目のexceptが呼び出されます。これは1番目のexceptがエラーにマッチせず、無視されるためです。
OSErrorが1番目に指定されていても、5/0で発生したエラーはOSErrorではなくZeroDivisionErrorなのでマッチしません。
しかし、2番目のExceptionはZeroDivisionErrorの親クラスなのでマッチし、"excepttion"が呼び出されます。
なお、エラークラスの親子関係は__base__で調べられます。
'''
try:
    5/0
except OSError:
    print('os error')
except Exception:
    print('exception')


'''
3.「エラーをキャッチするexcept は複数書くことができる」
複数書いた場合は先頭から順にチェックしていき、最初にマッチした処理が実行されます。
どのexceptもマッチしなければ例外処理が実行できずにエラーでプログラムそのものが停止してしまいます。
'''

# なお、例外クラスの利用はバグ対応に使うべきではない。

'''
例外クラスの主な親子関係
BaseException------Exception--------------ArithmetricError-----ZeroDivisionErro
               |                    |                       |--OverflowError
               |                    |
               |-SystemExit         |-OSError------FileNotFoundError
               |                    |          |---TimeoutError
               |-keybordinterrupt   |
                                    |-LookupError---IndexError
                                                  |-KeyError
'''
