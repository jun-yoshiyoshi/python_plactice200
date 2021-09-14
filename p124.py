import sys
print(sys.argv)
# コマンド入力された引数はsys.argvのリストに追加される
# コマンド引数に複数ファイルを入力するときには、", "を間に挿入する
for _ in sys.argv:
    print(_)
print("-" * 20)

for _ in sys.argv[1:]:
    print(_)
