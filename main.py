import pygame
from playerobject import Player
import gameplayer
import taskbar
import playerobject

# Variable initializations
player1 = Player("player33")

user_input_small = ""
medium_goal = ""
large_goal = ""

small_goal_list = []
medium_goal_list = []
large_goal_list = []



# Get goals from user input
small_goal = input("Please put in your small goals: ")
if(isinstance(small_goal, str)): #input will always return as a string, so dont need probs
    while(small_goal != "" or small_goal != "done"): #user input x_goal doesnt exist?
        small_goal_list.append(small_goal)
        small_goal = input("Please put in your small goals: ")
    player1.goals_to_goals(small_goal_list)


medium_goal = input("Please put in your medium goals: ") # if medium goal input is invalid it would have added to list

while(medium_goal != "" or medium_goal != "done"):
    medium_goal_list.append(medium_goal)
    medium_goal = input("Please put in your medium goals: ") # would have added last value inputted (invalid)

    
player1.goals_to_goals(medium_goal_list)
    
    
large_goal = input("Please put in your large goals: ")

while(large_goal != "" or large_goal != "done"):
    large_goal_list.append(large_goal)
    large_goal = input("Please put in your large goals: ")

    
player1.goals_to_goals(large_goal_list)
    


