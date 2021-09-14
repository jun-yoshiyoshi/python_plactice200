# \ooo 8進数ASCII文字　\xhh 16進数ASCII文字
print(" 8 進数 ASCII 文字[0101]：{0}".format("\101"))
print(" 8 進数 ASCII 文字[0102]：{0}".format("\102"))
print(" 8 進数 ASCII 文字[0103]：{0}".format("\103"))
print(" 16 進数 ASCII 文字[0x41]：{0}".format("\x41"))
print(" 16 進数 ASCII 文字[0x42]：{0}".format("\x42"))
print(" 16 進数 ASCII 文字[0x43]：{0}".format("\x43"))

# エスケープシークエンスの無効化
file_path = "C:\\work_python\\dir1\\dir2\\dir3\\file.txt"
print(file_path)
file_path = r"C:\work_python\dir1\dir2\dir3\file.txt"
print(file_path)
