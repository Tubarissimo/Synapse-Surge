import pygame
import random
from config import *
from game import exibir_texto

def gerar_pergunta(num_elementos=2):
    operacoes = ['+', '-', '*']
    elementos = [random.randint(1, 10) for _ in range(num_elementos)]
    operacoes_escolhidas = [random.choice(operacoes) for _ in range(num_elementos - 1)]

    expressao = f"{elementos[0]}"
    for i in range(1, num_elementos):
        expressao += f" {operacoes_escolhidas[i - 1]} {elementos[i]}"

    resposta_correta = eval(expressao)  # Calcula a resposta correta

    return expressao, resposta_correta

def main_rush():
    pontuacao = 0
    perguntas_respondidas = 0
    perguntas_erradas = 0
    num_elementos = 2  # Começa com 2 elementos na expressão
    pergunta, resposta_correta = gerar_pergunta(num_elementos)
    resposta_usuario = ''
    inicio_tempo = pygame.time.get_ticks()  # Armazena o tempo inicial
    tempo_restante = 30  # Tempo de jogo em segundos

    cursor_visivel = True
    contador_cursor = 0

    rodando = True
    while rodando:
        tempo_decorrido = (pygame.time.get_ticks() - inicio_tempo) // 1000
        tempo_restante = max(0, 30 - tempo_decorrido)

        screen.blit(tela_rush_mode_img, (0, 0))
        exibir_texto(f'{tempo_restante}s', 270, 320, PURPLE)
        exibir_texto(pergunta, WIDTH // 2, 320)
        exibir_texto(f'Feitas: {perguntas_respondidas}', WIDTH - 270, 320, PURPLE)

        # Renderiza a resposta do usuário e centraliza na tela
        superficie_resposta = fonte_regular.render(resposta_usuario, True, BLACK)
        rect_resposta = superficie_resposta.get_rect(center=(WIDTH // 2, 550))
        screen.blit(superficie_resposta, rect_resposta.topleft)

        # Lógica para o cursor piscando
        contador_cursor += 1
        if contador_cursor % 360 < 180:
            cursor_visivel = True
        else:
            cursor_visivel = False

        if cursor_visivel:
            cursor_x = rect_resposta.right + 5 if resposta_usuario else WIDTH // 2
            pygame.draw.line(screen, BLACK, (cursor_x, rect_resposta.top), (cursor_x, rect_resposta.bottom), 2)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
                return 'menu'  # Garante que o retorno seja para o menu ao fechar a janela
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    # Verifica se há pelo menos um caractere numérico na resposta antes de enviar
                    if any(char.isdigit() for char in resposta_usuario):
                        perguntas_respondidas += 1
                        if int(resposta_usuario) == resposta_correta:
                            pontuacao += num_elementos  # Ganha pontos equivalentes ao número de elementos
                        else:
                            perguntas_erradas += 1
                            pontuacao -= num_elementos  # Perde pontos equivalentes ao número de elementos
                        resposta_usuario = ''

                        # A cada 5 perguntas, aumenta o número de elementos na expressão
                        if perguntas_respondidas % 5 == 0:
                            num_elementos += 1

                        pergunta, resposta_correta = gerar_pergunta(num_elementos)
                elif evento.key == pygame.K_BACKSPACE:
                    resposta_usuario = resposta_usuario[:-1]
                elif evento.unicode.isdigit() or evento.unicode == '-':
                    if evento.unicode == '-' and len(resposta_usuario) == 0:
                        resposta_usuario += evento.unicode
                    elif evento.unicode.isdigit():
                        resposta_usuario += evento.unicode

        if tempo_restante == 0:
            rodando = False  # Sai do loop e vai para a tela de pontuação

        pygame.display.flip()

    # Retorna os dados necessários para a função `main_score`
    return 'score', (pontuacao, perguntas_respondidas, perguntas_respondidas - perguntas_erradas, perguntas_erradas)
