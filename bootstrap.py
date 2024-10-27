from config import db_config
from sturdy_palm_tree.src.api.core.db_handler import DatabaseHandler
from sturdy_palm_tree.src.api.core import tables

if __name__ == "__main__":
    with DatabaseHandler(**db_config) as db:
        db.create_tables(meta=tables.base)

        d = db.execute_raw(
            raw="create view audit_sum as select id, s_id, created_at, field_1 + field_2 + field_3 + field_4 + "
                "field_5 + field_6 + field_7 + field_8 + field_9 + field_10 as sn from audit_polls",
            is_ddl=True)
