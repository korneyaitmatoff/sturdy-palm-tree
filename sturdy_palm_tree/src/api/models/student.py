from enum import StrEnum

from pydantic import BaseModel, StrictStr, StrictInt


class Gender(StrEnum):
    MALE = "М"
    FEMALE = "Ж"


class Student(BaseModel):
    id: StrictInt | None = None
    name: StrictStr
    gender: Gender
    performance: StrictInt  # from 0 to 100
    stress: StrictInt  # уровень стресса от 0 до 10
    family_alcohol: bool  # алкоголь в семье
    classmates_relations: bool  # давление со стороны одноклассников
    alcohol_forecast: bool  # целевая переменная: склонность к алкоголизму
