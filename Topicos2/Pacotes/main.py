# main.py
import pygame
from configuracoes import LARGURA_JANELA, ALTURA_JANELA
from mover_jogador import MoverJogador
from gerenciar_objetos import GerenciarObjetos
from gerenciar_cenario import GerenciarCenario
from detectar_colisoes import ChecarColisoes
from gerenciar_som import iniciar_som, parar_som
from atualizar_tela import AtualizarTela

class Jogo:
    def __init__(self):
        pygame.init()
        self.janela = pygame.display.set_mode((LARGURA_JANELA, ALTURA_JANELA))
        pygame.display.set_caption('Aventura Sub-Aquatica')
        self.relogio = pygame.time.Clock()
        self.fonte_pontos = pygame.font.SysFont('bebaskai', 25)
        self.pausado = False
        self.pontos = 0

        self.cenario = GerenciarCenario(self.janela)
        self.gerenciar_objetos = GerenciarObjetos(self.cenario)  # Garantir que esta classe é instanciada corretamente
        self.mover_jogador = MoverJogador(self.gerenciar_objetos)
        self.checar_colisoes = ChecarColisoes(self.gerenciar_objetos)
        self.atualizar_tela = AtualizarTela(self.janela, self.fonte_pontos, self.cenario, self.gerenciar_objetos, self.checar_colisoes)
        
        iniciar_som()

    def rodar(self):
        deve_continuar = True
        while deve_continuar:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    deve_continuar = False
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_p:
                        self.pausado = not self.pausado
                        if self.pausado:
                            pygame.mixer.music.pause()
                        else:
                            pygame.mixer.music.unpause()
                self.mover_jogador.tratar_eventos(evento)

            if not self.pausado:
                self.cenario.mover_cenario()
                self.mover_jogador.mover_jogador()
                self.checar_colisoes.checar_colisoes()
                self.atualizar_tela.atualizar_tela()
                self.pontos = self.checar_colisoes.pontos

            self.relogio.tick(40)

        parar_som()
        pygame.quit()

if __name__ == "__main__":
    jogo = Jogo()
    jogo.rodar()
