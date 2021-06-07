import pygame
from Data import *

class Platform (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((WIDTH,20))
        self.surf.fill((0,254,0))
        self.rect = self.surf.get_rect(center = (WIDTH/2,HEIGHT))