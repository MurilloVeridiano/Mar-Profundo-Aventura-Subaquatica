import pygame
from configuracoes import LARGURA_JANELA, ALTURA_JANELA
from mover_jogador import MoverJogador
from gerenciar_objetos import GerenciarObjetos
from gerenciar_cenario import GerenciarCenario
from detectar_colisoes import ChecarColisoes
from gerenciar_som import iniciar_som, parar_som
from atualizar_tela import AtualizarTela
import tkinter as tk
from tkinter import messagebox, Toplevel, Scale, PhotoImage
from utils import mostrar_configuracao_volume
from SQL import get_hi_score, update_hi_score
from configuracoes import mostrar_instrucoes
from Sockets import *


class Jogo:
    def __init__(self, nome_jogador):
        pygame.init()
        self.janela = pygame.display.set_mode((LARGURA_JANELA, ALTURA_JANELA))
        pygame.display.set_caption('Aventura Sub-Aquatica')
        self.relogio = pygame.time.Clock()
        self.fonte_pontos = pygame.font.SysFont('bebaskai', 25)
        self.fonte_instrucoes = pygame.font.SysFont('bebaskai', 30)
        self.fonte_menu = pygame.font.SysFont('bebaskai', 40)
        self.fonte_morte = pygame.font.SysFont('bebaskai', 50)
        self.pausado = False
        self.pontos = 0
        self.nome_jogador = nome_jogador
        self.cenario = GerenciarCenario(self.janela)
        self.gerenciar_objetos = GerenciarObjetos(self.cenario)
        self.mover_jogador = MoverJogador(self.gerenciar_objetos)
        self.checar_colisoes = ChecarColisoes(self.gerenciar_objetos, self.cenario)
        self.atualizar_tela = AtualizarTela(self.janela, self.fonte_pontos, self.cenario, self.gerenciar_objetos, self.checar_colisoes, nome_jogador)
        
        iniciar_som()

        
    def mostrar_instrucoes(self):
        mostrar_instrucoes(self.janela, self.fonte_instrucoes, self.cenario, self.gerenciar_objetos)
        esperando_comeco = True
        while esperando_comeco:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()
                    elif evento.key == pygame.K_SPACE:
                        esperando_comeco = False

    def mostrar_menu_pausa(self):
        self.pausado = True
        pygame.mixer.music.pause()
        root = tk.Tk()
        root.withdraw()  # Oculta a janela principal do Tkinter
        self.menu_pausa(root)
        root.mainloop()

    def menu_pausa(self, root):
        menu_window = Toplevel(root)
        menu_window.title("Menu de Pausa")
        menu_window.geometry("300x200")

        tk.Label(menu_window, text="Menu de Pausa").pack(pady=10)

        retornar_button = tk.Button(menu_window, text="Retornar", command=lambda: self.retomar_jogo(menu_window, root))
        retornar_button.pack(pady=5)

        ajustar_volume_button = tk.Button(menu_window, text="Ajustar Volume", command=lambda: self.mostrar_configuracao_volume(menu_window, root))
        ajustar_volume_button.pack(pady=5)

        sair_button = tk.Button(menu_window, text="Sair", command=lambda: self.sair_jogo(menu_window, root))
        sair_button.pack(pady=5)

    def retomar_jogo(self, menu_window, root):
        if menu_window:
            menu_window.destroy()
        root.destroy()
        self.pausado = False
        pygame.mixer.music.unpause()

    def mostrar_configuracao_volume(self, menu_window, root):
        settings_window = Toplevel(root)
        settings_window.title("Configurações de Volume")
        settings_window.geometry("300x100")

        volume_scale = Scale(settings_window, from_=0, to=100, orient="horizontal", label="Volume", command=self.adjust_volume, bg="light blue")
        volume_scale.pack(pady=20, padx=20)
        volume_scale.set(pygame.mixer.music.get_volume() * 100)  # Inicializa a escala com o volume atual

        close_button = tk.Button(settings_window, text="Fechar", command=lambda: [settings_window.destroy(), self.retomar_jogo(menu_window, root)])
        close_button.pack(pady=10)

    def adjust_volume(self, value):
        volume_level = float(value) / 100.0  # Converter para 0 a 1
        pygame.mixer.music.set_volume(volume_level)

    def sair_jogo(self, menu_window, root):
        self.salvar_pontuacao()
        if menu_window:
            menu_window.destroy()
        root.quit()
        parar_som()
        pygame.quit()
        exit()

    def mostrar_tela_morte(self):
        self.janela.fill((0, 0, 0))
        texto_morte = self.fonte_morte.render("Você Morreu", True, (255, 0, 0))
        texto_sair = self.fonte_instrucoes.render("ESC para Sair", True, (255, 0, 0))
        texto_recomecar = self.fonte_instrucoes.render("Espaço para Recomeçar", True, (255, 0, 0))
        self.janela.blit(texto_morte, (LARGURA_JANELA // 2 - texto_morte.get_width() // 2, ALTURA_JANELA // 3 - texto_morte.get_height() // 2))
        self.janela.blit(texto_sair, (LARGURA_JANELA // 2 - texto_sair.get_width() // 2, 2 * ALTURA_JANELA // 3 - texto_sair.get_height() // 2))
        self.janela.blit(texto_recomecar, (LARGURA_JANELA // 2 - texto_recomecar.get_width() // 2, 2 * ALTURA_JANELA // 3 + texto_recomecar.get_height() // 2))
        pygame.display.update()
        esperando_resposta = True
        while esperando_resposta:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()
                    elif evento.key == pygame.K_SPACE:
                        self.recomecar_jogo()

    def recomecar_jogo(self):
        self.__init__(self.nome_jogador)
        self.rodar()

    def rodar(self):
        self.mostrar_instrucoes()  # Mostra a tela de instruções antes de iniciar o jogo
        deve_continuar = True
        while deve_continuar:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.salvar_pontuacao()
                    deve_continuar = False
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_p:
                        self.mostrar_menu_pausa()
                self.mover_jogador.tratar_eventos(evento)

            if not self.pausado:
                self.cenario.mover_cenario()
                self.mover_jogador.mover_jogador()
                self.gerenciar_objetos.atualizar()
                self.checar_colisoes.checar_colisoes()
                self.atualizar_tela.atualizar_tela()
                self.gerenciar_objetos.desenhar_obstaculos(self.janela)

                if self.mover_jogador.jogador['morto']:
                    self.salvar_pontuacao()
                    self.mostrar_tela_morte()
                    deve_continuar = False

            self.relogio.tick(40)

        parar_som()
        pygame.quit()

    def salvar_pontuacao(self):
        self.pontos = self.checar_colisoes.get_pontos()
        hi_score = get_hi_score(self.nome_jogador)
        if self.pontos > hi_score:
            update_hi_score(self.nome_jogador, self.pontos)
        print(f'Salvando pontuação: {self.pontos}')
        
class SocketServer:
            def __init__(self, host, port):
        # Inicialização anterior
             self.game_manager = GerenciarCenario()

             def handle_client(self, conn, addr):
        # Código existente para receber dados
                obj = pickle.loads(self)
                self.game_manager.update_game(obj)  # Atualiza o jogo
