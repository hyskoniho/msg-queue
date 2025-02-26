from socket import socket
from multiprocessing import freeze_support, set_start_method
import platform
from Utils import *
from Agency import *
from Keeper import *

if 'windows' not in platform.platform().lower():
    set_start_method('fork', force=True)

def main():
    cs: socket = start_connection(
        host = 'localhost', 
        port = 5000
    )
    
    # Criar distribuidor de tarefas e monitorar as mudanas no arquivo
    keeper = Keeper()
    distributor = TaskDistributor()

    while True:
        print("Waiting for tasks...")
        task: Task = get_task(cs)
        if task:
            task.keeper_queue = keeper.change_queue
            keeper.register_queue.put(task.info)
            distributor.distribute_task(task)

    cs.close()

if __name__ == '__main__':
    freeze_support()
    start()
    main()