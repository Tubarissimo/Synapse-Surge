import pygame
from config import *

def main_menu():
    running = True
    while running:
        screen.fill(LIGHT_GRAY)

        title_text = fonte.render("Synapse Surge", True, BLACK)
        title_rect = title_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 3))
        screen.blit(title_text, title_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit'
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    return 'quit'

        if exit_btn.draw(screen):
            return 'quit'

        if play_btn.draw(screen):
            return 'jogo'

        pygame.display.update()
