import pygame
from Platform import Platform
from Data import *
from Player import Player
#Charement du jeu
pygame.init()

frame_per_second = pygame.time.Clock()

displaysurface = pygame.display.set_mode((WIDTH,HEIGTH))
pygame.display.set_caption("C'est mon jeu")

P1 = Platform()
P1.surf = pygame.Surface((WIDTH,50))
P1.rect = P1.surf.get_rect(center = (WIDTH/2,HEIGTH -25))
P2 = Platform()
P2.surf = pygame.Surface((50,HEIGTH))
P2.rect = P2.surf.get_rect(center = (WIDTH-25,HEIGTH/2))
P3 = Platform()
P3.surf = pygame.Surface((50,HEIGTH))
P3.rect = P3.surf.get_rect(center = (25,HEIGTH/2))

Player = Player()

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(P2)
all_sprites.add(P3)
all_sprites.add(Player)

Platforms = pygame.sprite.Group()
Platforms.add(P1)
Platforms.add(P2)
Platforms.add(P3)

#Update du jeu 
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
        elif event.type == pygame.KEYDOWN:
            print("touche clavier")


    Player.Move()
    Player.Collide(Platforms)

    displaysurface.fill((255,50,0))

    for entity in all_sprites:
        displaysurface.blit(entity.surf,entity.rect)

    pygame.display.update()
    frame_per_second.tick(FPS)