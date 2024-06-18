import threading, time
          
class Threads:
    def __init__(self):
        pass
            
    def counter(self, nome):
        print(f'Nome: {nome}')
  
    def run(self):        
        th1 = threading.Thread(target=self.counter, args=('Joao',))
        th2 = threading.Thread(target=self.counter, args=('Maria',))
        
        print(threading.active_count())
        
        th1.start()
        th2.start()

        print(threading.active_count())

        th1.join()
        th2.join()

if __name__ == '__main__':
    t = Threads()
    t.run()