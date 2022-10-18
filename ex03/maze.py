import tkinter as tk
import tkinter.messagebox as tkm

root = tk.Tk()
root.title("迷えるこうかとん") #1

canv = tk.Canvas(root, width = 1500, height = 900, bg = "black")
canv.pack() #2

root.mainloop()