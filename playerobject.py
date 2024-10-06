class Goal:
    def __init__(self, goal: str) -> None:
        self.goal = goal
        self.check_status = False 

    def __str__(self) -> str:
        return f"[goal: {self.goal}, check_status: {self.check_status}]" 

class Player:
    def __init__(self, name: str) -> None:
        self.name = name  
        self.small_goals = []
        self.medium_goals = []
        self.large_goals = []
        self.score = 0
        self.play_time = 0

    def goals_to_goals(self, goals: list[str]) -> list[Goal]:
        """
        Converts list of goal strings into list of custom goal objects,
        see Goal class for more information
        """
        goal_list = []
        for goal in goals:
            goal_list.append(Goal(goal))

        return goal_list

    # setters
    def set_small_goals(self, goals: list) -> None:
        self.small_goals = self.goals_to_goals(goals)

    def set_medium_goals(self, goals: list) -> None:
        self.medium_goals = self.goals_to_goals(goals)

    def set_large_goals(self, goals: list) -> None:
        self.large_goals = self.goals_to_goals(goals)

    def __str__(self) -> str:
        return (f"Player: {self.name}\n" + 
                f"Small goals: {self.small_goals}\n" +
                f"Medium goals: {self.medium_goals}\n" +
                f"Large goals: {self.large_goals}\n")