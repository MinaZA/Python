import pygame
from Data import *
from Player import Player
from Platform import Platform
#loading
pygame.init()

frame_per_sec = pygame.time.Clock()

display_surface = pygame.display.set_mode((WIDTH,HEIGHT))

P = Player()
P1 = Platform()

P2 = Platform()
P2.surf = pygame.Surface((20,HEIGHT))
P2.surf.fill((0,254,0))
P2.rect = P2.surf.get_rect(midleft = (0,HEIGHT/2))
P3 = Platform()
P3.surf = pygame.Surface((20,HEIGHT))
P3.surf.fill((0,254,0))
P3.rect = P2.surf.get_rect(midright = (WIDTH,HEIGHT/2))


all_sprite = pygame.sprite.Group()
all_sprite.add(P)
all_sprite.add(P1)
all_sprite.add(P2)
all_sprite.add(P3)

Platforms = pygame.sprite.Group()
Platforms.add(P1)
Platforms.add(P2)
Platforms.add(P3)

#Update
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                P.Jump(Platforms)

   
    P.Move()
    P.Collision(Platforms)


    display_surface.fill((20,20,0))

    for entity in all_sprite:
        display_surface.blit(entity.surf, entity.rect)

    pygame.display.update()

    frame_per_sec.tick(60)
