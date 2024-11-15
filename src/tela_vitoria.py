import pygame
from classes import Button
from config import *

def main_vitoria():
    proceed_btn = Button(proceed_btn_img, (270, 57), 548, 502)

    running = True
    while running:
        screen.blit(tela_vitoria_img, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return 'quit'
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    return 'quit'

        # Verifica se os botões são clicados
        if proceed_btn.draw(screen):
            running = False
            return 'reward'

        pygame.display.flip()

    return 'reward'
