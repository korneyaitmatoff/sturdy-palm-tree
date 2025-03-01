import flet as ft


def bottom_bar(page: ft.Page):
    return ft.BottomAppBar(
        bgcolor=ft.colors.BLUE,
        shape=ft.NotchShape.CIRCULAR,
        content=ft.Row(
            controls=[
                ft.IconButton(icon=ft.icons.HOME, on_click=lambda x: page.go(route="/")),
                ft.IconButton(icon=ft.icons.PERSON, on_click=lambda x: page.go(route="/students")),
                ft.IconButton(icon=ft.icons.QUESTION_MARK, on_click=lambda x: page.go(route="/polls")),
            ]
        )
    )
