from enum import StrEnum

from pydantic import BaseModel, StrictStr, StrictInt


class Gender(StrEnum):
    MALE = "М"
    FEMALE = "Ж"

    @staticmethod
    def list():
        return [Gender.MALE, Gender.FEMALE]


class Student(BaseModel):
    id: StrictInt | None = None
    name: StrictStr
    gender: Gender
    age: StrictInt
    performance: StrictInt  # from 0 to 100
    stress: StrictInt  # уровень стресса от 0 до 10
    family_alcohol: bool  # алкоголь в семье
    classmates_relations: bool  # давление со стороны одноклассников
    alcohol_forecast: StrictInt  # целевая переменная: склонность к алкоголизму
