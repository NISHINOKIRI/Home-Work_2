import json
from dataclasses import asdict


class Decs:

    @staticmethod  # используем staticmethod, т.к. внутри нашего декоратора, мы не обращаемся к атрибутам и методам класса
    def log_create_task(fn):  # Объявляем название для декоратора
        # fn является create_task (см. файл client, 11-12 строки)
        def wrapper(*args, **kwargs):
            # Метод wrapper принимает на вход позиционные(*args) и именованные аргументы(**kwargs)
            # для последующего взаимодействия с ними и передачи их в нашу функцию
            print('Вызван метод для добавления задачи: ', {**kwargs}.get('name'))
            fn(*args, **kwargs)
            # В данном случае, мы кладём аргументы переданные в вызове метода create_task в вызов переданной функции
            # Ниже как раз и представлены переданные аргументы, они в таком же виде, передаются в fn
            # name='test',
            # priority='medium',
            # deadline=datetime.datetime(
            #         year=2024,
            #         month=10,
            #         day=1,
            #         hour=19,
            #         minute=0,
            # )
        return wrapper  # Тут как раз мы и возвращаем функцию-обёртку

    @staticmethod
    def logger(fn):
        def wrapper(*args, **kwargs):

            print(f'Вызван метод: {fn.__name__} с аргументами: ', *args, {**kwargs})
            fn(*args, **kwargs)

            with open('log.json', 'a', encoding='utf8') as f:
                f.write(f'Вызван метод: {fn.__name__} с аргументами: {json.dumps({**kwargs}, indent=2)}\n')

        return wrapper

    @staticmethod
    def json_logger(fn):
        def wrapper(*args, **kwargs):
            kwa = {**kwargs}
            task = asdict(kwa.get('task'))
            deadline = task.get('deadline')
            if deadline:
                deadline = deadline.strftime('%Y-%m-%d %H:%M')
                task.update(deadline=deadline)
            fn(task=task)
            json_str = json.dumps(task, indent=2)
            with open('tasks.json', 'a', encoding='utf8') as f:
                f.write(json_str)

        return wrapper


    @staticmethod  # Декоратор который работает везде) и в клиенте и таск менеджере хе-хе
    def log_del_task(func):
        def wrapper(*args,**kwargs):
            # Отладка аргументов
            for arg in args:
                try:
                    print(f"Argument: {arg}, Type: {type(arg)}, Repr: {repr(arg)}")
                except Exception as e:
                    print(f"Unable to repr: {arg}. Error: {e}")
            kwargs_repr = {k: repr(v) for k, v in kwargs.items()}
            print(f"Вызван метод: {func.__name__} с аргументами: {args}, {kwargs_repr}")
            return func(*args, **kwargs)
        return wrapper