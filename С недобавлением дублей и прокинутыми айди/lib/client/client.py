import datetime
from typing import Optional  # Импортируем Optional
from lib.achievement_manager.model import AchievmentManager
from lib.decorators import Decs
from lib.task_manager.dataclasses import Task
from lib.task_manager.model import TaskManager

class App(AchievmentManager, TaskManager):

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