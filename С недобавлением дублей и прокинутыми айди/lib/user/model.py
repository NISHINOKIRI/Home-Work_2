from lib.achievement_manager.dataclasses import Achievement


class User:
    _TASKS = {}
    _USER_ACHIEVMENTS: list[Achievement] = []
    _COMPLETE_TASKS = []
    _COMPLETE_TASKS_COUNT = 0

    def __init__(
        self,
        username: str,
        age: int,
    ):
        self.username = username
        self.age = age
