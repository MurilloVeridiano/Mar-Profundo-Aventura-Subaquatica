# Jogador/mover_jogador.py
import pygame
from configuracoes import LARGURA_JANELA, ALTURA_JANELA

class MoverJogador:
    def __init__(self, gerenciar_objetos):
        self.jogador = gerenciar_objetos.jogador
        self.teclas = {'esquerda': False, 'direita': False, 'cima': False, 'baixo': False}

    def mover_jogador(self):
        if self.teclas['esquerda'] and self.jogador['objRect'].left > 5:
            self.jogador['objRect'].x -= self.jogador['vel']
        if self.teclas['direita'] and self.jogador['objRect'].right < LARGURA_JANELA - 4:
            self.jogador['objRect'].x += self.jogador['vel']
        if self.teclas['cima'] and self.jogador['objRect'].top > 5:
            self.jogador['objRect'].y -= self.jogador['vel']
        if self.teclas['baixo'] and self.jogador['objRect'].bottom < ALTURA_JANELA:
            self.jogador['objRect'].y += self.jogador['vel']


    def tratar_eventos(self, evento):
        if evento.type == pygame.KEYDOWN:
            if evento.key in (pygame.K_LEFT, pygame.K_a):
                self.teclas['esquerda'] = True
            if evento.key in (pygame.K_RIGHT, pygame.K_d):
                self.teclas['direita'] = True
            if evento.key in (pygame.K_UP, pygame.K_w):
                self.teclas['cima'] = True
            if evento.key in (pygame.K_DOWN, pygame.K_s):
                self.teclas['baixo'] = True

        if evento.type == pygame.KEYUP:
            if evento.key in (pygame.K_LEFT, pygame.K_a):
                self.teclas['esquerda'] = False
            if evento.key in (pygame.K_RIGHT, pygame.K_d):
                self.teclas['direita'] = False
            if evento.key in (pygame.K_UP, pygame.K_w):
                self.teclas['cima'] = False
            if evento.key in (pygame.K_DOWN, pygame.K_s):
                self.teclas['baixo'] = False


