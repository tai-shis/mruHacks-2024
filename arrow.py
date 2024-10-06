import pygame

def loadify(img_name):
    return pygame.image.load(img_name).convert_alpha()

class Arrow(pygame.sprite.Sprite):
    def __init__(self, position: tuple[int, int], angle: int) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.position = position

        self.image = pygame.transform.smoothscale(loadify('arrow.png'),(32,32))
        self.image_orgin = self.image
        self.rect = self.image.get_rect(center=(self.position[0],self.position[1]))
    
    def draw(self) -> None:
        # draw object @ angle

        