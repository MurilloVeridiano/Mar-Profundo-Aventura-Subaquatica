import pygame
from menu import *
from jogo import SocketServer
import threading

def start_server():
    server = SocketServer('0.0.0.0', 4040)
    server.receive()  # Escuta e aceita conexões

if __name__ == "__main__":
    # Iniciar o servidor em uma thread separada
    server_thread = threading.Thread(target=start_server)
    server_thread.daemon = True  # Isso garante que a thread fechará quando a janela principal fechar
    server_thread.start()

    root = tk.Tk()  # Inicializa a janela principal
    app = Menu(root)
    root.mainloop()