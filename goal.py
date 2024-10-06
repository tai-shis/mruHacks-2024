import pygame

class Goal(pygame.sprite.Sprite):
    def __init__(self, position: tuple[int, int]) -> None:
        self.point_award = 1000 #decrement by like, 100 or 200 for each Block placed
        self.position = position
        self.goal_reached = False

    def update(self, dt):
        #do stuff
        pass