from tkinter import *
from tkinter import ttk
from playerobject import Player

#loads tkinter UI
def load_taskbar():
    window = Tk()
    notebook = ttk.Notebook(window)
    small = Frame(notebook)
    medium = Frame(notebook)
    large = Frame(notebook)

    # Add the frames to the notebook (tabs)
    notebook.add(small, text="Small Task")
    notebook.add(medium, text="Medium Task")
    notebook.add(large, text="Large Task")
    notebook.pack(expand=True, fill="both")

    window.mainloop()




# Function to create dynamic tasks
def create_tasks(tab_frame, task_name, num_tasks):
    Label(tab_frame, text=f"{task_name} Checklist", font=("Helvetica", 16, "bold")).pack(pady=10)
    
    # Create checkboxes dynamically based on the number of tasks
    for i in range(num_tasks):
        task_var = IntVar()  # Variable to store the checkbox state
        Checkbutton(tab_frame, text=f"Task {i+1}: Description {i+1}", variable=task_var, onvalue=1, offvalue=0).pack(anchor="w", padx=20)
