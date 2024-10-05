from tkinter import *
from tkinter import ttk

# Create the main window
window = Tk()

# Create a notebook widget that manages a collection of windows/displays
notebook = ttk.Notebook(window)

# Variable to store the checkbox state
x1 = IntVar()
x2 = IntVar()
x3 = IntVar()

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
Checkbutton(small, text="Task 1: Hello World", variable=x1, onvalue=1, offvalue=0).pack(anchor="w", padx=20)
Checkbutton(small, text="Task 2: Another Task", variable=x2, onvalue=1, offvalue=0).pack(anchor="w", padx=20)
Checkbutton(small, text="Task 3: Final Task", variable=x3, onvalue=1, offvalue=0).pack(anchor="w", padx=20)

# Add header and checkboxes to the "Medium Task" tab
Label(medium, text="Medium Task Checklist", font=("Helvetica", 16, "bold")).pack(pady=10)
Checkbutton(medium, text="Task 1: Medium Task 1", variable=x1, onvalue=1, offvalue=0).pack(anchor="w", padx=20)
Checkbutton(medium, text="Task 2: Medium Task 2", variable=x2, onvalue=1, offvalue=0).pack(anchor="w", padx=20)

# Add header and checkboxes to the "Large Task" tab
Label(large, text="Large Task Checklist", font=("Helvetica", 16, "bold")).pack(pady=10)
Checkbutton(large, text="Task 1: Large Task 1", variable=x1, onvalue=1, offvalue=0).pack(anchor="w", padx=20)

# Start the Tkinter event loop
window.mainloop()
