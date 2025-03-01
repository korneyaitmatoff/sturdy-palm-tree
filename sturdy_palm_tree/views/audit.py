import flet as ft
from flet_route import Basket, Params

from sturdy_palm_tree.components import audit_poll_form, bottom_bar


def audit(page: ft.Page, params: Params, basket: Basket):
    print(params)
    print(basket)

    return ft.View(
        route="/audit",
        controls=[
            audit_poll_form(page=page, s_id=params.get("s_id")),
        ],
        scroll=ft.ScrollMode.ALWAYS
    )
