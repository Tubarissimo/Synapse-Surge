import pygame
import sys
from menu import main_menu
from rush import main_rush
from game import main_game
from tela_vitoria import main_vitoria
from tela_reward import main_reward


def main():
    pygame.init()
    estado = 'menu'
    
    while estado != 'quit':
        if estado == 'menu':
            estado = main_menu()
        elif estado == 'rush':
            estado = main_rush()
        elif estado == 'game': 
            estado = main_game()
        elif estado == 'tela_vitoria':
            estado = main_vitoria()
        elif estado == 'reward':
            estado = main_reward()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
