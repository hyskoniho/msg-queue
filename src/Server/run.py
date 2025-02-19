from Host import *

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
else:
    import threading
    server_thread = threading.Thread(target=app.run, args=('0.0.0.0', 8080,), daemon=True)
    server_thread.start()