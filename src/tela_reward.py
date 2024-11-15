import pygame
from classes import Button
from config import *
from utils import *

def main_reward():
    proceed_btn = Button(proceed_btn_img, (270, 57), 706, 560)

    user_data = from_json('data/user_data.json')
    fase_atual = str(user_data['fase'])

    print("\n\n\na fase atual eh ", type(fase_atual), "\n\n\n")

    data = from_json("data/rewards.json")
    caminho_fase_img = data[fase_atual]
    
    fase_img = pygame.image.load(caminho_fase_img)

    user_data['fase'] = int(fase_atual) + 1
    if int(user_data['fase']) > 10: user_data['fase'] = 1
    to_json(user_data,'data/user_data.json')

    running = True
    while running:
        screen.blit(fase_img, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return 'quit'
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    return 'menu'

        # Verifica se os botões são clicados
        if proceed_btn.draw(screen):
            running = False
            return 'menu'

        pygame.display.flip()

    return 'menu'
