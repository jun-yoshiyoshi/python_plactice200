# ジェネレータ yield
def color_gene():
    yield "red"
    yield "green"
    yield "blue"
    yield "white"
    yield "yellow"
    yield "black"
    yield "cyan"
    yield "magnet"
    yield "gray"


for color in color_gene():
    print(color)
