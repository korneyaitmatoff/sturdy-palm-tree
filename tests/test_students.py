from faker import Faker

from config import db_config
from sturdy_palm_tree.src.api.service import StudentService
from sturdy_palm_tree.src.api.models import Student, Gender
from sturdy_palm_tree.src.api.core import tables


class TestStudents:

    def test_create(self):
        f = Faker()
        service = StudentService(table=tables.Students, **db_config)

        service.create(data=dict(Student(
            name=f.name(),
            gender=Gender.MALE,
            performance=f.random_int(0, 100),
            stress=f.random_int(0, 10),
            family_alcohol=f.boolean(chance_of_getting_true=50),
            classmates_relations=f.boolean(chance_of_getting_true=50),
            alcohol_forecast=f.boolean(chance_of_getting_true=50),
        )))

        service.read()
