import datetime
from lib.client.client import App
from reader_task_json import ReadJson


app = App(
    username='ogmnogoel',
    age=22,
)

app.create_task(
    name='test1',
    priority='medium',
    deadline=datetime.datetime(
        year=2024,
        month=10,
        day=1,
        hour=19,
        minute=0,
    )
)

app.create_task(
    name='test2',
    priority='medium',
    deadline=datetime.datetime(
        year=2024,
        month=10,
        day=1,
        hour=19,
        minute=0,
    )
)


app.create_task(
    name='test4',
    priority='medium',
    deadline=datetime.datetime(
        year=2024,
        month=10,
        day=1,
        hour=19,
        minute=0,
    )
)


# Читаем таски
def read_task():
    print('\n' + ReadJson.print_title())
    print(ReadJson.load_tasks_from_file())

read_task()
