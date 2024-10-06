import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self, position : tuple[int, int], angle : int) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.position = position #position of center
        self.angle = angle
        self.is_placed = False #init as true so you can move it around when you first call the var

    def user_place(self, mouse_button):
        mouse_button = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_r]: # if key pressed is r
            #make mouse movement change the rotation
            pass
        elif mouse_button[0]:
            self.place()
        else:
            self.position = mouse_pos

    def place(self, mouse_pos):
        self.is_placed = True
        self.postition = mouse_pos

    def update(self, dt):
        if not self.is_placed:
            self.user_place()
        else:
            #place the block or something idk
            pass
    
    def delete(self):
        #delete a block somehow
        pass