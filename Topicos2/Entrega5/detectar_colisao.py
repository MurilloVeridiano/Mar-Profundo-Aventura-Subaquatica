import random
from configuracoes import LARGURA_JANELA, ALTURA_JANELA

class ChecarColisoes:
    def __init__(self, gerenciar_objetos, cenario):
        self.jogador = gerenciar_objetos.jogador
        self.obj_minhoca = gerenciar_objetos.obj_minhoca
        self.cenario = cenario
        self.pontos = 0

    def checar_colisoes(self):
        bateu = self.jogador['objRect'].colliderect(self.obj_minhoca['objRect'])
        if bateu:
            self.pontos += 1
            self.matar_minhoca()
            self.cenario.gerar_nova_posicao_minhoca()

    def matar_minhoca(self):
        # Move a minhoca para fora da tela temporariamente
        self.obj_minhoca['objRect'].x = -self.obj_minhoca['objRect'].width
        self.obj_minhoca['objRect'].y = -self.obj_minhoca['objRect'].height
