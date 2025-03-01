import flet as ft

from config import db_config
from sturdy_palm_tree.src.api.service import AuditPollService, StudentService
from sturdy_palm_tree.src.api.core import tables


def poll_table(page):
    def _get_polls_data() -> list:
        return AuditPollService(table=tables.AuditPolls, **db_config).read()

    def _get_student(id: int):
        return StudentService(table=tables.Students, **db_config).read_by_id(entity_id=id)[0]

    return ft.Container(
        ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Студент")),
                ft.DataColumn(ft.Text("Поле 1")),
                ft.DataColumn(ft.Text("Поле 2")),
                ft.DataColumn(ft.Text("Поле 3")),
                ft.DataColumn(ft.Text("Поле 4")),
                ft.DataColumn(ft.Text("Поле 5")),
                ft.DataColumn(ft.Text("Поле 6")),
                ft.DataColumn(ft.Text("Поле 7")),
                ft.DataColumn(ft.Text("Поле 8")),
                ft.DataColumn(ft.Text("Поле 9")),
                ft.DataColumn(ft.Text("Поле 10")),
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(_get_student(id=item.s_id).name)),
                        ft.DataCell(ft.Text(item.field_1)),
                        ft.DataCell(ft.Text(item.field_2)),
                        ft.DataCell(ft.Text(item.field_3)),
                        ft.DataCell(ft.Text(item.field_4)),
                        ft.DataCell(ft.Text(item.field_5)),
                        ft.DataCell(ft.Text(item.field_6)),
                        ft.DataCell(ft.Text(item.field_7)),
                        ft.DataCell(ft.Text(item.field_8)),
                        ft.DataCell(ft.Text(item.field_9)),
                        ft.DataCell(ft.Text(item.field_10)),
                    ]
                )
                for item in _get_polls_data()
            ]
        )
    )
