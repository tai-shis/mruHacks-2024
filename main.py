import pygame
from playerobject import Player
import gameplayer
import taskbar
import playerobject

# Variable initializations
player1 = Player("player33")
gamer1 = gameplayer

user_input_small = ""
user_input_medium = ""
user_input_large = ""

small_goal_list = []
medium_goal_list = []
large_goal_list = []



# Get small goals from user 
user_input_small = input("PLease put in your small goals: ")
if(user_input_small  != ""):
    small_goal_list.append(user_input_small)
    
while(user_input_small != ""):
    user_input_small = input("PLease put in your small goals: ")
    small_goal_list.append(user_input_small)
    
player1.goals_to_goals(small_goal_list)

# Get medium goals from user 
user_input_medium = input("PLease put in your medium goals: ")
if(user_input_medium != ""):
    medium_goal_list.append(user_input_medium)
while(user_input_medium != ""):
    user_input_medium = input("PLease put in your medium goals: ")
    medium_goal_list.append(user_input_medium)
    
player1.golas_to_goals(medium_goal_list)
    
# Get large goals from user
user_input_large = input("PLease put in your large goals: ")
if(user_input_large != ""):
    large_goal_list.append(user_input_large)
while(user_input_large != "" ):
    user_input_large = input("PLease put in your large goals: ")
    large_goal_list.append(user_input_large)
    
player1.goals_to_goals(large_goal_list)
    


