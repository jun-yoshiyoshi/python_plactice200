sentence = input("index,rindexの機能確認　文字列を入力してください：")
# 検索対象が存在しなかった場合エラーで終了する
search_1 = input("検索文字１を入力してください")
point_1 = sentence.index(search_1)
search_2 = input("検索文字２を入力してください")
point_2 = sentence.index(search_2)
search_3 = input("検索文字３(rindex)を入力してください")
point_3 = sentence.rindex(search_3)

print("検索文字:{},結果:{}".format(search_1, point_1))
print("検索文字:{},結果:{}".format(search_2, point_2))
print("検索文字:{},結果:{}".format(search_3, point_3))
