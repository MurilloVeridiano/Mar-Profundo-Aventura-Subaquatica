# configuracoes.py
import pygame

VEL = 5
LARGURA_JANELA = 500
ALTURA_JANELA = 400
ESPACO_OBSTACULOS = 200  # Definindo o valor se for necessário

def mostrar_instrucoes(janela, fonte, cenario, gerenciar_objetos):
    # Desenhar o cenário e objetos do jogo
    cenario.desenhar()
    gerenciar_objetos.desenhar_obstaculos(janela)
    
    # Adicionar texto de instruções
    texto_esc = fonte.render("ESC para sair", True, (255, 255, 255))
    texto_espaco = fonte.render("Espaço para começar", True, (255, 255, 255))
    janela.blit(texto_esc, (janela.get_width() // 2 - texto_esc.get_width() // 2, janela.get_height() // 2 - texto_esc.get_height() // 2 - 20))
    janela.blit(texto_espaco, (janela.get_width() // 2 - texto_espaco.get_width() // 2, janela.get_height() // 2 - texto_espaco.get_height() // 2 + 20))
    pygame.display.update()

