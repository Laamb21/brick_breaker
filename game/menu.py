#game/menu.py

import pygame
import sys
from settings import WIDTH, HEIGHT, BLACK, WHITE, LAVENDER, DEEP_PURPLE, DEEP_MAUVE

def show_menu(screen):
    menu_active = True
    clock = pygame.time.Clock()
    
    #Create a font object
    font = pygame.font.Font(None, 74)
    
    #Render the menu text
    brick_text = font.render("Brick", True, DEEP_MAUVE)
    brick_text_rect = brick_text.get_rect(center=(WIDTH //2, HEIGHT * 0.20))
    breaker_text = font.render("Breaker", True, DEEP_MAUVE)
    breaker_text_rect = breaker_text.get_rect(center=(WIDTH //2, HEIGHT * 0.33))

    #Render button text
    button_text = font.render("Play", True, DEEP_PURPLE)
    #Create button rectangle slightly larger than text
    button_width = button_text.get_width() + 20
    button_height = button_text.get_height() + 10
    button_rect = pygame.Rect(0, 0, button_width, button_height)
    button_rect.center = (WIDTH //2, HEIGHT * 0.75)

    while menu_active:
        clock.tick(60)
        #Fill screen with background color
        screen.fill(LAVENDER)
        #Blit the menu text
        screen.blit(brick_text, brick_text_rect)
        screen.blit(breaker_text, breaker_text_rect)
        screen.blit(button_text, button_rect)
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if button_rect.collidepoint(mouse_pos):
                    menu_active = False
