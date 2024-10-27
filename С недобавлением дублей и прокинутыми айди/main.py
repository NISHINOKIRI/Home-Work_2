import datetime

from lib.client.client import App

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
    name='test3',
    priority='medium',
    deadline=datetime.datetime(
        year=2024,
        month=10,
        day=1,
        hour=19,
        minute=2,
    )
)
app.create_task(
    name='test3',
    priority='medium',
    deadline=datetime.datetime(
        year=2024,
        month=10,
        day=1,
        hour=19,
        minute=2,
    )
)
app.create_task(
    name='test3',
    priority='medium',
    deadline=datetime.datetime(
        year=2024,
        month=10,
        day=1,
        hour=19,
        minute=2,
    )
)

app.create_task(
    name='test3',
    priority='medium',
    deadline=datetime.datetime(
        year=2024,
        month=10,
        day=1,
        hour=19,
        minute=2,
    )
)

app.create_task(
    name='test3',
    priority='medium',
    deadline=datetime.datetime(
        year=2024,
        month=10,
        day=1,
        hour=19,
        minute=2,
    )
)

app.create_task(
    name='test3',
    priority='medium',
    deadline=datetime.datetime(
        year=2024,
        month=10,
        day=1,
        hour=19,
        minute=2,
    )
)

app.create_task(
    name='test3',
    priority='medium',
    deadline=datetime.datetime(
        year=2024,
        month=10,
        day=1,
        hour=19,
        minute=2,
    )
)

print(app.get_tasks())
app.remove_task(1)
print(app.get_profile())