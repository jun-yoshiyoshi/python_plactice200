fp = open(R"C:\Users\adsol\OneDrive\ドキュメント\Python Scripts入門\100Pack\200pack\test.txt")
content = fp.read()
print("readの機能確認：\n"+content)
fp.close()


fp_2 = open("test2.txt")
# 200packと同じフォルダ内に配置
content_2 = fp_2.read()
print(content_2)
fp_2.close()


fp = open(R"C:\Users\adsol\OneDrive\ドキュメント\Python Scripts入門\100Pack\200pack\test.txt")
content_3 = fp.readlines()
print("readlinesの機能確認：")
for _ in content_3:
    print(_)
fp.close()

fp_2 = open("test2.txt")
content_2 = fp_2.read()
print("forループを使って：")
for _ in content:
    print(_)
fp_2.close()

fp_3 = open("test3.txt", encoding="utf-8")
# マルチバイト文字列が含まれているとき。"cp932"エラー。
content_3 = fp_3.read()
print(content_3)
fp_3.close()
