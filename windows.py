from os import write
import pygame
from pygame.surfarray import pixels_blue
#from player import *





pygame.init()
windows = pygame.display.set_mode((1386,490))
font_titre = pygame.font.SysFont(None,50)
text_titre = font_titre.render("WORD WAR", True, (255, 255, 255))
font = pygame.font.SysFont(None,30)
text_start = font.render("Press Entrer pour lancer", True, (255, 255, 255))
text_quit = font.render("Press Echap pour quitter", True, (255, 255, 255))
text_son = font.render("Press F1 ,stop music / F3 , play music", True, (255,255,255))
button_start = pygame.image.load('start_button.png')
button_start = pygame.transform.scale(button_start, (150,50))
button_start_rectangle = button_start.get_rect()
button_start_rectangle.x = 630
button_start_rectangle.y = 250
button_quit = pygame.image.load('quit_button.png')
button_quit = pygame.transform.scale(button_quit, (150,50))
button_quit_rectangle = button_quit.get_rect()
background_menu = pygame.image.load('menu_background.jpg')
background_menu = pygame.transform.scale(background_menu, (1386,490))
background_game = pygame.image.load('fond.jpg')
background_game = pygame.transform.scale(background_game, (1386,490))
frame_per_sec = pygame.time.Clock()
music_combat = pygame.mixer.Sound('music_combat.wav')
music_menu = pygame.mixer.music.load('music_menu.wav')
music_menu = pygame.mixer.music.play(-1)
mus = pygame.mouse.get_pos(650,300)
windows.blit(text_son, (10, 20))
windows.blit(background_game, (0,0))
windows.blit(background_menu, (0,0))
windows.blit(button_start, button_start_rectangle)
windows.blit(button_quit, (630,350))
windows.blit(text_start, (590, 310))
windows.blit(text_quit, (590, 430))
windows.blit(text_titre, (600, 20))
music_combat_compte = 0
#pygame.font.init()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
            if event.key == pygame.K_KP_ENTER:
                windows.blit(background_game, (0,0))
                windows.blit(text_son, (10, 20))
                music_menu = pygame.mixer.music.stop()
                music_combat.play(-1)
                music_combat_compte = 1
            if event.key == pygame.K_F3 and music_combat_compte != 1 :
                music_combat.play(-1)
                music_combat_compte = 1
            elif event.key == pygame.K_F1 and music_combat_compte == 1 :
                music_combat.stop()
                music_combat_compte = 0
            #elif event.type == pygame.MOUSEBUTTONDOWN:
                #if pygame.Rect.collidepoint(button_start_rectangle, event.pos):
                #if (event.pos > button_start_rectangle.x and event.pos < 
                #(button_start_rectangle.x + 100)) and (event.pos > button_start_rectangle.y and 
                #event.pos < (button_start_rectangle.y + 60)) :
                 #   windows.blit(background_game, (0,0))
                    #music_menu = pygame.mixer.music.stop()
                    #music_combat.play(-1)
    pygame.display.update()

