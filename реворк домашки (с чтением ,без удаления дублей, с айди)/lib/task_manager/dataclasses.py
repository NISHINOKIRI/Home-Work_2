import dataclasses
import datetime
from typing import Optional

@dataclasses.dataclass
class Task:
    id: int = dataclasses.field(init=False)  # Уникальный идентификатор задачи
    name: Optional[str] = None  # Название задачи
    priority: Optional[str] = None  # Приоритет задачи
    create_datetime: str = dataclasses.field(default_factory=lambda: datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))  # Время создания задачи
    deadline: Optional[datetime.datetime] = None  # Дедлайн задачи

    def __post_init__(self):
        if not hasattr(Task, '_current_id'):
            Task._current_id = 0
        Task._current_id += 1
        self.id = Task._current_id

    def __repr__(self):
        return (f'Task(id={self.id}, name={self.name}, priority={self.priority}, '
                f'create_datetime={self.create_datetime}, deadline={self.deadline})')