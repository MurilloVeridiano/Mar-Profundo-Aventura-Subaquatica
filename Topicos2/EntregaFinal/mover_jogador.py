import pygame
from configuracoes import LARGURA_JANELA, ALTURA_JANELA

class MoverJogador:
    def __init__(self, gerenciar_objetos):
        self.jogador = gerenciar_objetos.jogador
        self.jogador['vel'] = 0  # Velocidade inicial
        self.gravidade = 0.2
        self.pulo = 5
        self.jogador['morto'] = False

    def mover_jogador(self):
        self.jogador['vel'] += self.gravidade  # Aplica gravidade
        if not self.jogador['morto']:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
                self.jogador['vel'] = -self.pulo  # Aplica pulo se a tecla de espaço ou cima for pressionada

        self.jogador['objRect'].y += self.jogador['vel']  # Atualiza a posição do jogador

        # Limita a posição do jogador à tela
        if self.jogador['objRect'].top < 0:
            self.jogador['objRect'].top = 0
        if self.jogador['objRect'].bottom > ALTURA_JANELA:
            self.jogador['objRect'].bottom = ALTURA_JANELA

    def tratar_eventos(self, evento):
        if evento.type == pygame.KEYDOWN:
            if evento.key in (pygame.K_SPACE, pygame.K_UP):
                self.jogador['vel'] = -self.pulo  # Aplica pulo se a tecla de espaço ou cima for pressionada
