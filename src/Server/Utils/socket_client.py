import socket, pickle
from Agency.Task import Task

def start_connection(host: str = 'localhost', port: int = 5000) -> socket.socket:
    """Iniciar conexão com o servidor principal"""
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    return client_socket

def get_task(sock: socket.socket) -> Task:
    """Receber tarefas do servidor principal"""
    try:
        data = sock.recv(2048)
        if data:
            return pickle.loads(data)
    except Exception as e:
        print(f"Erro ao receber dados: {e}")
    return None

def send_task(sock: socket.socket, task: Task) -> None:
    """Enviar tarefas para o servidor secundário"""
    sock.send(pickle.dumps(task))

def is_socket_alive(sock: socket.socket) -> bool:
    """Verificar se o socket está ativo"""
    try:
        sock.send(b'')
        return True
    except (socket.error, BrokenPipeError):
        return False
