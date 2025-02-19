from flask import Flask, request, jsonify
from Agency.Task import Task
from Utils.socket_connector import send_task, is_socket_alive
from .tools import connect_to_socket, verify_content, get_task_data

app = Flask(__name__)
cs = connect_to_socket()

@app.route('/new-task', methods=['POST'])
def receive_data():
    global cs
    
    content: dict = request.json

    if not content:
        return jsonify({'error': 'No content received'}), 400
    
    if not verify_content(content):
        return jsonify({'error': 'Invalid content'}), 400

    # Creating your Task object from the content
    task: Task = Task(**get_task_data(content))  # You need to adjust this to match how your Task is constructed

    try:
        if not cs or not is_socket_alive(cs): cs = connect_to_socket()
        send_task(cs, task)
        
    except Exception as e:
        return jsonify({'error': f'Failed to send task: {str(e)}'}), 500
    
    else:
        return jsonify({'status': 'Task sent successfully'}), 200


