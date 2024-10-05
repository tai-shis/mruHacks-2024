class Player:
    def __init__(self, name: str) -> None:
        self.name = name  
        self.small_goals = None
        self.medium_goals = None
        self.large_goals = None
        self.score = 0
        self.play_time = 0

    # setters
    def add_small_goals(self, goals: str) -> None:
        self.small_goals = goals

    def add_medium_goals(self, goals: str) -> None:
        self.medium_goals = goals

    def add_large_goals(self, goals: str) -> None:
        self.large_goals = goals

    # getters for each 
    def get_small_goals(self) -> list:
        return self.small_goals
    
    def get_medium_goals(self) -> list:
        return self.medium_goals
    
    def get_large_goals(self) -> list:
        return self.large_goals


    def __str__(self) -> str:
        return (f"Player: {self.name}\n" + 
                f"small goals: {self.small_goals}\n" +
                f"medium goals: {self.medium_goals}\n" +
                f"large goals: {self.large_goals}\n")

