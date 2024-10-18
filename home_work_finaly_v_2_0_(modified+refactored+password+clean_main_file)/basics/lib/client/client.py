import datetime

from lib.decorators import Decs
from lib.achievement_manager.model import AchievmentManager
from lib.task_manager.dataclasses import Task
from lib.task_manager.model import TaskManager


class App(AchievmentManager, TaskManager):
    @Decs.log_create_task
    def create_task(
            self,
            name: str,
            priority: str,
            deadline: datetime.datetime,
    ) -> Task:
        if not self._TASKS:
            self._add_achievement('ach_add_first_task')
        task = Task(
            name=name,
            priority=priority,
            deadline=deadline,
        )
        self._TASKS_COUNT += 1
        self.check_achievement_for_five_tasks()
        self.check_achievement_for_ten_tasks()
        self._add_task(task)
        return task

    def get_achievements(self):
        return self._USER_ACHIEVMENTS

    def get_and_print_achievements(self):
        achievements = '\n'
        for achievement in self._USER_ACHIEVMENTS:
            achievements += f' — "{achievement.name}";\n'
        print (f'\nДостижения:{achievements}\n')
        
    @Decs.log_del_task
    def remove_task(self, id_: int):
        if not self._COMPLETE_TASKS_COUNT:
            self._add_achievement('ach_complete_first_task')
        task = Task(**self._TASKS[id_])
        self._remove_task(id_)
        self._COMPLETE_TASKS.append(task)
        self._COMPLETE_TASKS_COUNT += 1
        if self._COMPLETE_TASKS_COUNT == 5:
            self._add_achievement('ach_complete_five_task')
        # return f'\nЗадача {task.name} удалена\выполнена'
        return "" # Заглушка (что бы избавиться от None)
        

    def get_tasks(self):
        return self._get_tasks()

    def get_profile(self):
        tasks = '\n'
        for id_, info in self._TASKS.items():
            tasks += (
                f'\n{info.get("name")}\n'
                f'\t-ID: {id_}\n'
                f'\t-Приоритет: {info.get("priority")}\n'
                f'\t-Дата создания: {info.get("create_datetime")}\n'
                f'\t-Выполнить до: {info.get("deadline")}\n'
            )
        achievements = '\n'
        for achievement in self._USER_ACHIEVMENTS:
            achievements += f' — "{achievement.name}";\n'
        print (f'\nДостижения:{achievements}\n')
        info = (
            f'\nНикнейм: {self.username}\n'
            f'Возраст: {self.age}\n'
            f'Текущие задачи:\t{tasks}'
        )
        return info.strip()