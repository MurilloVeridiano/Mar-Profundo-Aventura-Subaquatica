import pygame
import random
from configuracoes import LARGURA_JANELA, ALTURA_JANELA

class GerenciarCenario:
    def __init__(self, janela):
        self.janela = janela
        # Carregar cenários
        self.cenarios = [self.carregar_e_escalar(f'Imagens/cenario{i}.png', (LARGURA_JANELA, LARGURA_JANELA)) for i in range(1, 5)]
        self.posicoes_cenario = [(i * LARGURA_JANELA, 0) for i in range(len(self.cenarios))]
        # Carregar imagens do peixe e da minhoca
        self.peixe = pygame.image.load('Imagens/peixe.png')
        self.minhoca = pygame.image.load('Imagens/minhoca.png')
        self.posicao_minhoca = [550, 150]
        self.obj_rect_minhoca = self.minhoca.get_rect(topleft=self.posicao_minhoca)

    def carregar_e_escalar(self, caminho, dimensoes):
        imagem = pygame.image.load(caminho)
        return pygame.transform.scale(imagem, dimensoes)

    def mover_cenario(self):
        for i, (x, y) in enumerate(self.posicoes_cenario):
            if x + LARGURA_JANELA < 0:
                x = self.posicoes_cenario[(i - 1) % len(self.posicoes_cenario)][0] + LARGURA_JANELA
            self.posicoes_cenario[i] = (x - 1, y)
        
        self.mover_minhoca()

    def mover_minhoca(self):
        self.posicao_minhoca[0] -= 1
        if self.posicao_minhoca[0] < 0:
            self.posicao_minhoca[0] = LARGURA_JANELA + random.randint(50, 100)
            self.posicao_minhoca[1] = random.randint(0, ALTURA_JANELA - self.minhoca.get_height())
        self.obj_rect_minhoca.topleft = self.posicao_minhoca

    def gerar_nova_posicao_minhoca(self):
        # Gera uma nova posição fora da tela à direita
        nova_x = LARGURA_JANELA + random.randint(50, 100)  # Para garantir que ela comece fora da tela
        nova_y = random.randint(0, ALTURA_JANELA - self.obj_rect_minhoca.height)
        self.posicao_minhoca = [nova_x, nova_y]
        self.obj_rect_minhoca.topleft = self.posicao_minhoca
            
    def desenhar(self):
        # Desenha os cenários
        for posicao, cenario in zip(self.posicoes_cenario, self.cenarios):
            self.janela.blit(cenario, posicao)
        # Desenha a minhoca se ela estiver dentro da tela
        if self.obj_rect_minhoca.x > -self.obj_rect_minhoca.width:
            self.janela.blit(self.minhoca, self.obj_rect_minhoca.topleft)
