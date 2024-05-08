#gerenciar_objetos.py
import pygame
from configuracoes import VEL

class GerenciarObjetos:
    def __init__(self, cenario):
        # Inicializa jogador
        self.jogador = {
            'objRect': pygame.Rect(50, 50, cenario.peixe.get_width(), cenario.peixe.get_height()),
            'imagem': cenario.peixe,
            'vel': VEL
        }
        # Inicializa minhoca
        self.obj_minhoca = {
            'objRect': pygame.Rect(250, 200, cenario.minhoca.get_width(), cenario.minhoca.get_height()),
            'imagem': cenario.minhoca,
            'vel': VEL
        }
