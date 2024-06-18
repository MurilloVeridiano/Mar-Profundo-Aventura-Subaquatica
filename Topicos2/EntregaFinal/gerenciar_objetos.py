import pygame
import random
from configuracoes import VEL, LARGURA_JANELA, ALTURA_JANELA, ESPACO_OBSTACULOS

class GerenciarObjetos:
    def __init__(self, cenario):
        try:
            self.obstaculo = pygame.image.load('Imagens/obstaculo.png')
            print("Imagem do obstáculo carregada com sucesso.")
        except pygame.error as e:
            print(f"Erro ao carregar a imagem do obstáculo: {e}")
        
        self.obstaculo_cima = pygame.transform.flip(self.obstaculo, False, True)
        print("Imagem do obstáculo invertida com sucesso.")
        
        self.obj_rect_obstaculo = self.obstaculo.get_rect()

        # Inicializa jogador
        self.jogador = {
            'objRect': pygame.Rect(50, 200, cenario.peixe.get_width(), cenario.peixe.get_height()),
            'imagem': cenario.peixe,
            'vel': VEL
        }

        # Inicializa minhoca
        self.obj_minhoca = {
            'objRect': cenario.obj_rect_minhoca,
            'imagem': cenario.minhoca,
            'vel': VEL
        }

        self.obstaculos = []
        self.cenario = cenario
        self.tempo_para_proximo_obstaculo = 0
        self.espaco_entre_obstaculos = ESPACO_OBSTACULOS
        self.altura_gap = 140  # Ajustar conforme necessário

    def gerar_obstaculo(self):
        largura_obstaculo = 74  # Largura fixa do obstáculo

        altura_maxima_disponivel = ALTURA_JANELA - self.altura_gap
        altura_obstaculo_cima = random.randint(50, altura_maxima_disponivel - 50)
        altura_obstaculo_baixo = altura_maxima_disponivel - altura_obstaculo_cima

        proporcao_original = self.obstaculo.get_height() / self.obstaculo.get_width()
        nova_altura_cima = int(largura_obstaculo * proporcao_original)
        nova_altura_baixo = int(largura_obstaculo * proporcao_original)

        obstaculo_cima_imagem = pygame.transform.scale(self.obstaculo_cima, (largura_obstaculo, altura_obstaculo_cima))
        obstaculo_baixo_imagem = pygame.transform.scale(self.obstaculo, (largura_obstaculo, altura_obstaculo_baixo))

        obstaculo_cima = {
            'imagem': obstaculo_cima_imagem,
            'objRect': pygame.Rect(LARGURA_JANELA, 0, largura_obstaculo, altura_obstaculo_cima),
            'vel': VEL
        }

        obstaculo_baixo = {
            'imagem': obstaculo_baixo_imagem,
            'objRect': pygame.Rect(LARGURA_JANELA, ALTURA_JANELA - altura_obstaculo_baixo, largura_obstaculo, altura_obstaculo_baixo),
            'vel': VEL
        }

        self.obstaculos.append(obstaculo_cima)
        self.obstaculos.append(obstaculo_baixo)

    def mover_obstaculos(self):
        for obstaculo in self.obstaculos:
            obstaculo['objRect'].x -= obstaculo['vel']

    def atualizar(self):
        self.mover_obstaculos()
        if self.tempo_para_proximo_obstaculo <= 0:
            self.gerar_obstaculo()
            self.tempo_para_proximo_obstaculo = random.randint(40, 55)  # Ajustar conforme necessário
        else:
            self.tempo_para_proximo_obstaculo -= 1

    def desenhar_obstaculos(self, tela):
        for obstaculo in self.obstaculos:
            rect = obstaculo['objRect']
            # Depuração: imprimir os detalhes dos obstáculos
            pygame.draw.rect(tela, (255, 0, 0), rect, 2)  # Cor vermelha, espessura 2
            # Desenhar imagem para verificar se a imagem é o problema
            tela.blit(obstaculo['imagem'], rect)
