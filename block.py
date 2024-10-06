import pygame
import math
import time

def loadify(img_name):
    return pygame.image.load(img_name).convert_alpha()

class Block(pygame.sprite.Sprite):
    def __init__(self, position : tuple[int, int], angle : int) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.positionX = position[0]
        self.positionY = position[1]
        self.angle = angle
        self.is_placed = False #init as true so you can move it around when you first call the var

        self.image = pygame.transform.smoothscale(loadify('Block.png'),(96,8))
        self.image_orgin = self.image
        self.rect = self.image.get_rect(center=(self.positionX,self.positionY))

        self.placeCoolDown = True
        self.placeCoolDownStart = time.time()
        self.placeCoolDownDur = 0.5


    def user_place(self):
        mouse_button = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()
        keys = pygame.key.get_pressed()
        self.image.set_alpha(100)
        
        self.rect = self.image.get_rect(center=mouse_pos)
        if keys[pygame.K_r]: # if key pressed is r
            #make mouse movement change the rotation
            self.angle += math.radians(5)

            self.image = pygame.transform.rotate(self.image_orgin, math.degrees(self.angle))
            print(math.degrees(self.angle))
            pass
        elif mouse_button[0] and not self.placeCoolDown:
            self.place()
        else:
            self.position = mouse_pos

        if self.placeCoolDownStart + self.placeCoolDownDur < time.time():
            self.placeCoolDown = False
    
    def place(self):
        self.image.set_alpha(255)
        self.is_placed = True

    def delete(self):
        self.kill()
    def update(self, dt):
        if not self.is_placed:
            self.user_place()
        else:
            #place the block or something idk
            pass
    
    def delete(self):
        #delete a block somehow
        self.kill()