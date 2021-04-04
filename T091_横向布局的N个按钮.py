# 在这里写上你的代码 :-)
import tkinter as tk

root = tk.Tk()

tk.Label(root, text="Red", bg="red", fg="white").pack(side='left')
tk.Label(root, text="Yellow", bg="yellow", fg="black").pack(side='left')
tk.Label(root, text="Green", bg="green", fg="white").pack(side='left')
tk.Label(root, text="Blue", bg="blue", fg="white").pack(side='left')

root.mainloop()
