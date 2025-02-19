def verify_content(content: dict) -> bool:
    return all(key in content for key in ['task_id', 'responsible', 'description'])

def get_task_data(content: dict) -> dict:
    return {key: content[key] for key in ['task_id', 'responsible', 'description']}