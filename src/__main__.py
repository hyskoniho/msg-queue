import threading, multiprocessing, time
from Agency import *

def main():
    # Criar departamentos
    commercial = Department("Comercial")
    finance = Department("Financeiro")
    hr = Department("Recursos Humanos")

    # Criar distribuidor de tarefas
    distributor = TaskDistributor()
    distributor.add_department(commercial)
    distributor.add_department(finance)
    distributor.add_department(hr)

    # Criar tarefas
    tasks = [Task(i, f"Tarefa {i}") for i in range(1, 6)]

    # Distribuir as tarefas
    for task in tasks:
        distributor.distribute_task(task)

if __name__ == '__main__':
    multiprocessing.freeze_support()
    main()