import pygame, time

# definindo as cores
PRETO = (0, 0, 0)
AMARELO = (255, 255, 0)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

# definindo outras constantes do jogo
LARGURAJANELA = 500
ALTURAJANELA = 400

# definindo a função mover()
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

# inicializando módulos de pygame
pygame.init()

# criando a janela
janela = pygame.display.set_mode((LARGURAJANELA, ALTURAJANELA))
pygame.display.set_caption('Animação')

# criando as figuras
f1 = {'objRect': pygame.Rect(300, 80, 40, 80), 'cor': VERMELHO, 'vel': [0,-5], 'forma': 'ELIPSE'}
f2 = {'objRect': pygame.Rect(200, 200, 20, 20), 'cor': VERDE, 'vel': [5,5], 'forma': 'ELIPSE'}
f3 = {'objRect': pygame.Rect(100, 150, 60, 60), 'cor': AZUL, 'vel': [-5,5], 'forma': 'RETANGULO'}
f4 = {'objRect': pygame.Rect(200, 150, 80, 40), 'cor': AMARELO, 'vel': [5,0], 'forma': 'RETANGULO'}

figuras = [f1, f2, f3, f4]

deve_continuar = True

# loop do jogo
while deve_continuar:
    #checando se ocorreu um evento QUIT
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            deve_continuar = False

    # preenchendo o fundo com a cor preta
    janela.fill(PRETO)

    for figura in figuras:
        # reposicionando a figura
        mover(figura,(LARGURAJANELA, ALTURAJANELA))

        # desenhando a figura na janela
        if figura['forma'] == 'RETANGULO':
            pygame.draw.rect(janela, figura['cor'], figura['objRect'])
        elif figura['forma'] == 'ELIPSE':
            pygame.draw.ellipse(janela, figura['cor'], figura['objRect'])
            
    # atualizando na tela tudo o que foi desenhado
    pygame.display.update()
    # esperando 0.02 segundos
    time.sleep(0.02)

# encerrando módulos de Pygame
pygame.quit()