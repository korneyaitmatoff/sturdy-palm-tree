import flet as ft

from sturdy_palm_tree.src.api.service import StudentService
from sturdy_palm_tree.src.api.core import tables
from config import db_config

WIDTH = 320


def add_student_form(page: ft.Page):
    def _onclick(e):
        if "" in (
                name.value,
                gender.value,
                performance.value,
                stress.value,
                family_alcohol.value,
                classmates_relations.value,
                age.value
        ):
            page.snack_bar = ft.SnackBar(ft.Text("Заполните все поля!"))
            page.snack_bar.open = True
            page.update()
        else:

            StudentService(table=tables.Students, **db_config).create(data={
                "name": name.value,
                "gender": gender.value,
                "age": age.value,
                "performance": performance.value,
                "stress": stress.value,
                "family_alcohol": family_alcohol.value,
                "classmates_relations": classmates_relations.value
            })

            page.snack_bar = ft.SnackBar(ft.Text("Студент бы добавлен"))
            page.snack_bar.open = True

            page.update()

    return ft.Container(
        content=ft.Column(
            [
                name := ft.TextField(
                    label="ФИО",
                    border="underline",  # type: ignore
                    width=WIDTH,
                    text_size=14,
                    value=""
                ),
                age := ft.TextField(
                    label="Возраст",
                    border="underline",  # type: ignore
                    width=WIDTH,
                    text_size=14,
                    keyboard_type=ft.KeyboardType.NUMBER
                ),
                gender := ft.Dropdown(
                    options=[
                        ft.dropdown.Option(text="М"),
                        ft.dropdown.Option(text="Ж"),
                    ],
                    width=WIDTH,
                    height=60,
                    text_size=14,
                ),
                performance := ft.TextField(
                    label="Успеваемость",
                    border="underline",  # type: ignore
                    width=WIDTH,
                    text_size=14,
                    value=""
                ),
                stress := ft.TextField(
                    label="Уровень стресса",
                    border="underline",  # type: ignore
                    width=WIDTH,
                    text_size=14,
                    value=""
                ),
                family_alcohol := ft.Checkbox(
                    label="Алкоголь в семье",
                ),
                classmates_relations := ft.Checkbox(
                    label="Отношения с одноклассниками",
                ),
                ft.CupertinoButton(text="Добавить", on_click=_onclick)
            ]
        )
    )
