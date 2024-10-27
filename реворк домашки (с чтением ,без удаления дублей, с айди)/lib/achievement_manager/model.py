from lib.achievement_manager.dataclasses import Achievement
from lib.decorators import Decs
from lib.user.model import User


class AchievmentManager(User):  # Создаём класс-наследник
    __ACHIEVMENTS = {  # Объявляем ачивки
        'ach_add_first_task': {'name': 'Приступим', 'description': 'Добавить первую задачу'},
        'ach_add_five_task': {'name': 'Расширяемся, уже 5 задач', 'description': 'Добавить пять задач'},
        'ach_complete_first_task': {'name': 'Сама продуктивность', 'description': 'Завершить первую задачу'},
    }

    @Decs.logger
    def _add_achievement(
            self,
            achievement_code_name: str,
    ):
        achievement = Achievement(
            name=self.__ACHIEVMENTS[achievement_code_name].get('name'),
            description=self.__ACHIEVMENTS[achievement_code_name].get('description')
        )
        self._USER_ACHIEVMENTS.append(achievement)
