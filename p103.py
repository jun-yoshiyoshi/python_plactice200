color = "red green blue yellow cyan magenta"
color_list = color.split()
print(color)
print(color_list)

color = "red\ green\t blue\n yellow\t\tcyan magenta"
color_list = color.split()
print(color)
print(color_list)

color = "red, green, blue, yellow, cyan, magenta"
color_list = color.split(",")
print(color)
print(color_list)

color = "red100green100 blue100,yellow100/cyan100/tmagenta"
color_list = color.split("100")
print(color)
print(color_list)

color = "red, green, blue, yellow, cyan, magenta"
print(color)
color_list = color.split(",", 1)
print("color_list(\',',1):{}".format(color_list))
color_list = color.split(",", 4)
print("color_list(\',',4):{}".format(color_list))
