import random
import datetime

def create_tasks_gen(app):
    priorities_list = ['trivial (-1)', 'low (0)', 'medium (1)', 'high (2)', 'major (3)', 'critical (99)']

    # Генерация задач
    task_ids = []
    num_tasks = random.randint(1, 15)  # Генерация случайного количества (от 1 до 15)
    for i in range(1, num_tasks + 1):  # Генерация случайного числа (от 1 до num_tasks)
        tn = f'Задача {i}'  # Название задачи
        priority = random.choice(priorities_list)  # Случайный выбор приоритета

        # Генерация даты
        d_gen = random.randint(0, 10)
        dl_gen = datetime.datetime.now() + datetime.timedelta(days=d_gen)

        # Генерация времени дедлайна
        random_hours = random.randint(0, 23)
        random_minutes = random.randint(0, 59)
        deadline = dl_gen.replace(hour=random_hours, minute=random_minutes, second=0)

        task_id = app.create_task(
            name=tn,
            priority=priority,
            deadline=deadline
        )
        task_ids.append(task_id)