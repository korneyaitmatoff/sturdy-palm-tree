from sqlalchemy.orm import declarative_base
from sqlalchemy import VARCHAR, Integer, Column, Boolean, ForeignKey

base = declarative_base()


class Students(base):
    __tablename__ = "students"

    id = Column(type_=Integer, primary_key=True, autoincrement=True)
    name = Column(type_=VARCHAR, )
    gender = Column(type_=VARCHAR, )
    performance = Column(type_=Integer, )
    stress = Column(type_=Integer, )
    family_alcohol = Column(type_=Boolean, )
    classmates_relations = Column(type_=Boolean, ) 
    alcohol_forecast = Column(type_=Boolean, default=False)


class AuditPolls(base):
    __tablename__ = "audit_polls"

    id = Column(type_=Integer, primary_key=True, autoincrement=True)
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
