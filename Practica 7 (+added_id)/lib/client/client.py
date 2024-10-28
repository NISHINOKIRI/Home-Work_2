import datetime

from lib.achievement_manager.model import AchievmentManager
from lib.decorators import Decs
from lib.task_manager.dataclasses import Task
from lib.task_manager.model import TaskManager


class App(AchievmentManager, TaskManager):

    def create_task(self, name: str, priority: str, deadline: datetime.datetime | None) -> Task:
        if not self._TASKS:
            self._add_achievement('ach_add_first_task')
        task = Task(
            name=name,
            priority=priority,
            deadline=deadline,
        )
        self._add_task(task=task)  # Сохранение задачи
        return task

    def get_achievements(self):
        return self._USER_ACHIEVMENTS

    @Decs.log_del_task
    def remove_task(self, id_: int):
        if not self._COMPLETE_TASKS_COUNT:
            self._add_achievement('ach_complete_first_task')
        task = Task(**self._TASKS[id_])
        self._remove_task(id_)
        self._COMPLETE_TASKS.append(task)
        self._COMPLETE_TASKS_COUNT += 1
        return f'task {task.name} removed'

    def get_tasks(self):
        return self._get_tasks()

    def get_profile(self):
        tasks = '\n'
        for id_, info in self._TASKS.items():
            tasks += (
                f'{id_}: {info.get("name")}\n'
                f'\t-Приоритет: {info.get("priority")}\n'
                f'\t-Дата создания: {info.get("create_datetime")}\n'
                f'\t-Крайний срок: {info.get("deadline")}'
            )
        achievements = '\n'
        for achievement in self._USER_ACHIEVMENTS:
            achievements += f'\t{achievement.name}\n'
        info = (
            f'Никнейм: {self.username}\n'
            f'Возраст: {self.age}\n'
            f'Достижения: {achievements}\n'
            f'Текущие задачи: {tasks}'
        )
        return info
