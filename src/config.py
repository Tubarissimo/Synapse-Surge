import pygame
from utils import *
from classes import Button

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

# Fontes
fonte_light = pygame.font.Font('assets/fonts/NeueMachina-Light.otf', 48)
fonte_regular = pygame.font.Font('assets/fonts/NeueMachina-Regular.otf', 48)
fonte_ultrabold = pygame.font.Font('assets/fonts/NeueMachina-Ultrabold.otf', 48)

# Carregamento de imagens dos botões
exit_btn_img = pygame.image.load('assets/buttons/exit_btn.png')
normal_mode_btn_img = pygame.image.load('assets/buttons/normal_mode_btn.png')
rush_mode_btn_img = pygame.image.load('assets/buttons/rush_mode_btn.png')
menu_btn_img = pygame.image.load('assets/buttons/menu_btn.png')
proceed_btn_img = pygame.image.load('assets/buttons/proceed_btn.png')
restart_btn_img = pygame.image.load('assets/buttons/restart_btn.png')

# Criação dos botões
exit_btn = Button(exit_btn_img, (50, 50), WIDTH - 50, 10)
normal_mode_btn = Button(normal_mode_btn_img, (373, 57), 222, 550)
rush_mode_btn = Button(rush_mode_btn_img, (373, 57), 222, 610)

# botoes renomear, menu e prosseguir cada um deve ser criado na sua própria tela

# Backgrounds
tela_vitoria_img = pygame.image.load('assets/images/tela_vitoria.png')
tela_derrota_img = pygame.image.load('assets/images/tela_derrota.png')
tela_menu_img = pygame.image.load('assets/images/tela_menu.png')
tela_normal_mode_img = pygame.image.load('assets/images/tela_normal_mode.png')
tela_rush_mode_img = pygame.image.load('assets/images/tela_rush_mode.png')
tela_score_img = pygame.image.load('assets/images/tela_score.png')

initialize_user_json("data/user_data.json")
