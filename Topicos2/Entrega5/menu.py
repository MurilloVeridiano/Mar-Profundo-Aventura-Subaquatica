#menu.py
import tkinter as tk
from tkinter import messagebox, Toplevel, Scale, PhotoImage
import pygame
import subprocess
import os
from Jogo import *

class Menu:
    def __init__(self, root):
        self.root = root
        self.root.title("Mar Profundo")
        self.root.geometry("400x500")
        
        # Inicializar Pygame Mixer
        pygame.mixer.init()
        # Carregar e tocar música de fundo
        #self.music = pygame.mixer.Sound("Som/musicadefundo.wav")
        #self.music.play(-1)  

        # Frame principal
        self.main_menu = tk.Frame(root)
        self.main_menu.pack(fill="both", expand=True)
        
        # Imagem de fundo
        self.background_image = PhotoImage(file="Imagens/cenario1.png")
        self.background_label = tk.Label(self.main_menu, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)

        # Título com estilo marinho
        self.title_label = tk.Label(self.main_menu, text="Mar Profundo", font=("Comic Sans MS", 24, "bold"), bg="light blue", fg="navy")
        self.title_label.pack(pady=20)
        
        # Botão de iniciar o jogo com estilo marinho
        self.start_button = tk.Button(self.main_menu, text="Iniciar Jogo", font=("Comic Sans MS", 18), command=self.start_game, bg="light blue", fg="white")
        self.start_button.pack(pady=10)
        
        # Botão de configurações com estilo marinho
        self.settings_button = tk.Button(self.main_menu, text="Configurações", font=("Comic Sans MS", 18), command=self.open_settings, bg="light blue", fg="white")
        self.settings_button.pack(pady=10)
        
        # Botão de saída com estilo marinho
        self.exit_button = tk.Button(self.main_menu, text="Sair", font=("Comic Sans MS", 18), command=self.exit_game, bg="light blue", fg="white")
        self.exit_button.pack(pady=10)

    def start_game(self):
        self.root.destroy()  # Fechar o menu antes de iniciar o jogo
        main_script_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'main.py'))
        #subprocess.run(["python", main_script_path])  # Executar o arquivo main.py para iniciar o jogo
        jogo = Jogo()
        jogo.rodar()
    
    def open_settings(self):
        self.settings_window = Toplevel(self.root)
        self.settings_window.title("Configurações de Volume")
        self.settings_window.geometry("300x100")
        
        # Escala de volume
        self.volume_scale = Scale(self.settings_window, from_=0, to=100, orient="horizontal", label="Volume", command=self.adjust_volume, bg="light blue")
        self.volume_scale.pack(pady=20, padx=20)
        self.volume_scale.set(pygame.mixer.music.get_volume() * 100)  # Inicializa a escala com o volume atual

    def adjust_volume(self, value):
        volume_level = float(value) / 100.0  # Converter para 0 a 1
        self.music.set_volume(volume_level)

    def exit_game(self):
        if messagebox.askyesno("Sair", "Você realmente deseja sair?"):
            pygame.mixer.quit()
            self.root.quit()

#if __name__ == "__main__":
#    root = tk.Tk()  # Inicializa a janela principal
#    app = Menu(root)
#    root.mainloop()
