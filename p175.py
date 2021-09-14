# ウィジェットの継承
import tkinter as tk

# 悪い実装例


class Counter:
    def __init__(self, value):
        self.value = value
        frame = tk.Frame()
        font = ('Helevetica', 32, 'bold')
        self.label = tk.Label(frame, text=self.getText(), font=font, bg='red')
        button = tk.Button(frame, text='Click', command=self.clicked)
        self.label.pack()
        button.pack()
        frame.pack()
        frame.mainloop()

    def clicked(self):
        self.value += 1
        self.label.configure(text=self.getText())

    def getText(self):
        return 'Count:{}'.format(self.value)


c = Counter(0)

# Counter2にtk.Frameを継承させた、一般的な実装


class Counter2(tk.Frame):
    def __init__(self, master=None, value=0):
        self.value = value
        tk.Frame.__init__(self, master)
        font = ('Helevetica', 32, 'bold')
        self.label = tk.Label(self, text=self.getText(), font=font, bg='red')
        self.button = tk.Button(self, text='Click', command=self.clicked)
        self.label.pack()
        self.button.pack()

    def clicked(self):
        self.value += 1
        self.label.configure(text=self.getText())

    def getText(self):
        return 'Count:{}'.format(self.value)


f = tk.Frame()
c1 = Counter2(value=0, master=f)
c2 = Counter2(value=5, master=f)
#c3 = Counter2(value=10, master=f)
# 新しいウィジェットの追加が容易
c1.pack()
c2.pack()
# c3.pack()
f.pack()
f.mainloop()

# 原則としてIS-A関係では継承、HAS-A関係ではコンポジションを使う。
