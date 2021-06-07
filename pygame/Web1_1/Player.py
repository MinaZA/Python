import pygame
from Data import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((25,25))
        self.surf.fill((128,0,128))
        self.rect = self.surf.get_rect(center = (WIDTH/2,75) )


        self.pos = vec(WIDTH/2,75)
        self.acc = vec(0,0)
        self.vel = vec(0,0)

    def Move(self):
        
        self.acc = vec(0,GRAVITY)

        key_pressed = pygame.key.get_pressed()

        if key_pressed[pygame.K_LEFT]:
            self.acc.x = -ACC
        if key_pressed[pygame.K_RIGHT]:
            self.acc.x = ACC

        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel 

        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH 

        self.rect = self.surf.get_rect(midbottom = (self.pos.x,self.pos.y) )

    def Collide(self,list_platform):
        hits = pygame.sprite.spritecollide(self ,list_platform , False)
        if hits:
            self.pos.y = hits[0].rect.top + 1
            self.vel.y = 0

    
    
    
    
    
    
 