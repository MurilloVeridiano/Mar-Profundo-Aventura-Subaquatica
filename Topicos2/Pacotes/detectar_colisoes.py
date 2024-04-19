#detectar_colisoes.py

import random
from configuracoes import LARGURA_JANELA, ALTURA_JANELA

class ChecarColisoes:
    def __init__(self, gerenciar_objetos):
        self.jogador = gerenciar_objetos.jogador
        self.obj_minhoca = gerenciar_objetos.obj_minhoca
        self.pontos = 0

    def checar_colisoes(self):
        bateu = self.jogador['objRect'].colliderect(self.obj_minhoca['objRect'])
        if bateu:
            self.pontos += 1
            self.obj_minhoca['objRect'].x = random.randint(0, LARGURA_JANELA - self.obj_minhoca['objRect'].width)
            self.obj_minhoca['objRect'].y = random.randint(0, ALTURA_JANELA - self.obj_minhoca['objRect'].height)
