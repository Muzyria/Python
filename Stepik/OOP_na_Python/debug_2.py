class Task:
    def __init__(self, name, description, status=False):
        self.name = name
        self.description = description
        self.status = status

    def display(self):
        status_str = "Сделана" if self.status else "Не сделана"
        print(f"{self.name} ({status_str})")


class TaskList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)


class TaskManager:
    def __init__(self, task_list):
        self.task_list = task_list

    def mark_done(self, task):
        task.status = True

    def mark_undone(self, task):
        task.status = False

    def show_tasks(self):
        for task in self.task_list.tasks:
            task.display()
