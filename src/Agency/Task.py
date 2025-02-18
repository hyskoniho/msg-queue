import time, random

class Task:
    def __init__(self, task_id, description):
        self.task_id = task_id
        self.description = description
    
    def execute(self):
        """Método para simular a execução da tarefa."""
        # Simula o tempo de execução da tarefa
        time.sleep(random.uniform(0.5, 2))
        return f"Tarefa {self.task_id} executada: {self.description}"