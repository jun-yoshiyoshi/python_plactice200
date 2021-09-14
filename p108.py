sentence = input("find,rfindの機能確認　文字列を入力してください：")
# 検索対象は先頭から一つめの位置のみ検出。第二引数で検索開始位置と終了位置を指定できる。
search_1 = input("検索文字１を入力してください")
point_1 = sentence.find(search_1)
search_2 = input("検索文字２を入力してください")
point_2 = sentence.find(search_2)
search_3 = input("検索文字３(rfind)を入力してください")
point_3 = sentence.rfind(search_3)

print("検索文字:{},結果:{}".format(search_1, point_1))
print("検索文字:{},結果:{}".format(search_2, point_2))
print("検索文字:{},結果:{}".format(search_3, point_3))

search_4 = input("検索文字４を入力してください：")
point_4 = sentence.find(search_4)
while point_4 != -1:
    point = sentence.find(search_4, point_4)
    if point == -1:
        break
    print("検索文字４:{},結果:{}".format(search_4, point))
    point_4 = point + 1
