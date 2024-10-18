import dataclasses
import datetime


@dataclasses.dataclass
class Achievement:
    name: str
    description: str
    receipt_date: datetime.date = datetime.date.today().strftime('%Y-%m-%d')
