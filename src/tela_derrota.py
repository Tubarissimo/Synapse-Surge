import pygame
from classes import Button
from config import *

def main_derrota():
    menu_btn = Button(menu_btn_img, (315, 57), 523, 553)
    restart_btn = Button(restart_btn_img, (315, 57), 523, 485)

    running = True
    while running:
        screen.blit(tela_derrota_img, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return 'quit'
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    return 'quit'

        if menu_btn.draw(screen):
            running = False
            return 'menu'
        
        if restart_btn.draw(screen):
            running = False
            return 'game'

        pygame.display.flip()

    return 'menu'
