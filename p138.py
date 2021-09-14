# イテレータ next関数　イテレータの値を全て取り出すとどうなるか
color = ["red", "blue", "green", "yellow", "cyan", "magenta"]
color_iter = iter(color)
print(next(color_iter))
print(next(color_iter))
print(next(color_iter))
print(next(color_iter))
print(next(color_iter))
print(next(color_iter))
print(next(color_iter))


print("-"*10)
for color in color_iter:
    print(color)
