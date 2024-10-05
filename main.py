import pygame
from playerobject import Player
import gameplayer
import taskbar
import playerobject

# Get user goals input

player1 = Player("player33")

user_input_small = ""
user_input_medium = ""
user_input_large = ""

small_goal_list = []
medium_goal_list = []
large_goal_list = []


while(user_input_small == "" or user_input_small != "done" or user_input_small == "none"):
    small_goal = input("PLease put in your small goals: ")
    small_goal_list.append(small_goal)
    
    
    

while(user_input_medium == "" or user_input_medium != "done" or user_input_medium == "none"):
    medium_goal = input("PLease put in your small goals: ")
    medium_goal_list.append(medium_goal)
    
    

while(user_input_large == "" or user_input_large != "done" or user_input_large == "none"):
    large_goal = input("PLease put in your small goals: ")
    large_goal_list.append(large_goal)
    


