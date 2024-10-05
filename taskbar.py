from tkinter import *
from tkinter import ttk

# Function to create dynamic tasks from a list of tasks
def create_tasks(tab_frame, task_name, task_list):
    Label(tab_frame, text=f"{task_name} Checklist", font=("Helvetica", 16, "bold")).pack(pady=10)
    
    # Create checkboxes dynamically based on the list of tasks
    for i, task in enumerate(task_list):
        task_var = IntVar()  # Variable to store the checkbox state
        Checkbutton(tab_frame, text=f"Task {i+1}: {task}", variable=task_var, onvalue=1, offvalue=0).pack(anchor="w", padx=20)

# Function to load the taskbar with tasks passed from main.py
def load_taskbar(small_tasks, medium_tasks, large_tasks):
    # Create the main window
    window = Tk()

    # Create a notebook widget that manages a collection of windows/displays
    notebook = ttk.Notebook(window)

    # Create frames for each tab
    small = Frame(notebook)
    medium = Frame(notebook)
    large = Frame(notebook)

    # Add the frames to the notebook (tabs)
    notebook.add(small, text="Small Task")
    notebook.add(medium, text="Medium Task")
    notebook.add(large, text="Large Task")
    notebook.pack(expand=True, fill="both")

    # Call the function to create checklists dynamically from the user input
    create_tasks(small, "Small Task", small_tasks)   # Pass the list of small tasks
    create_tasks(medium, "Medium Task", medium_tasks) # Pass the list of medium tasks
    create_tasks(large, "Large Task", large_tasks)   # Pass the list of large tasks

    window.attributes('-fullscreen', True)


    # Start the Tkinter event loop
    window.mainloop()
