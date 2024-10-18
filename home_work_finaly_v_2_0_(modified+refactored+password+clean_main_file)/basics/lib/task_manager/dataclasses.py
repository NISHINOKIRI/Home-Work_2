import dataclasses
import datetime


@dataclasses.dataclass
class Task:
    name: str | None = None
    priority: str | None = None
    create_datetime: str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    deadline: datetime.datetime | None = None
