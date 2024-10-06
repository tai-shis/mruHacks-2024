import pygame
import math
from random import randint
import time

def loadify(img_name):
    return pygame.image.load(img_name).convert_alpha()

class Ball(pygame.sprite.Sprite):
    def __init__(self, start_position : tuple[int,int], launch_angle : float, blockGroup) -> None:
        '''
            launch_angle based on the trig circle where 90 degree
        '''
        pygame.sprite.Sprite.__init__(self)
        self.positionX = start_position[0]
        self.positionY = start_position[1]

        self.current_angle = launch_angle

        self.blockGroup = blockGroup

        self.movement_vector = [math.cos(self.current_angle), math.sin(self.current_angle)] #initial movement_vector at zero and spawning the ball will set one
        self.speed = 5
        self.image = pygame.transform.smoothscale(loadify('Ball.png'),(8,8))
        self.image_orgin = self.image
        self.rect = self.image.get_rect(center=(self.positionX,self.positionY))
        print(self.movement_vector)

        self.hitCoolDown = False
        self.hitCoolDownStart = math.inf
        self.hitCoolDownDur = 0.5
        
        #de

    def check_collision(self):
         # check if pos of ball is touching a wall or intersecting with corresponding vector direction, 
         # if so, then flip vector
        if self.positionX < 8 or self.positionX > 492:
            self.movement_vector = [self.movement_vector[0] * -1, self.movement_vector[1]]
        if self.positionY < 8 or self.positionY > 492:
            self.movement_vector = [self.movement_vector[0], self.movement_vector[1] * -1]

    def spawn(self):
        #calculate random position
       # rand_x = randint(8, 500 - 8) # from dimensions with size of sprite included
       # rand_y = randint(8, 500 - 8 )
        #self.position = [rand_x, rand_y]
        #self.movement_vector = [0.5, 0.5] #arbitrary init movement_vector going at a 45 deg angle, random later
        pass
    
    def hit(self):
        listOfCollideBlocks = pygame.sprite.spritecollide(self, self.blockGroup , False,  pygame.sprite.collide_rect)
        if listOfCollideBlocks and not self.hitCoolDown:
            self.hitCoolDown = True
            self.hitCoolDownStart = time.time()
            for block in listOfCollideBlocks:
                newAngle = 2*block.angle - self.current_angle
                print(newAngle)
                self.current_angle = newAngle
                self.movement_vector[0] = -math.cos(newAngle)
                self.movement_vector[1] = -math.sin(newAngle)

        if self.hitCoolDownStart + self.hitCoolDownStart > time.time():
            self.hitCoolDown = False
            self.hitCoolDownStart = math.inf



    def move(self,dt) -> None:
        #x, y = self.position[0] + self.movement_vector[0], -1 * (self.position[1] + self.movement_vector[1])
        self.positionX += self.speed * self.movement_vector[0]
        self.positionY -= self.speed * self.movement_vector[1]
        self.position = [self.speed, self.speed]
        self.rect = self.image.get_rect(center=(self.positionX,self.positionY))

    def update(self,dt):
        self.check_collision()
        self.hit()
        self.move(dt)

     