import flet as ft


def main(page):
    return ft.View(
        "/",
        [
            ft.AppBar(title=ft.Text("Sturdy palm tree"), bgcolor=ft.colors.SURFACE_VARIANT),
            ft.ElevatedButton("Students", on_click=lambda _: page.go("/students")),
            ft.ElevatedButton("Polls", on_click=lambda _: page.go("/polls")),
        ],
    )
