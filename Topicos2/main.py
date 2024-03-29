import pygame

# definindo as cores
PRETO = (0, 0, 0)
AMARELO = (255, 255, 0)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
BRANCO = (255, 255, 255)

# definindo outras constantes do jogo
LARGURAJANELA = 500
ALTURAJANELA = 400

# definindo a função mover(), que registra a posição de uma figura
def mover(figura, dim_janela):
    borda_esquerda = 0
    borda_superior = 0
    borda_direita = dim_janela[0]
    borda_inferior = dim_janela[1]
    if figura['objRect'].top < borda_superior or figura['objRect'].bottom > borda_inferior:
        # figura atingiu o topo ou a base da janela
        figura['vel'][1] = -figura['vel'][1]
    if figura['objRect'].left < borda_esquerda or figura['objRect'].right > borda_direita:
        # figura atingiu o lado esquerdo ou direito da janela
        figura['vel'][0] = -figura['vel'][0]
    figura['objRect'].x += figura['vel'][0]
    figura['objRect'].y += figura['vel'][1]

# inicializando pygame
pygame.init()

# criando um objeto pygame.time.Clock
relogio = pygame.time.Clock()

# criando a janela
janela = pygame.display.set_mode((LARGURAJANELA, ALTURAJANELA))
pygame.display.set_caption('Colisão')

# criando os blocos e colocando-os em uma lista
b1 = {'objRect': pygame.Rect(375, 80, 40, 40), 'cor': VERMELHO, 'vel': [0,2]}
b2 = {'objRect': pygame.Rect(175, 200, 40, 40), 'cor': VERDE, 'vel': [0,-3]}
b3 = {'objRect': pygame.Rect(275, 150, 40, 40), 'cor': AMARELO, 'vel': [0,-1]}
b4 = {'objRect': pygame.Rect(75, 150, 40, 40), 'cor': AZUL, 'vel': [0,4]}
blocos = [b1, b2, b3, b4]

# criando a bola
bola = {'objRect': pygame.Rect(270, 330, 30, 30), 'cor': BRANCO, 'vel': [3,3]}

deve_continuar = True

# loop do jogo
while deve_continuar:
    # checando se ocorreu um evento QUIT
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            deve_continuar = False

    # preenchendo o fundo com a cor preta
    janela.fill(PRETO)

    for bloco in blocos:
        # reposicionando o bloco
        mover(bloco, (LARGURAJANELA,ALTURAJANELA))

        # desenhando o bloco na janela
        pygame.draw.rect(janela, bloco['cor'], bloco['objRect'])

        # mudando a cor da bola caso colida com algum bloco
        mudarCor = bola['objRect'].colliderect(bloco['objRect'])
        if mudarCor:
            bola['cor'] = bloco['cor']

    # reposicionando e desenha a bola
    mover(bola, (LARGURAJANELA, ALTURAJANELA))
    pygame.draw.ellipse(janela, bola['cor'], bola['objRect'])

    # mostrando na tela tudo o que foi desenhado
    pygame.display.update()

    # limitando a 40 quadros por segundo
    relogio.tick(40)

# encerrando módulos de Pygame
pygame.quit()
