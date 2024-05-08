#gerenciar_som.py

import pygame

def iniciar_som():
    pygame.mixer.music.load('Som/musicadefundo.wav')
    pygame.mixer.music.play(-1)

def parar_som():
    pygame.mixer.music.stop()

def pausar_som():
    pygame.mixer.music.pause()
    
