from socket import socket
from multiprocessing import freeze_support
from Utils import *
from Agency import *

def main():
    cs: socket = start_connection(
        host = 'localhost', 
        port = 5000
    )
    
    # Criar distribuidor de tarefas
    distributor = TaskDistributor()

    while True:
        print("Waiting for tasks...")
        task: Task = get_task(cs)
        if task:
            distributor.distribute_task(task)

    cs.close()

if __name__ == '__main__':
    freeze_support()
    start()
    main()