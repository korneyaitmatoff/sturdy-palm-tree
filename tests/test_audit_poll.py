from faker import Faker

from config import db_config
from sturdy_palm_tree.src.api.service import AuditPollService
from sturdy_palm_tree.src.api.core import tables
from sturdy_palm_tree.src.api.models import AuditPoll


class TestAuditPoll:
    service = AuditPollService(table=tables.AuditPolls, **db_config)

    def test_create(self):
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
        )))

    def test_read(self):
        data = self.service.read()
        assert len(data) > 0
