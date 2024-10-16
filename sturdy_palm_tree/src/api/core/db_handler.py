from typing import Type, Any

from sqlalchemy import create_engine
from sqlalchemy.orm import create_session, Session, DeclarativeMeta


class DatabaseHandler:
    session: Session

    def __init__(self, host: str, port: str, user: str, password: str, database: str):
        self.url = f"postgresql://{user}:{password}@{host}:{port}/{database}"
        self.engine = create_engine(url=self.url, echo=False)

        self.session = None

    def __enter__(self):
        self.session = create_session(bind=self.engine)

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()

    def select(self, table, filters):
        return self.session.query(table).filter(*filters).all()

    def insert(self, table: Type[Any], data: dict):
        nr = table(**data)

        self.session.add(nr)
        self.session.commit()
        self.session.refresh(nr)

    def create_tables(self, meta):
        meta.metadata.create_all(self.engine)
