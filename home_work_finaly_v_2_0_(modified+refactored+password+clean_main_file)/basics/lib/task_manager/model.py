from lib.task_manager.dataclasses import Task
from dataclasses import asdict
from lib.decorators import Decs

from lib.user.model import User

class TaskManager(User):
    def __get_id(
            self,
    ) -> int:
        length_tasks = len(self._TASKS)
        e = self._COMPLETE_TASKS
        return length_tasks + 1

    def _add_task(
            self,
            task: Task,
    ) -> None:
        id_ = self.__get_id()
        task = asdict(task)
        deadline = task.get('deadline')
        if deadline:
            deadline = deadline.strftime('%Y-%m-%d %H:%M')
            task.update(deadline=deadline)
        self._TASKS[id_] = task

    def _add_complete_task(self, task: Task):
        self._COMPLETE_TASKS.append(task)
        
    # @Decs.log_del_task # Тут отрабатывает без заглушки
    def _remove_task(
        self,
        id_: int,
    ) -> None | bool:
        if id_ < 0:
            return False
        self._TASKS.pop(id_)
        # self.__sort_tasks()

    # def _remove_task(
    #         self,
    #         id_: int,
    # ) -> None | bool:
    #     if id_ in self._TASKS:
    #         del self._TASKS[id_]
    #         # self.__sort_tasks()  # Вызываем сортировку, если необходимо (Нет, если хотим сохранить идентичные названия задачи и айди)
    #         return True  # Можно вернуть True, если удаление было успешным
    #     return False  # Возвращаем False, если ID не найден



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

    def _get_tasks(self):
        tasks = ''
        for id_, info in self._TASKS.items():
            tasks += (
                f'\n{info.get("name")}\n'
                f'\t-ID: {id_}\n'
                f'\t-Приоритет: {info.get("priority")}\n'
                f'\t-Дата создания: {info.get("create_datetime")}\n'
                f'\t-Выполнить до: {info.get("deadline")}\n'
            )
        return tasks.strip()  # Удаляем лишние пробелы и пустые строки в конце (да-да, оказывается так можно -_-)


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
