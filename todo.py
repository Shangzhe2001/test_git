# todo.py

def get_tasks():
    return ["Buy milk", "Read book"]

if __name__ == "__main__":
    tasks = get_tasks()
    for task in tasks:
        print(f"- {task}")
