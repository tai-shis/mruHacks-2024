import pygame

def loadify(img_name):
    return pygame.image.load(img_name).convert_alpha()

class Block(pygame.sprite.Sprite):
    def __init__(self, position : tuple[int, int], angle : int) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.positionX = position[0]
        self.positionY = position[1]
        self.angle = angle
        self.is_placed = False #init as true so you can move it around when you first call the var

        self.image = pygame.transform.smoothscale(loadify('Ball.png'),(8,8))
        self.image_orgin = self.image
        self.rect = self.image.get_rect(center=(self.positionX,self.positionY))

    def user_place(self):
        mouse_button = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()
        keys = pygame.key.get_pressed()
        
        self.rect = self.image.get_rect(center=mouse_pos)
        if keys[pygame.K_r]: # if key pressed is r
            #make mouse movement change the rotation
            print("r")
            pass
        elif mouse_button[0]:
            #self.place(mouse_pos)
            pass
        else:
            self.position = mouse_pos
    '''
    def place(self):
        self.is_placed = True
        self.postition = mouse_pos
    '''
    def update(self, dt):
        if not self.is_placed:
            self.user_place()
        else:
            #place the block or something idk
            pass
    
    def delete(self):
        #delete a block somehow
        pass