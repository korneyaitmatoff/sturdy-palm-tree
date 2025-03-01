from enum import Enum

from pydantic import BaseModel, StrictStr, StrictInt


class Gender(Enum):
    MALE = "М"
    FEMALE = "Ж"

    @staticmethod
    def list():
        return [Gender.MALE.value, Gender.FEMALE.value]


class Student(BaseModel):
    id: StrictInt | None = None
    name: StrictStr
    gender: str
    age: StrictInt
    performance: StrictInt  # from 0 to 100
    stress: StrictInt  # уровень стресса от 0 до 10
    family_alcohol: bool  # алкоголь в семье
    classmates_relations: bool  # давление со стороны одноклассников
    alcohol_forecast: StrictInt  # целевая переменная: склонность к алкоголизму
