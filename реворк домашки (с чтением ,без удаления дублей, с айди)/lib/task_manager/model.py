import json
import os
from lib.task_manager.dataclasses import Task
from dataclasses import asdict
from lib.user.model import User
import datetime
from typing import Optional

class TaskManager(User):
    def __get_id(self, task: Task) -> int:
        return task.id

    def __repr__(self):
        return f'TaskManager with {len(self._TASKS)} task(s)'

    @staticmethod
    def task_saver(task: Task) -> None:
        task_dict = asdict(task)  # Преобразуем Task обратно в словарь для сериализации
        json_str = json.dumps(task_dict, indent=2, default=str)
        with open('tasks.json', 'a', encoding='utf8') as f:
            f.write(json_str + "\n")  # добавлено перенос строки для каждой записи

    def _add_task(self, task: Task) -> None:
        id_ = self.__get_id(task)  # Используем id из объекта Task

        # Check if task already exists to avoid duplicates
        if id_ in self._TASKS:
            raise ValueError(f'Task with ID {id_} already exists.')

        self._TASKS[id_] = task  # Храним экземпляр Task
        self.task_saver(task)  # Сохраняем задачу

    def _add_complete_task(self, task: Task) -> None:
        self._COMPLETE_TASKS.append(task)

    def _remove_task(self, id_: int) -> Optional[bool]:
        if id_ < 0 or id_ not in self._TASKS:
            return False
        task = self._TASKS.pop(id_)  # Получаем задачу и удаляем её из _TASKS
        self._add_complete_task(task)  # Добавляем задачу в завершенные
        self.__sort_tasks()

    def __sort_tasks(self) -> None:
        """Сортируем задачи по id."""
        self._TASKS = dict(sorted(self._TASKS.items()))  # Сортируем по ключам (ID)

    def _get_tasks(self) -> str:
        tasks_str = 'Ваши задачи:\n'
        for id_, task_info in self._TASKS.items():
            tasks_str += f'{id_}: {task_info}\n'
        return tasks_str

    def load_tasks(self) -> None:
        """Загрузка задач из файла tasks.json."""
        if os.path.exists('tasks.json'):
            with open('tasks.json', 'r', encoding='utf8') as f:
                try:
                    tasks_data = json.load(f)
                    for task_info in tasks_data:
                        task = Task(
                            id=task_info["id"],
                            name=task_info["name"],
                            priority=task_info["priority"],
                            create_datetime=datetime.datetime.strptime(task_info["create_datetime"], '%Y-%m-%d %H:%M'),
                            deadline=datetime.datetime.strptime(task_info["deadline"], '%Y-%m-%d %H:%M') if task_info["deadline"] else None
                        )
                        self._TASKS[task.id] = task  # Сохраняем экземпляр Task

                except json.JSONDecodeError:
                    print("Ошибка при декодировании JSON файла.")
                except Exception as e:
                    print(f"Произошла ошибка: {e}")
        else:
            print("Файл tasks.json не найден.")

    def __str__(self):
        return 'объект класса TaskManager'

    def __bool__(self):
        return bool(self._TASKS)  # Проверяем, есть ли задачи

    def __getattr__(self, item):
        if item == 'tasks':
            return self._get_tasks()
        else:
            return 'Атрибут не существует'

if __name__ == '__main__':
    print('Это модуль!')