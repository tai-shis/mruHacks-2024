from tkinter import *
from tkinter import ttk

# Create the main window
window = Tk()

# Create a notebook widget that manages a collection of windows/displays
notebook = ttk.Notebook(window)

# Variable to store the checkbox state
def check_checkbox(var, task_name)->bool:
    if var.get() == 1:
        print (f"{task_name} is complete!")
        return True
        

    else:
        print (f"{task_name} is unchecked")
        return False

# Create frames for each tab
small = Frame(notebook)
medium = Frame(notebook)
large = Frame(notebook)

# Add the frames to the notebook (tabs)
notebook.add(small, text="Small Task")
notebook.add(medium, text="Medium Task")
notebook.add(large, text="Large Task")
notebook.pack(expand=True, fill="both")

# Add header and checkboxes to the "Small Task" tab
Label(small, text="Small Task Checklist", font=("Helvetica", 16, "bold")).pack(pady=10)
SmallTasks = ["Task 1: Hello World", "Task 2: Learn Python", "Task 3: Build a GUI"]

# Create a list to hold the IntVar() variables for each checkbutton
check_vars = []

# Create checkbuttons in a for loop
for i, task in enumerate(SmallTasks):
    var = IntVar()
    check_vars.append(var)
    checkbutton = Checkbutton(small, text=task, variable=var,
                                  command=lambda v=var, t=task: check_checkbox(v, t))
    checkbutton.pack(anchor="w", padx=20)
# Add header and checkboxes to the "Medium Task" tab
Label(medium, text="Medium Task Checklist", font=("Helvetica", 16, "bold")).pack(pady=10)
MediumTasks = ["Task 1: Lock in", "Task 2: Learn Tkinter", "Task 3: Build this shi","Grind"]


# Create checkbuttons in a for loop
for task in MediumTasks: 
    var = IntVar()
    check_vars.append(var)
    checkbutton = Checkbutton(medium, text=task, variable=var)
    checkbutton.pack(anchor="w", padx=20)

# Add header and checkboxes to the "Large Task" tab
Label(large, text="Large Task Checklist", font=("Helvetica", 16, "bold")).pack(pady=10)

LargeTasks = ["Do Comp 2655 Midterm" , "Finish Assignment 4"]
# Create a list to hold the IntVar() variables for each checkbutton

# Create checkbuttons in a for loop
for task in LargeTasks: #replace with large task array passed from main object
    var = IntVar()
    check_vars.append(var)
    checkbutton = Checkbutton(large, text=task, variable=var)
    checkbutton.pack(anchor="w", padx=20)

# Start the Tkinter event loop
window.mainloop()
