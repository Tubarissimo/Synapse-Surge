import pygame
import sys
from menu import main_menu
from jogo import main_jogo

def main():
    pygame.init()
    estado = 'menu'
    
    while estado != 'quit':
        if estado == 'menu':
            estado = main_menu()
        elif estado == 'jogo':
            estado = main_jogo()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
