import tkinter as tk
import tkinter.messagebox as tkm

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん") #1

    canv = tk.Canvas(root, width = 1500, height = 900, bg = "black")
    canv.pack() #2

    tori = tk.PhotoImage(file="ex03/fig/3.png")
    cx, cy = 300, 400
    canv.create_image(cx, cy, image=tori, tag="tori") #3

    key = "" #現在押されているキーを表す　#4

    #5
    root.bind("<KeyPress>", key_down) #5
    root.bind("<KeyRelease", key_up) #6


    root.mainloop()