import flet as ft
from flet_route import Basket, Params

from sturdy_palm_tree import auth_required
from sturdy_palm_tree.components import (add_student_form, bottom_bar,
                                         students_table)


@auth_required
def students(page: ft.Page, params: Params, basket: Basket):
    return ft.View(
        route="/students",
        controls=[
            ft.Row(
                controls=[
                    add_student_form(page),
                    students_table(page),
                ],
                spacing=20
            )
        ],
        bottom_appbar=bottom_bar(page=page)
    )
