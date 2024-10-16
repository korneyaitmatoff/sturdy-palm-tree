from typing import Type, Any

from sturdy_palm_tree.src.api.repository.repository import Repository


class Service:
    repository: Repository

    def __init__(self, table: Type[Any], **kwargs):
        self.repository = Repository(table=table, **kwargs)

    def create(self, data: Any):
        self.repository.create(data=data)

    def read(self):
        return self.repository.read(filters=())

    def read_by_id(self, entity_id: int):
        return self.repository.read(filters=(self.repository.table.id == entity_id,))
