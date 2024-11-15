import pygame
from classes import Button
from config import *
from game import exibir_texto

def main_score(pontuacao, perguntas_respondidas, perguntas_corretas, perguntas_erradas):
    menu_btn = Button(menu_btn_img, (315, 57), 523, 553)
    restart_btn = Button(restart_btn_img, (315, 57), 523, 485)

    running = True
    while running:
        screen.blit(tela_score_img, (0, 0))

        exibir_texto(f'Pontuação: {pontuacao}', 50, 150, BLACK)
        exibir_texto(f'Perguntas respondidas: {perguntas_respondidas}', 50, 200, BLACK)
        exibir_texto(f'Perguntas corretas: {perguntas_corretas}', 50, 250, GREEN)
        exibir_texto(f'Perguntas erradas: {perguntas_erradas}', 50, 300, RED)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return 'quit'
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    return 'quit'

        # Verifica se os botões são clicados
        if menu_btn.draw(screen):
            running = False
            return 'menu'
        
        if restart_btn.draw(screen):
            running = False
            return 'rush'

        pygame.display.flip()

    return 'menu'
