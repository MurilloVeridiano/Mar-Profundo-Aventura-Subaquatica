# Salve isto como client_test.py
import socket
import pickle
from jogo import Obj

def test_client():
    host, port = '192.168.56.1', 4040
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    obj = Obj("Hello Server!")
    data = pickle.dumps(obj)
    client_socket.send(data)
    client_socket.close()

if __name__ == "__main__":
    test_client()