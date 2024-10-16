import time

import flet as ft

from sturdy_palm_tree.src.api.service import StudentService
from sturdy_palm_tree.src.api.core import tables
from config import db_config
from sturdy_palm_tree.components.add_student_form import add_student_form


def _get_rows(page) -> list:
    service = StudentService(table=tables.Students, **db_config)

    return [ft.DataRow(
        cells=[
            ft.DataCell(ft.Text(item.id)),
            ft.DataCell(ft.Text(item.name)),
            ft.DataCell(ft.Text(item.gender)),
            ft.DataCell(ft.Text(item.performance)),
            ft.DataCell(ft.Text(item.stress)),
            ft.DataCell(ft.Text(item.family_alcohol)),
            ft.DataCell(ft.Text(item.classmates_relations)),
            ft.DataCell(ft.Text(item.alcohol_forecast)),
            ft.DataCell(
                ft.CupertinoButton(text="profile",
                                   on_click=lambda x, item_id=item.id: page.go(route=f"/student/{item_id}"))
            )
        ]
    ) for item in service.read()]


def students_table(page):
    def _onclick(e):
        table.rows = _get_rows(page)
        page.update()

    table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("ID")),
            ft.DataColumn(ft.Text("Имя")),
            ft.DataColumn(ft.Text("Пол")),
            ft.DataColumn(ft.Text("Успеваемость")),
            ft.DataColumn(ft.Text("Уровень стресса")),
            ft.DataColumn(ft.Text("Алкоголь в семье")),
            ft.DataColumn(ft.Text("Давление со стороны одноклассников")),
            ft.DataColumn(ft.Text("Склонность к алкоголизму")),
            ft.DataColumn(ft.IconButton(icon=ft.icons.UPDATE_ROUNDED, on_click=_onclick)),
            # ft.DataColumn(ft.CupertinoButton("Update", icon=ft.icons.UPDATE, on_click=_onclick), ),
        ],
        rows=_get_rows(page),
        column_spacing=20
    )

    return table
