from tkinter import *
from tkinter import ttk

window = Tk()

notebook = ttk.Notebook(window) #widget that manages a collection of windows/displays

small = Frame(notebook) #new frame for small task
medium = Frame(notebook) #new frame for medium task
large = Frame(notebook) #new frame for large task


notebook.add(small,text="Small Task")
notebook.add(medium,text="Medium Task")
notebook.add(large,text="Large Task")
notebook.pack(expand=True,fill="both")  #expand = expand to fill any space not otherwise used
                                       #fill = fill space on x and y axis
Label(small,text="Small Task: ",width=50,height=25).pack()
Label(medium,text="Medium Task: ",width=50,height=25).pack()
Label(large,text="Large Task: ",width=50,height=25).pack()


window.mainloop()

"""
def display():
    if (x.get()==1):
        print("done")
    else:
        print("not done")
window = Tk()
x = IntVar()

check_button = Checkbutton(window, text = "hello world",  variable = x, onvalue = 1, offvalue= 0, command= display)
print(x)

check_button.pack()

window.mainloop()
"""