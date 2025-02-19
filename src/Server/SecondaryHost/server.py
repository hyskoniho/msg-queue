import socket, threading
clients = []

def handle_client(client, addr):    
    while True:
        try:
            data = client.recv(2048)
            if not data: 
                break
            broadcast(data, client)
            
        except:
            break
        
    clients.remove(client)
    client.close()

def broadcast(data, sender):
    for client in clients:
        if client != sender:
            try:
                client.send(data)
            except:
                pass

def start_server(host: str, port: int) -> None:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(2)

    while True:
        client, addr = server.accept()
        clients.append(client)
        thread = threading.Thread(target=handle_client, args=(client, addr))
        thread.start()

