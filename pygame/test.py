import pygame

pygame.init()
windows = pygame.display.set_mode((640,400))
background = pygame.image.load('background.jpg')
launched = True

while launched:
    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False