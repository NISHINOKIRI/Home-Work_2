from lib.achievement_manager.dataclasses import Achievement
from lib.user.model import User


class AchievmentManager(User):  # Создаём класс-наследник
    __ACHIEVMENTS = {  # Объявляем ачивки
        'ach_add_first_task': {'name': 'Приступим', 'description': 'Добавить первую задачу'},
        'ach_add_five_task': {'name': 'Расширяемся, уже 5 задач', 'description': 'Добавить 5 задач'},
        'ach_complete_first_task': {'name': 'Начало продуктивного пути', 'description': 'Завершить первую задачу'},
        'ach_add_ten_task': {'name': 'Отлично, уже 10 задач!', 'description': 'Добавить 10 задач'},
        'ach_complete_five_task': {'name': 'Сама продуктивность!', 'description': 'Завершить 5 задач'},
    }

    def _add_achievement(
            self,
            achievement_code_name: str,
    ):
        achievement = Achievement(
            name=self.__ACHIEVMENTS[achievement_code_name].get('name'),
            description=self.__ACHIEVMENTS[achievement_code_name].get('description')
        )
        self._USER_ACHIEVMENTS.append(achievement)

    def check_achievement_for_five_tasks(self):
        """Проверяет, добавлено ли 5 задач."""
        if self._TASKS_COUNT == 5:
            self._add_achievement('ach_add_five_task')

    def check_achievement_for_ten_tasks(self):
        """Проверяет, добавлено ли 10 задач."""
        if self._TASKS_COUNT == 10:
            self._add_achievement('ach_add_ten_task')

    def add_achievement_for_activity(self, achievement_code_name: str):
        """Добавляет ачивку за определённую активность."""
        self._add_achievement(achievement_code_name)
