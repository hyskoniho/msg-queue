import socket
import threading
import time

def start_server(host: str = 'localhost', port: int = 5000) -> None:
    while True:
        try:
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.bind((host, port))
            server_socket.listen()

            print(f"Socket server started on {host}:{port}")

            while True:
                conn, addr = server_socket.accept()
                threading.Thread(target=handle_client, args=(conn, addr)).start()

        except Exception as e:
            print(f"Socket server error: {e}. Restarting...")
            time.sleep(2) 

def handle_client(conn, addr):
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break

server_thread = threading.Thread(target=start_server, daemon=True)
server_thread.start()