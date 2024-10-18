from lib.task_manager.create_tasks import create_tasks_gen
from lib.client.client import App
from lib.client.manage import manage_tasks_and_achievements
from lib.client.added_task_number import show_added_task_number
from lib.client.remove_tasks import num_done_tasks
from lib.start import start_our_program

# Запуск программы
if start_our_program():
    app = App(
        username='Nishinokiri',
        age=27,
    )
    create_tasks_gen(app)
    num_tasks = create_tasks_gen(app) # без это строки не работает если использовать строки ниже напрямую в мейне
    show_added_task_number(num_tasks)
    num_done_tasks(app, num_tasks)
    manage_tasks_and_achievements(app)
else:
    print('\nНеверный пароль'
          '\nЗавершение программы')