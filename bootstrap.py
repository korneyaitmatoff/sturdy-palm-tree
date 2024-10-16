from config import db_config
from sturdy_palm_tree.src.api.core.db_handler import DatabaseHandler
from sturdy_palm_tree.src.api.core import tables

if __name__ == "__main__":
    with DatabaseHandler(**db_config) as db:
        db.create_tables(meta=tables.base)
