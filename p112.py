import re

sentence = "電話番号は0120-0000-1111だったかな。0120-0-222だったかもね、0120-0000-3333のはず。いや0120-00-44444だ, おれは0120-000-5555だと思う。やっぱり。"
pattern = "0120-[0-9]{2,4}-[0-9]{4}"
match_list = re.findall(pattern, sentence)
print("findallの機能確認\n正規表現：" + pattern + "\n結果:")
if len(match_list) > 0:
    for _ in match_list:
        print(_)
else:
    print("正規表現と一致するものはありません")
