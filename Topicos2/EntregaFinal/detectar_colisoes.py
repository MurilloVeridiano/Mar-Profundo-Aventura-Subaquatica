import pygame
import random
from configuracoes import *

class ChecarColisoes:
    def __init__(self, gerenciar_objetos, cenario):
        self.jogador = gerenciar_objetos.jogador
        self.obj_minhoca = gerenciar_objetos.obj_minhoca
        self.obstaculos = gerenciar_objetos.obstaculos
        self.cenario = cenario
        self._pontos = 0
        self.bonus_text = ""
        self.bonus_text_counter = 0

    def checar_colisoes(self):
        bateu_minhoca = self.jogador['objRect'].colliderect(self.obj_minhoca['objRect'])
        if bateu_minhoca:
            self._pontos += 5
            self.matar_minhoca()
            self.cenario.gerar_nova_posicao_minhoca()
            self.bonus_text = "+5 bônus"
            self.bonus_text_counter = 40  # Mostrar o texto de bônus por 40 frames

        for obstaculo in self.obstaculos:
            if self.jogador['objRect'].colliderect(obstaculo['objRect']):
                self.jogador['morto'] = True  # Jogador colidiu com obstáculo
                pygame.mixer.music.stop()

        self.contar_pontos()

    def contar_pontos(self):
        for obstaculo in self.obstaculos:
            if obstaculo['objRect'].right < self.jogador['objRect'].left and not obstaculo.get('pontuado', False):
                self._pontos += 0.5
                obstaculo['pontuado'] = True

    def matar_minhoca(self):
        # Move a minhoca para fora da tela temporariamente
        self.obj_minhoca['objRect'].x = -self.obj_minhoca['objRect'].width
        self.obj_minhoca['objRect'].y = -self.obj_minhoca['objRect'].height

    def get_pontos(self):
        return self._pontos


