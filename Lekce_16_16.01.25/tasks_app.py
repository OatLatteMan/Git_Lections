# tasks_app.py

from tasks import Task, TaskList

task_list = TaskList('New Task list')

while True:
    command = input('Put a command: ')

    if command == 'add':
        text = input('Put a text ')
        task_list.add_task(Task(text))

    if command == 'finish':
        task_id = int(input('Put a task id '))
        task_list.finish_task_by_id(task_id)

    # if command.startswith('add:'):
    #     text = command.split('add:')[1]
    #     task_list.add_task(Task(text))

    # if command.startswith('finish:'):
    #     task_id = int(command.split('finish:')[1])
    #     task_list.finish_task_by_id(task_id)

    task_list.show()