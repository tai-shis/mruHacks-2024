import pygame
from playerobject import Player
from playerobject import Goal
from gameplayer import GamePlayer
#import taskbar
import playerobject
from tkinter import *
from tkinter import ttk
time = 0
import asyncio
import time

def check_checkbox(var, task_name: str, goals: list[Goal], grant_time: int)->bool:
    #check which goal is being checked
    i = 0
    while(task_name != goals[i].goal): #while goal name/string doesnt match increment counter
        i += 1

    if var.get() == 1:
        print (f"{task_name} is complete!")
        if not goals[i].check_status:
            player1.play_time += grant_time
            goals[i].check_status = True 
    else:
        print (f"{task_name} is unchecked")
        
    print(player1.play_time)
    print(goals[i])
    print(task_name)



# Variable initializations
player1 = Player("player33")
# gamer1 = gameplayer

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

for i, task in enumerate(player1.small_goals):
    var = IntVar()
    check_vars.append(var)
    checkbutton = Checkbutton(small, text=task.goal, variable=var,
                                  command=lambda v=var, t=task.goal: check_checkbox(v, t, player1.small_goals, 30))
    checkbutton.pack(anchor="w", padx=20)

# Create checkbuttons in a for loop
for j, task in enumerate(player1.medium_goals): 
    var = IntVar()
    check_vars.append(var)
    checkbutton = Checkbutton(medium, text=task.goal, variable=var,
                                  command=lambda v=var, t=task.goal: check_checkbox(v, t, player1.medium_goals, 60))
    checkbutton.pack(anchor="w", padx=20)

    # Create checkbuttons in a for loop
for k, task in enumerate(player1.large_goals): #replace with large task array passed from main object
    var = IntVar()
    check_vars.append(var)
    checkbutton = Checkbutton(large, text=task.goal, variable=var,
                                  command=lambda v=var, t=task.goal: check_checkbox(v, t, player1.large_goals, 120))
    checkbutton.pack(anchor="w", padx=20)

end_time = time.time() + 120
curr_time = time.time()
while curr_time < end_time:
    if player1.play_time >= 60:
        main = GamePlayer(player1.play_time)
        main.run()
        player1.play_time = 0
        player1.score = main.currentTotalScore
    curr_time = time.time()
    window.update()

print(f"Good job completing your tasks! Score: {player1.score}")
