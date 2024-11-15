import pygame
import sys
from menu import main_menu
from rush import main_rush
from game import main_game
from tela_vitoria import main_vitoria
from tela_derrota import main_derrota
from tela_reward import main_reward
from tela_score import main_score


def main():
    pygame.init()
    estado = 'menu'
    dados_jogo = None
    
    while estado != 'quit':
        if estado == 'menu':
            estado = main_menu()
        elif estado == 'rush':
            resultado = main_rush()
            if isinstance(resultado, tuple) and resultado[0] == 'score':
                estado, dados_jogo = resultado
        elif estado == 'game': 
            estado = main_game()
        elif estado == 'tela_vitoria':
            estado = main_vitoria()
        elif estado == 'tela_derrota': 
            estado = main_derrota()
        elif estado == 'reward':
            estado = main_reward()
        elif estado == 'score' and dados_jogo is not None:
            estado = main_score(*dados_jogo)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
