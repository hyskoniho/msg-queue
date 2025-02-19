from socket import socket
from multiprocessing import freeze_support
from Utils.socket_connector import start_connection, get_task
from Agency import *
from run import *

def main():
    cs: socket = start_connection(
        host = 'localhost', 
        port = 5000
    )
    
    # Criar distribuidor de tarefas
    distributor = TaskDistributor()

    while True:
        task: Task = get_task(cs)
        if task:
            distributor.distribute_task(task)

    cs.close()

if __name__ == '__main__':
    freeze_support()
    main()