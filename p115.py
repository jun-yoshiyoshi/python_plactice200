import re
# p112.pyを参照
sentence = "電話番号は0120-0000-1111だったかな。0120-0-222だったかもね、0120-0000-3333のはず。いや0120-00-44444だ, おれは0120-000-5555だと思う。やっぱり。"
pattern = "0120-[0-9]{2,4}-[0-9]{4}"
re_comp = re.compile(pattern)
match_list = re_comp.findall(sentence)
print("findall,compileの機能確認\n正規表現：" + pattern + "\n結果:")
if len(match_list) > 0:
    for _ in match_list:
        print(_)
else:
    print("正規表現と一致するものはありません")

# p114.pyを参照
rep_word = "フリーダイヤル"
res = re_comp.sub(rep_word, sentence)
print("sub,compileの機能確認\n正規表現" + pattern)
print("置換文字列" + rep_word + "\n結果：\n"+res)
