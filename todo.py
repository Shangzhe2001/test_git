# todo.py

tasks = ["Buy milk", "Read book"]

def get_tasks():
    return tasks

def add_task(task):
    tasks.append(task)

if __name__ == "__main__":
    add_task("Write code")  # 新添加的任务
    for task in get_tasks():
        print(f"- {task}")

