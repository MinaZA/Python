import pygame


class Platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((50,50))
        self.surf.fill((128,128,128))
        self.rect = self.surf.get_rect(center = (100,100))