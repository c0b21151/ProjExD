import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker as mm #9

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def main_proc(): #7
    global mx, my
    global cx, cy
    if key == "Up":
        my -= 1
    if key == "Down":
        my += 1
    if key == "Left":
        mx -= 1
    if key == "Right":
        mx += 1
    if maze_list[my][mx] == 0:
        cx, cy = mx*100+50, my*100+50
    else:
        if key == "Up":
            my += 1
        if key == "Down":
            my -= 1
        if key == "Left":
            mx += 1
        if key == "Right":
            mx -= 1
    canv.coords("tori", cx, cy)
    root.after(100, main_proc)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん") #1

    canv = tk.Canvas(root, width = 1500, height = 900, bg = "black")
    canv.pack() #2

    maze_list = mm.make_maze(15, 9) #1が壁、0が床 #9
    maze_show = mm.show_maze(canv, maze_list) #10

    tori = tk.PhotoImage(file="ex03/fig/3.png")
    mx, my = 1, 1
    cx, cy = mx*100, my*100
    canv.create_image(cx, cy, image=tori, tag="tori") #3

    key = "" #現在押されているキーを表す　#4

    root.bind("<KeyPress>", key_down) #5
    root.bind("<KeyRelease>", key_up) #6

    main_proc()

    root.mainloop()