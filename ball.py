import pygame

class Ball(pygame.sprite.Sprite):
    def __init__(self, start_position : tuple[int,int], launch_angle : int) -> None:
        '''
            launch_angle based on the trig circle where 90 degree
        '''
        self.position = start_position

        self.current_angle = launch_angle

        #de
    
    def draw(self) -> None:
        pass
    
    def move(self) -> None:
        pass

     