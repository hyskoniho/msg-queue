import time, random, subprocess

class Task:
    def __init__(self, task_id: int, responsible: str , description: str) -> None:
        self.task_id: int = task_id
        self.responsible: str = responsible
        self.description: str = description
    
    def execute(self) -> None:
        """Método para simular a execução da tarefa."""
        # time.sleep(random.randint(1, 3))
        pass
        # subprocess.Popen([self.description])