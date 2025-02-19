from socket import socket
from Utils.socket_connector import start_connection

def verify_content(content: dict) -> bool:
    return all(key in content for key in ['task_id', 'responsible', 'description'])

def connect_to_socket() -> socket:
    return start_connection(host='localhost', port=5000)

def get_task_data(content: dict) -> dict:
    return {key: content[key] for key in ['task_id', 'responsible', 'description']}