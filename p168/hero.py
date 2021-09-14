import getch

KEY_CTRL_C, KEY_W, KEY_A, KEY_S, KEY_Z, KEY_D = 3, 119, 97, 115, 122, 100


class Townsman:
    def __init__(self, x, y, icon, message):
        self.x, self.y = x, y
        self.icon = icon
        self.message = message


class Map:
    def __init__(self, width, height):
        self.width, self.height = width, height
        self.hero = Hero(3, 3, self.is_movable, self.get_message, self.draw)
        self.townspeople = [
            Townsman(3, 1, 'K', "i'm King"),
            Townsman(1, 5, 'S', "i'm Solder1"),
            Townsman(5, 5, 'S', "i'm Solder2")
        ]

    def run(self):
        self.hero.run()

    def get_message(self, x, y):
        for _ in self.townspeople:
            if (x == _.x and y == _.y):
                return _.message
        return "no one exists."

    def is_movable(self, x, y):
        if (x < 0):
            return False
        elif (self.width - 1 < x):
            return False
        elif (y < 0):
            return False
        elif (self.height - 1 < y):
            return False

        for _ in self.townspeople:
            if (x == _.x and y == _.y):
                return False
        return True

    def draw(self, message):
        characters = {}
        characters[(self.hero.x, self.hero.y)] = self.hero.icon
        for _ in self.townspeople:
            characters[(_.x, _.y)] = _.icon

        def get_row(y):
            row_list = []
            row_list.append('|')
            for x in range(0, self.width):
                if ((x, y) in characters):
                    row_list.append(characters[(x, y)])
                else:
                    row_list.append(" ")
            row_list.append("|\n")
            return ''.join(row_list)
        map_list = []
        map_list.append(f"+{'-'*self.width}+\n")
        for y in range(0, self.height):
            map_list.append(get_row(y))
        map_list.append(f"+{'-'*self.width}+\n")

        map_list.append(f"+{'-'*self.width}+\n")
        map_list.append(message+"\n")
        map_list.append(f"+{'-'*self.width}+\n")

        print(''.join(map_list))


class Hero:
    # マップのis_movableとdrawメソッドを受け取り登録
    def __init__(self, x, y, is_movable, get_message, draw_map):
        self.x, self.y = x, y
        self.icon = '^'
        self.is_movable = is_movable
        self.get_message = get_message
        self.draw_map = draw_map

    def run(self):
        print('-----------------------------')
        print('w: up, a: left, s: right, z: down, d: talk')
        print('ctrl-c: quit')
        print('-----------------------------')
        self.draw_map('')

        while (True):
            message = ''
            key = ord(getch.getch())
            if (key == KEY_CTRL_C):
                # Quit
                print('bye!!')
                break
            elif (key == KEY_W):
                # Up
                self.icon = '^'
                if (self.is_movable(self.x, self.y-1)):
                    self.y -= 1
            elif (key == KEY_A):
                # Left
                self.icon = '<'
                if (self.is_movable(self.x - 1, self.y)):
                    self.x -= 1
            elif (key == KEY_S):
                # Right
                self.icon = '>'
                if (self.is_movable(self.x + 1, self.y)):
                    self.x += 1
            elif (key == KEY_Z):
                # Down
                self.icon = 'v'
                if (self.is_movable(self.x, self.y + 1)):
                    self.y += 1
            elif (key == KEY_D):
                # TALK
                # 会話をしてメッセージを取得
                message = self.talk()
            else:
                continue

            self.draw_map(message)

    def talk(self):
        message = ''
        if (self.icon == '^'):
            message = self.get_message(self.x, self.y-1)
        elif (self.icon == '<'):
            message = self.get_message(self.x-1, self.y)
        elif (self.icon == '>'):
            message = self.get_message(self.x+1, self.y)
        elif (self.icon == 'v'):
            message = self.get_message(self.x, self.y+1)
        else:
            pass
        return message


dqmap = Map(7, 7)
dqmap.run()
