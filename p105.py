sentence = "あいうえお１２３４５あ　a b c d e い"
print(sentence.replace("いう", "イウ").replace("abc", "ABC"))

trans_table = str.maketrans("お", "！", "abde")
# 第三引数は削除対象文字
print(sentence.translate(trans_table))

print("元となる文章：" + sentence)
print("strip(\'あい\'):" + sentence.strip("あい"))
print("lstrip(\'あい\'):" + sentence.lstrip("あい"))
print("rstrip(\'あい\'):" + sentence.rstrip("あい"))
sentence = "\tあいうえお１２３４５あ\n　a b c d e い\n"
print(sentence.strip())
sentence = "\tあいうえお１２３４５あ\n　a b c d e い\n"
print(sentence.rstrip())
sentence = "\tあいうえお１２３４５あ\n　a b c d e い\n"
print(sentence.lstrip())
