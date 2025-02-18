import threading, time

def spawn_thread_for_task(department):
    """Função que será executada em uma thread para processar a tarefa"""
    while department.is_busy:
        time.sleep(1)  # Aguardar por resposta ou timeout
    department.process_task()


class TaskDistributor:
    def __init__(self):
        self.departments = {}

    def add_department(self, department):
        """Adicionar departamento ao sistema"""
        self.departments[department.name] = department

    def distribute_task(self, task):
        """Distribuir tarefa entre os departamentos com base na fila de cada um"""
        available_department = None
        for department in self.departments.values():
            if department.task_queue.empty():
                continue  # Departamento sem tarefas
            if not department.is_busy:
                available_department = department
                break
        
        if available_department:
            # Se o departamento estiver disponível, distribui a tarefa
            available_department.add_task(task)
            available_department.is_busy = True
            print(f"Distribuindo a tarefa {task.task_id} para o departamento {available_department.name}.")
            thread = threading.Thread(target=spawn_thread_for_task, args=(available_department,))
            thread.start()
        else:
            print("Todos os departamentos estão ocupados. Tentando novamente.")
            time.sleep(2)
            self.distribute_task(task)