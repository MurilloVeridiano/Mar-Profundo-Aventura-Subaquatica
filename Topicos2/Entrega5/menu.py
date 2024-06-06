import tkinter as tk
from tkinter import messagebox, Toplevel, Scale, PhotoImage
import pygame
import os
from jogo import Jogo
from SQL import *

class Menu:
    def __init__(self, root):
        self.root = root
        self.root.title("Mar Profundo")
        self.root.geometry("550x350")
        
        # Inicializar Pygame Mixer
        pygame.mixer.init()

        # Frame principal
        self.main_menu = tk.Frame(root)
        self.main_menu.pack(fill="both", expand=True)
        
        # Imagem de fundo
        self.background_image = PhotoImage(file="Imagens/fundo.png")
        self.background_label = tk.Label(self.main_menu, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)

        # Título com estilo marinho
        self.title_label = tk.Label(self.main_menu, text="Mar Profundo: Aventura Subaquática", font=("Times New Roman", 22, "bold"), bg="#009afe", fg="navy")
        self.title_label.pack(pady=20)
        
        # Botão de iniciar o jogo com estilo marinho
        self.start_button = tk.Button(self.main_menu, text="Iniciar Jogo", font=("Times New Roman", 15), command=self.show_login, bg="navy", fg="white")
        self.start_button.pack(pady=10)
        
        # Botão de cadastro com estilo marinho
        self.register_button = tk.Button(self.main_menu, text="Cadastrar", font=("Times New Roman", 15), command=self.show_register, bg="navy", fg="white")
        self.register_button.pack(pady=10)
        
        # Botão de configurações com estilo marinho
        self.settings_button = tk.Button(self.main_menu, text="Configurações", font=("Times New Roman", 15), command=self.open_settings, bg="navy", fg="white")
        self.settings_button.pack(pady=10)
        
        # Botão de saída com estilo marinho
        self.exit_button = tk.Button(self.main_menu, text="Sair", font=("Times New Roman", 15), command=self.exit_game, bg="navy", fg="white")
        self.exit_button.pack(pady=10)

    def show_login(self):
        self.login_window = Toplevel(self.root)
        self.login_window.title("Login")
        self.login_window.geometry("300x200")
        
        tk.Label(self.login_window, text="Nome:").pack(pady=5)
        self.login_name = tk.Entry(self.login_window)
        self.login_name.pack(pady=5)
        
        tk.Label(self.login_window, text="Senha:").pack(pady=5)
        self.login_password = tk.Entry(self.login_window, show="*")
        self.login_password.pack(pady=5)
        
        self.login_button = tk.Button(self.login_window, text="Login", command=self.login_user)
        self.login_button.pack(pady=20)
        
    def login_user(self):
        name = self.login_name.get()
        password = self.login_password.get()
        
        if check_login(name, password):
            self.login_window.destroy()  # Fechar a janela de login
            self.root.destroy()  # Fechar o menu principal antes de iniciar o jogo
            pygame.mixer.quit()
            jogo = Jogo(name)  # Pass the player's name
            jogo.rodar()
        else:
            messagebox.showerror("Erro de Login")

    def show_register(self):
        self.register_window = Toplevel(self.root)
        self.register_window.title("Registrar")
        self.register_window.geometry("300x200")
        
        tk.Label(self.register_window, text="Nome:").pack(pady=5)
        self.register_name = tk.Entry(self.register_window)
        self.register_name.pack(pady=5)
        
        tk.Label(self.register_window, text="Senha:").pack(pady=5)
        self.register_password = tk.Entry(self.register_window, show="*")
        self.register_password.pack(pady=5)
        
        self.register_button = tk.Button(self.register_window, text="Registrar", command=self.register_user)
        self.register_button.pack(pady=20)
        
    def register_user(self):
        name = self.register_name.get()
        password = self.register_password.get()
        
        register_user(name, password)
        messagebox.showinfo("Registro", "Usuário registrado com sucesso!")
        self.register_window.destroy()
    
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
        pygame.mixer.music.set_volume(volume_level)

    def exit_game(self):
        if messagebox.askyesno("Sair", "Você realmente deseja sair?"):
            pygame.mixer.quit()
            self.root.quit()
