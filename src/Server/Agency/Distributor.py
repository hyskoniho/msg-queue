from .Executor import Component
from .Task import Task

class TaskDistributor:
    def __init__(self) -> None:
        self.components: dict = {}

    def distribute_task(self, task: Task) -> None:
        """Distribuir tarefa para o departamento disponível"""
        component_id: str = task.responsible
        
        if not self.components.get(component_id, None):
            self.components[component_id] = Component(component_id)
            
        self.components[component_id].add_task(task)
        