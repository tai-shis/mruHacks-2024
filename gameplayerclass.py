import pygame
import ball
import math

class LevelMarker(pygame.sprite.Sprite):
    """

    """
    def __init__(self, ballGroup) -> None: # blockGroup, blockTarget
        super().__init__()
        self.currentBall = ball((300,300),math.pi/2)
        ballGroup.add(self.currentBall)
        print("-------------------------------")

    def level_clear(self):
        self.currentBall.kill()
        

class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        self.total_points = 0   
        