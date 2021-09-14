sentence = input("文章を入力してください：")
search = input("判定する文字列を入力してください：")
res = search in sentence
res_1 = sentence.startswith(search)
res_2 = sentence.endswith(search)

print("[in]検索文字列：{}、結果:{}".format(search, res))
print("[startswith]検索文字列：{}、結果:{}".format(search, res_1))
print("[endswith]検索文字列：{}、結果:{}".format(search, res_2))
