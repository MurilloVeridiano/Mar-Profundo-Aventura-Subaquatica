import pygame
import tkinter as tk
from tkinter import messagebox, Toplevel, Scale, PhotoImage
from jogo import *

def mostrar_configuracao_volume(janela, fonte):
    janela.fill((0, 0, 0))  # Ou desenhe o cenário aqui se quiser
    texto_volume = fonte.render("Configuração de Volume", True, (255, 255, 255))
    janela.blit(texto_volume, (janela.get_width() // 2 - texto_volume.get_width() // 2, janela.get_height() // 2 - texto_volume.get_height() // 2))
    pygame.display.update()
    
    esperando_volume = True
    while esperando_volume:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    esperando_volume = False
                elif evento.key == pygame.K_v:
                    # Código para ajustar o volume aqui
                    pass

def mostrar_menu(janela, fonte):
    janela.fill((0, 0, 0))  # Ou desenhe o cenário aqui se quiser
    texto_menu = fonte.render("Menu", True, (255, 255, 255))
    janela.blit(texto_menu, (janela.get_width() // 2 - texto_menu.get_width() // 2, janela.get_height() // 2 - texto_menu.get_height() // 2))
    pygame.display.update()
    
    esperando_selecao = True
    while esperando_selecao:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    esperando_selecao = False
                elif evento.key == pygame.K_r:  # Retornar
                    return "retornar"
                elif evento.key == pygame.K_v:  # Ajustar Volume
                    return "ajustar_volume"
                elif evento.key == pygame.K_s:  # Sair
                    pygame.quit()
                    exit()

def mostrar_menu_opcoes(root, ajustar_volume_callback):
    menu_window = Toplevel(root)
    menu_window.title("Menu")
    menu_window.geometry("300x200")

    tk.Label(menu_window, text="Menu de Opções").pack(pady=10)

    retornar_button = tk.Button(menu_window, text="Retornar", command=lambda: menu_window.destroy())
    retornar_button.pack(pady=5)

    ajustar_volume_button = tk.Button(menu_window, text="Ajustar Volume", command=lambda: [menu_window.destroy(), ajustar_volume_callback()])
    ajustar_volume_button.pack(pady=5)

    sair_button = tk.Button(menu_window, text="Sair", command=lambda: [menu_window.destroy(), root.quit()])
    sair_button.pack(pady=5)
