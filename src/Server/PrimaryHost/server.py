from flask import Flask, request, jsonify
from .tools import verify_content, get_task_data

try:
    from Agency.Task import Task
    from Utils.socket_client import start_connection, send_task, is_socket_alive
    
except ModuleNotFoundError:
    import sys, os
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

    from Agency.Task import Task
    from Utils.socket_client import start_connection, send_task, is_socket_alive

app = Flask(__name__)
cs = start_connection()

@app.route('/new-task', methods=['POST'])
def receive_data():
    global cs
    
    content: dict = request.json

    if not content:
        return jsonify({'error': 'No content received'}), 400
    
    if not verify_content(content):
        return jsonify({'error': 'Invalid content'}), 400

    task: Task = Task(**get_task_data(content))  

    try:
        if not cs or not is_socket_alive(cs): cs = start_connection()
        send_task(cs, task)
        
    except Exception as e:
        return jsonify({'error': f'Failed to send task: {str(e)}'}), 500
    
    else:
        return jsonify({'status': 'Task sent successfully'}), 200


