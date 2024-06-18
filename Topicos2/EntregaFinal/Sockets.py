import socket
import pickle
import threading
#from Settings import settings

class Obj:
    def __init__(self, name):
        self.name = name
    def get(self):
        return self.name

class SocketServer:
    def __init__(self, host, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port
        self.connections = []

    def handle_client(self, conn, addr):
        try:
            print(f'received connection from {addr}') 
            while True:
                data = conn.recv(4096)
                if not data:
                    break
                obj = pickle.loads(data)
                print(obj.get())
                last_message = obj.get()
                last_obj = obj
        except Exception as e:
            print(f"Error handling connection from {addr}: {e}")
        finally:
            conn.close()

    def receive(self):
        self.socket.bind((self.host, self.port))
        self.socket.listen(1)
        print('Server up!')

        try:
            while True:
                conn, addr = self.socket.accept()
                thread = threading.Thread(target=self.handle_client, args=(conn, addr))
                thread.start()
                self.connections.append(thread)
        except KeyboardInterrupt:
            print("Server shutting down.")
        finally:
            self.socket.close()

if __name__ == '__main__':
    server = SocketServer('0.0.0.0', 4040)
    server_thread = threading.Thread(target=server.receive)
    server_thread.start()
