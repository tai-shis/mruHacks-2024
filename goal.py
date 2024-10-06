import pygame

def loadify(img_name):
    return pygame.image.load(img_name).convert_alpha()

class Goal(pygame.sprite.Sprite):
    def __init__(self, position: tuple[int, int]) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.point_award = 1000 #decrement by like, 100 or 200 for each Block placed
        self.position = position
        self.goal_reached = False

        self.image = pygame.transform.smoothscale(loadify('Ball.png'),(8,8))
        self.image_orgin = self.image
        self.rect = self.image.get_rect(center=(self.positionX,self.positionY))

    def update(self, dt):
        #do stuff
        pass