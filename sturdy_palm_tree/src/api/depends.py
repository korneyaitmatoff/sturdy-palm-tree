from config import db_config
from sturdy_palm_tree.src.api.service import StudentService, AuditPollService
from sturdy_palm_tree.src.api.core import tables

students_service = StudentService(table=tables.Students, **db_config)
audit_service = AuditPollService(table=tables.AuditPolls, **db_config)
