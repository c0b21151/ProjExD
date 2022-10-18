import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker as mm #9
import time

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def main_proc(): #7
    global mx, my
    global cx, cy
    global ismove
    global goal
    global gmsg
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
        print(mx,my)
        print(goal)
        if key != "":
            if ismove == False:
                canv.create_image(cx, cy, image=move, tag="move")
                canv.delete("start")
                ismove = True
    else:
        if key == "Up":
            my += 1
        if key == "Down":
            my -= 1
        if key == "Left":
            mx += 1
        if key == "Right":
            mx -= 1
    
    if mx == 1 and my == 1 and ismove == False:
        canv.coords("start", cx, cy)
        root.after(100, main_proc)
    else:
        canv.coords("move", cx, cy)
        root.after(100, main_proc)
        if mx == 13 and my == 7 and goal == False:
            goal = True
            if goal == True:
                canv.create_image(cx, cy, image=goali, tag="goal")
                canv.delete("move")
                tkm.showinfo("goal","goal")
            
        
if __name__ == "__main__":
    
    root = tk.Tk()
    root.title("迷えるこうかとん") #1

    canv = tk.Canvas(root, width = 1500, height = 900, bg = "black")
    canv.pack() #2

    maze_list = mm.make_maze(15, 9) #1が壁、0が床 #9
    maze_show = mm.show_maze(canv, maze_list) #10

    ismove = False
    goal = False
    
    sti = tk.PhotoImage(file="ex03/fig/4.png")
    move = tk.PhotoImage(file="ex03/fig/3.png")
    goali = tk.PhotoImage(file="ex03/fig/6.png")
    mx, my = 1, 1
    cx, cy = mx*100+50, my*100+50 #3
    canv.create_image(cx, cy, image=sti, tag="start")
    

    key = "" #現在押されているキーを表す　#4

    root.bind("<KeyPress>", key_down) #5
    root.bind("<KeyRelease>", key_up) #6

    main_proc()

    root.mainloop()