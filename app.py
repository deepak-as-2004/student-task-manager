# Simple Task Manager (Demo Project)

tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added!")

def view_tasks():
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def delete_task(index):
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print(f"Removed task: {removed}")
    else:
        print("Invalid task number")

# Demo run
add_task("Complete assignment")
add_task("Study AWS basics")
view_tasks()