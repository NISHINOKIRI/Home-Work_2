import json
import os
from lib.decorators import Decs


class ReadJson:
    @staticmethod
    def print_title():
        return str(f'Задачи из файла tasks.json:')

    # @Decs.print_title
    def load_tasks_from_file(filename='tasks.json'):
            # Проверяем, существует ли файл
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf8') as f:
                    try:
                        # Читаем данные из файла
                        data = f.read()
                        # Превращаем строку в объект
                        tasks = json.loads(data)
                        task_list = ''
                        for id, info in tasks.items():
                            task_list += (
                                f'\nID: {id}\n'
                                f'\t- Задача: {info.get("name")}\n'
                                f'\t- Приоритет: {info.get("priority")}\n'
                                f'\t- Дата создания: {info.get("create_datetime")}\n'
                                f'\t- Крайний срок: {info.get("deadline")}\n'
                            )
                        return task_list # Возвращаем загруженные задачи
                    except json.JSONDecodeError:
                        return ''
            else:
                return ''

    load_tasks_from_file()


# tasks = '\n'
# for id_, info in self._TASKS.items():
#     tasks += (
#         f'{id_}: {info.get("name")}\n'
#         f'\t-Приоритет: {info.get("priority")}\n'
#         f'\t-Дата создания: {info.get("create_datetime")}\n'
#         f'\t-Крайний срок: {info.get("deadline")}'
#     )