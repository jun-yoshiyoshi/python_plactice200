import re

sentence = """ 電話番号は0120-0000-1111だったかな。0120-0-222だったかもね、0120-0000-3333のはず。いや0120-00-44444だ, おれは0120-000-5555だと思う。やっぱり。"""

pattern = "0120-[0-9]{2,4}-[0-9]{4}"
rep_word = "フリーダイヤル"

res = re.sub(pattern, rep_word, sentence)
print("subの機能確認\n正規表現" + pattern)
print("置換文字列" + rep_word + "\n結果：\n"+res)
