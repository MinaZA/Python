import pygame
from Data import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((50,50))
        self.surf.fill((254,0,0))
        self.rect = self.surf.get_rect(center = (100,100))

        self.pos = pygame.math.Vector2((100,100))
        self.vel = pygame.math.Vector2((0,0))
        self.acc = pygame.math.Vector2((0,0))

    def Move(self):

        self.acc.x = 0
        self.acc.y = GRAVITY

        pressed_key = pygame.key.get_pressed()

        if pressed_key[pygame.K_LEFT]:
            self.acc.x = -ACC
        if pressed_key[pygame.K_RIGHT]:
            self.acc.x = ACC


        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel

        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        self.rect.midbottom = self.pos

    def Collision(self,list_platform):
        hits = pygame.sprite.spritecollide(self ,list_platform , False)
        if hits:
            self.pos.y = hits[0].rect.top + 1
            self.vel.y = 0

    def Jump(self,list_platform):
        hits = pygame.sprite.spritecollide(self ,list_platform , False)
        if hits:
            self.vel.y += -JUMP_FORCE