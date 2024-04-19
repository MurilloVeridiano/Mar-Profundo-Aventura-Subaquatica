#atualizar_tela.py

import pygame

class AtualizarTela:
    def __init__(self, janela, fonte_pontos, cenario, gerenciar_objetos, checar_colisoes):
        self.janela = janela
        self.fonte_pontos = fonte_pontos
        self.cenario = cenario
        self.gerenciar_objetos = gerenciar_objetos
        self.checar_colisoes = checar_colisoes

    def atualizar_tela(self):
        # Limpa a tela
        self.janela.fill((0, 0, 0))
        # Desenha os cenários
        for posicao, cenario in zip(self.cenario.posicoes_cenario, self.cenario.cenarios):
            self.janela.blit(cenario, posicao)
        # Desenha o jogador e a minhoca
        self.janela.blit(self.gerenciar_objetos.jogador['imagem'], self.gerenciar_objetos.jogador['objRect'])
        self.janela.blit(self.gerenciar_objetos.obj_minhoca['imagem'], self.gerenciar_objetos.obj_minhoca['objRect'])
        # Atualiza a pontuação
        texto_pontuacao = self.fonte_pontos.render(f"PONTUAÇÃO: {self.checar_colisoes.pontos}", True, (255, 255, 255))
        self.janela.blit(texto_pontuacao, (self.janela.get_width() - 10 - texto_pontuacao.get_width(), 10))
        pygame.display.update()
