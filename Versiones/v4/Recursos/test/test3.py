from tkinter import *
things = [{"dictionaryItem":"value"}, {"anotherDict":"itsValue"}, 3, "foo", ["bar", "baz"]]
root = Tk()
f = Frame(root).pack()
l = Listbox(root)
b = Button(root, text = "delete selection", command = lambda: delete(l))
b.pack()
l.pack()

for i in range(5):
    l.insert(END, things[i])

def delete(listbox):

    global things
    # Delete from Listbox
    selection = l.curselection()
    l.delete(selection[0])
    # Delete from list that provided it
    value = eval(l.get(selection[0]))
    ind = things.index(value)
    del(things[ind])
    print(things)

root.mainloop()