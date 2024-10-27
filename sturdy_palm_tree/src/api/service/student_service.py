from typing import Type, Any

from sturdy_palm_tree.src.api.service import Service
from sturdy_palm_tree.src.api.repository.student_repository import StudentRepository


class StudentService(Service):
    repository: StudentRepository

    def __init__(self, table: Type[Any], **kwargs):
        super().__init__(table, **kwargs)
        self.repository = StudentRepository(table=table, **kwargs)

    def get_students_group_by_alco_depends(self):
        """Получение кол-ва студентов, разбитым по разным уровням риска зависимости"""
        return [
            {
                "title": item[0],
                "value": item[1],
            }
            for item in self.repository.get_students_group_by_alco_depends()
        ]

    def get_students_group_by_gender(self):
        """Получение кол-ва студентов с группировкой по полу и связи с алкогольной зависимостью"""
        return [
            {
                "title": item[1],
                "value": item[0],
            }
            for item in self.repository.get_count_group_by(by="gender")
        ]

    def get_students_group_by_age(self):
        """Получение кол-ва студентов с группировкой по возрастным группам"""
        return [
            {
                "title": item[0],
                "value": item[1],
            }
            for item in self.repository.get_students_group_by_age()
        ]

    def get_students_group_by_perf(self):
        """Получение кол-ва студентов с группировкой по успеваемости"""
        tmp = [
            {
                "title": item[0],
                "value": round(item[1]),
            }
            for item in self.repository.get_students_group_by_perf()
        ]
        tmp.sort(key=lambda x: x["title"])

        return tmp

    def get_students_group_by_stress(self):
        """Получение кол-ва студентов с группировкой по уровню стресса"""
        tmp = [
            {
                "value": round(item[1]),
                "title": item[0]
            }
            for item in self.repository.get_students_group_by_stress()
        ]
        tmp.sort(key=lambda x: x["value"])

        return tmp

    def get_avg_audit_group_by_dates(self):
        """Получение среднего балла audit с группировкой по датам"""
        res = []

        for item in self.repository.get_avg_audit_group_by_dates():
            res.append(
                {
                    "title": str(item[1]).replace("00:00:00", ""),
                    "value": item[0]
                }
            )

        return res
