import getch

KEY_CTRL_C = 3
KEY_W = 119
KEY_A = 97
KEY_S = 115
KEY_Z = 122


class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.hero = Hero(3, 3, self.is_movable, self.draw)
        # Heroクラスの第三、第四引数はMapクラスのis_movable,drawをとる。関数渡し。

    def run(self):
        self.hero.run()

    def is_movable(self, x, y):
        # 勇者の移動の可否判定機能はマップクラスのis_movableに実装されている
        if (x < 0):
            return False
        elif (self.width - 1 < x):
            return False
        elif (y < 0):
            return False
        elif (self.height - 1 < y):
            return False
        return True

    def draw(self):
        characters = {}
        characters[(self.hero.x, self.hero.y)] = self.hero.icon

        def get_row(y):
            row_list = []
            row_list.append("|")
            for x in range(0, self.width):
                if ((x, y) in characters):
                    row_list.append(characters[(x, y)])
                else:
                    row_list.append(" ")
            row_list.append("|\n")
            return "".join(row_list)

        map_list = []
        map_list.append("+{}+\n".format('-'*self.width))
        for y in range(0, self.height):
            map_list.append(get_row(y))
        map_list.append("+{}+\n".format('-'*self.width))

        print("".join(map_list))


class Hero:
    def __init__(self, x, y, movable, draw_map):
        self.x = x
        self.y = y
        self.icon = '^'
        self.is_movable = movable
        self.draw_map = draw_map

    def run(self):
        print("-" * 10)
        print("W:up,A:left,S:right,Z:down")
        print("ctrl=c:quit")
        print("-" * 10)
        self.draw_map()

        while (True):
            key = ord(getch.getch())
            if (key == KEY_CTRL_C):
                print("bye!!")
                break

            elif (key == KEY_W):
                self.icon = '^'
                if (self.is_movable(self.x, self.y - 1)):
                    self.y -= 1
                    # print(self.icon)

            elif (key == KEY_S):
                self.icon = '>'
                if (self.is_movable(self.x + 1, self.y)):
                    self.x += 1
                    # print(self.icon)
            elif (key == KEY_A):
                self.icon = '<'
                if (self.is_movable(self.x - 1, self.y)):
                    self.x -= 1
                    # print(self.icon)
            elif (key == KEY_Z):
                self.icon = 'v'
                if(self.is_movable(self.x, self.y+1)):
                    self.y += 1
                    # print(self.icon)
            else:
                continue

            self.draw_map()


dqmap = Map(7, 7)
dqmap.run()
#hero = Hero(0, 0)
# hero.run()
