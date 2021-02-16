from tkinter import *


def insertar():
    list1.insert(END,mivalor.get())

v0 = Tk ()
v0.geometry("700x700")

list1 = Listbox(v0)
list1.pack()
list1.place(x = 100, y = 100)

mivalor = StringVar()
e1 = Entry(v0,textvar =mivalor).pack()

b1 = Button(v0,text = "entrada",command = insertar).pack()

v0.mainloop()