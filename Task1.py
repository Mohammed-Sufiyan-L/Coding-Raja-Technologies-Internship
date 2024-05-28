import json
from datetime import datetime, timedelta

class Task:
    def __init__(self, name, priority='medium', due_date=None, completed=False):
        self.name = name
        self.priority = priority
        self.due_date = due_date
        self.completed = completed

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"{self.name} (Priority: {self.priority}, Due: {self.due_date}, Status: {status})"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task_name):
        self.tasks = [task for task in self.tasks if task.name != task_name]

    def mark_task_completed(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True

    def list_tasks(self):
        for task in self.tasks:
            print(task)

    def save_tasks(self, filename):
        with open(filename, 'w') as f:
            json.dump([vars(task) for task in self.tasks], f)

    def load_tasks(self, filename):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.tasks = [Task(**task) for task in data]
        except FileNotFoundError:
            pass

def main():
    task_manager = TaskManager()
    task_manager.load_tasks("tasks.json")

    while True:
        print("\n1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. List Tasks")
        print("5. Save and Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter task name: ")
            priority = input("Enter priority (high/medium/low): ")
            due_date_str = input("Enter due date (YYYY-MM-DD) or leave empty: ")
            due_date = datetime.strptime(due_date_str, "%Y-%m-%d") if due_date_str else None
            task = Task(name, priority, due_date)
            task_manager.add_task(task)
        elif choice == '2':
            name = input("Enter task name to remove: ")
            task_manager.remove_task(name)
        elif choice == '3':
            name = input("Enter task name to mark as completed: ")
            task_manager.mark_task_completed(name)
        elif choice == '4':
            task_manager.list_tasks()
        elif choice == '5':
            task_manager.save_tasks("tasks.json")
            print("Tasks saved. Quitting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
