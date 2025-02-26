import threading, multiprocessing#, requests
from datetime import datetime, timedelta
from .Task import Task

class Component:
    def __init__(self, name: str, max_executors: int = 15, tolerancy: float = 0.1) -> None:
        manager = multiprocessing.Manager()
        
        self.name: str = name
        self.task_queue = manager.Queue()
        self.executors: list[threading.Thread] = []
        self.max_executors: int = max_executors
        self.tolerancy: float = tolerancy
        
        self.process: multiprocessing.Process = multiprocessing.Process(target=self.main, daemon=True, name=f'P-{self.name}')
        self.process.start()
        
    def __bool__(self) -> bool:
        return self._state() in ['idle', 'busy']
        
    def _state(self) -> str:
        """Verificar se o componente está ocupado"""
        if not self.process.is_alive(): return 'offline'
        elif not self.task_queue.empty(): return 'busy'
        else: return 'idle' 
        
    def add_task(self, task: Task) -> None:
        """Adicionar tarefa à fila do componente"""
        self.task_queue.put(task)
    
    def main(self):
        """Processar tarefa da fila"""
        last_queue_len: int = self.task_queue.qsize()
        empty_timestamp: datetime | None = None

        while True:
            current_queue_len: int = self.task_queue.qsize()
            
            if ((current_queue_len > 0) and
                (current_queue_len > (last_queue_len + (last_queue_len * self.tolerancy))) and
                    (len(self.executors) < self.max_executors)) or (len(self.executors) == 0):
                self._add_executor()
            
            elif current_queue_len == 0:
                if not empty_timestamp:
                    empty_timestamp: datetime = datetime.now()
                elif (datetime.now() - empty_timestamp) > timedelta(minutes=5):
                    break
            
            last_queue_len: int = current_queue_len
            self.remove_unused_executors()
    
    def remove_unused_executors(self) -> None:
        """Remover executores inativos"""
        for executor in self.executors:
            if not executor.is_alive():
                self.executors.remove(executor)
        
    def _add_executor(self) -> None:
        """Adicinar uma thread de executor ao componente"""
        new_executor: Executor = Executor(self.task_queue, self.name, len(self.executors)+1)
        executor_thread: threading.Thread = threading.Thread(target=new_executor.main, daemon=True, name=f'T-{self.name}-{len(self.executors)+1}')
        self.executors.append(executor_thread)
        executor_thread.start()

class Executor:
    def __init__(self, queue_reference, component_reference, exc_reference) -> None:
        self.queue = queue_reference
        self.component = component_reference
        self.exc = exc_reference
                
    def main(self) -> None:
        """The worker that processes tasks from the queue"""
        while not self.queue.empty():
            try:
                task = self.queue.get()
                task.execute()
                print(f"[C-{self.component}-{self.exc}] Task {task.task_id} executed! ({self.queue.qsize()}) tasks remaining...")
            except Exception as e:
                print(f"[C-{self.component}-{self.exc}] Error: {str(e)}")
                continue
            else:
                task.save()