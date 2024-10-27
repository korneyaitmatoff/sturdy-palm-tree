import datetime

from sqlalchemy.orm import declarative_base
from sqlalchemy import VARCHAR, Integer, Column, Boolean, ForeignKey, DateTime

base = declarative_base()


class Students(base):
    __tablename__ = "students"

    id = Column(type_=Integer, primary_key=True, autoincrement=True)
    name = Column(type_=VARCHAR, )
    gender = Column(type_=VARCHAR, )
    age = Column(type_=Integer, )
    performance = Column(type_=Integer, )  # from 0 to 100
    stress = Column(type_=Integer, )  # уровень стресса от 0 до 10
    family_alcohol = Column(type_=Boolean, )  # алкоголь в семье
    classmates_relations = Column(type_=Boolean, )  # давление со стороны одноклассников
    alcohol_forecast = Column(type_=Integer, default=0)  # целевая переменная: склонность к алкоголизму


class AuditPolls(base):
    __tablename__ = "audit_polls"

    id = Column(type_=Integer, primary_key=True, autoincrement=True)
    created_at = Column(type_=DateTime, default=datetime.datetime.now())
    field_1 = Column(type_=Integer, )
    field_2 = Column(type_=Integer, )
    field_3 = Column(type_=Integer, )
    field_4 = Column(type_=Integer, )
    field_5 = Column(type_=Integer, )
    field_6 = Column(type_=Integer, )
    field_7 = Column(type_=Integer, )
    field_8 = Column(type_=Integer, )
    field_9 = Column(type_=Integer, )
    field_10 = Column(type_=Integer, )
    s_id = Column(Integer, ForeignKey("students.id"))
