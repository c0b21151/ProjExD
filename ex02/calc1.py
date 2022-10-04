import tkinter as tk
import tkinter.messagebox as tkm

count1 = 1

def click_number(event):
    global count1
    btn = event.widget
    num = btn["text"]
    entry.insert(tk.END, num)
    count1 = 0

def click_eq(event):
    eqn = entry.get()
    res = eval(eqn)
    entry.delete(0, tk.END)
    entry.insert(tk.END, res)

def click_k1(event):
    global count1
    btn = event.widget
    num = btn["text"]
    if count1 == 0:
        if num == "÷":
            entry.insert(tk.END, "/")
            count1 += 1
        elif num == "x":
            entry.insert(tk.END, "*")
            count1 += 1
        elif num == "+":
            entry.insert(tk.END, "+")
            count1 += 1
        elif num == "-":
            entry.insert(tk.END, "-")
            count1 += 1
    else:
        pass

def click_del(event):
    entry.delete(0,tk.END)

def click_Num(event):
    pass

root = tk.Tk()
root.geometry("380x600")

entry = tk.Entry(root, width=14, font=("", 40), justify="right")
entry.grid(row=0, column=0, columnspan=6)

r, c = 1, 0
numbers = list(range(9, -1, -1))
operators = ["+","-","x","÷"]

for i, num in enumerate(numbers, 1):
    btn = tk.Button(root, text=f"{num}", font=("", 30), width=4, height=2)
    btn.bind("<1>", click_number)
    btn.grid(row=r+1, column=c)
    c += 1
    if i%3 == 0:
        r += 1
        c = 0
        if i == 9:
            r = 4
            c = 1

for n,s in enumerate(operators,1):
    btn = tk.Button(root, text=f"{s}", font=("", 30), width=4, height=2)
    if s == "+" or "-" or "x" or "÷":
        btn.bind("<1>", click_k1)
    
    btn.grid(row=n, column=4)

btn = tk.Button(root, text="=", font=("", 30), width=4, height=2)
btn.bind("<1>", click_eq)
btn.grid(row=5, column=2)

btn = tk.Button(root, text="C", font=("", 30), width=4, height=2)
btn.bind("<1>", click_del)
btn.grid(row=5, column=0)

btn = tk.Button(root, text="Num", font=("", 30), width=4, height=2)
btn.bind("<1>", click_Num)
btn.grid(row=1, column=0)

root.mainloop()
