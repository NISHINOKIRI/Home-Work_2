import json
import os
import dataclasses
from lib.decorators import Decs
from lib.task_manager.dataclasses import Task
from dataclasses import asdict

from lib.user.model import User


class TaskManager(User):
    def __get_id(
            self,
    ) -> int:
        length_tasks = len(self._TASKS)
        e = self._COMPLETE_TASKS
        return length_tasks + 1

    @staticmethod
    def task_saver(task):
        # Проверяем, существует ли файл с задачами
        if os.path.exists('tasks.json'):
            with open('tasks.json', 'r', encoding='utf8') as f:
                try:
                    # Загружаем существующие задачи
                    tasks_dict = json.load(f)
                except json.JSONDecodeError:
                    # Если файл пустой или поврежден, инициализируем пустой словарь
                    tasks_dict = {}
        else:
            tasks_dict = {}

        # Проверяем, что задача уже имеет id
        if 'id' not in task:
            raise ValueError("Задача должна иметь 'id'")

        task_id = task['id']  # Используем id как ключ

        # Проверяем, существует ли задача с таким id
        if task_id in tasks_dict:
            print(f"Задача с id {task_id} уже существует и будет обновлена.")
            # Обновляем данные существующей задачи
            tasks_dict[task_id].update(task)
        else:
            # Добавляем задачу в словарь
            tasks_dict[task_id] = task

        # Сохраняем обновленный словарь в файл
        with open('tasks.json', 'w', encoding='utf8') as f:
            json.dump(tasks_dict, f, indent=2, default=str)



            # @staticmethod
    # def task_saver(task):
    #     json_str = json.dumps(task, indent=2)
    #     with open('tasks.json', 'a', encoding='utf8') as f:
    #         f.write(json_str)

    # @staticmethod
    # def task_saver(task):
    #     # Проверяем, существует ли файл с задачами
    #     if os.path.exists('tasks.json'):
    #         with open('tasks.json', 'r', encoding='utf8') as f:
    #             try:
    #                 # Загружаем существующие задачи
    #                 tasks_dict = json.load(f)
    #             except json.JSONDecodeError:
    #                 # Если файл пустой или поврежден, инициализируем пустой словарь
    #                 tasks_dict = {}
    #     else:
    #         tasks_dict = {}
    #
    #     # Проверяем, что задача уже имеет id
    #     if 'id' not in task:
    #         raise ValueError("Задача должна иметь 'id'")
    #
    #     task_id = task['id']  # Используем id как ключ
    #     tasks_dict[task_id] = task  # Добавляем задачу в словарь
    #
    #     # Сохраняем обновленный словарь в файл
    #     with open('tasks.json', 'w', encoding='utf8') as f:
    #         json.dump(tasks_dict, f, indent=2, default=str)  # Указываем default для преобразования объектов, таких как datetime



    # def _add_task(
    #         self,
    #         task: Task,
    # ) -> None:
    #     id_ = self.__get_id()
    #     task = asdict(task)
    #     deadline = task.get('deadline')
    #     if deadline:
    #         deadline = deadline.strftime('%Y-%m-%d %H:%M')
    #         task.update(deadline=deadline)
    #     self.task_saver(task={id_: task})
    #     self._TASKS[id_] = task

    def _add_task(self, task: Task) -> None:
        id_ = self.__get_id()
        task_dict = asdict(task)  # Конвертируем объект в словарь
        task_dict['id'] = id_  # Добавляем ключ id к задаче

        # Форматирование срока
        deadline = task_dict.get('deadline')
        if deadline:
            deadline = deadline.strftime('%Y-%m-%d %H:%M')
            task_dict.update(deadline=deadline)

        self.task_saver(task=task_dict)  # Передаем task_dict, который теперь включает id
        self._TASKS[id_] = task_dict  # Сохраняем задачу в локальном словаре


    def _add_complete_task(self, task: Task):
        self._COMPLETE_TASKS.append(task)

    def _remove_task(
        self,
        id_: int,
    ) -> None | bool:
        if id_ < 0:
            return False
        self._TASKS.pop(id_)
        self.__sort_tasks()

    def __sort_tasks(
        self
    ) -> None:
        """
        Private метод, доступный только из класса.
        Сортирует задачи по id
        :return: None
        """
        values = [*self._TASKS.values()]
        self._TASKS.clear()
        self._TASKS.update(
            {
                task + 1: values[task] for task in range(0, len(values))
            }
        )

    def _get_tasks(self) -> str:
        tasks_str = 'Ваши задачи:\n'
        for id_, task_name in self._TASKS.items():
            tasks_str += f'{id_}: {task_name}\n'
        return tasks_str

    def __str__(self):  # Дандер(Магические) методы
        return 'объект класса TaskManager'

    def __repr__(self):
        ...

    def __bool__(self):
        return self.__TASKS

    def __getattr__(self, item):
        if item == 'tasks':
            return self._get_tasks()
        else:
            return 'Атрибут не существует'


if __name__ == '__main__':
    print('Это модуль!')