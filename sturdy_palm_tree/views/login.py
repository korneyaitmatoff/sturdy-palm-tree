from os import getenv

import flet as ft
from dotenv import load_dotenv
from flet_route import Basket, Params

load_dotenv()


def login(page: ft.Page, params: Params, basket: Basket):
    def show_snack(text: str):
        page.snack_bar = ft.SnackBar(ft.Text(text))
        page.snack_bar.open = True
        page.update()

    def _onclick(e):
        if password.value == "" or username.value == "":
            show_snack(text="Поля логин и пароль обязательные")
        else:
            if getenv("admin_login") != username.value or getenv("admin_password") != password.value:
                show_snack(text="Неверные данные")
            else:
                page.session.set("is_auth", True)
                page.go(route="/")

    if page.session.contains_key("is_auth"):
        return page.go(route="/")

    page.horizontal_alignment = "center"

    username = ft.TextField(
        label="Логин",
        border="underline",  # type: ignore
        width=320,
        text_size=14,
        value=""
    )

    password = ft.TextField(
        label="Пароль",
        border="underline",  # type: ignore
        width=320,
        text_size=14,
        password=True,
        can_reveal_password=True,
        value=""
    )

    return ft.View(
        route="/login",
        controls=[
            ft.Container(
                ft.Column(
                    controls=[
                        username,
                        password,
                        ft.CupertinoButton("Войти", on_click=_onclick)
                    ]
                ),
                alignment=ft.alignment.center
            )
        ]
    )
