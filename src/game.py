import pygame
import random
from config import *
from utils import *

def gerar_pergunta(num_elementos=2):
    operacoes = ['+', '-', '*']
    elementos = [random.randint(1, 10) for _ in range(num_elementos)]
    operacoes_escolhidas = [random.choice(operacoes) for _ in range(num_elementos - 1)]

    expressao = f"{elementos[0]}"
    for i in range(1, num_elementos):
        expressao += f" {operacoes_escolhidas[i - 1]} {elementos[i]}"

    resposta_correta = eval(expressao)  # Calcula a resposta correta

    return expressao, resposta_correta

def exibir_texto(texto, x, y, cor=BLACK):
    superficie_texto = fonte_regular.render(texto, True, cor)
    screen.blit(superficie_texto, (x, y))

def main_game():
    # Carrega a fase atual do arquivo JSON
    user_data = from_json('data/user_data.json')
    fase_atual = user_data.get("fase", 1)  # Pega a fase atual; se não existir, usa 1 como padrão
    meta = 5 + (5 * fase_atual)  # Calcula a meta de pontos

    pontuacao = 0
    perguntas_respondidas = 0
    perguntas_erradas = 0
    num_elementos = 2  # Começa com 2 elementos na expressão
    pergunta, resposta_correta = gerar_pergunta(num_elementos)
    resposta_usuario = ''
    inicio_tempo = pygame.time.get_ticks()  # Armazena o tempo inicial
    tempo_restante = 30  # Tempo de jogo em segundos

    campo_texto_rect = pygame.Rect(50, 250, 400, 50)
    cursor_visivel = True
    contador_cursor = 0

    rodando = True
    while rodando:
        tempo_decorrido = (pygame.time.get_ticks() - inicio_tempo) // 1000
        tempo_restante = max(0, 30 - tempo_decorrido)

        screen.fill(LIGHT_GRAY)
        exibir_texto(f'Tempo restante: {tempo_restante}s', 50, 50, PURPLE)
        exibir_texto(f'Perguntas respondidas: {perguntas_respondidas}', 50, 100, PURPLE)
        exibir_texto(f'Meta de pontos: {meta}', 50, 150, PURPLE)
        exibir_texto(pergunta, 50, 200)

        pygame.draw.rect(screen, WHITE, campo_texto_rect)
        pygame.draw.rect(screen, GRAY, campo_texto_rect, 2)

        superficie_resposta = fonte_regular.render(resposta_usuario, True, BLACK)
        screen.blit(superficie_resposta, (campo_texto_rect.x + 5, campo_texto_rect.y + 5))

        contador_cursor += 1
        if contador_cursor % 360 < 180:
            cursor_visivel = True
        else:
            cursor_visivel = False

        if cursor_visivel:
            cursor_x = campo_texto_rect.x + 5 + superficie_resposta.get_width()
            pygame.draw.line(screen, BLACK, (cursor_x, campo_texto_rect.y + 5), (cursor_x, campo_texto_rect.y + 45), 2)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    if resposta_usuario.isdigit() or (resposta_usuario.startswith('-') and resposta_usuario[1:].isdigit()):
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

        # Verifica se a meta de pontos foi atingida
        if pontuacao >= meta:
            screen.fill(LIGHT_GRAY)
            exibir_texto('Parabéns! Você alcançou a meta!', 50, 50, GREEN)
            pygame.display.flip()
            pygame.time.wait(3000)
            return 'tela_vitoria'  # Leva o jogador para outra tela

        if exit_btn.draw(screen):
            return 'menu'

        pygame.display.flip()

    # Exibe as estatísticas finais
    screen.fill(LIGHT_GRAY)
    exibir_texto(f'Jogo Finalizado!', 50, 50, PURPLE)
    exibir_texto(f'Pontuação: {pontuacao}', 50, 150, BLACK)
    exibir_texto(f'Perguntas respondidas: {perguntas_respondidas}', 50, 200, BLACK)
    exibir_texto(f'Perguntas corretas: {pontuacao // num_elementos}', 50, 250, GREEN)
    exibir_texto(f'Perguntas erradas: {perguntas_erradas}', 50, 300, RED)

    pygame.display.flip()
    pygame.time.wait(5000)

    return 'menu'
