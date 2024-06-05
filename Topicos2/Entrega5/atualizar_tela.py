import pygame
from SQL import run_query, update_hi_score

def get_hi_score():
    hosts = ['localhost']
    port = 3306
    db_query = 'USE game; SELECT hi_score FROM score WHERE idscore = 1;'
    result = run_query(hosts, port, db_query)
    if result and len(result) > 0 and len(result[0]) > 0:
        return result[0][0][0]
    else:
        return 0

class AtualizarTela:
    def __init__(self, janela, fonte_pontos, cenario, gerenciar_objetos, checar_colisoes):
        self.janela = janela
        self.fonte_pontos = fonte_pontos
        self.cenario = cenario
        self.gerenciar_objetos = gerenciar_objetos
        self.checar_colisoes = checar_colisoes
        self.hi_score = get_hi_score()

    def atualizar_tela(self):
        # Limpa a tela
        self.janela.fill((0, 0, 0))
        # Desenha os cenários e a minhoca
        self.cenario.desenhar()
        # Desenha o jogador
        self.janela.blit(self.gerenciar_objetos.jogador['imagem'], self.gerenciar_objetos.jogador['objRect'])
        # Atualiza a pontuação
        texto_pontuacao = self.fonte_pontos.render(f"PONTUAÇÃO: {self.checar_colisoes.pontos}", True, (255, 255, 255))
        self.janela.blit(texto_pontuacao, (0, 0))
        
        # Verifica se a pontuação atual é maior que o hi_score
        if self.checar_colisoes.pontos > self.hi_score:
            self.hi_score = self.checar_colisoes.pontos
            update_hi_score(self.hi_score)

        # Atualiza a pontuação máxima (hi-score)
        texto_hi_score = self.fonte_pontos.render(f'Hi-Score: {self.hi_score}', True, (255, 255, 255))
        self.janela.blit(texto_hi_score, (205, 0))

        pygame.display.update()
