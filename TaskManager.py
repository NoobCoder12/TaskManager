import os


class Task:
    def __init__(self, task, is_completed=False):
        self.task = task
        self.is_completed = is_completed

    def mark_completed(self):
        self.is_completed = True

    def __str__(self):
        status = '✅ Completed' if self.is_completed else '❌ Unfinished'
        return f'{self.task} is {status}'


class TaskManager:
    def __init__(self):
        self.task_list = []

    def add_task(self, task_name):
        task = Task(task_name)
        self.task_list.append(task)
        print('Task was added to list.')

    def complete_task(self, task_name):
        for task in self.task_list:
            if task.task == task_name:
                task.mark_completed()
                print('Task status was changed.')
                break

        else:
            print('This task was not found on the list.')

    def show_list(self):
        for task in self.task_list:
            print(task)

    def remove_from_list(self, task):
        if task in self.task_list:
            self.task_list.remove(task)
            print(f'Task {task} removed from list.')
        else:
            print('Task is not on the list.')

    def list_of_completed_tasks(self):
        for task in self.task_list:
            if task.is_completed == True:
                print(task)

    def list_of_unfinished_tasks(self):
        for task in self.task_list:
            if task.is_completed == False:
                print(task)

    def save_list(self):
        try:
            file_path = os.path.dirname(__file__)
            path = os.path.join(file_path, 'task_list.txt')

            with open(path, 'w', encoding='UTF-8') as file:
                for task in self.task_list:
                    file.write(f"{task.task}|{task.is_completed}\n")
            print("List was saved")
        except Exception as e:
            print(f'File was not saved: {e}')

    def load_list(self):
        try:
            file_path = os.path.dirname(__file__)
            path = os.path.join(file_path, 'task_list.txt')
            # file name or directory can be changed

            with open(path, 'r', encoding='UTF-8') as file:
                self.task_list.clear()
                for line in file:
                    name, status = line.strip().split('|', 1)
                    task = Task(name)
                    if status == 'True':
                        task.mark_completed()
                    self.task_list.append(task)
                print('File loaded')
        except Exception as e:
            print(f'Could not load file: {e}')


lista = TaskManager()

lista.load_list()
lista.show_list()
lista.complete_task('Pranie')
lista.show_list()
