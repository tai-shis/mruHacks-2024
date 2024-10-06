import pygame
from playerobject import Player
import gameplayer
#import taskbar
import playerobject
from tkinter import *
from tkinter import ttk

def check_checkbox(var, task_name)->bool:
    if var.get() == 1:
        print (f"{task_name} is complete!")
        return True
        

    else:
        print (f"{task_name} is unchecked")
        return False

# Variable initializations
player1 = Player("player33")
gamer1 = gameplayer

user_input_small = ""
user_input_medium = ""
user_input_large = ""

small_goal_list = []
medium_goal_list = []
large_goal_list = []

check_vars = []


# Get small goals from user 
user_input_small = input("PLease put in your small goals: ")
if(user_input_small  != ""):
    small_goal_list.append(user_input_small)
    
while(user_input_small != ""):
    user_input_small = input("PLease put in your small goals: ")
    if(user_input_small  != ""):
        small_goal_list.append(user_input_small)
    
player1.set_small_goals(small_goal_list)

# Get medium goals from user 
user_input_medium = input("PLease put in your medium goals: ")
if(user_input_medium != ""):
    medium_goal_list.append(user_input_medium)
while(user_input_medium != ""):
    user_input_medium = input("PLease put in your medium goals: ")
    if(user_input_medium != ""):
        medium_goal_list.append(user_input_medium)
    
player1.set_medium_goals(medium_goal_list)
    
# Get large goals from user
user_input_large = input("PLease put in your large goals: ")
if(user_input_large != ""):
    large_goal_list.append(user_input_large)
while(user_input_large != "" ):
    user_input_large = input("PLease put in your large goals: ")
    if(user_input_large != ""):
        large_goal_list.append(user_input_large)
    
player1.set_large_goals(large_goal_list)
#window initialization
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

#add labels
Label(small, text="Small Task Checklist", font=("Helvetica", 16, "bold")).pack(pady=10)
Label(medium, text="Medium Task Checklist", font=("Helvetica", 16, "bold")).pack(pady=10)
Label(large, text="Large Task Checklist", font=("Helvetica", 16, "bold")).pack(pady=10)    

for i, task in enumerate(small_goal_list):
    var = IntVar()
    check_vars.append(var)
    checkbutton = Checkbutton(small, text=task, variable=var,
                                  command=lambda v=var, t=task: check_checkbox(v, t))
    checkbutton.pack(anchor="w", padx=20)

# Create checkbuttons in a for loop
for j, task in enumerate(medium_goal_list): 
    var = IntVar()
    check_vars.append(var)
    checkbutton = Checkbutton(medium, text=task, variable=var,
                                  command=lambda v=var, t=task: check_checkbox(v, t))
    checkbutton.pack(anchor="w", padx=20)

    # Create checkbuttons in a for loop
for k, task in enumerate(large_goal_list): #replace with large task array passed from main object
    var = IntVar()
    check_vars.append(var)
    checkbutton = Checkbutton(large, text=task, variable=var,
                                  command=lambda v=var, t=task: check_checkbox(v, t))
    checkbutton.pack(anchor="w", padx=20)



window.mainloop()
