#gerenciar_cenario.py

import pygame
from configuracoes import LARGURA_JANELA

class GerenciarCenario:
    def __init__(self, janela):
        self.janela = janela
        # Carregar cenários
        self.cenarios = [self.carregar_e_escalar(f'Imagens/cenario{i}.png', (LARGURA_JANELA, LARGURA_JANELA)) for i in range(1, 5)]
        self.posicoes_cenario = [(i * LARGURA_JANELA, 0) for i in range(len(self.cenarios))]
        # Carregar imagens do peixe e da minhoca
        self.peixe = pygame.image.load('Imagens/peixe.png')
        self.minhoca = pygame.image.load('Imagens/minhoca.png')

    def carregar_e_escalar(self, caminho, dimensoes):
        imagem = pygame.image.load(caminho)
        return pygame.transform.scale(imagem, dimensoes)

    def mover_cenario(self):
        for i, (x, y) in enumerate(self.posicoes_cenario):
            if x + LARGURA_JANELA < 0:
                x = self.posicoes_cenario[(i - 1) % len(self.posicoes_cenario)][0] + LARGURA_JANELA
            self.posicoes_cenario[i] = (x - 1, y)
