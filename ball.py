import pygame
from random import randint

def loadify(img_name):
    return pygame.image.load(img_name).convert_alpha()

class Ball(pygame.sprite.Sprite):
    def __init__(self, start_position : tuple[int,int], launch_angle : int) -> None:
        '''
            launch_angle based on the trig circle where 90 degree
        '''
        self.position = start_position

        self.current_angle = launch_angle

        self.velocity = [0, 0] #initial velocity at zero and spawning the ball will set one

        self.image = pygame.transform.smoothscale(loadify('Bullet.png').size)
        self.image_orgin = self.image
        self.rect = self.image.get_rect(center=self.position)
        #de

    def spawn(self):
        #calculate random position
        rand_x = randint(8, 500 - 8) # from dimensions with size of sprite included
        rand_y = randint(8, 500 - 8 )
        self.position = [rand_x, rand_y]
        self.velocity = [0.5, 0.5] #arbitrary init velocity going at a 45 deg angle, random later
    
    def move(self) -> None:
        pass

     