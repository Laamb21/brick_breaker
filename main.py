#main.py

import pygame
from game.game_loop import run_game
from game.menu import show_menu
from settings import WIDTH, HEIGHT, BLACK

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Brick Breaker")

    #Show the menu before starting the game
    show_menu(screen)

    #Now start main game loop
    run_game(screen)

if __name__ == "__main__":
    main()