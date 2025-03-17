#game/menu.py

import pygame
import sys
from settings import WIDTH, HEIGHT, BLACK, WHITE

def show_menu(screen):
    menu_active = True
    #Create a font object
    font = pygame.font.Font(None, 74)
    #Render the menu text
    text = font.render("Press Enter to Play", True, WHITE)
    text_rect = text.get_rect(center=(WIDTH //2, HEIGHT //2))

    while menu_active:
        #Fill screen with background color
        screen.fill(BLACK)
        #Blit the menu text
        screen.blit(text, text_rect)
        #Update game display
        pygame.display.flip()

        #Process events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #Wait for user to press the enter key
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    menu_active = False
                    