import pygame
from config import *

def main_menu():
    running = True
    while running:
        screen.blit(tela_menu_img, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit'
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    return 'quit'

        if exit_btn.draw(screen):
            return 'quit'

        if normal_mode_btn.draw(screen):
            return 'game'

        if rush_mode_btn.draw(screen):
            return 'rush'
        
        pygame.display.flip()
