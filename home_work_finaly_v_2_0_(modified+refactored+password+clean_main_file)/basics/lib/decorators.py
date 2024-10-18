
class Decs:

    @staticmethod  # используем staticmethod, т.к. внутри нашего декоратора, мы не обращаемся к атрибутам и методам класса
    def log_create_task(fn):  # Объявляем название для декоратора
        # fn является create_task (см. файл client, 11-12 строки)
        print('')
        def wrapper(*args, **kwargs):
            # Метод wrapper принимает на вход позиционные(*args) и именованные аргументы(**kwargs)
            # для последующего взаимодействия с ними и передачи их в нашу функцию
            print({**kwargs}.get('name') + ' добавлена')
            print('-------------------')
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



    @staticmethod # Декоратор который работает везде) и в клиенте и таск менеджере хе-хе
    def log_del_task(fn):
        def wrapper(self, id_, *args, **kwargs):
            tasks = self._TASKS.get(id_)
            name = tasks.get('name')
            result = fn(self, id_, *args, **kwargs)
            print(f'Задача {name} решена')
            return result
        return wrapper
