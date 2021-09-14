content = """ \
    writeの機能確認
    abcdef
    123456
    ABCDEF
"""
with open("test_w.txt", "w") as fp:
    fp.write(content)

content_utf = """test_w_utf.txtの機能確認
あいうえお
ABCDEFG
！ ” ＃ ＄ ％ ＆ ’ ’ （ ）
"""
with open("test_w_utf.txt", "w", encoding="utf-8") as fp:
    fp.write(content_utf)

l = ["writelinesの機能確認", "0123456789\n", "abcdefghojk\n", "あいうえおかきく"]
with open("test_w_utf.txt", "w", encoding="utf-8") as fp:
    fp.writelines(l)

f = "no_exist.txt"
try:
    with open(f, "r") as f:
        content = f.read()
    print(content)
except FileNotFoundError:
    print(f + "は見つかりませんでした")
except UnicodeDecodeError:
    print(f + "でコードできません。文字コードを確認してください")
except Exception as e:
    print(f"{f}において例外{e}が発生しました")
