import flet as ft
from flet_route import Basket, Params

from config import db_config
from sturdy_palm_tree import auth_required
from sturdy_palm_tree.components import bottom_bar
from sturdy_palm_tree.src.api.core import tables
from sturdy_palm_tree.src.api.service import StudentService


@auth_required
def student(page: ft.Page, params: Params, basket: Basket):
    def _get_student(id: str | int):
        data = StudentService(table=tables.Students, **db_config).read_by_id(entity_id=id)

        return {key: item for key, item in data[0].__dict__.items() if "_" != key[0]}

    def _get_student_table(data: dict):
        return ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("ID")),
                ft.DataColumn(ft.Text("Имя")),
                ft.DataColumn(ft.Text("Пол")),
                ft.DataColumn(ft.Text("Успеваемость")),
                ft.DataColumn(ft.Text("Уровень стресса")),
                ft.DataColumn(ft.Text("Алкоголь в семье")),
                ft.DataColumn(ft.Text("Давление со стороны одноклассников")),
                ft.DataColumn(ft.Text("Склонность к алкоголизму")),
            ],
            rows=[
                ft.DataRow(cells=[
                    ft.DataCell(ft.Text(data["id"])),
                    ft.DataCell(ft.Text(data["name"])),
                    ft.DataCell(ft.Text(data["gender"])),
                    ft.DataCell(ft.Text(data["performance"])),
                    ft.DataCell(ft.Text(data["stress"])),
                    ft.DataCell(ft.Text(data["family_alcohol"])),
                    ft.DataCell(ft.Text(data["classmates_relations"])),
                    ft.DataCell(ft.Text(data["alcohol_forecast"])),
                ])
            ]
        )

    s_id = params.get("sid")
    return ft.View(
        route="/student",
        controls=[
            ft.Text("student"),
            _get_student_table(data=_get_student(id=s_id)),
            ft.CupertinoButton("Ссылка на опрос для данного студента",
                               on_click=lambda x: page.go(route=f"/audit/{s_id}")),
            bottom_bar(page=page)
        ]
    )
