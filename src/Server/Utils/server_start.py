import subprocess
import os
import sys

def start_flask_server():
    return subprocess.Popen([sys.executable, '-m', r'src.Server.PrimaryHost.runner'], cwd=os.getcwd())

def start_socket_server():
    return subprocess.Popen([sys.executable, '-m', r'src.Server.SecondaryHost.runner'], cwd=os.getcwd())

def start():
    flash_server = start_flask_server()
    print('Primary server started!')
    
    socket_server = start_socket_server()
    print('Secondary server started!')

if __name__ == '__main__':
    start()