import datetime as dt


class Task:
    counter = 0 # class variable
    symbol = '✓'

    def __init__(self, name: str, priority: int = 1, due_dt: dt.datetime = None):
        self.__class__.counter += 1

        self.id = self.counter
        self.name = name
        self.status = False
        self.priority = priority
        self.created_dt = dt.datetime.now()
        self.due_dt = due_dt

    def __str__(self):
        symbol = self.symbol if self.status else ' '
        due_dt = f'({self.due_dt})' if self.due_dt else ''
        return f"{self.id}. [{symbol}] {self.name} {due_dt}"

    def finish(self):
        self.status = True

    def undo(self):
        self.status = False

class SuperTask(Task):
    symbol = '🌟'


class TaskList():
    def __init__(self, name: str):
        self.name = name
        self.tasks = {}

    def add_task(self, task: Task):
        if task.id not in self.tasks:
            self.tasks[task.id] = task

    def remove_task(self, task: Task):
        return self.remove_task_by_id(task.id)

    def remove_task_by_id(self, _id: int):
        try:
            removed_Task = self.tasks.pop(_id)
            return removed_Task
        except KeyError:
            return None

    def show(self):
        for tasks in self.tasks.values():
            print(tasks)


task1 = Task('Ukol 1')
task2 = Task('Ukol 2')
task3 = SuperTask('Ukol 3', priority=10, due_dt=dt.datetime(2025, 1, 31))

task_list = TaskList('Pracovni Ukoly')

task_list.add_task(task1)
task_list.add_task(task2)
task_list.add_task(task3)

task3.finish()

task_list.show()
