from typing import Type, Any

from sturdy_palm_tree.src.api.core.db_handler import DatabaseHandler


class Repository:
    db: DatabaseHandler

    def __init__(self, table: Type[Any], **kwargs):
        self.db = DatabaseHandler(**kwargs)
        self.table = table

    def read(self, filters=()):
        with self.db as db:
            return db.select(table=self.table, filters=filters)

    def create(self, data):
        with self.db as db:
            db.insert(table=self.table, data=data)
