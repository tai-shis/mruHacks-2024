import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self, position : tuple[int, int], angle : int) -> None:

        self.position = position #position of center
        self.angle = angle
        self.is_ghost = True #init as true so you can move it around when you first call the var

    def user_place(self):
        pass

    def place(self):
        self.is_ghost = False

    def update(self, dt):
        if self.is_ghost:
            self.user_place()
        else:
            #place the block or something idk
            pass
    
    def delete(self):
        #delete a block somehow
        pass