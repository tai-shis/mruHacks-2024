import pygame
from playerobject import Player
import gameplayer
import taskbar
from taskbar import load_taskbar

# Initialize player
player1 = Player("player33")

# Lists to hold the goals
small_goal_list = []
medium_goal_list = []
large_goal_list = []

# Function to get goals from user
def get_goals_from_user(goal_type):
    goal_list = []
    while True:
        user_input = input(f"Please enter your {goal_type} goal (or press Enter to finish): ")
        if user_input == "":  # Exit the loop if input is empty
            break
        goal_list.append(user_input)
    return goal_list

# Get small, medium, and large goals from user
# Get small, medium, and large goals from user
small_goal_list = get_goals_from_user("small")
medium_goal_list = get_goals_from_user("medium")
large_goal_list = get_goals_from_user("large")

# Set goals for the player (corrected method calls)
player1.set_small_goals(small_goal_list)
player1.set_medium_goals(medium_goal_list)
player1.set_large_goals(large_goal_list)

# Pass the goals to the taskbar to display as checklists
load_taskbar(small_goal_list, medium_goal_list, large_goal_list)
