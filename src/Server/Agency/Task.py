import time, random, subprocess

class Task:
    def __init__(self, task_id: int, component: str , description: str) -> None:
        self.task_id: int = task_id
        self.component: str = component
        self.description: str = description
        self.state: str = 'pending'
    
    def execute(self) -> None:
        """Método para simular a execução da tarefa."""
        time.sleep(random.randint(1, 3))
        pass
        # subprocess.Popen([self.description])
        
    def save(self) -> None:
        if self.keeper_queue: 
            try:
                self.keeper_queue.put((self.task_id, 'done'))
            except Exception as e:
                print(e)
            else:
                self.state = 'done'

    @property
    def info(self) -> dict:
        return {
            'task_id': self.task_id,
            'component': self.component,
            'description': self.description,
            'task_state': self.state
        }