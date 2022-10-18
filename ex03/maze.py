import tkinter as tk
import tkinter.messagebox as tkm

root = tk.Tk()
root.title("迷えるこうかとん") #1

canv = tk.Canvas(root, width = 1500, height = 900, bg = "black")
canv.pack() #2

tori = tk.PhotoImage(file="ex03/fig/3.png")
cx, cy = 300, 400
canv.create_image(cx, cy, image=tori, tag="tori") #3

key = "" #現在押されているキーを表す　#4

root.mainloop()