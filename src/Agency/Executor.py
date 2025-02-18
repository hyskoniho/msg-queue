import queue

class Department:
    def __init__(self, name):
        self.name = name
        self.task_queue = queue.Queue()  # Fila de tarefas do departamento
        self.is_busy = False  # Indica se o departamento está ocupado
    
    def add_task(self, task):
        """Adicionar tarefa à fila do departamento"""
        self.task_queue.put(task)
    
    def process_task(self):
        """Processar tarefa da fila"""
        while not self.task_queue.empty():
            task = self.task_queue.get()
            print(f"{self.name} está processando: {task.description}")
            response = task.execute()
            print(f"{self.name} finalizou: {response}")
            self.is_busy = False
            return response  # Tarefa completada
        return None