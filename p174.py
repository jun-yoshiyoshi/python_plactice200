# Tkinterで承継の理解と練習

import tkinter as tk

font = ("Helecetica", 32, "bold")
label = tk.Label(text="Hello Tkinter", font=font, bg="red")
label.pack()
label.mainloop()

frame = tk.Frame()
font = ("Helecetica", 32, "bold")
label1 = tk.Label(text="hello python", font=font, bg="red")
label2 = tk.Label(text="Hello Python", font=font, bg="blue")
label1.pack()
label2.pack()
frame.pack()
label.mainloop()

frame1 = tk.Frame()
frame2 = tk.Frame(frame1)
font = ("Helecetica", 32, "bold")
label3 = tk.Label(frame2, text="hello tk", font=font, bg="red")
label4 = tk.Label(frame2, text="Hello Tk", font=font, bg="blue")
label3.pack(side=tk.LEFT)
label4.pack(side=tk.LEFT)
frame2.pack()

label5 = tk.Label(frame1, text="Hello World", font=font, bg="green")
label5.pack(fill=tk.X)

frame1.pack()
frame1.mainloop()
