import pygame
from utils import *

pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 1366, 768
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# Cores
WHITE = (255, 255, 255)
LIGHT_GRAY = (220, 220, 220)
BLACK = (0, 0, 0)
PURPLE = (102, 0, 102)
GRAY = (169, 169, 169)
GREEN = (76, 156, 0)
RED = (204, 0, 0)

# Fonte
fonte = pygame.font.Font('assets/Fonte_braba.otf', 48)

# Carregamento de imagens dos botões
exit_btn_img = pygame.image.load('assets/exit_btn.png')
play_btn_img = pygame.image.load('assets/play_btn.png')

# Criação dos botões
from classes import Button
exit_btn = Button(exit_btn_img, (50, 50), WIDTH - 50, 10)
play_btn = Button(play_btn_img, (100, 100), WIDTH // 2 - 50, HEIGHT // 2 - 50)

caminho = "data/user_data.json"
initialize_user_json(caminho)
