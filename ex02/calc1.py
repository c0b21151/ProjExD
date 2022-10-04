import tkinter as tk
import tkinter.messagebox as tkm

def click_number(event):
    btn = event.widget
    num = int(btn["text"])
    tkm.showinfo(f"{num}", f"{num}のボタンが押されました")

root = tk.Tk()
root.geometry("300x500")
w = 0
r = 0
for i, num  in enumerate(range(9, -1, -1), 1):
    button = tk.Button(root, text=f"{num}",font=("Times New Roman", 30), width=4, height=2)
    button.bind("<1>", click_number)
    button.grid(row=w, column=r)
    r += 1
    if i%3 == 0:
        w += 1
        r = 0 

root.mainloop()