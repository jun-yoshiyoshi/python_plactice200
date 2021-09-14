color_list = ["red", "green", "blue", "yellow", "cyan", "magenta"]
color = ",".join(color_list)
print(color_list)
print(color)

color_list = ["red", 1234, "green", 5678, "blue", "yellow", "cyan", "magenta"]
color = ",".join(map(str, color_list))
print(color_list)
print(color)

color = "red,green,blue,yellow,cyan,magenta"
color_list = color.rsplit(",")
print(color)
print(color_list)

color_list = color.rsplit(",", 1)
print(f"color_list(\',\',1):{color_list}")
color_list = color.rsplit(",", 3)
print(f"color_list(\',\',3):{color_list}")

sentence = """\n
あいうえお
かきくけこ


ABCDEFG
abcdefg
0123456789 \n
"""
sentence_list = sentence.splitlines()
print(sentence_list)
