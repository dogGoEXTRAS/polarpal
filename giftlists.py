import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import askyesno

root = tk.Tk()
root.geometry('350x250')
root.title("Gift List by PolarPal A.I.")

data = tk.StringVar()

title = ttk.Label(root, text="Gift List")
instruction = ttk.Label(root, text="Enter your gifts: ")

gift = ttk.Entry(root, width=20, textvariable=data)
lists = tk.Listbox(root, height=10, selectmode='SINGLE')

def add(): 
    global gift
    data_text = gift.get()
    lists.insert(0, data_text)
    lists.see(0)

def remove(): 
    lists.delete(0)
    lists.see(0)

def request():
    answer = askyesno("Confirmation", "Are you sure you want to request Santa for your wishful gifts?")

    if answer: 
        messagebox.showinfo("Congrats!", f"You have sent your wish list to Santa.")    
        lists.delete(0, tk.END)  

b1 = ttk.Button(root, text="Add Gift", command=add)
b2 = ttk.Button(root, text="Delete Gift", command=remove)
b3 = ttk.Button(root, text="Request Santa", command=request)

title.place(x=150, y=10)
instruction.place(x=50, y=50)
gift.place(x=50, y=80)
b1.place(x=50, y=110)
b2.place(x=50, y=140)
b3.place(x=50, y=170)
lists.place(x=190, y=60)

root.mainloop()

