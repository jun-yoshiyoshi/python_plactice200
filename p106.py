sentence = input("isalphaの機能確認")
print(sentence.isalpha())
# 言語文字のみ含むときTrue 半角数字または全角数字,記号(スペースを含む)が含まれるときFalse

sentence = input("isdigitの機能確認")
print(sentence.isdigit())
# 半角・全角数字のみ含むときTrue

sentence = input("isalnumの機能確認")
print(sentence.isalnum())
# 言語文字判定True 数字・記号(スペースを含む)が含まれるとFalse

sentence = input("isnumeric機能確認")
print(sentence.isnumeric())
# 半角・全角数字および漢数字のみ含むとき（混在も）True　記号(スペースを含む)が含まれるとFalse

sentence = input("isdecimalの機能確認")
print(sentence.isdecimal())
# 半角・全角の十進法の整数（半角・全角の混在、0が頭についている正の整数）True

sentence = input("isupperの機能確認")
print(sentence.isupper())
# 1.半角・全角の大文字のみ 2.スペースやタブのみを含む 3.小文字を含んでいない（大文字を含む）ときTrue

sentence = input("islowerの機能確認")
print(sentence.islower())
# 1.半角・全角の小文字のみ 2.スペースやタブのみを含む 3.大文字を含んでいないとき（小文字を含む）True

sentence = input("isspaceの機能確認")
print(sentence.isspace())
# 半角・全角スペース\n\tのみのときTrue

sentence = input("istitleの機能確認")
print(sentence.istitle())
# 単語全ての１文字目が半角・全角アルファベット大文字のとき(数字は無視される)True
