import datetime

from pydantic import BaseModel, StrictInt


class AuditPoll(BaseModel):
    """Схема данных для бд"""
    id: StrictInt | None = None
    created_at: datetime.datetime
    field_1: StrictInt
    field_2: StrictInt
    field_3: StrictInt
    field_4: StrictInt
    field_5: StrictInt
    field_6: StrictInt
    field_7: StrictInt
    field_8: StrictInt
    field_9: StrictInt
    field_10: StrictInt
    s_id: StrictInt
