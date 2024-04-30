import pygame
from configuracoes import LARGURA_JANELA, ALTURA_JANELA

class GerenciarCenario:
    def __init__(self, janela):
        self.janela = janela
        # Carregar cenários
        self.cenarios = [self.carregar_e_escalar(f'Imagens/cenario{i}.png', (LARGURA_JANELA, ALTURA_JANELA)) for i in range(1, 5)]
        self.posicoes_cenario = [(i * LARGURA_JANELA, 0) for i in range(len(self.cenarios))]
        # Velocidade do movimento do cenário
        self.velocidade_cenario = 1

    def carregar_e_escalar(self, caminho, dimensoes):
        imagem = pygame.image.load(caminho)
        return pygame.transform.scale(imagem, dimensoes)

    def mover_cenario(self):
        # Atualizar a posição de cada cenário
        for i in range(len(self.posicoes_cenario)):
            # Mover cenário para a esquerda
            self.posicoes_cenario[i] = (self.posicoes_cenario[i][0] - self.velocidade_cenario, 0)

            # Se o cenário saiu completamente da tela, reposicione-o para o fim da fila
            if self.posicoes_cenario[i][0] + LARGURA_JANELA < 0:
                # Achar o índice do cenário mais à direita e colocar este cenário à sua direita
                max_x = max(pos[0] for pos in self.posicoes_cenario)
                self.posicoes_cenario[i] = (max_x + LARGURA_JANELA, 0)

    def desenhar_cenario(self):
        # Desenhar cada cenário na posição atual
        for imagem, posicao in zip(self.cenarios, self.posicoes_cenario):
            self.janela.blit(imagem, posicao)
