# \エスケープシークエンスの用法
print(a, "\\", b)  # 円マーク、バックスラッシュ
print(a, "\"", b)
print(a, "\'", b)
print(a, "\a", b)  # アラート
print(a, "\b", b)  # バックスペース
print(a, "\r", b)  # キャリッジリターン、カーソルを文頭へ戻す
# \f 改ページ
print(a, "\n", b)  # 改行
print(a, "\t", b)  # 水平タブ
print(a, "\v", b)  # 垂直タブ

val = "formatメソッドの中括弧をエスケープ"
print("{}{{}}".format(val))
