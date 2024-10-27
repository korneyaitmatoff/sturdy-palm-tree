from faker import Faker
from pytest import mark

from config import db_config
from sturdy_palm_tree.src.api.service import StudentService
from sturdy_palm_tree.src.api.models import Student, Gender
from sturdy_palm_tree.src.api.core import tables


class TestStudents:

    @mark.parametrize("i", list(range(0, 300)), indirect=False)
    def test_create(self, i):
        f = Faker()
        service = StudentService(table=tables.Students, **db_config)

        service.create(data=dict(Student(
            name=f.name(),
            gender=f.random_element(Gender.list()),
            age=f.random_int(5, 18),
            performance=f.random_int(0, 100),
            stress=f.random_int(0, 10),
            family_alcohol=f.boolean(chance_of_getting_true=50),
            classmates_relations=f.boolean(chance_of_getting_true=50),
            alcohol_forecast=f.random_int(0, 100),
        )))

        service.read()
