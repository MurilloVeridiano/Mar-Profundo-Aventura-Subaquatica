import pygame
from SQL import run_query, update_hi_score

def get_hi_score(name):
    hosts = ['localhost']
    port = 3306
    user = 'user_game'
    pwd = '123'
    db_query = f"USE game; SELECT hi_score FROM score WHERE name = '{name}';"
    result = run_query(hosts, port, db_query, user, pwd)
    if result and len(result) > 0 and len(result[0]) > 0:
        return result[0][0][0]
    else:
        return 0


class AtualizarTela:
    def __init__(self, janela, fonte_pontos, cenario, gerenciar_objetos, checar_colisoes, nome_jogador):
        self.janela = janela
        self.fonte_pontos = fonte_pontos
        self.cenario = cenario
        self.gerenciar_objetos = gerenciar_objetos
        self.checar_colisoes = checar_colisoes
        self.hi_score = get_hi_score(nome_jogador)
        self.nome_jogador = nome_jogador

    def atualizar_tela(self):
        # Limpa a tela
        self.janela.fill((0, 0, 0))
        # Desenha os cenários e a minhoca
        self.cenario.desenhar()
        # Desenha o jogador
        self.janela.blit(self.gerenciar_objetos.jogador['imagem'], self.gerenciar_objetos.jogador['objRect'])
        # Desenha obstáculos
        self.gerenciar_objetos.desenhar_obstaculos(self.janela)
        # Atualiza a pontuação
        pontos = self.checar_colisoes.get_pontos()
        texto_pontuacao = self.fonte_pontos.render(f"PONTUAÇÃO: {pontos}", True, (255, 255, 255))
        self.janela.blit(texto_pontuacao, (0, 0))

        # Atualiza a pontuação máxima (hi-score)
        texto_hi_score = self.fonte_pontos.render(f'Hi-Score: {self.hi_score}', True, (255, 255, 255))
        self.janela.blit(texto_hi_score, (205, 0))

        # Exibir texto de bônus
        if self.checar_colisoes.bonus_text_counter > 0:
            texto_bonus = self.fonte_pontos.render(self.checar_colisoes.bonus_text, True, (255, 255, 0))
            self.janela.blit(texto_bonus, (self.janela.get_width() // 2 - texto_bonus.get_width() // 2, self.janela.get_height() // 2 - texto_bonus.get_height() // 2))
            self.checar_colisoes.bonus_text_counter -= 1

        pygame.display.update()



