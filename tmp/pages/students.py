import reflex as rx

from sturdy_palm_tree.src.api.core import tables
from sturdy_palm_tree.src.api.service import StudentService
from rxconfig import db_config


def get_students():
    service = StudentService(table=tables.Students, **db_config)

    data = []

    for item in service.read():
        data.append(
            rx.table.row(
                rx.table.row_header_cell(item.id),
                rx.table.cell(item.name),
                rx.table.cell(item.gender),
                rx.table.cell(item.performance),
                rx.table.cell(item.stress),
                rx.table.cell(item.family_alcohol),
                rx.table.cell(item.classmates_relations),
                rx.table.cell(item.alcohol_forecast),
                rx.button("Профиль студента", on_click=lambda: rx.redirect(f"/student/{item.id}"))
            ),
        )

    return rx.table.root(
        rx.table.header(
            rx.table.column_header_cell("ID"),
            rx.table.column_header_cell("Имя"),
            rx.table.column_header_cell("Пол"),
            rx.table.column_header_cell("Успеваемость"),
            rx.table.column_header_cell("Уровень стресса"),
            rx.table.column_header_cell("Алкоголь в семье"),
            rx.table.column_header_cell("Давление со стороны одноклассников"),
            rx.table.column_header_cell("Склонность к алкоголизму"),
            rx.table.cell(""),
        ),
        rx.table.body(
            *data
        )
    )


def students():
    return {
        "route": "/students",
        "component": rx.container(
            rx.heading("Students page"),
            rx.container(
                rx.vstack(
                    get_students()
                )
            )
        )
    }
