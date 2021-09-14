import sys
import os
import re
# python p125.py test_1.txt,test_2.txt,test_3.txt
try:
    for r_file_path in sys.argv[1:]:
        base, ext = os.path.splitext(r_file_path)
        # ファイル名を拡張子と分離する
        w_file_path = base + "_done" + ext
        r_content = ""
        with open(r_file_path, "r", encoding="utf-8") as r_fp:
            r_content = r_fp.read()
            w_content = re.sub("[0-9]{4,8}", "*******", r_content)
        with open(w_file_path, "w") as w_fp:
            w_fp.write(w_content)

        print("読込:" + r_file_path)
        print("出力:" + w_file_path)
        print("-" * 30)
except Exception as e:
    print(str(e) + "が発生しました")
