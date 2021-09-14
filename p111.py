import re

sentence_list = ["電話番号は0120-0000-1111だったかな。", "0120-0-222だったかもね、", "0120-0000-3333のはず",
                 "いや0120-00-44444だ", "おれは0120-000-5555だと思う", "やっぱり"
                 ]
pattern = "0120-[0-9]{2,4}-[0-9]{4}"

for sentence in sentence_list:
    match = re.match(pattern, sentence)
    print("matchの機能確認\n正規表現：" + pattern + "\n結果:")
    if match is not None:
        print("group():{}".format(match.group()))
        print("start():{}".format(match.start()))
        print("end():{}".format(match.end()))
        print("span():{}".format(match.span()))
    else:
        print("正規表現と一致しませんでした")
    print("-"*20)
