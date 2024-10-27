import datetime
import json
import os
from typing import Optional  # Импортируем Optional
from lib.achievement_manager.model import AchievmentManager
from lib.decorators import Decs
from lib.task_manager.dataclasses import Task
from lib.task_manager.model import TaskManager

class App(AchievmentManager, TaskManager):
    def load_tasks(self) -> None:
        if os.path.exists('tasks.json'):
            with open('tasks.json', 'r', encoding='utf8') as f:
                try:
                    tasks_data = json.load(f)
                    for task_info in tasks_data.values():
                        # Создаем экземпляр Task, передавая нужные параметры
                        task = Task(
                            name=task_info.get("name"),
                            priority=task_info.get("priority"),
                            create_datetime=task_info.get("create_datetime"),
                            deadline=datetime.datetime.strptime(task_info["deadline"], '%Y-%m-%d %H:%M')
                            if task_info.get("deadline") else None
                        )
                        self._TASKS[task.id] = task  # Храним экземпляр Task в словаре
                except json.JSONDecodeError:
                    print("Ошибка при декодировании JSON файла.")
                except KeyError as e:
                    print(f"Отсутствует ключ в данных задачи: {e}")
                except Exception as e:
                    print(f"Произошла ошибка: {e}")
        else:
            print("Файл tasks.json не найден.")

    def create_task(self, name: str, priority: str, deadline: Optional[datetime.datetime] = None) -> Task:
        if not self._TASKS:
            self._add_achievement('ach_add_first_task')

        task = Task(name=name, priority=priority, deadline=deadline)
        self._add_task(task=task)  # Добавляем задачу в список задач
        return task  # Возвращаем созданную задачу

    @Decs.log_del_task
    def remove_task(self, id_: int):
        if not self._COMPLETE_TASKS_COUNT:
            self._add_achievement('ach_complete_first_task')

        task = self._TASKS.get(id_)
        if task:  # Если задача найдена
            self._remove_task(id_)
            self._COMPLETE_TASKS.append(task)
            self._COMPLETE_TASKS_COUNT += 1
            return f'Task {task.name} removed'
        else:
            return f'Task with ID {id_} not found'

    def get_tasks(self):
        return {task.id: repr(task) for task in self._TASKS.values()}

    def get_profile(self):
        tasks = '\n'.join(repr(task) for task in self._TASKS.values())
        achievements = '\n'.join(achievement.name for achievement in self._USER_ACHIEVMENTS)
        info = (
            f'Никнейм: {self.username}\n'
            f'Возраст: {self.age}\n'
            f'Достижения: {achievements}\n'
            f'Текущие задачи:\n{tasks or "Нет текущих задач."}'
        )
        return info