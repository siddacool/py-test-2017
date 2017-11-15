# Multi-Threaded program

import threading

class MyMessenger(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.currentThread().getName())

x = MyMessenger(name='send msg')
y = MyMessenger(name='get msg')

x.start()
y.start()