from datetime import datetime

from faker import Faker
from pytest import mark

from config import db_config
from sturdy_palm_tree.src.api.service import AuditPollService, StudentService
from sturdy_palm_tree.src.api.core import tables
from sturdy_palm_tree.src.api.models import AuditPoll


class TestAuditPoll:
    service = AuditPollService(table=tables.AuditPolls, **db_config)
    students_service = StudentService(table=tables.Students, **db_config)

    @mark.parametrize("std", list(students_service.read()), indirect=False)
    def test_create(self, std):
        f = Faker()

        self.service.create(data=dict(AuditPoll(
            field_1=f.random_int(0, 4),
            field_2=f.random_int(0, 4),
            field_3=f.random_int(0, 4),
            field_4=f.random_int(0, 4),
            field_5=f.random_int(0, 4),
            field_6=f.random_int(0, 4),
            field_7=f.random_int(0, 4),
            field_8=f.random_int(0, 4),
            field_9=f.random_int(0, 4),
            field_10=f.random_int(0, 4),
            created_at=f.date_between_dates(date_start=datetime(2020, 1, 1), date_end=datetime(2024, 12, 31)),
            s_id=std.id
        )))

    def test_read(self):
        data = self.service.read()
        assert len(data) > 0
