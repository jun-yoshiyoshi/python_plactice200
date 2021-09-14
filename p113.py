import re

sentence = "電話番号は0120-0000-1111だったかな。0120-0-222だったかもね、0120-0000-3333のはず。いや0120-00-44444だ, おれは0120-000-5555だと思う。やっぱり。"
pattern = "0120-[0-9]{2,4}-[0-9]{4}"
match_iter = re.finditer(pattern, sentence)
print("finditerの機能確認\n正規表現：" + pattern + "\n結果:")
flag = True
for match in match_iter:
    print(f"group():{match.group()}")
    print(f"group():{match.start()}")
    print(f"group():{match.end()}")
    print(f"group():{match.span()}")
    print("-"*20)
    loop_flab = True
if not flag:
    print("正規表現と一致するものはありません")
