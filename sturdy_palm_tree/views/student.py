import flet as ft
from flet_route import Basket, Params

from config import db_config
from sturdy_palm_tree import auth_required
from sturdy_palm_tree.components import bottom_bar
from sturdy_palm_tree.src.api.core import tables
from sturdy_palm_tree.src.api.service import StudentService
from sturdy_palm_tree.components import get_col_chart


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
                ft.DataColumn(ft.Text("")),
            ],
            rows=[
                ft.DataRow(cells=[
                    ft.DataCell(ft.Text(data["id"])),
                    ft.DataCell(ft.Text(data["name"])),
                    ft.DataCell(ft.Text(data["gender"])),
                    ft.DataCell(ft.TextField(
                        value=data["performance"]
                    )),
                    ft.DataCell(
                        ft.TextField(
                            value=data["stress"]
                        )
                    ),
                    ft.DataCell(
                        ft.TextField(
                            value=data["family_alcohol"]
                        )
                    ),
                    ft.DataCell(
                        ft.TextField(
                            value=data["classmates_relations"]
                        )
                    ),
                    ft.DataCell(ft.Text(data["alcohol_forecast"])),
                    ft.DataCell(ft.IconButton(ft.icons.SAVE)),
                ])
            ]
        )

    s_id = params.get("sid")
    return ft.View(
        route="/student",
        controls=[
            ft.Row(
                controls=[_get_student_table(data=_get_student(id=s_id)), ]
            ),
            ft.Row(
                controls=[get_col_chart(
                    title="Динамика шкалы AUDIT",
                    data=[
                        {
                            "title": "01.01.2024",
                            "value": 10,
                        },
                        {
                            "title": "01.03.2024",
                            "value": 15,
                        },
                        {
                            "title": "01.05.2024",
                            "value": 12,
                        },
                        {
                            "title": "01.07.2024",
                            "value": 3,
                        },

                    ]
                )]
            ),
            ft.Row(
                controls=[ft.CupertinoButton("Запустить прогнозирование")]
            ),
            ft.Row(
                controls=[ft.Text("Последнее обновление: 12.11.2024 22:11")]
            ),
            ft.Row(
                controls=[ft.CupertinoButton("Ссылка на опрос для данного студента",
                                             on_click=lambda x: page.go(route=f"/audit/{s_id}"))]
            ),
            bottom_bar(page=page)
        ]
    )
