import pygame
from playerobject import Player
import gameplayer
import taskbar
import playerobject

# Variable initializations
player1 = Player("player33")

user_input_small = ""
user_input_medium = ""
user_input_large = ""

small_goal_list = []
medium_goal_list = []
large_goal_list = []



# Get goals from user input
small_goal = input("PLease put in your small goals: ")
if(isinstance(small_goal, str)):
    small_goal_list.append(small_goal)
    
    while(user_input_small != "" or user_input_small != "done"):
        small_goal = input("PLease put in your small goals: ")
        small_goal_list.append(small_goal)
    player1.goals_to_goals(small_goal_list)


medium_goal = input("PLease put in your medium goals: ")
while(user_input_medium != "" or user_input_medium != "done"):
    medium_goal = input("PLease put in your medium goals: ")
    medium_goal_list.append(medium_goal)
    
player1.golas_to_goals(medium_goal_list)
    
    
large_goal = input("PLease put in your large goals: ")
while(user_input_large != "" or user_input_large != "done"):
    large_goal = input("PLease put in your large goals: ")
    large_goal_list.append(large_goal)
    
player1.goals_to_goals(large_goal_list)
    


