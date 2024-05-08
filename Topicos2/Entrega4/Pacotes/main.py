import pygame
import random
#from exemplo import *
#from Imagens.carregar_imagens import *
# Constantes
LARGURA_JANELA = 500
ALTURA_JANELA = 400
VEL = 6

class Jogo:
    def __init__(self):
        pygame.init()
        self.janela = pygame.display.set_mode((LARGURA_JANELA, ALTURA_JANELA))
        pygame.display.set_caption('Colisão')
        self.relogio = pygame.time.Clock()
        self.fonte_pontos = pygame.font.SysFont('bebaskai', 25)
        self.pausado = False
        self.pontos = 0

        # Carregar recursos
        self.cenarios = [self.carregar_e_escalar(f'Imagens/cenario{i}.png', (LARGURA_JANELA, ALTURA_JANELA)) for i in range(1, 5)]
        self.peixe = pygame.image.load('imagens/peixe.png')
        self.minhoca = pygame.image.load('imagens/minhoca.png')
        self.tridente = pygame.image.load('Objetos/tridente.png')
        self.imagem_invertida = pygame.transform.flip(self.tridente, False, True)

        # Posições iniciais dos cenários
        self.posicoes_cenario = [(i * LARGURA_JANELA, 0) for i in range(len(self.cenarios))]
        
        # Inicializa objetos do jogo
        self.jogador = {'objRect': pygame.Rect(50, 50, self.peixe.get_width(), self.peixe.get_height()), 'imagem': self.peixe, 'vel': VEL}
        self.obj_minhoca = {'objRect': pygame.Rect(250, 200, self.minhoca.get_width(), self.minhoca.get_height()), 'imagem': self.minhoca, 'vel': VEL}
        self.obj_trindente = {'objRect': pygame.Rect(-200, 100, self.tridente.get_width(), self.tridente.get_height()), 'imagem': self.tridente, 'vel': VEL}
        self.obj_trindente1 = {'objRect': pygame.Rect(-60, 100, self.tridente.get_width(), self.tridente.get_height()), 'imagem': self.tridente, 'vel': VEL}
        self.obj_trindente2 = {'objRect': pygame.Rect(90, 100, self.tridente.get_width(), self.tridente.get_height()), 'imagem': self.tridente, 'vel': VEL}
        self.obj_trindente3 = {'objRect': pygame.Rect(180, 100, self.tridente.get_width(), self.tridente.get_height()), 'imagem': self.tridente, 'vel': VEL}
        self.obj_trindente4 = {'objRect': pygame.Rect(200, -235, self.imagem_invertida.get_width(), self.imagem_invertida.get_height()), 'imagem': self.imagem_invertida, 'vel': VEL}
        self.obj_trindente5 = {'objRect': pygame.Rect(20, -235, self.imagem_invertida.get_width(), self.imagem_invertida.get_height()), 'imagem': self.imagem_invertida, 'vel': VEL}
        self.obj_trindente6 = {'objRect': pygame.Rect(-110, -235, self.imagem_invertida.get_width(), self.imagem_invertida.get_height()), 'imagem': self.imagem_invertida, 'vel': VEL}

        self.teclas = {'esquerda': False, 'direita': False, 'cima': False, 'baixo': False}
        
        # Inicializa som
        pygame.mixer.music.load('Som/som_ambiente.wav')
        pygame.mixer.music.play(-1)
    
    def carregar_e_escalar(self, caminho, dimensoes):
        imagem = pygame.image.load(caminho)
        return pygame.transform.scale(imagem, dimensoes)
    
    def mover_jogador(self):
        if self.teclas['esquerda'] and self.jogador['objRect'].left > 5:
            self.jogador['objRect'].x -= self.jogador['vel']
        if self.teclas['direita'] and self.jogador['objRect'].right < LARGURA_JANELA - 4:
            self.jogador['objRect'].x += self.jogador['vel']
        if self.teclas['cima'] and self.jogador['objRect'].top > 5:
            self.jogador['objRect'].y -= self.jogador['vel']
        if self.teclas['baixo'] and self.jogador['objRect'].bottom < ALTURA_JANELA:
            self.jogador['objRect'].y += self.jogador['vel']

    def mover_cenario(self):
        for i, (x, y) in enumerate(self.posicoes_cenario):
            if x + LARGURA_JANELA < 0:
                x = self.posicoes_cenario[(i - 1) % len(self.posicoes_cenario)][0] + LARGURA_JANELA
            self.posicoes_cenario[i] = (x - 1, y)

    def checar_colisoes(self):
        bateu = self.jogador['objRect'].colliderect(self.obj_minhoca['objRect'])
        if bateu:
            self.pontos += 1
            self.obj_minhoca['objRect'].x = random.randint(0, LARGURA_JANELA - self.obj_minhoca['objRect'].width)
            self.obj_minhoca['objRect'].y = random.randint(0, ALTURA_JANELA - self.obj_minhoca['objRect'].height)
    
    def atualizar_tela(self):
        for posicao, cenario in zip(self.posicoes_cenario, self.cenarios):
            self.janela.blit(cenario, posicao)
        self.janela.blit(self.jogador['imagem'], self.jogador['objRect'])
        self.janela.blit(self.obj_minhoca['imagem'], self.obj_minhoca['objRect'])
        self.janela.blit(self.obj_trindente['imagem'], self.obj_trindente['objRect'])
        self.janela.blit(self.obj_trindente1['imagem'], self.obj_trindente1['objRect'])
        self.janela.blit(self.obj_trindente2['imagem'], self.obj_trindente2['objRect'])
        self.janela.blit(self.obj_trindente3['imagem'], self.obj_trindente3['objRect'])
        self.janela.blit(self.obj_trindente4['imagem'], self.obj_trindente4['objRect'])
        self.janela.blit(self.obj_trindente5['imagem'], self.obj_trindente5['objRect'])
        self.janela.blit(self.obj_trindente6['imagem'], self.obj_trindente6['objRect'])
        texto_pontuacao = self.fonte_pontos.render(f"PONTUAÇÃO: {self.pontos}", True, (255, 255, 255))
        self.janela.blit(texto_pontuacao, (LARGURA_JANELA - 10 - texto_pontuacao.get_width(), 10))
        pygame.display.update()

    def rodar(self):
        deve_continuar = True
        while deve_continuar:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    deve_continuar = False
                # Tratar teclas pressionadas
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        deve_continuar = False
                    if evento.key in (pygame.K_LEFT, pygame.K_a):
                        self.teclas['esquerda'] = True
                    if evento.key in (pygame.K_RIGHT, pygame.K_d):
                        self.teclas['direita'] = True
                    if evento.key in (pygame.K_UP, pygame.K_w):
                        self.teclas['cima'] = True
                    if evento.key in (pygame.K_DOWN, pygame.K_s):
                        self.teclas['baixo'] = True
                    if evento.key == pygame.K_p:
                        self.pausado = not self.pausado
                        pygame.mixer.music.pause() if self.pausado else pygame.mixer.music.unpause()
                # Tratar teclas soltas
                if evento.type == pygame.KEYUP:
                    if evento.key in (pygame.K_LEFT, pygame.K_a):
                        self.teclas['esquerda'] = False
                    if evento.key in (pygame.K_RIGHT, pygame.K_d):
                        self.teclas['direita'] = False
                    if evento.key in (pygame.K_UP, pygame.K_w):
                        self.teclas['cima'] = False
                    if evento.key in (pygame.K_DOWN, pygame.K_s):
                        self.teclas['baixo'] = False
            
            if not self.pausado:
                self.mover_cenario()
                self.mover_jogador()
                self.checar_colisoes()
                self.atualizar_tela()
            
            self.relogio.tick(40)
        
        pygame.mixer.music.stop()
        pygame.quit()

# Cria uma instância do jogo e inicia
if __name__ == "__main__":
    jogo = Jogo()
    jogo.rodar()

